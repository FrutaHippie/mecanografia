#!/usr/bin/env python3
"""Servidor local de Teclea Rápido: sirve la app y guarda tus métricas en datos.json."""
import json
import os
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DIR = Path(__file__).resolve().parent
PAGE = DIR / "index.html"
DATA = DIR / "datos.json"
BACKUP = DIR / "datos.anterior.json"
HOST, PORT = "127.0.0.1", 8765
URL = f"http://{HOST}:{PORT}/"
ALLOWED_HOSTS = {f"{HOST}:{PORT}", f"localhost:{PORT}"}
MAX_BYTES = 20 * 1024 * 1024


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body=b"", ctype="text/plain; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _trusted(self):
        # Solo atiende a la propia app: evita que otras páginas web lean o borren tus datos.
        if self.headers.get("Host") not in ALLOWED_HOSTS:
            return False
        origin = self.headers.get("Origin")
        return origin is None or origin.split("//", 1)[-1] in ALLOWED_HOSTS

    def do_GET(self):
        if not self._trusted():
            return self._send(403)
        if self.path in ("/", "/index.html"):
            self._send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/contenido.js":
            self._send(200, (DIR / "contenido.js").read_bytes(), "text/javascript; charset=utf-8")
        elif self.path == "/api/datos":
            body = DATA.read_bytes() if DATA.exists() else b"null"
            self._send(200, body, "application/json")
        else:
            self._send(404, "No encontrado".encode())

    def do_POST(self):
        if not self._trusted() or self.path != "/api/datos":
            return self._send(403)
        if "application/json" not in self.headers.get("Content-Type", ""):
            return self._send(415)
        length = int(self.headers.get("Content-Length") or 0)
        if not 0 < length <= MAX_BYTES:
            return self._send(413)
        try:
            data = json.loads(self.rfile.read(length))
        except ValueError:
            return self._send(400, "JSON inválido".encode())
        tmp = DATA.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        if DATA.exists():
            os.replace(DATA, BACKUP)
        os.replace(tmp, DATA)
        self._send(200, b'{"ok":true}', "application/json")

    def log_message(self, *args):
        pass


def main():
    try:
        server = ThreadingHTTPServer((HOST, PORT), Handler)
    except OSError:
        print("Teclea Rápido ya está funcionando. Abriendo el navegador…")
        webbrowser.open(URL)
        return
    print(f"Teclea Rápido funcionando en {URL}")
    print(f"Tus métricas se guardan en {DATA}")
    print("Para apagarlo, cierra esta ventana o pulsa Ctrl+C.")
    threading.Timer(0.5, webbrowser.open, [URL]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

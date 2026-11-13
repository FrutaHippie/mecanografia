# Teclea Rápido

Práctica de mecanografía en español que aprende de tus errores: repite las palabras que fallas, insiste en las teclas y combinaciones que te cuestan y te muestra tu progreso.

- **Palabras**: más de 3.600 palabras variadas, incluido vocabulario técnico (ciencia de datos, estadística, matemáticas y salud).
- **Textos con sentido**: párrafos, pequeñas historias y refranes.
- **Mis puntos débiles**, **Fila guía**, **Agilidad** y **Mi texto** (pega el texto que quieras).
- Funciona sin internet. Tus datos se quedan en tu computador.

## Cómo abrirla

### Mac
Haz doble clic en **`Abrir Teclea Rápido.command`**.
La primera vez, macOS puede bloquearlo: haz clic derecho sobre el archivo → **Abrir** → **Abrir**.

### Windows
1. Instala Python desde [python.org](https://www.python.org/downloads/) si no lo tienes (marca la casilla **"Add python.exe to PATH"**).
2. Haz doble clic en **`Abrir Teclea Rápido.bat`**.

Se abrirá una ventana negra (el servidor) y la app en tu navegador. Para cerrarla, cierra esa ventana.

### Sin Python
Abre **`index.html`** con doble clic. Todo funciona igual, pero tu progreso solo se guarda en ese navegador (si borras sus datos, se pierde).

## Tus datos
Con el servidor, tu progreso se guarda en `datos.json` en esta misma carpeta (y una copia anterior en `datos.anterior.json`). Desde **Mi progreso** puedes exportar e importar copias.

## Teclado
Las pistas del teclado en pantalla siguen la distribución **latinoamericana**. Con otra distribución puedes practicar igual, pero algunos símbolos no coincidirán con lo que muestra la pantalla.

## Agregar tus propias palabras o textos
Edita `contenido.js`: añade palabras separadas por espacios en las listas, o textos con el formato `['tema', 'Tu texto aquí.'],` dentro de `textos`.

## Archivos
| Archivo | Para qué sirve |
|---|---|
| `index.html` | La aplicación |
| `contenido.js` | Palabras, textos, refranes e historias |
| `servidor.py` | Servidor local que guarda tu progreso en `datos.json` |
| `Abrir Teclea Rápido.command` | Lanzador para Mac |
| `Abrir Teclea Rápido.bat` | Lanzador para Windows |

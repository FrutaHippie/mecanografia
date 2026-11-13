@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Teclea Rapido

rem Busca Python: primero el lanzador "py", luego "python".
py -3 --version >nul 2>nul && (py -3 servidor.py & goto fin)
python --version >nul 2>nul && (python servidor.py & goto fin)

echo.
echo  No encontre Python en este computador.
echo.
echo  Opcion 1: instala Python desde https://www.python.org/downloads/
echo            (marca la casilla "Add python.exe to PATH" al instalar)
echo            y vuelve a abrir este archivo.
echo.
echo  Opcion 2: abre index.html con doble clic. La app funciona igual,
echo            pero tu progreso solo se guarda en ese navegador.
echo.
pause
exit /b

:fin
if errorlevel 1 pause

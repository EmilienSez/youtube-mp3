@echo off
REM === Chemin vers l'environnement virtuel ===
REM ⚠️ Remplace-le par le chemin réel si besoin
set "VENV_PATH=E:\1 - Projet\youtube-mp3-app\.venv"

REM Active l'environnement virtuel
call "%VENV_PATH%\Scripts\activate.bat"

REM Lance PyInstaller
pyinstaller --noconfirm --onedir --windowed --name "youtube_mp3" ^
--add-data "E:\1 - Projet\youtube-mp3-app\assets;assets/" ^
--add-data "E:\1 - Projet\youtube-mp3-app\modules;modules/" ^
--add-data "E:\1 - Projet\youtube-mp3-app\ui;ui/" ^
"E:\1 - Projet\youtube-mp3-app\main.py"

REM Pause pour garder la fenêtre ouverte à la fin
echo.
echo ✅ Fichier .exe généré dans dist\youtube_mp3\
pause

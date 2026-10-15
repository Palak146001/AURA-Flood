@echo off
title AURA-Flood | Dual-System Master Launcher
echo =================================================================
echo   AURA-Flood: Autonomous Urban Rainfall and Assessment System
echo   BuildFest 2.0 Hackathon - PS-18
echo   Team: TryAgain (GNDU) - Vanshika, Niharika, Palak
echo =================================================================
echo.

cd /d "%~dp0"

echo [*] Checking Python environment...
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PY_CMD=python
    goto RUN
)

where py >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PY_CMD=py -3.12
    goto RUN
)

echo [!] Python executable not found in PATH. Please ensure Python is installed.
pause
exit /b 1

:RUN
echo [*] Starting AURA-Flood Dual Platform (PWA + 3D Command Center)...
%PY_CMD% run_all.py
pause

@echo off
title AURA-Flood | Nationwide Citizen PWA
cd /d "%~dp0"
echo Starting FastAPI Citizen PWA on http://127.0.0.1:8000 ...
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
pause

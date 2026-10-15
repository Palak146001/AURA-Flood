@echo off
title AURA-Flood | 3D AI Command Center
cd /d "%~dp0"
echo Starting Streamlit 3D Command Center on http://127.0.0.1:8501 ...
python -m streamlit run command_center.py --server.port 8501
pause

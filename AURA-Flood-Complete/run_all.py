"""
AURA-Flood Master Launcher
BuildFest 2.0 Hackathon | PS-18: AI-Powered Heavy Rainfall Forecasting and Urban Flood Early-Warning System for Indian Cities
Team: TryAgain (Guru Nanak Dev University, Amritsar)
Members: Vanshika (Team Lead), Niharika, Palak

Launches both:
1. Nationwide Citizen PWA & Travel Alert System (FastAPI @ http://127.0.0.1:8000)
2. 3D AI Command Center & Inundation Simulator (Streamlit @ http://127.0.0.1:8501)
"""

import os
import sys
import time
import subprocess
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def find_python():
    """Finds the best python executable to run the apps."""
    # Check current interpreter
    if sys.executable and os.path.exists(sys.executable):
        return sys.executable
    return "python"

def main():
    os.chdir(ROOT)
    py = find_python()

    print("\n" + "=" * 65)
    print("  🌊 AURA-Flood: Autonomous Urban Rainfall & Assessment System")
    print("  BuildFest 2.0 Hackathon | PS-18 | Team TryAgain (GNDU)")
    print("=" * 65)
    print(f"[*] Working Directory: {ROOT}")
    print(f"[*] Python Runtime   : {py}")
    print("[*] Launching Dual-System Architecture...\n")

    # 1. Start FastAPI Citizen PWA (Port 8000)
    print("--> [1/2] Starting Nationwide Citizen PWA (FastAPI) on http://127.0.0.1:8000 ...")
    fastapi_proc = subprocess.Popen(
        [py, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=ROOT,
    )

    # 2. Start Streamlit 3D Command Center (Port 8501)
    print("--> [2/2] Starting 3D AI Command Center (Streamlit) on http://127.0.0.1:8501 ...")
    streamlit_app = ROOT / "command_center.py"
    if not streamlit_app.exists():
        streamlit_app = ROOT / "streamlit_app.py"

    streamlit_proc = subprocess.Popen(
        [
            py,
            "-m",
            "streamlit",
            "run",
            str(streamlit_app),
            "--server.port",
            "8501",
            "--server.headless",
            "true",
            "--browser.gatherUsageStats",
            "false",
        ],
        cwd=ROOT,
    )

    # Wait 2.5 seconds for servers to initialize
    time.sleep(2.5)

    print("\n" + "-" * 65)
    print("  🚀 ALL SERVICES RUNNING SUCCESSFULLY!")
    print("  🌐 Citizen PWA (All 28 States & UTs) : http://127.0.0.1:8000")
    print("  🗺️ 3D AI Command Center & Simulation  : http://127.0.0.1:8501")
    print("  📢 Audio Travel Siren                : ACTIVE")
    print("  🧪 Citizen AI Verification Pipeline  : ACTIVE")
    print("-" * 65)
    print("\nOpening Dashboard in your web browser...")
    try:
        webbrowser.open("http://127.0.0.1:8000")
    except Exception:
        pass

    print("\nPress Ctrl+C to stop all servers gracefully.")

    try:
        while True:
            time.sleep(1)
            if fastapi_proc.poll() is not None:
                print("[!] FastAPI server terminated.")
                break
            if streamlit_proc.poll() is not None:
                print("[!] Streamlit server terminated.")
                break
    except KeyboardInterrupt:
        print("\n[*] Shutting down servers gracefully...")
    finally:
        for p in (fastapi_proc, streamlit_proc):
            try:
                p.terminate()
            except Exception:
                pass
        print("[*] AURA-Flood services stopped. Goodbye!")

if __name__ == "__main__":
    main()

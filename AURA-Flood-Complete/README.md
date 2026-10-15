# AURA-Flood: Autonomous Urban Rainfall and Assessment System

**BuildFest 2.0 Hackathon | Problem Statement PS-18:**  
*AI-Powered Heavy Rainfall Forecasting and Urban Flood Early-Warning System for Indian Cities*

**Team:** TryAgain (Guru Nanak Dev University, Amritsar)  
**Members:** Vanshika (Team Lead), Niharika, Palak

---

## 🌊 Overview & Dual-System Architecture

**AURA-Flood** is a unified, end-to-end urban flood forecasting and civic response platform that merges two complementary subsystems into a single cohesive project:

```
                                  ┌──────────────────────────────────────────────┐
                                  │           AURA-Flood Master System           │
                                  └──────────────────────┬───────────────────────┘
                                                         │
                        ┌────────────────────────────────┴────────────────────────────────┐
                        ▼                                                                 ▼
      ┌───────────────────────────────────┐                             ┌───────────────────────────────────┐
      │   1. Nationwide Citizen PWA       │ <====== Cross-Linked =====> │   2. 3D AI Command Center         │
      │      (FastAPI @ Port 8000)        │                             │      (Streamlit @ Port 8501)      │
      ├───────────────────────────────────┤                             ├───────────────────────────────────┤
      │ • All 28 States & 8 UTs Coverage  │                             │ • 3D PyDeck Inundation Simulator  │
      │ • Real-time Travel Siren Alarm    │                             │ • SRTM 30m Digital Elevation Model│
      │ • Offline PWA Caching / Service Wk│                             │ • Live Open-Meteo Weather Stream  │
      │ • Crowdsourced Community Reports  │                             │ • 4-Stage AI Verification Pipeline│
      │ • Local Hydrological Heuristics   │                             │ • Time-to-Threshold Risk Engine   │
      └───────────────────────────────────┘                             └───────────────────────────────────┘
```

---

## 🚀 Quick Start (1-Click Run)

### Option A: Windows (Double-Click)
Simply double-click:
```bat
start.bat
```
This launcher checks Python, starts both the FastAPI Citizen PWA (`:8000`) and the 3D Command Center (`:8501`), and opens your browser automatically.

### Option B: Python Command Line (Cross-Platform)
```bash
# 1. Install dependencies
python -m pip install -r requirements.txt

# 2. Launch both platforms simultaneously
python run_all.py
```

### Option C: Launching Individual Subsystems
- **Citizen PWA only**: `start_citizen_pwa.bat` or `python -m uvicorn main:app --port 8000` -> [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **3D Command Center only**: `start_command_center.bat` or `python -m streamlit run command_center.py --server.port 8501` -> [http://127.0.0.1:8501](http://127.0.0.1:8501)

---

## 🌟 Key Features & Hackathon Highlights

### 1. 🇮🇳 Nationwide Scope (All 28 States & 8 UTs)
- Comprehensive hydrological, drainage capacity, and historical flood databases spanning every Indian State and Union Territory.
- Chronic urban chokepoint cataloging (`data/waterlogging_spots.csv` & `data/flood_spots.csv`).

### 2. 🗺️ 3D Digital Elevation Model (DEM) & Topography Risk Curves
- Integrates SRTM 30m elevation rasters to analyze natural runoff slopes, depressions, railway subway underpasses, and tidal river basins.
- Computes non-linear **Time-to-Threshold (hours until critical flooding)** and dynamic drainage clogging penalties.

### 3. 🚨 Audible Travel Warning Alarm
- Automatic audio alert siren sounds in the web browser when severe rainfall or critical road waterlogging is screened along travel corridors.

### 4. 🧪 4-Stage AI Citizen Report Verification Pipeline
Filters out spam and hallucinations before community reports affect civil alert models:
1. **Spatial Catchment Geofence Test** (Validates GPS in known basin)
2. **Atmospheric & Rain Plausibility Test** (Cross-checks against Open-Meteo precipitation telemetry)
3. **Multi-Source Cluster Consensus Test** (Corroboration from nearby municipal pings)
4. **AI Siltation & Obstruction Semantic Scoring** (Evaluates civic credibility)

### 5. 📴 Offline Resilience & PWA Support
- Offline Service Worker caches app shell and baseline datasets.
- Graceful degradation with local synthetic simulations when external APIs are disconnected.

---

## 📁 Repository Structure

```
AURA-Flood/
├── main.py                     # FastAPI entry point (Citizen PWA + REST APIs)
├── command_center.py           # Streamlit + PyDeck 3D Command Center
├── streamlit_app.py            # Alias for Streamlit deployment
├── run_all.py                  # Dual-system orchestrator
├── start.bat                   # 1-click Windows master launcher
├── start_citizen_pwa.bat       # Dedicated PWA launcher
├── start_command_center.bat    # Dedicated Command Center launcher
├── requirements.txt            # Python dependencies (pinned and tested)
├── .gitignore                  # Git size optimizer (excludes venvs/caches < 5MB total)
├── README.md                   # Project documentation
│
├── backend/                    # Core Python API & hydrological logic
│   ├── engine.py               # Risk calculation, terrain heuristics & ML classifier
│   ├── india_dataset.py        # 28 States & 8 UTs offline hydrological catalog
│   └── community.py            # SQLite database interface for citizen submissions
│
├── frontend/                   # Citizen PWA assets
│   ├── index.html              # Main dashboard UI
│   ├── alerts.html             # Travel screening & local alert context
│   ├── app.js                  # Frontend client logic & audio alarms
│   ├── alerts.js               # Screening and alert scripts
│   ├── styles.css              # Custom styling
│   ├── manifest.json           # PWA progressive web app manifest
│   └── sw.js                   # Offline caching service worker
│
├── data/                       # Hydrological & Chokepoint datasets
│   ├── flood_spots.csv         # Mumbai & urban hotspot coordinates and elevation
│   ├── waterlogging_spots.csv  # Nationwide chronic underpass/chokepoint directory
│   └── community_reports.sqlite3 # Persistent community verification database
│
└── tests/                      # Automated test suite
    ├── test_api.py             # FastAPI REST endpoint tests
    └── test_engine.py          # Hydrological engine unit tests (24/24 passing)
```

---

## 🧪 Testing

Run the automated test suite with Python:
```bash
python -m unittest discover -s tests
```
*Result: 24/24 tests pass in under 0.3 seconds.*

---

## 📦 Git & GitHub Submission Guide

This project is fully optimized for GitHub's file limits:
- The entire repository is **under 3 MB** (excluding `.venv`, caches, and build artifacts managed by `.gitignore`).
- Ready to initialize as a Git repository:
  ```bash
  git init
  git add .
  git commit -m "feat: AURA-Flood unified dual-system platform"
  git branch -M main
  git remote add origin https://github.com/<your-username>/aura-flood.git
  git push -u origin main
  ```

---

## ⚠️ Advisory & Disclaimer
*AURA-Flood is an experimental AI proof-of-concept developed for BuildFest 2.0 Hackathon. It is not an official government warning system. In actual emergency scenarios, citizens must prioritize official directives issued by the India Meteorological Department (IMD) and National Disaster Management Authority (NDMA).*

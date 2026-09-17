# Railway Block Optimization - SIH 2026

### Intelligent Railway Maintenance Block Planning using MILP Optimization

This project optimizes railway maintenance scheduling to minimize train delays and maximize track availability using Mixed-Integer Linear Programming (MILP).

### Problem Statement
Indian Railways faces challenges in scheduling maintenance blocks without disrupting train traffic. Manual scheduling leads to inefficiencies and delays.

### Our Solution
- Graph-based representation of rail network (`railgraph.py`)
- MILP-based optimization model for block scheduling (`final.py`)
- Generates optimized schedule in JSON format
- Minimizes total disruption while ensuring all maintenance tasks are completed

### Files in this Repo
- `final.py` - Main optimization solver
- `railgraph.py` - Rail network graph construction
- `rail_network.json` - Sample rail network data
- `optimized_schedule.json` - Output optimized schedule

### Tech Stack
- Python 3.10+
- PuLP / OR-Tools (for MILP)
- NetworkX
- JSON

### How to Run
```bash
pip install pulp networkx
python railgraph.py
python final.py

# rail_graph.py - Digital Twin of Howrah-Bardhaman (10 stations)
import json

rail_network = {
    "stations": [
        {"id": "HWH", "name": "Howrah", "km": 0},
        {"id": "LLH", "name": "Liluah", "km": 5},
        {"id": "BZL", "name": "Belur", "km": 8},
        {"id": "BLY", "name": "Bally", "km": 10},
        {"id": "UTP", "name": "Uttarpara", "km": 13},
        {"id": "HND", "name": "Hindmotor", "km": 15},
        {"id": "KOG", "name": "Konnagar", "km": 18},
        {"id": "RIS", "name": "Rishra", "km": 20},
        {"id": "SRP", "name": "Serampore", "km": 25},
        {"id": "SHE", "name": "Sheoraphuli", "km": 30},
    ],
    "tracks": [
        {"from": "HWH", "to": "LLH", "id": "T1", "length": 5, "condition": 0.8},
        {"from": "LLH", "to": "BZL", "id": "T2", "length": 3, "condition": 0.6}, # needs maintenance
        {"from": "BZL", "to": "BLY", "id": "T3", "length": 2, "condition": 0.9},
        {"from": "BLY", "to": "UTP", "id": "T4", "length": 3, "condition": 0.4}, # critical
        {"from": "UTP", "to": "HND", "id": "T5", "length": 2, "condition": 0.7},
    ],
    "maintenance_requests": [
        {"id": "M1", "track": "T2", "dept": "PWay", "type": "Tamping", "duration_hr": 3, "priority": 3},
        {"id": "M2", "track": "T2", "dept": "TRD", "type": "OHE Check", "duration_hr": 2, "priority": 2},
        {"id": "M3", "track": "T4", "dept": "PWay", "type": "Rail Grinding", "duration_hr": 4, "priority": 5},
        {"id": "M4", "track": "T4", "dept": "S&T", "type": "Signal Repair", "duration_hr": 2, "priority": 4},
        {"id": "M5", "track": "T5", "dept": "PWay", "type": "Ballast Cleaning", "duration_hr": 3, "priority": 1},
    ],
    "trains": [
        {"id": "12301", "name": "Rajdhani", "path": ["HWH","LLH","BZL","BLY"], "time": "02:00", "priority": 10},
        {"id": "37811", "name": "Local", "path": ["HWH","LLH","BZL"], "time": "03:30", "priority": 2},
        {"id": "13005", "name": "Amritsar Mail", "path": ["HWH","LLH","BZL","BLY","UTP"], "time": "04:00", "priority": 7},
    ]
}

with open("rail_network.json","w") as f:
    json.dump(rail_network, f, indent=2)

print("✅ rail_network.json created - 10 stations, 5 maintenance requests")
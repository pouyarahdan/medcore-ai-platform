import json
import os
from datetime import datetime

DATA_FILE = "backend/data/results.json"

def save_result(filename: str, prediction: str, confidence: float):
    result = {
        "filename": filename,
        "prediction": prediction,
        "confidence": confidence,
        "timestamp": datetime.utcnow().isoformat()
    }

    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(result)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_results():
    if not os.path.exists(DATA_FILE):
        return []
    
    with open(DATA_FILE, "r") as f:
        return json.load(f)
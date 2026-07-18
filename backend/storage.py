import json
import os
from datetime import datetime

from sqlalchemy.orm import Session
from backend.database.models import Analysis

DATA_FILE = "backend/data/results.json"


def save_result(filename: str, prediction: str, confidence: float, job_id: str):
    result = {
    "job_id": job_id,
    "filename": filename,
    "prediction": prediction,
    "confidence": confidence,
    "status": "completed",
    "timestamp": datetime.utcnow().isoformat()
}

    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(result)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def save_result_db(
    db: Session,
    filename: str,
    prediction: str,
    confidence: float,
    job_id: str
):
    result = Analysis(
        job_id=job_id,
        filename=filename,
        prediction=prediction,
        confidence=confidence,
        status="completed",
        timestamp=datetime.utcnow()
    )

    db.add(result)
    db.commit()
    db.refresh(result)

    return result


def load_results():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def get_result_by_job_id(job_id: str):
    results = load_results()

    for item in results:
        if item["job_id"] == job_id:
            return item

    return None
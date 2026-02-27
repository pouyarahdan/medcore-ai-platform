from pydantic import BaseModel
from datetime import datetime


class AnalysisResult(BaseModel):
    job_id: str
    filename: str
    prediction: str
    confidence: float
    timestamp: datetime
from pydantic import BaseModel
from datetime import datetime

class AnalysisResult(BaseModel):
    filename: str
    prediction: str
    confidence: float
    timestamp: datetime
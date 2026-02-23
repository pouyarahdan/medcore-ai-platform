from fastapi import APIRouter
from backend.storage import load_results
from backend.schemas.result import AnalysisResult
from typing import List

router = APIRouter()

@router.get("/results", response_model=List[AnalysisResult])
def get_results():
    return load_results()
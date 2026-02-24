from fastapi import APIRouter, File, UploadFile
from backend.services.analyze_service import run_analysis

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    return await run_analysis(file)
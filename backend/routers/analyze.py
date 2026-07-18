from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session

from backend.services.analyze_service import run_analysis
from backend.database.database import get_db

router = APIRouter()


@router.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return await run_analysis(file, db)
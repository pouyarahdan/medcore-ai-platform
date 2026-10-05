from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.services.analyze_service import run_analysis
from backend.database.database import get_db

router = APIRouter(
    tags=["Analysis"]
)

ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/png"
}


@router.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    file_content = await file.read()

    if not file_content:
        raise HTTPException(
            status_code=400,
            detail="Empty file"
        )

    await file.seek(0)

    return await run_analysis(file, db)
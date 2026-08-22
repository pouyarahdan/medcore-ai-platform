from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.storage import (
    load_results_db,
    get_result_by_job_id_db
)
from backend.schemas.result import AnalysisResult

router = APIRouter()


@router.get("/results", response_model=List[AnalysisResult])
def get_results(db: Session = Depends(get_db)):
    return load_results_db(db)


@router.get("/results/{job_id}", response_model=AnalysisResult)
def get_result(
    job_id: str,
    db: Session = Depends(get_db)
):
    result = get_result_by_job_id_db(db, job_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Result not found"
        )

    return result


@router.get("/results-db")
def get_results_db(db: Session = Depends(get_db)):
    return load_results_db(db)
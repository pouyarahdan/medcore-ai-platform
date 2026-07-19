from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.storage import (
    load_results,
    get_result_by_job_id,
    load_results_db
)
from backend.schemas.result import AnalysisResult

router = APIRouter()


# گرفتن لیست همه نتایج (فعلاً از JSON)
@router.get("/results", response_model=List[AnalysisResult])
def get_results():
    return load_results()


# گرفتن نتیجه بر اساس job_id (فعلاً از JSON)
@router.get("/results/{job_id}", response_model=AnalysisResult)
def get_result(job_id: str):
    result = get_result_by_job_id(job_id)

    if not result:
        return {"status": "not_found"}

    return result


# گرفتن نتایج از دیتابیس
@router.get("/results-db")
def get_results_db(db: Session = Depends(get_db)):
    return load_results_db(db)
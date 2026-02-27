from fastapi import APIRouter
from backend.storage import load_results, get_result_by_job_id
from backend.schemas.result import AnalysisResult
from typing import List

router = APIRouter()


# گرفتن لیست همه نتایج
@router.get("/results", response_model=List[AnalysisResult])
def get_results():
    return load_results()


# گرفتن نتیجه بر اساس job_id
@router.get("/results/{job_id}", response_model=AnalysisResult)
def get_result(job_id: str):
    result = get_result_by_job_id(job_id)

    if not result:
        return {"status": "not_found"}

    return result
from datetime import datetime

from sqlalchemy.orm import Session

from backend.database.models import Analysis


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


def load_results_db(db: Session):
    return db.query(Analysis).all()


def get_result_by_job_id_db(db: Session, job_id: str):
    return db.query(Analysis).filter(
        Analysis.job_id == job_id
    ).first()
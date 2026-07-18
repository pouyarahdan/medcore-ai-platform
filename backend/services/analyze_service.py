from backend.ai.classifier_model import SimpleClassifier
from backend.storage import save_result_db
from sqlalchemy.orm import Session
import uuid


async def run_analysis(file, db: Session):

    job_id = str(uuid.uuid4())

    model = SimpleClassifier()
    result = model.predict(file)

    save_result_db(
        db=db,
        filename=file.filename,
        prediction=result["prediction"],
        confidence=result["confidence"],
        job_id=job_id
    )

    return {
        "job_id": job_id,
        "status": "completed"
    }
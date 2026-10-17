from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from backend.core.config import settings
from backend.routers.analyze import router as analyze_router
from backend.routers.upload import router as upload_router
from backend.routers.results import router as results_router
from backend.database.database import engine, get_db
from backend.database.models import Base


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)


@app.get("/", tags=["System"])
def read_root():
    return {"message": "MedCore AI Backend is running"}


@app.get("/health", tags=["System"])
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )

    return {
        "status": "healthy",
        "database": "connected"
    }


app.include_router(analyze_router)
app.include_router(upload_router)
app.include_router(results_router)


Base.metadata.create_all(bind=engine)
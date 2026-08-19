from fastapi import FastAPI

from backend.core.config import settings
from backend.routers.analyze import router as analyze_router
from backend.routers.upload import router as upload_router
from backend.routers.results import router as results_router
from backend.database.database import engine
from backend.database.models import Base


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)


@app.get("/")
def read_root():
    return {"message": "MedCore AI Backend is running"}


app.include_router(analyze_router)
app.include_router(upload_router)
app.include_router(results_router)


Base.metadata.create_all(bind=engine)
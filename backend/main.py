from fastapi import FastAPI
from backend.routers.analyze import router as analyze_router
from backend.routers.upload import router as upload_router
from backend.routers.results import router as results_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MedCore AI Backend is running"}

app.include_router(analyze_router)
app.include_router(upload_router)
app.include_router(results_router)
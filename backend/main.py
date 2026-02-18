from fastapi import FastAPI

app = FastAPI(
    title="MedCore AI Platform",
    version="0.1.0",
    description="Core Backend API for MedCore AI System"
)


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "MedCore AI Backend is running 🚀"
    }
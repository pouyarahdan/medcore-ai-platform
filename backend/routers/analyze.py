from fastapi import APIRouter, File, UploadFile
from backend.model import analyze_image
from backend.storage import save_result

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    result = analyze_image(file.filename)

    save_result(
        filename=file.filename,
        prediction=result["prediction"],
        confidence=result["confidence"]
    )

    return {
        "filename": file.filename,
        "prediction": result["prediction"],
        "confidence": result["confidence"]
    }
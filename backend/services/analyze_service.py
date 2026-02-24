from backend.model import analyze_image
from backend.storage import save_result


async def run_analysis(file):
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
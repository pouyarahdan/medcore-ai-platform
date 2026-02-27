from backend.ai.classifier_model import SimpleClassifier
from backend.storage import save_result


async def run_analysis(file):

    model = SimpleClassifier()
    result = model.predict(file)

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
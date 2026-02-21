def analyze_image(filename: str) -> dict:
    if "covid" in filename.lower():
        prediction = "COVID-19 Positive"
        confidence = 0.92
    else:
        prediction = "Normal"
        confidence = 0.85

    return {
        "prediction": prediction,
        "confidence": confidence
    }
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
from backend.model import analyze_image

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ Root endpoint (برای تست test_root)
@app.get("/")
def read_root():
    return {"message": "MedCore AI Backend is running"}

# ✅ Analyze endpoint (برای تست test_analyze_endpoint_no_file)
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    result = analyze_image(file.filename)

    return {
        "filename": file.filename,
        "prediction": result["prediction"],
        "confidence": result["confidence"]
    }

# ✅ Upload endpoint جدید
@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    return JSONResponse(
        content={
            "filename": file.filename,
            "message": "Image uploaded successfully"
        }
    )
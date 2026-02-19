from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "MedCore AI Backend is running 🚀"
    }

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Image received successfully"
    }
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload-image/")
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
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os

router = APIRouter(
    tags=["Uploads"]
)

UPLOAD_FOLDER = "uploads"

ALLOWED_CONTENT_TYPES = {
    "image/jpeg",
    "image/png"
}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    file_content = await file.read()

    if not file_content:
        raise HTTPException(
            status_code=400,
            detail="Empty file"
        )

    file_location = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_location, "wb") as f:
        f.write(file_content)

    return JSONResponse(
        content={
            "filename": file.filename,
            "message": "Image uploaded successfully"
        }
    )
from fastapi import FastAPI,File, UploadFile
import uvicorn
from fastapi.exceptions import HTTPException
import os
import shutil

app = FastAPI()   

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # check the content type (MIME type)
    content_type = file.content_type
    if content_type not in ["application/pdf"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    upload_dir = os.path.join(os.getcwd(), "uploads")
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # get the destination path
    dest = os.path.join(upload_dir, file.filename)
    print(dest)

    # copy the file contents
    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
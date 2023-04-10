from fastapi import FastAPI, File, UploadFile
import shutil

app = FastAPI()


@app.post("/files")
async def UploadImage(file: UploadFile = File(...)):
    path="server_images/"
    try:
        with open(path+file.filename, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        
    return {"message": f"Successfully uploaded {file.filename}"}


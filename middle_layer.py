from fastapi import FastAPI, File, UploadFile
import shutil
import pathlib

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(GZipMiddleware)

@app.post("/files")
async def UploadImage(file: UploadFile = File(...)):
    path="server_images/"
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    try:
        with open(path+file.filename, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        
    return {"message": f"Successfully uploaded {file.filename}"}


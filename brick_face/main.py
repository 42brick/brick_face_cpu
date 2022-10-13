import os
import shutil

from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

from upload_file import upload_file
from run_func import run_model

app = FastAPI()


@app.get('/')
def root():
    return "Hello FastAPI!"


@app.post('/ai')
async def run_ai(file: UploadFile):

    if os.path.exists("./ouput/result"):
        shutil.rmtree("./ouput/result")

    res = await upload_file(file)
    if res == False:
        return {
            'status': 400
        }

    await run_model(4,	8)

    return FileResponse(path="./ouput/generate1.png")

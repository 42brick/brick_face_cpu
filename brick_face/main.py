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

    if os.path.exists("./output/result"):
        shutil.rmtree("./output/result")

    await upload_file(file)
    await run_model(4,	8)

    return FileResponse(path="./output/result/test4~8.png")

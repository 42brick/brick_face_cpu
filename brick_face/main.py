import os
from os import getcwd
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

    if os.path.exists("./brick_face/ouput/result"):
        shutil.rmtree("./brick_face/ouput/result")

    res = await upload_file(file)
    if res == False:
        return {
            'status': 400
        }

    await run_model(4,	8)

    return FileResponse(path=getcwd() + "/brick_face/ouput/generate1.png")

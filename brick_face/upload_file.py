import os
from fastapi import UploadFile


async def upload_file(file: UploadFile):
    UPLOAD_DIR = "./test_images/"
    content = await file.read()
    filename = "test3.jpg"
    with open(os.path.join(UPLOAD_DIR, filename), 'wb') as fp:
        fp.write(content)
        fp.close()

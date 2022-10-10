# aws 에서 제공하는 lambda base image (python)
# FROM amazon/aws-lambda-python:3.8
FROM public.ecr.aws/lambda/python:3.8

# optional : ensure that pip is up to data
RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

# install git 
RUN yum install git -y
RUN yum install mesa-libGL -y

# git clone
RUN git clone https://github.com/42brick/lambda_and_ecr.git

# install packages
# RUN pip install -r lambda_and_ecr/requirements.txt
# RUN pip install imageio-ffmpeg==0.4.3 pyspng==0.1.0
RUN pip install absl-py==1.2.0
RUN pip install aiohttp==3.8.3
RUN pip install aiosignal==1.2.0
RUN pip install analytics-python==1.4.0
RUN pip install async-timeout==4.0.2
RUN pip install backoff==1.10.0
RUN pip install bcrypt==4.0.0
RUN pip install brotlipy==0.7.0
RUN pip install cachetools==5.2.0
RUN pip install certifi==2022.6.15
RUN pip install click==8.1.3
RUN pip install cycler==0.11.0
RUN pip install fastapi==0.85.0
RUN pip install ffmpy==0.3.0
RUN pip install fonttools==4.34.4
RUN pip install frozenlist==1.3.1
RUN pip install fsspec==2022.8.2
RUN pip install google-auth==2.12.0
RUN pip install google-auth-oauthlib==0.4.6
RUN pip install gradio==3.4
RUN pip install grpcio==1.49.1
RUN pip install h11==0.12.0
RUN pip install httpcore==0.15.0
RUN pip install httpx==0.23.0
RUN pip install imageio-ffmpeg==0.4.7
RUN pip install importlib-metadata==5.0.0
RUN pip install joblib==1.1.0
RUN pip install kiwisolver==1.4.4
RUN pip install linkify-it-py==1.0.3
RUN pip install Markdown==3.4.1
RUN pip install markdown-it-py==2.1.0
RUN pip install matplotlib==3.5.2
RUN pip install mdit-py-plugins==0.3.1
RUN pip install mdurl==0.1.2
RUN pip install mistune==0.8.4
RUN pip install monotonic==1.6
RUN pip install multidict==6.0.2
RUN pip install ninja==1.10.2.3
RUN pip install oauthlib==3.2.1
RUN pip install opencv-python==4.6.0.66
RUN pip install orjson==3.8.0
RUN pip install numpy==1.23.1
RUN pip install pandas==1.5.0
RUN pip install paramiko==2.11.0
RUN pip install ply==3.11
RUN pip install protobuf==3.19.6
RUN pip install psutil==5.9.1
RUN pip install pyasn1==0.4.8
RUN pip install pyasn1-modules==0.2.8
RUN pip install pycryptodome==3.15.0
RUN pip install pydantic==1.10.2
RUN pip install pydub==0.25.1
RUN pip install PyNaCl==1.5.0
RUN pip install PyQt5==5.15.7
RUN pip install python-multipart==0.0.5
RUN pip install PyYAML==6.0
RUN pip install requests-oauthlib==1.3.1
RUN pip install rfc3986==1.5.0
RUN pip install rsa==4.9
RUN pip install scikit-learn==1.1.2
RUN pip install scipy==1.9.0
RUN pip install sklearn==0.0
RUN pip install starlette==0.20.4
RUN pip install tensorboard==2.10.1
RUN pip install tensorboard-data-server==0.6.1
RUN pip install tensorboard-plugin-wit==1.8.1
RUN pip install threadpoolctl==3.1.0
RUN pip install timm==0.6.7
RUN pip install torch==1.7.1
RUN pip install torchaudio==0.7.2
RUN pip install torchvision==0.8.2
RUN pip install tqdm==4.64.0
RUN pip install uc-micro-py==1.0.1
RUN pip install uvicorn==0.18.3
RUN pip install webencodings==0.5.1
RUN pip install websockets==10.3
RUN pip install Werkzeug==2.2.2
RUN pip install wincertstore==0.2
RUN pip install yarl==1.8.1

# git repository 의 lambda_function.py 를 Container 내부의 /var/task/ 로 이동
RUN cp lambda_and_ecr/lambda_function.py /var/task/

# lambda_function.handler 실행
CMD ["lambda_function.handler"]

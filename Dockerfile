# aws 에서 제공하는 lambda base image (python)
FROM amazon/aws-lambda-python:3.8

# optional : ensure that pip is up to data
RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

# install git 
RUN yum install git -y

# git clone
RUN git clone https://github.com/42brick/lambda_and_ecr.git

# install packages
RUN pip install -r lambda_and_ecr/requirements.txt

# git repository 의 lambda_function.py과 brick_face/ 를 Container 내부의 /var/task/ 로 이동
RUN cp lambda_and_ecr/lambda_function.py /var/task/
RUN cp -r brick_face/ /var/task/

# lambda_function.handler 실행
CMD ["lambda_function.handler"
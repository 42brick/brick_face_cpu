import os
import shutil
import json
import boto3
import cv2

from brick_face.run_func import run_model

result_path = './brick_face/ouput/result'
save_file = './brick_face/test_images/test2.jpg'

s3 = boto3.resource('s3')


async def handler(event, context):

    # ./brick_face/ouput/result 삭제
    if os.path.exists(result_path):
        shutil.rmtree(result_path)

    # ./brick_face/test_image/test2.jpg로 받은 이미지 저장
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    img = readImageFromBucket(key, bucket_name)
    cv2.imwrite(save_file, img)

    # run_model() 실행
    await run_model(4, 8)

    # ./brick_face/output/result에 생상된 이미지 외부 반출
    s3.meta.client.upload_file(
        '/tmp/result.jpg', '42brickoutputimg', 'result.txt')

    return {
        'statusCode': 200,
        'body': {
            'hello': 'world',
        }
    }


def readImageFromBucket(key, bucket_name):
    bucket = s3.Bucket(bucket_name)
    object = bucket.Object(key)
    response = object.get()
    return cv2.imread(response['Body'])

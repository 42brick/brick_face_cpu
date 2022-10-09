from brick_face.run_func import run_model


def handler(event, context):

    # ./brick_face/ouput/result 삭제

    # ./brick_face/test_image/test2.jpg로 받은 이미지 저장

    # run_model() 실행

    # ./brick_face/output/result에 생상된 이미지 외부 반출
    
    return {
        'statusCode': 200,
        'body': {
            'hello': 'world',
        }
    }

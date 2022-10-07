# lambda_and_ecr

- API Gateway 로부터 이미지와 함께 POST 받았을 시, 생성된 레고 아바타 이미지를 반환하는 Lambda Function 구현 (Container 기반)
  -  Lambda Function 에서 사용하고 싶은 Package 들은 Dockerfile 에 작성 후 Image 로 만들어서 사용해야함
  -  Dockerfile 로부터 생성된 Image 는 ECR 에 업로드
  -  Lambda Function 은, ECR Image 기반 Container 내에서 동작
  
> 참고
  -  https://wooono.tistory.com/337?category=1006410

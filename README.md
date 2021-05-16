# Object Detection Assistance


## 앱 설명

사칙연산 함수 프로그램으로 DevOps 실습



## 앱 사용법

1. git clone

  ```
  $ git clone https://github.com/adele2020/object-detection-assistance.git
  ```

2. 패키지 설치

  ```
  $ pip install -r requirements.txt
  ```

3. 웹서버 실행

  ```
  $ python3 start_oda_app.py
  ```

4. 앱 실행  
  POST - submit 실행  

  `http://0.0.0.0:5000/calculator`   

  GET  
  `http://0.0.0.0:5000/calculator?arg1=2&arg2=3&op=plus`  



## 테스트 방법

사칙연산 함수 테스트

```
  $ cd object-detection-assistance/unittest
  $ pytest
```

서버 상태 테스트

```
  $ cd object-detection-assistance/integration
  $ pytest
```


## Smart Bowl - Raspberry Pi Part
안태현(taehyoun1219) 장혜진(G2nie)

### 필요 라이브러리

#### 1. PiCamera 
```
pip install picamera
```
#### 2. Firebase Admin SDK:
•	설명: 라즈베리 파이에서 Firebase를 사용하기 위한 SDK.
```
pip install firebase-admin
```
#### 3. Servo 라이브러리:
•	설명: 서보 모터를 제어하기 위한 라이브러리.
```
#include <Servo.h>
```

### firebase 연결
----------------------------------------------

1. 앱에서 firebase db에 데이터 넣기
```
FirebaseDatabase.getInstance().getReference("servo_control");

databaseReference.setValue("90");
```
2. 라즈베리파이에서 데이터 받고 아두이노로 보내기
```
ser = serial.Serial('/dev/ttyUSB0', 9600) 

   while True:
       # Firebase에서 데이터 읽기
       servo_angle = ref.get()
       //센서별로 다른 db에 전송

       # 아두이노로 데이터 전송
       ser.write(servo_angle.encode())
```
3. 아두이노 값 변경
```
     if (Serial.available() > 0) {
       int angle = Serial.parseInt();  // 시리얼에서 각도 값을 읽음
       myservo.write(angle);           
```

### 환경 설정 정보
----------------------------------------------
* 운영체제 : Rasbian OS
* 코드 readme 생성, 정리


로직1
*라즈베리에서 데이터 전송
라즈베리가 센서로부터 데이터 받아서 -> DB에 전송(센서별) -> DB에 전송된 데이터 -> 안드로이드에서 받기
*안드로이드에서 데이터 요청 
버튼을 누르면 -> DB에 전송 -> DB에서 라즈베리파이로 전송 -> 라즈베리파이가 아두이노 제어 -> 이 값을 다시...

로직2
라즈베리파이(while true) => DB, 아두이노

1. 라즈베리파이 환경설정 패키지 깔고 (카메라 디비 파이썬)
2. 네트워크(학교 ip)
3. 카메라pi -> motion 사용

firebase 만들기 key
제어하는 코드 작성하고
카메라 코드
==> 금요일에 테스트

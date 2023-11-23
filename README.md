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
sudo pip3 install firebase-admin
```
#### 2-1. uuid Module:
•	설명: UID를 생성하기 위한 모듈 설치
```
sudo pip3 install uuid
```
#### 3. Servo 라이브러리:
•	설명: 서보 모터를 제어하기 위한 라이브러리.
```
#include <Servo.h>
```
#### 4. motion 
•	설명: 카메라로 영상을 촬영해서 실시간으로 스트리밍할 수 있다. 
![image](https://github.com/wireless-network-team2/Raspberry/assets/110397586/62594bce-9903-45de-a52a-3b246efcf928)
```
//설치 및 세팅
sudo apt-get install motion

//설정 파일
sudo nano /etc/motion/motion.conf

//실행
sudo motion
```
* daemon:부팅 시 백그라운드에서 자동으로 실행
* framerate:영상 프레임 세팅
* stream_maxrate:스트리밍 영상 프레임
* stream_port ~~:TCP/IP포트 설정
* stream_localhost:캠 접속을 로컬호스트에서만 가능하게 할 것인지
* 스티리밍 웹 = http://라즈베리파이ip:stream_port





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
       //센서별로 다른 헤더에 전송

       # 아두이노로 데이터 전송
       ser.write(servo_angle.encode())
```
3. 아두이노 값 변경
```
     if (Serial.available() > 0) {
       int angle = Serial.parseInt();  // 시리얼에서 각도 값을 읽음
       myservo.write(angle);           
```

### 개발 환경
----------------------------------------------
* Rasbian OS (Debian Bullseye)
* Python 3.9.2
* Firebase




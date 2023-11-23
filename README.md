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
•	설명: Pi카메라로 실시간 스트리밍을 구현할 수 있는 프로그램 
![image](https://github.com/wireless-network-team2/Raspberry/assets/110397586/62594bce-9903-45de-a52a-3b246efcf928)
```
//설치 및 세팅
sudo apt-get install motion

//설정 파일
sudo nano /etc/motion/motion.conf

//실행
sudo service motion start
```
* 웹 스트리밍:http://'ip주소':'포트번호'

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




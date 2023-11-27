## Smart Bowl - Raspberry Pi Part (안태현-taehyoun1219, 장혜진-G2nie)

### 🔨진행 상황
- [x] PiCamera 웹 스트리밍 테스트
![motiontest](https://github.com/wireless-network-team2/Raspberry/assets/110397586/8607016c-1f43-4942-a245-042fc4e30ec7)
```
웹 스트리밍 http://ip주소:포트번호
motion status 실행중 inactive(dead)는 연결 오류임, motion.conf 파일 확인해볼 것
log file 권한 오류시 var/log/motion/motion.log 777 권한 부여
웹에서 요청했는데 회색 화면이 뜨면 카메라 모듈이 잘못됐을 확률이 높음
방화벽 오류시 ufw allow 포트번호
``` 
- [x] 파이어베이스 연동 테스트 & 아두이노 센서 제어 테스트
![image](https://github.com/wireless-network-team2/Raspberry/assets/149992750/b95b89a9-e52d-4790-a320-6de2307b4952)

- [ ] 다중 아두이노 - 라즈베리파이 - 파이어베이스 연동
- [ ] 웹 스트리밍 - 안드로이드 연동


### 필요 라이브러리
```
1. PiCamera 
pip install picamera

2. Firebase Admin SDK : 라즈베리 파이에서 Firebase를 사용하기 위한 SDK.
sudo pip3 install firebase-admin

2-1. uuid Module : UID를 생성하기 위한 모듈 설치
sudo pip3 install uuid

3. Servo 라이브러리 : 서보 모터를 제어하기 위한 라이브러리.
#include <Servo.h>

4.motion : Pi카메라로 실시간 스트리밍을 구현할 수 있는 프로그램 
설치 및 세팅
sudo apt-get install motion

설정 파일
sudo nano /etc/motion/motion.conf

실행
sudo service motion start

motion 상태 확인
sudo service motion status

카메라 정상 작동 확인, 작동하면 video 파일 여러 개 존재
sudo ls /dev/video*
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
import serial
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("path/to/your/firebase/credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://your-project-id.firebaseio.com"})

ref = db.reference("your_data_key")

port = '/dev/ttyACM0'
brate = 9600
cmd = 'temp'

seri = serial.Serial(port, baudrate = brate, timeout = None)
seri.write(cmd.encode())

a = 1
while a:
	if seri.in_waiting !=0 :
		content = seri.readline()
		print(content[:-2].decode())
		data = {"sensor_data": 25.5, "timestamp": "2023-11-24T12:34:56Z"}
		ref.set(data)
		a=0
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





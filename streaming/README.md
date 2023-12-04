# 📷 실시간 수조 스트리밍 : 장혜진(202144081)
### 작동 원리
- 라즈베리파이에 파이카메라를 연결하여 모션을 통해 웹 서버에서 스트리밍 영상 출력
- 출력된 영상은 안드로이드 앱을 통해 웹 서버에 접속하여 사용자의 화면에 실시간으로 촬영중인 카메라 화면을 영상으로 보여줌

### 필요 라이브러리
```
1. PiCamera 
pip install picamera

2. motion
설치 및 세팅
sudo apt-get install motion

설정 파일
sudo nano /etc/motion/motion.conf

실행
sudo service motion start

상태 확인
sudo service motion status
```

### 구현
- [x] 정상 작동 테스트
![motiontest](https://github.com/wireless-network-team2/Raspberry/assets/110397586/8607016c-1f43-4942-a245-042fc4e30ec7)
- [x] 카메라 오류로 회색 화면만 뜨는 모습
![streaming (2)](https://github.com/wireless-network-team2/Raspberry/assets/110397586/1b9edbff-7d4c-4eef-bbe3-c194a0d7cf17)
- [x] 카메라 센서 연결한 모습
![카메라연결모습](https://github.com/wireless-network-team2/Raspberry/assets/110397586/fa5246fa-9bf0-4655-ab58-05691675939f)


해결한 오류
```
- http://ip주소:포트번호
- motion status 실행중 inactive(dead)는 연결 오류임, motion.conf 파일 확인해볼 것
- log file 권한 오류시 var/log/motion/motion.log 777 권한 부여
- 웹에서 요청했는데 회색 화면이 뜨면 카메라 모듈이 잘못됐을 확률이 높음
- 방화벽 오류시 ufw allow 포트번호
```

<br>

해결 못 한 오류
```
user@raspberrypi:~ $ raspistill -o test.jpg
mmal: mmal_vc_component_enable: failed to enable component: ENOSPC
mmal: camera component couldn't be enabled
mmal: main: Failed to create camera component
mmal: Failed to run camera app. Please check for firmware updates
```
카메라 인식은 되지만 카메라가 출력이 안 되는 현상<br>
처음 테스트를 진행했을 땐 정상 작동하였으나 라즈베리파이 초기화 후 작동 안 함<br>
시도해본 방법
- [x] 버전, 업데이트 문제 : sudo apt-get update, upgrade, raspi upgrade 작동X
- [x] GPU 메모리 설정 128->144
- [x] 카메라 센서, 라즈베리파이 다수 교체

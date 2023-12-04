# 📷 먹이 급여기 제어 : 장혜진(202144081)
### 작동 원리
- 안드로이드 앱에서 먹이 급여기 제어 버튼을 누르면 데이터베이스에 값이 들어옴
- 들어온 값은 라즈베리파이를 통해 받고, 그 값을 아두이노로 보내 서보 모터를 제어함

### 데이터베이스 구축
![image](https://github.com/wireless-network-team2/Raspberry/assets/110397586/96d4a914-79aa-4ad1-a2c4-cbf96242a851)
- feeding 필드에 각각 급여 양에 따라 full, half, little key에 기본값 0을 저장
- 모바일에서 사용자가 먹이 급여 제어 버튼을 누르면 해당되는 key의 값에 1이 저장됨

### 라즈베리파이
![image](https://github.com/wireless-network-team2/Raspberry/assets/110397586/e5a92da0-d4d3-423c-9322-2c953f9d587f)
- 라즈베리파이에서 데이터베이스의 각 key값을 검사하여 1이 저장된 키를 도출함
- 도출해낸 키에 따라 해당되는 제어값을 아두이노로 전달함

### 아두이노
![image](https://github.com/wireless-network-team2/Raspberry/assets/110397586/5a20cf0c-6124-42a4-b306-8b19923bfda5)
- 전달받은 제어값에 따라 서보모터를 제어함

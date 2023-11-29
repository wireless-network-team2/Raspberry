import serial
import time
import firebase import firebase

# Firebase 초기화
firebase = firebase.FirebaseApplication('https://smartbowl-b05d9-default-rtdb.firebaseio.com/', None)

# 시리얼 포트 설정
ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    # 아두이노에서 값 읽어오기
    arduino_data = ser.readline().decode('utf-8').rstrip().split(',')

    # pH 값과 수위 값 추출
    ph_value = float(arduino_data[0])
    water_level = float(arduino_data[1])

    # Firebase에 데이터 업로드
    data = {
        'waterdetection': ph_value,
        'watermeasurement': water_level
    }

    result = firebase.post('data', data)
    print(f"파이어베이스 업로드 완료 {result}")

    time.sleep(10)  # 10초마다 데이터 업로드

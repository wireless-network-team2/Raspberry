import serial
import firebase_admin
from firebase_admin import credentials, db

# Firebase 초기화
cred = credentials.Certificate("/home/pi/project2/firebase/smartbowl-b05d9-firebase-adminsdk-ldgsu-b9626cd4c3.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://smartbowl-b05d9-default-rtdb.firebaseio.com/'})
ref = db.reference('/data')

# 시리얼 포트 설정
ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    # 아두이노에서 값 읽어오기
    arduino_data = ser.readline().decode('utf-8').strip()
    
    values = arduino_data.split(',')
    print(values)

    # pH 값과 수위 값 추출
    ph_value = values[0]
    water_level = values[1]

    # Firebase에 데이터 업로드
    data = {
        'waterdetection': ph_value,
        'watermeasurement': water_level
    }
    
    ref.set(data)
    


import firebase_admin
from firebase_admin import credentials, db
import requests
import time
import serial

//firebase_url = 'https://smartbowl-b05d9.firebaseio.com/feeding.json'

firebase_admin.initialize_app(cred, {'databaseURL': 'https://smartbowl-b05d9.firebaseio.com/feeding'})
cred = credentials.Certificate("path/to/your/firebase/credentials.json")
ref = db.reference('/data')

arduino_serial_port = '/dev/ttyACM0'

ser = serial.Serial(arduino_serial_port, 9600)

while True:
    try:
        # Firebase에서 데이터 읽기
        data = ref.get()

         if data:
        for key, value in data.items():
            if value == 1:
                if key == "little":
                    ser.write("L".encode('utf-8'))
                    print("Little")
                elif key == "half":
                    ser.write("H".encode('utf-8'))
                    print("Half")
                elif key == "full":
                    ser.write("F".encode('utf-8'))
                    print("Full")
                    
                data[key] = 0
                requests.patch('https://your-firebase-project-id.firebaseio.com/data.json', json={key: 0})

    except Exception as e:
        print(f"Error: {e}")
        
time.sleep(1)

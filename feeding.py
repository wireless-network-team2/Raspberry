import requests
import time
import serial

firebase_url = 'https://smartbowl-b05d9.firebaseio.com/feeding.json'
arduino_serial_port = '/dev/ttyACM0'

ser = serial.Serial(arduino_serial_port, 9600, timeout=1)

while True:
    try:
        response = requests.get(firebase_url)
        data = response.json()

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
                requests.patch(firebase_url, json={key: 0})

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(10)  # 10초마다 데이터를 가져옴

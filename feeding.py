import requests
import time
import serial

firebase_url = 'https://smartbowl-b05d9.firebaseio.com/feeding.json'
arduino_serial_port = '/dev/ttyUSB0'

ser = serial.Serial(arduino_serial_port, 9600, timeout=1)

while True:
    try:
        response = requests.get(firebase_url)
        data = response.json()

        if data:
            for key, value in data.items():
                if value == 1:
                    if key == "L":
                        ser.write("L".encode('utf-8'))
                        print("Little")
                    elif key == "H":
                        ser.write("H".encode('utf-8'))
                        print("Half")
                    elif key == "F":
                        ser.write("F".encode('utf-8'))
                        print("Full")

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(10)  # 10초마다 데이터를 가져옴

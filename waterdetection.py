import serial
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("---------------------")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartbowl-b05d9-default-rtdb.firebaseio.com/'
})

db = firestore.client()

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

try:
    while True:
        if ser.in_waiting > 0:
            message = ser.readline().decode('utf-8').rstrip()
            print(message)

            if "물 넘침 위험" in message:
                data = {'waterdetection': 1}
                # db.collection('sensor_data').add(data)
            elif "물 부족 위험" in message:
                data = {'waterdetection': 0}
                # db.collection('sensor_data').add(data)

except KeyboardInterrupt:
    ser.close()

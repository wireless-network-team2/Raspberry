import serial
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("----------------")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartbowl-b05d9-default-rtdb.firebaseio.com/'
})

db = firestore.client()

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

try:
    while True:
        door_value = db.reference('btn_door').get()
        feeding_value = db.reference('btn_feeding').get()

        ser.write(str(door_value).encode('utf-8'))
        ser.write(str(feeding_value).encode('utf-8'))

except KeyboardInterrupt:
    ser.close()

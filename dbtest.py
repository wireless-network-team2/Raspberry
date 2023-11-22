import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import firestore

cred = credentials.Certificate("json 파일")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://smartbowl-b05d9-default-rtdb.firebaseio.com/'})
ref = db.reference('/testdb/testNum')

value = 1
ref.set(value)

print(print(f"success")

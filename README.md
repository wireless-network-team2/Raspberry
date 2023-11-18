# Raspberry
Smart Bowl - Raspberry part

### 데이터 통신 방식
라즈베리파이-안드로이드 블루투스 통신
#### 1. 블루투스 모듈 연결
----------------------------------------------
* 라즈베리파이 설정
1. 블루투스 패키지 설치
```
sudo apt-get update
sudo apt-get install bluetooth bluez blueman
```
2. 블루투스 활성화 및 페어링
```
bluetoothctl
power on
agent on
discoverable on
pairable on
//디바이스 찾기:scan on, 페어링:pair
```

* 안드로이드 설정
1. 블루투스 권한 추가 (AndroidManifest.xml)
```
<uses-permission android:name="android.permission.BLUETOOTH"/>
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN"/>
```
2. 블루투스 연결 관리 (별도의 클래스 활용)


### 데이터베이스
InfluxDB 1.0
```
pip install influxdb
```
```
from influxdb import InfluxDBClient

# InfluxDB에 연결
client = InfluxDBClient(host='your_influxdb_host', port=8086, database='your_database_name')

# 데이터 쓰기
json_body = [
    {
        "measurement": "sensor_data",
        "tags": {
            "sensor": "temperature"
        },
        "time": "2023-01-01T00:00:00Z",
        "fields": {
            "value": 25.0
        }
    }
]

client.write_points(json_body)

# 데이터 읽기
result = client.query('SELECT "value" FROM "sensor_data" WHERE "sensor" = \'temperature\'')
print(result.raw)

# 연결 종료
client.close()
```



### 환경 설정 정보
*운영체제 : Rasbian OS

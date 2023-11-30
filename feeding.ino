//아두이노 먹이급여기 부분 수정
//라즈베리파이에서 보낸 문자를 읽고 해당 레벨에 맞게 급여

if (Serial.available() > 0) {
    char receivedChar = Serial.read();
    if (receivedChar == 'L') {
      Pos = 30;
      myservo.write(Pos);
      delay(1000); 
      Pos = 0;
      myservo.write(Pos);
    }
    else if (receivedChar == 'H') {
      Pos = 60;
      myservo.write(Pos);
      delay(1000);
      Pos = 0;
      myservo.write(Pos);
    }
    else if (receivedChar == 'F') {
      Pos = 90;
      myservo.write(Pos);
      delay(1000);
      Pos = 0;
      myservo.write(Pos);
    }
  }

#include <Servo.h>  //library

Servo myservo;

void setup() {
  Serial.begin(9600);
  myservo.attach(9); // Yellow --> D9 pin, Brown --> GND, Red --> 5V
  myservo.write(90); // neutral
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();

    if (cmd == '1') {
      myservo.write(0);   // press
      delay(1000);
      myservo.write(90);  // back to the neutral position
    } 
    
    else if (cmd == '0') {
      myservo.write(180); // opposite
      delay(1000);
      myservo.write(90);  // back to the neutral position
    }
  }
}

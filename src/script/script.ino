const int LED_COUNT = 5;
const int LED_PIN[LED_COUNT] = {7, 8, 9, 10, 11};

void setup() {
  Serial.begin(9600);

  for (const int PIN: LED_PIN) {
    pinMode(PIN, OUTPUT);
  }
  
}

void loop() {

 if (Serial.available() > 0) {

  String data = Serial.readStringUntil('*');

  for (int i = 0; i < 5; ++i) {

    if (data[i] == '1') { // ON LED
      digitalWrite(LED_PIN[i], HIGH);
    } else {
      digitalWrite(LED_PIN[i], LOW);
    }

  }

 }

}
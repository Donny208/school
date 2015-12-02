int x = 1000;
int y = 100;

void setup() {
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
}

void loop() {
  tone(8,y);
  digitalWrite(7, HIGH);  
  delay(x);
  noTone(8);
  digitalWrite(7, LOW);
  delay(x);
  x = x / 1.1;  
  y = y + 100;
}

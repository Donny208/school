int x = 1000;


void setup() {
  // initialize digital pin 13 as an output.
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop() {
  tone(9,1000,10);
  digitalWrite(13, HIGH);  
  digitalWrite(12, LOW);  
  delay(100);
  noTone(9);              
  digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
  delay(x);
  x = x / 1.1;  
}

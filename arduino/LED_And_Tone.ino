int x = 0;
int y = 0;
int photocellPin = 0;
int photocellReading; 
int pitch = 8;
String fat = "You Are This Uncool: ";
int sound = 0;


void setup() {
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  photocellReading = analogRead(photocellPin);  
  tone(8,photocellReading*pitch);
  sound = map(photocellReading*pitch,500,800,1000,3000);
  if (x == 1){
    Serial.println(fat+photocellReading*pitch);
    x = 0;
  }
  if (photocellReading*pitch > 500){
    digitalWrite(7,HIGH);
  }
  else{
    digitalWrite(7,LOW);
  }
  clear();
  delay(100);
}

void clear(){
  y = y + 1;
  //Serial.println(y);
  if (y >= 10){
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    Serial.println();
    y = 1;
    x = 1;
  }
}

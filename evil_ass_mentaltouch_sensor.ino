int readD = 4;
int readA = A0;
int led = 6;


void setup() {
  // put your setup code here, to run once:
pinMode (readD, INPUT);
pinMode (readA, INPUT);
pinMode (led, OUTPUT);

Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
int analogValue = analogRead(readA);
Serial.print("readA is ");
Serial.println(analogValue);
/*Serial.print("readD is ");
Serial.println(readD);*/
}

const int pinD = 2; // Connect the sensor's digital pin to Arduino pin 2
const int pinA = A0; // Connect the sensor's analog pin to Arduino A0
int touchedD;
int touchedA;
int counting = 0;

void setup() {
  Serial.begin(9600); // Start serial communication
  pinMode(pinD, INPUT); // Set the sensor's digital pin as input
}
void loop() {
  Serial.println("bbb");
  delay(100);
  counting = 0;
  while(counting = 0)
  {
    int read1 =  analogRead(pinA);
    Serial.println("blip");
    int read2 =  analogRead(pinA);
    Serial.println("blip");
    int read3 =  analogRead(pinA);
    Serial.println("blip");
    int read4 =  analogRead(pinA);
    Serial.println("blip");
    
    int readFinal =(read1 + read2 + read3 + read4);
    Serial.println(readFinal);
    
    counting = 1;
  }
}

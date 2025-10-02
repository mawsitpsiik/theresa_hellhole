const int pinD = 2; // Connect the sensor's digital pin to Arduino pin 2
const int pinA = A0; // Connect the sensor's analog pin to Arduino A0
int counting = 0;
int runningRating;

void setup() {
  Serial.begin(9600); // Start serial communication
  pinMode(pinD, INPUT); 
  pinMode(pinA, OUTPUT);
}
void loop() {
  int touchedD = digitalRead(pinD);
  int touchedA = digitalRead(pinA);

  while(counting == 0)
  {
    Serial.println("Put two fingers pinching the sensor; reset to test again");
    delay(1000);

    int read1 =  analogRead(pinA);
    Serial.println(read1);
    delay(400);
    int read2 =  analogRead(pinA);
    Serial.println(read2);
    delay(400);
    int read3 =  analogRead(pinA);
    Serial.println(read3);
    delay(400);
    int read4 =  analogRead(pinA);
    Serial.println(read4);
    delay(400);
    int read5 =  analogRead(pinA);
    Serial.println(read5);
    delay(400);
    
    int readFinal =((read1 + read2 + read3 + read4 + read5)/5);
    
    /*if(readFinal <= 300 && readFinal >= 200) */
    
    int runningRating =(map(readFinal, 200, 800, 10, 1)); 
    
    
    Serial.print("Your average conductivity is ");
    Serial.print(readFinal);
    Serial.print(". This gives you a conductivity rating of ");
    Serial.print(runningRating);
    Serial.println("/10.");
    Serial.println("(Hint: Lower average conductivity means you're more connected to the sensor. Aim for lower!)");
    
    counting = 1;
  }
}

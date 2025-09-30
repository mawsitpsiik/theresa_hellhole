/* I'm using this to list a bunch of the formatting that I need to look back at to understand how to format new code */
int ledPin = 3;
int potPin = A0;

void setup()
{
  pinMode (ledPin, OUTPUT);
  pinMode (potPin, INPUT);
    Serial.begin(9600); // Starts the serial communication

}

void loop()
{
int potValue = analogRead(potPin) / 4;
analogWrite (ledPin, potValue);
  Serial.println (potValue);
} 
/* this is a potentiometer reader */

/* important: do not attempt to run this code all together */

const int trigPin = 11;
const int echoPin = 12;

long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT); 

  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600); 
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distance = duration * 0.034 / 2;
  
  
 
  if(distance >= 4) 
  {
    Serial.print ("STOP! Distance is ");
    Serial.print (distance);
    Serial.println (" cm above ground. The rover may fall!");
   } else {
    Serial.print ("Safe. Distance is ");
    Serial.print (distance);
    Serial.println (" cm above ground. The rover is alright.");
  }
 } /* this is for ultrasound; helps me learn serial print*/


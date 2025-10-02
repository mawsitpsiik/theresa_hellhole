const int pinA = A0; 
int counting = 0;

void setup() {
  Serial.begin(9600); 
  pinMode(pinA, OUTPUT);
}
void loop() {
  while(counting == 0)
  {
    Serial.println("Put two fingers pinching the sensor, trying to avoid the metal bar.");
    delay(1000); //advice on how to use

    int read1 =  analogRead(pinA); //reading the same pin, with a delay, gives new results
    Serial.println(read1); //probably a better way to store these than just 5 variables, but it works
    delay(400); //delay is arbitrary but this gives some nice pacing
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
    //this just takes the mean of the numbers
    int runningRating =(map(readFinal, 200, 800, 10, 1)); 
    //arbitrary numbers just to make it a bit more fun to get a rating
    
    Serial.print("Your average conductivity is ");
    Serial.print(readFinal);
    //direct printing of answers, was helpful for debug testing
    Serial.print(". This gives you a conductivity rating of ");
    Serial.print(runningRating);
    Serial.println("/10.");
    Serial.println("(Hint: Lower average conductivity means you're more connected to the sensor. Aim for lower!)");
    
    counting = 1; //this stops it from just looping forever
  }
}

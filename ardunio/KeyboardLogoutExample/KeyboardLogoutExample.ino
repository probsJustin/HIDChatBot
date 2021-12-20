String incomingString = ""; // for incoming serial data
#include "Keyboard.h"

void setup() {
    Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
    Keyboard.begin();
}
// 'a''\n'
// 'a'
void loop() {
  if (Serial.available() > 0) {
    incomingString = Serial.readString();

    Serial.print("I received: ");
    Serial.println(incomingString);
    if(incomingString != "" && incomingString.length() > 0){
      for(int i = 0; i < incomingString.length(); i++){
        Keyboard.press(incomingString.substring(0, incomingString.length()-1)[i]);
        Keyboard.releaseAll();
      }
        Serial.println("end");
    }
    incomingString = "";
  }
}

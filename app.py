

import json
import serial

'''
Example Arduino Script for reading: (this is likely going to change a lot since we will need to mimic HID witha  different board)
void setup ()
{
    // ..... // 
    Serial.begin (115200);
    Serial.print ("Ready...\n");
}'''


def createSerialConnection(location, baudRate):
    ser = serial.Serial(location, baudRate)
    print(ser.readline())

with open('./content.json') as f:
  content = json.load(f)

def displayList():
    for x in content.keys():
        subjectCounter = 0
        for y in range(0, len(content[x])):
            subjectCounter = subjectCounter + 1
            for z in content[x][y]:
                print(f'[{subjectCounter}][{z}]\n')
                for item in range(0, len(content[x][y][z])):
                    print(f'\t [{item}]{content[x][y][z][item]}')
                print("\n")

def getInput():
    user_message = input("What would you like to say?")

displayList()
getInput()

# display list of content
# get input <number>,<number> or <string-subject>, <number>
# get input option random which will pick a item at random to send

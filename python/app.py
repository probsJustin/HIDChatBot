

import json
#import serial
from collections import OrderedDict


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

with open('content.json') as f:
  content = OrderedDict(json.load(f))

def displayList():
    for x in enumerate(content):
        print(f'[{x[0]}]:{x[1]}')
        for y in enumerate(content[x[1]]):
            for z in enumerate(y[1]):
                print(f'\t[{y[0]}]:{z[1]}')
                for g in enumerate(content[x[1]][y[0]][z[1]]):
                    print(f'\t\t[{g[0]}]:{g[1]}')

def selectItem(input_dict, input_number):
    indexKeys = list(input_dict.keys())
    print(f'[{indexKeys[input_number]}]')
    return input_dict[indexKeys[input_number]]

def getNumbers(input_list):
    return [int(x) for x in input_list.split('.')]

def getInput():
    user_message = input("What would you like to say?")

def getSelectedItems(input_list_of_numbers, input_list_of_items):
    first = selectItem(input_list_of_items, input_list_of_numbers[0])
    second = selectItem(first[input_list_of_numbers[1]], 0)
    return second[input_list_of_numbers[2]]

displayList()

while (True):
    print(getSelectedItems(getNumbers(input("What would you like to select?")), content))

# display list of content
# get input <number>,<number> or <string-subject>, <number>
# get input option random which will pick a item at random to send

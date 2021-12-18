

import json
#import serial
from collections import OrderedDict
import random


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

def getRandSelectedItems(input_list_of_numbers, input_list_of_items):
    first = selectItem(input_list_of_items, input_list_of_numbers[0])
    second = selectItem(first[input_list_of_numbers[1]], 0)
    return second[random.randint(0, len(second) - 1)]

def printHelp():
    print("To select a thing to type do something like 0.0.0 where each number is an index to select \n")
    print("\tHelp Menu:")
    print(f'\tchar \t|\t full command \n')
    print(f'\td \t\t|\t display \t\t will display the full output of the content json')
    print(f'\th \t\t|\t help \t\t\t will display this menu')
displayList()

while (True):
    inputToCheck = input("What would you like to select?")
    if(inputToCheck == "help" or inputToCheck == "h"):
        printHelp()
    else:
        if(inputToCheck == "display" or inputToCheck == "d"):
            displayList()
        else:
            try:
                if(inputToCheck[-1] == '+'):
                    print(getRandSelectedItems(getNumbers(inputToCheck[0:-2]), content))
                else:
                    print(getSelectedItems(getNumbers(inputToCheck), content))
            except Exception as error:
                print("There was a problem with the command")
                continue

    print('\n')

# display list of content
# get input <number>,<number> or <string-subject>, <number>
# get input option random which will pick a item at random to send

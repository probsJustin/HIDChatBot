

import json


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
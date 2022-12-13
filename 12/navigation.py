#!/bin/python3

file = open("input", "r")
input = file.readlines()
file.close()


def getSteps(mapCpy, startPos):
    steps = 0
    currPos = startPos
    map = mapCpy
    while True:
        possibleDirs = [False, False, False, False]
        # look up
        if currPos[0] > 0 and (ord(map[y-1][x]) - 96) <= currHeight+1:
            possibleDirs[0] = True
        # Look down
        if currPos[0] < len(map)-1 and (ord(map[y+1][x]) - 96) <= currHeight+1:
            possibleDirs[1] = True
        # Look left
        if currPos[1] > 0 and (ord(map[y][x-1]) - 96) <= currHeight+1:
            possibleDirs[2] = True
        # Look right
        if currPos[1] < len(map[0])-1 and (ord(map[y][x+1]) - 96) <= currHeight+1:
            possibleDirs[3] = True
        for (i, val) in enumerate(possibleDirs):
            newPos = currPos
            if val is True:
                if i == 0:
                    newPos[0] -= 1
                    steps += getSteps(map, newPos)
                elif i == 1:
                    newPos[0] += 1
                    steps += getSteps(map, newPos)
                elif i == 2:
                    newPos[1] -= 1
                    steps += getSteps(map, newPos)
                elif i == 3:
                    newPos[1] += 1
                    steps += getSteps(map, newPos)

    return steps


map = []

for line in input:
    tmplist = []
    for char in line:
        if char != "\n":
            tmplist.append(char)
    map.append(tmplist)

currHeight = ord('a') - 96
currPos = [0, 0]
destPos = [0, 0]
steps = 0

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            currPos = [i, j]
            map[i][j] = "a"
        elif map[i][j] == "E":
            destPos = [i, j]
            map[i][j] = "z"

while currPos != destPos:
    x = currPos[1]
    y = currPos[0]
    
    print(currPos)
    
    steps += 1

print(steps)

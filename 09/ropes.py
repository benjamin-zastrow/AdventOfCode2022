#!/bin/python3

file = open("input", "r")
input = file.readlines()
file.close()

# Assignment 1

headPos = [0, 0]
tailPos = [0, 0]
visitedPos = []


def moveTail(headPos, tailPos):
    dX = headPos[0] - tailPos[0]
    dY = headPos[1] - tailPos[1]
    if (dX == 1 and dY == 2) or (dX == 2 and dY == 1) or (dX == 2 and dY == 2):
        tailPos[0] += 1
        tailPos[1] += 1
    elif (dX == 2 and dY == -1) or (dX == 1 and dY == -2) or (dX == 2 and dY == -2):
        tailPos[0] += 1
        tailPos[1] -= 1
    elif (dX == -1 and dY == 2) or (dX == -2 and dY == 1) or (dX == -2 and dY == 2):
        tailPos[0] -= 1
        tailPos[1] += 1
    elif (dX == -2 and dY == -1) or (dX == -1 and dY == -2) or (dX == -2 and dY == -2):
        tailPos[0] -= 1
        tailPos[1] -= 1
    elif dX == 2 and dY == 0:
        tailPos[0] += 1
    elif dX == -2 and dY == 0:
        tailPos[0] -= 1
    elif dY == 2 and dX == 0:
        tailPos[1] += 1
    elif dY == -2 and dX == 0:
        tailPos[1] -= 1
    return tailPos


for line in input:
    steps = int(line[2:line.find("\n")])
    direction = line[0]
    for i in range(steps):
        if direction == "U":
            headPos[1] += 1
        elif direction == "D":
            headPos[1] -= 1
        elif direction == "L":
            headPos[0] -= 1
        elif direction == "R":
            headPos[0] += 1
        tailPos = moveTail(headPos, tailPos)
        if tailPos not in visitedPos:
            visitedPos.append(tailPos.copy())

print(len(visitedPos))

# Assignment 2
headPos = [0, 0]
tailPos = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visitedPos = []

for line in input:
    steps = int(line[2:line.find("\n")])
    direction = line[0]
    for i in range(steps):
        if direction == "U":
            headPos[1] += 1
        elif direction == "D":
            headPos[1] -= 1
        elif direction == "L":
            headPos[0] -= 1
        elif direction == "R":
            headPos[0] += 1

        headPosTemp = headPos
        for i in range(10):
            tailPos[i] = moveTail(headPosTemp, tailPos[i])
            headPosTemp = tailPos[i]
        if tailPos[8] not in visitedPos:
            visitedPos.append(tailPos[8].copy())

print(len(visitedPos))


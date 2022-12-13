#!/bin/python3

from ast import literal_eval


def compareLists(a, b):
    # print("Comparing " + str(a) + " vs " + str(b))
    useLen = max(len(a), len(b))

    for i in range(useLen):
        if i >= len(a):
            return True
        if i >= len(b):
            return False

        if isinstance(a[i], int) and isinstance(b[i], int):
            if a[i] > b[i]:
                return False
            if a[i] < b[i]:
                return True
        elif isinstance(a[i], list) and isinstance(b[i], list):
            retval = compareLists(a[i], b[i])
            if retval is not None:
                return retval
        elif isinstance(a[i], int) and isinstance(b[i], list):
            tmpVal = a[i]
            a[i] = []
            a[i].append(tmpVal)
            retval = compareLists(a[i], b[i])
            if retval is not None:
                return retval
        elif isinstance(a[i], list) and isinstance(b[i], int):
            tmpVal = b[i]
            b[i] = []
            b[i].append(tmpVal)
            retval = compareLists(a[i], b[i])
            if retval is not None:
                return retval


file = open("input", "r")
input = file.readlines()
file.close()

pairs = []
correctCounter = 0

for line in input:
    if line != "\n":
        pairs.append(literal_eval(line.strip()))

tmpCounter = 1
locPairs = pairs.copy()
for i in range(0, len(pairs), 2):
    compareResult = compareLists(locPairs[i], locPairs[i+1])
    # print(str(tmpCounter) + ": " + str(compareResult))
    if(compareResult):
        correctCounter += tmpCounter
    tmpCounter += 1

print(correctCounter)


# Part 2
def bubbleSort(pairs):
    for i in range(len(pairs)-1):
        for j in range(0, len(pairs)-i-1):
            if compareLists(pairs[j+1], pairs[j]):
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]


strList = []
resolution = [-1, -1]
pairs += [[2]]
pairs += [[6]]
bubbleSort(pairs)

for (i, line) in enumerate(pairs):
    print(line)
    if line == [[[[2]]]]:
        resolution[0] = i+1
    elif line == [[[[6]]]]:
        resolution[1] = i+1

print(resolution[0] * resolution[1])

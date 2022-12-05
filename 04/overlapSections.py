#!/bin/python3

file = open("input", "r")
input = file.readlines()
file.close()

includeCounter = 0
overlapCounter = 0
for line in input:
    pos1 = line.find('-')
    e1_1 = int(line[0:pos1])
    pos2 = line.find(',')
    e1_2 = int(line[pos1+1:pos2])
    pos1 = line.find('-', pos2)
    e2_1 = int(line[pos2+1:pos1])
    e2_2 = int(line[pos1+1:])

    range1 = range(e1_1, e1_2+1)
    range2 = range(e2_1, e2_2+1)

    if (range1.start in range2 and range1[-1] in range2) or (range2.start in range1 and range2[-1] in range1):
        includeCounter = includeCounter + 1
    if len(range(max(range1[0], range2[0]), min(range1[-1], range2[-1])+1)) > 0:
        overlapCounter = overlapCounter + 1

print("Containing each other fully: " + str(includeCounter))
print("Overlapping each other: " + str(overlapCounter))

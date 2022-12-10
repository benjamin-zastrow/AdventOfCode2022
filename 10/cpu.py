#!/bin/python3

file = open("input", "r")
input = file.readlines()
file.close()

cycleResults = []
currX = 1

for line in input:
    if line[0] == 'n':
        cycleResults.append(currX)
    else:
        steps = int(line[5:line.find("\n")])
        for i in range(2):
            if i == 1:
                currX += steps
            cycleResults.append(currX)

res = 0
for i in range(20, 221, 40):
    res += cycleResults[i-2]*i

print(res)

cycleResults.insert(0, 1)
pic = str()
cnt = 0
for i in range(241):
    if cnt in range(cycleResults[i] - 1, cycleResults[i] + 2):
        pic += '#'
    else:
        pic += '.'
    cnt += 1
    if cnt % 40 == 0:
        pic += '\n'
        cnt = 0

print(pic)

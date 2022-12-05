#!/bin/python3

lists = [['R', 'G', 'H', 'Q', 'S', 'B', 'T', 'N'], ['H', 'S', 'F', 'D', 'P', 'Z', 'J'], ['Z', 'H', 'V'], ['M', 'Z', 'J', 'F', 'G', 'H'], ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R'], ['M', 'T', 'W', 'V', 'H', 'Z', 'J'], ['T', 'F', 'P', 'L', 'Z'], ['Q', 'V', 'W', 'S'], ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']]

file = open("input", "r")
input = file.readlines()
file.close()

for line in input:
    pos = line.find(" ")
    amount = int(line[pos+1:line.find(" ", pos+1)])
    pos = line.find(" ", pos+4)
    src = int(line[pos+1])
    pos = line.find(" ", pos+4)
    dest = int(line[pos+1])

    tmpList = list()
    for i in range(amount):
        tmpList.append(lists[src-1].pop())
    for i in range(amount):
        lists[dest-1].append(tmpList.pop())

for list in lists:
    print(list[-1])

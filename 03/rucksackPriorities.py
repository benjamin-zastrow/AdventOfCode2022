#!/bin/python3

file = open("input", "r")
input = file.readlines()
file.close()

sum = 0
for line in input:
    length = len(line) - 1
    first = line[0:int((length / 2))]
    last = line[int((length/2)):]
    char = None
    for i in first:
        if char is not None:
            break
        for j in last:
            if j == i:
                char = i
                break
    if char.islower():
        sum += ord(char) - 96
        print(str(char) + " -> " + str(ord(char) - 96))
    else:
        sum += ord(char) - 38
        print(str(char) + " -> " + str(ord(char) - 38))

print("Sum of all the priorities: " + str(sum))

sum = 0
for i in range(0, int(len(input) / 3)):
    char = set.intersection(*map(set, input[i*3:(((i+1)*3))]))
    char.remove('\n')
    for i in char:
        if i.islower():
            sum += ord(i) - 96
            print(str(i) + " -> " + str(ord(i) - 96))
        else:
            sum += ord(i) - 38
            print(str(i) + " -> " + str(ord(i) - 38))

print("Sum of all the priorities: " + str(sum))

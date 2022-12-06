#!/bin/python3

file = open("input", "r")
line = file.readline()
file.close()

buffer = list()
retval = -1
for (pos, char) in enumerate(line):
    buffer.append(char)
    if len(buffer) == 4:
        if buffer.count(buffer[0]) == 1 and buffer.count(buffer[1]) == 1 and buffer.count(buffer[2]) == 1 and buffer.count(buffer[3]) == 1:
            retval = pos+1
            break
        del buffer[0]

print("First occurence of four different chars at pos: " + str(retval))

for (pos, char) in enumerate(line):
    buffer.append(char)
    if len(buffer) == 14:
        if buffer.count(buffer[0]) == 1 and buffer.count(buffer[1]) == 1 and buffer.count(buffer[2]) == 1 and buffer.count(buffer[3]) == 1 and buffer.count(buffer[4]) == 1 and buffer.count(buffer[5]) == 1 and buffer.count(buffer[6]) == 1 and buffer.count(buffer[7]) == 1 and buffer.count(buffer[8]) == 1 and buffer.count(buffer[9]) == 1 and buffer.count(buffer[10]) == 1 and buffer.count(buffer[11]) == 1 and buffer.count(buffer[12]) == 1 and buffer.count(buffer[13]) == 1:
            retval = pos+1
            break
        del buffer[0]

print("First occurrence of 14 different characters at pos: " + str(retval))


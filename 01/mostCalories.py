#!/bin/python3

file = open("input", "r")

index = 0
list = list()
list.append(0)
for line in file:
    if len(line.strip()) == 0:
        index = index + 1
        list.append(0)
    else:
        list[index] += int(line)

print(max(list))

list.sort(reverse=True)
print(sum(list[0:3]))

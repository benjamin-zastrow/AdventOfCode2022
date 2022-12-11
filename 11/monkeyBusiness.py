#!/bin/python3

file = open("input", "r")
input = file.readlines()
file.close()

commonDiv = 1  # Assignment 2
monkeys = []
tmpMonkey = []
for line in input:
    if line[0] == "\n":
        tmpMonkey.append(0)
        monkeys.append(tmpMonkey)
        tmpMonkey = []
    elif line[0] == "M":
        tmpMonkey.append(int(line[line.find(" ")+1:line.find(":")]))
    elif line[2] == "S":
        sItems = []
        sPos = line.find(":") + 2
        while sPos != 1:
            sItems.append(int(line[sPos:sPos+2]))
            sPos = line.find(",", sPos) + 2
        tmpMonkey.append(sItems)
    elif line[2] == "O":
        op = line[line.find("d")+2:line.find("\n")]
        tmpMonkey.append(op)
    elif line[2] == "T":
        test = int(line[line.find("y")+2:line.find("\n")])
        tmpMonkey.append(test)
        commonDiv *= test  # Assignment 2
    elif line[8] == "r":
        tThrow = int(line[line.find("y")+2:line.find("\n")])
        tmpMonkey.append(tThrow)
    elif line[8] == "a":
        fThrow = int(line[line.find("y")+2:line.find("\n")])
        tmpMonkey.append(fThrow)

for i in range(10000):  # 20 Rounds in part 1, 10000 rounds in part 2
    for monkey in monkeys:
        for (j, item) in enumerate(monkey[1]):
            if monkey[2][0] == "+":
                item += int(monkey[2][2:4])
            elif monkey[2][0] == "-":
                item -= int(monkey[2][2:4])
            elif monkey[2][0] == "*":
                if monkey[2][2] == "o":
                    item *= item
                else:
                    item *= int(monkey[2][2:4])
            elif monkey[2][0] == "/":
                item /= int(monkey[2][2:4])
            # Reduction by division disabled for assignment 2
            # item /= 3
            item %= commonDiv
            monkey[1][j] = item
            monkey[6] += 1
            if item % monkey[3] == 0:
                monkeys[monkey[4]][1].append(item)
            elif item % monkey[3] != 0:
                monkeys[monkey[5]][1].append(item)
        monkey[1].clear()


resList = []
for i in monkeys:
    resList.append(i[6])

print(resList)
resList.sort(reverse=True)
print(resList[0]*resList[1])

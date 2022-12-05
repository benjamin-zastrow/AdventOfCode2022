#!/bin/python3

file = open("input", "r")
input = file.readlines()
file.close()

score = 0
for line in input:
    if line[2] == 'X':
        score += 1
        if line[0] == 'A':
            score += 3
        elif line[0] == 'B':
            score += 0
        elif line[0] == 'C':
            score += 6

    elif line[2] == 'Y':
        score += 2
        if line[0] == 'A':
            score += 6
        elif line[0] == 'B':
            score += 3
        elif line[0] == 'C':
            score += 0
    elif line[2] == 'Z':
        score += 3
        if line[0] == 'A':
            score += 0
        elif line[0] == 'B':
            score += 6
        elif line[0] == 'C':
            score += 3

print(score)


score2 = 0
for line in input:
    if line[2] == 'X':
        if line[0] == 'A':
            score2 += 3
        elif line[0] == 'B':
            score2 += 1
        elif line[0] == 'C':
            score2 += 2

    elif line[2] == 'Y':
        score2 += 3
        if line[0] == 'A':
            score2 += 1
        elif line[0] == 'B':
            score2 += 2
        elif line[0] == 'C':
            score2 += 3
    elif line[2] == 'Z':
        score2 += 6
        if line[0] == 'A':
            score2 += 2
        elif line[0] == 'B':
            score2 += 3
        elif line[0] == 'C':
            score2 += 1

print(score2)


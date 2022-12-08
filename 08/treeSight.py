#!/bin/python3

file = open("input", "r")
input = file.readlines()
file.close()

matrix = [[]]
visibility = [True, True, True, True]
visibilityCnt = 0

for (i, line) in enumerate(input):
    for char in line:
        if char != '\n':
            matrix[i].append(int(char))
    matrix.append(list())
matrix.pop()

for x in range(1, len(matrix)-1):
    for y in range(1, len(matrix[x])-1):
        ownHeight = matrix[x][y]
        # check upwards
        for i in range(x-1, -1, -1):
            if matrix[i][y] >= ownHeight:
                visibility[0] = False
                break
        # check downwards
        for i in range(x+1, len(matrix), 1):
            if matrix[i][y] >= ownHeight:
                visibility[1] = False
                break
        # check left
        for i in range(y-1, -1, -1):
            if matrix[x][i] >= ownHeight:
                visibility[2] = False
                break
        # check right
        for i in range(y+1, len(matrix[x]), 1):
            if matrix[x][i] >= ownHeight:
                visibility[3] = False
                break
        if True in visibility:
            visibilityCnt += 1
        visibility = [True, True, True, True]

visibilityCnt += 2*len(matrix) + 2*len(matrix[0]) - 4
print(visibilityCnt)

viewingDistances = [0, 0, 0, 0]
bestScenicScore = 0

for x in range(1, len(matrix)-1):
    for y in range(1, len(matrix[x])-1):
        viewingDistances = [0, 0, 0, 0]
        ownHeight = matrix[x][y]
        # check upwards
        for i in range(x-1, -1, -1):
            viewingDistances[0] += 1
            if matrix[i][y] >= ownHeight:
                break
        # check downwards
        for i in range(x+1, len(matrix), 1):
            viewingDistances[1] += 1
            if matrix[i][y] >= ownHeight:
                break
        # check left
        for i in range(y-1, -1, -1):
            viewingDistances[2] += 1
            if matrix[x][i] >= ownHeight:
                break

        # check right
        for i in range(y+1, len(matrix[x]), 1):
            viewingDistances[3] += 1
            if matrix[x][i] >= ownHeight:
                break

        scenicScore = viewingDistances[0]*viewingDistances[1]*viewingDistances[2]*viewingDistances[3]
        if scenicScore > bestScenicScore:
            bestScenicScore = scenicScore

print(bestScenicScore)

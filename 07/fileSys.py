#!/bin/python3

file = open("input", "r")
input = file.readlines()
file.close()


def Assignment1(currDir):
    retval = 0
    if currDir.getSize() <= 100000:
        retval += currDir.getSize()
    for i in currDir.getContents().values():
        if isinstance(i, Directory):
            retval += Assignment1(i)
    return retval


def Assignment2(currDir, needed):
    candidates = list()
    if currDir.getSize() > needed:
        candidates.append(currDir.getSize())
    for i in currDir.getContents().values():
        if isinstance(i, Directory):
            candidates.extend(Assignment2(i, needed))
    return candidates


class Directory:
    def __init__(self, path, parent=None):
        self.path = path
        self.contents = dict()
        self.parent = parent

    def addFile(self, name, size):
        self.contents.update({name: size})

    def addDir(self, name, parent):
        self.contents.update({name: Directory(self.path + name + "/", parent)})

    def getPath(self):
        return self.path

    def getContents(self):
        return self.contents

    def getParent(self):
        return self.parent

    def print(self):
        for key, value in self.contents.items():
            if isinstance(value, Directory):
                value.print()
            else:
                print(self.path + str(key) + " : " + str(value))

    def getSize(self):
        retval = 0
        for value in self.contents.values():
            if isinstance(value, Directory):
                retval += value.getSize()
            else:
                retval += int(value)
        return retval


currDir = Directory("/")
lsMode = False
for line in input:
    if line[0:7] == "$ cd ..":
        lsMode = False
        currDir = currDir.getParent()
    elif line[0:4] == "$ cd":
        lsMode = False
        chdir = line[5:line.find("\n")]
        currDir = currDir.getContents()[chdir]
    elif line[0:4] == "$ ls":
        lsMode = True
    elif lsMode is True:
        if line[0:3] == "dir":
            currDir.addDir(line[4:line.find("\n")], currDir)
        else:
            size = line[0:line.find(" ")]
            name = line[line.find(" ")+1:line.find("\n")]
            currDir.addFile(name, size)


while currDir.getParent() is not None:
    currDir = currDir.getParent()

print("Assignment 1: " + str(Assignment1(currDir)))

while currDir.getParent() is not None:
    currDir = currDir.getParent()

print("Total size: " + str(currDir.getSize()))
print("Free: " + str(70000000-currDir.getSize()))
needed = 30000000 - (70000000-currDir.getSize())
print("Needed for update: " + str(needed))
candidates = Assignment2(currDir, needed)
candidates.sort()
print("Assignment 2: " + str(candidates[0]))

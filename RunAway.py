import random
animatronicMap = [
    [" ", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", " ",  "_", "_"],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", ".", "."],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", ".", "."],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", ".", "."],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", ".", "."],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", ".", "."],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", ".", "."],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|", ".", "."],
    ["\\", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|", "_", "_"]
]



def createMap():
    global animatronicMap
    animatronicMap = [[], [], [], [], [], [], [], [], [], [], []]
    mapLength = random.randint(9, 60)
    print(mapLength)
    doorSpot = random.randint(1, 9)
    for i in range(11):
        if i == 0 or i == 10:
            for j in range(mapLength):
                if j == 0 and i == 0:
                    animatronicMap[i].append(" ")
                    continue
                elif j == 0 and i == 10:
                    animatronicMap[i].append("\\")
                    continue
                animatronicMap[i].append("_")
            
            if i == 0 and doorSpot != 0:
                animatronicMap[i].extend([" ", "_", "_"])
            elif i == 0 and doorSpot == 0:
                animatronicMap[i].extend(["_", "_", "_"])
            elif i == 10 and doorSpot != 9:
                animatronicMap[i].extend(["|", "_", "_"])
            elif i == 10 and doorSpot == 9:
                animatronicMap[i].extend(["_", "_", "_"])
            
        else:
            for j in range(mapLength):
                if j == 0:
                    animatronicMap[i].append("|")
                    continue
                animatronicMap[i].append(".")
            
            if i == doorSpot or i == doorSpot + 1:
                animatronicMap[i].extend([".", ".", "."])
            else:
                animatronicMap[i].extend(["|", ".", "."])
    
    print()

def printMap():
    for line in animatronicMap:
        #print("".join(line))
        printLine = []
        for thing in line:
            if thing == ".":
                printLine.append(" ")
            else:
                printLine.append(thing)
        #print(printLine)
        print("".join(printLine))

createMap()
printMap()
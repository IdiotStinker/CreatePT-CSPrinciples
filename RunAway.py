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

def spawnTable():
    tableSpawn = (random.randint(1, 9), random.randint(1, mapLength - 2))
    if animatronicMap[tableSpawn[0]][tableSpawn[1]] != ".":
        spawnTable()
        return
    
    animatronicMap[tableSpawn[0]][tableSpawn[1]] = "□"

    for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        if animatronicMap[tableSpawn[0] + dy][tableSpawn[1] + dx] != ".":
            continue

        if random.randint(0, 1) == 0:
            animatronicMap[tableSpawn[0] + dy][tableSpawn[1] + dx] = "⑁"
    


def createMap():
    global knockedOut
    knockedOut = False
    global animatronicMap
    animatronicMap = [[], [], [], [], [], [], [], [], [], [], []]
    global mapLength
    mapLength = random.randint(20, 60)
    #print(mapLength)
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
            
            if i == 0 and doorSpot != 1:
                animatronicMap[i].extend([" ", "_", "_"])
            elif i == 0 and doorSpot == 1:
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
    
    playerSpawn = (random.randint(1, 9), random.randint(1, 10))
    global playerPos
    playerPos = [playerSpawn[0], playerSpawn[1]]
    #animatronicMap[playerSpawn[0]][playerSpawn[1]] = "P"
    #animatronicMap[playerSpawn[0]][playerSpawn[1] + 1] = ""

    fredSpawn = (random.randint(1, 9), random.randint(mapLength - 5, mapLength - 2))
    global fredPos
    fredPos = [fredSpawn[0], fredSpawn[1]]
    #animatronicMap[fredSpawn[0]][fredSpawn[1]] = "F"

    for i in range(random.randint(3, 8)):
        spawnTable()
    
    

def printMap():
    for l, line in enumerate(animatronicMap):
        #print("".join(line))
        printLine = []
        for t, thing in enumerate(line):
            if [l, t] == [playerPos[0], playerPos[1]]:
                printLine.append("P")
            elif [l, t] == [fredPos[0], fredPos[1]]:
                printLine.append("F")
            elif thing == ".":
                printLine.append(" ")
            else:
                printLine.append(thing)
        #print(printLine)
        print("".join(printLine))

def playerTurn():
    global knockedOut
    if knockedOut:
        knockedOut = False
        return
    move = "defined"
    while not move in ["w", "a", "s", "d"]:
        move = input("What direction do you want to go? (wasd) ").lower()
        if move == "w":
            if animatronicMap[playerPos[0]-1][playerPos[1]] != "." or [playerPos[0]-1, playerPos[1]] == fredPos:
                move = "defined"
                continue
        if move == "a":
            if animatronicMap[playerPos[0]][playerPos[1]-1] != "." or [playerPos[0], playerPos[1]-1] == fredPos:
                move = "defined"
                continue
        if move == "s":
            if animatronicMap[playerPos[0]+1][playerPos[1]] != "." or [playerPos[0]+1, playerPos[1]] == fredPos:
                move = "defined"
                continue
        if move == "d":
            if animatronicMap[playerPos[0]][playerPos[1]+1] != "." or [playerPos[0], playerPos[1]+1] == fredPos:
                move = "defined"
                continue
    
    if move == "w":
        playerPos[0] -= 1
    if move == "a":
        playerPos[1] -= 1
    if move == "s":
        playerPos[0] += 1
    if move == "d":
        playerPos[1] += 1
    
    #printMap()
    #playerTurn()

def fredTurn():
    dy = playerPos[0] - fredPos[0]
    dx = playerPos[1] - fredPos[1]

    space = [animatronicMap[fredPos[0]-1][fredPos[1]] == "." and [fredPos[0]-1, fredPos[1]] != playerPos, animatronicMap[fredPos[0]][fredPos[1]+1] == "." and [fredPos[0], fredPos[1]+1] != playerPos, animatronicMap[fredPos[0]+1][fredPos[1]] == "." and [fredPos[0]+1, fredPos[1]] != playerPos, animatronicMap[fredPos[0]][fredPos[1]-1] == "." and [fredPos[0], fredPos[1]-1] != playerPos]
    up = space[0]
    right = space[1]
    down = space[2]
    left = space[3]
    #UP RIGHT DOWN LEFT

    while True:
        if abs(dy) > abs(dx) and dy < 0:
            if up:
                fredPos[0] -= 1
                return
            dy = 0
        if abs(dy) > abs(dx) and dy > 0:
            if down:
                fredPos[0] += 1
                return
            dy = 0
        if abs(dy) < abs(dx) and dx < 0:
            if left:
                fredPos[1] -= 1
                return
            dx = 0
        if abs(dy) < abs(dx) and dx > 0:
            if right:
                fredPos[1] += 1
                return
            dx = 0
        
        if abs(dy) == abs(dx):
            if dx > 0 and dy > 0:
                if (not right and down) or (right and not down):
                    if right:
                        fredPos[1] += 1
                        break
                    if down:
                        fredPos[0] += 1
                        break


                    
            if dx > 0 and dy < 0:
                if (not right and up) or (right and not up):
                    if right:
                        fredPos[1] += 1
                        break
                    if up:
                        fredPos[0] -= 1
                        break

            if dx < 0 and dy > 0:
                if (not left and down) or (left and not down):
                    if left:
                        fredPos[1] -= 1
                        break
                    if down:
                        fredPos[0] += 1
                        break

            if dx < 0 and dy < 0:
                if (not left and up) or (left and not up):
                    if left:
                        fredPos[1] -= 1
                        break
                    if down:
                        fredPos[0] -= 1
                        break


        
        if dy == 0 and dx == 0:
            print("both spots clogged")
            return
            #if space
            #if random.randint(0,1) == 0:

        #else:
            
    #elif abs(dx) > abs(dy):



def turn():
    playerTurn()
    fredTurn()
    printMap()

    

createMap()
printMap()
#playerTurn()
while True:
    turn()

print('dine?')
import random
import os
import math
from time import sleep

def spawnTable():
    tableSpawn = (random.randint(1, 9), random.randint(1, mapLength - 3))
    if animatronicMap[tableSpawn[0]][tableSpawn[1]] != ".":
        spawnTable()
        return
    
    animatronicMap[tableSpawn[0]][tableSpawn[1]] = "□"

    for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        if animatronicMap[tableSpawn[0] + dy][tableSpawn[1] + dx] != ".":
            continue

        if random.randint(0, 1) == 0:
            animatronicMap[tableSpawn[0] + dy][tableSpawn[1] + dx] = "⑁"
    
def spawnStunGun():
    stunGunSpawn = (random.randint(1, 9), random.randint(1, mapLength - 2))
    if animatronicMap[stunGunSpawn[0]][stunGunSpawn[1]] != ".":
        spawnStunGun()
        return

    animatronicMap[stunGunSpawn[0]][stunGunSpawn[1]] = "г"

def createMap():
    global sprint
    sprint = False
    global sprintMeter
    sprintMeter = 0
    global stunCount
    stunCount = 0
    global over
    over = False
    global knockedOut
    knockedOut = False
    global animatronicMap
    animatronicMap = [[], [], [], [], [], [], [], [], [], [], []]
    global mapLength
    mapLength = random.randint(20, 60)
    global stunned
    stunned = False
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
    animatronicMap[playerSpawn[0]][playerSpawn[1]] = "P"
    

    fredSpawn = (random.randint(1, 9), random.randint(mapLength - 5, mapLength - 2))
    global fredPos
    fredPos = [fredSpawn[0], fredSpawn[1]]
    animatronicMap[fredPos[0]][fredPos[1]] = "F"

    for i in range(random.randint(3, 8)):
        spawnTable()
    
    for i in range(random.randint(2, 5)):
        spawnStunGun()

    animatronicMap[fredPos[0]][fredPos[1]] = "."
    animatronicMap[playerSpawn[0]][playerSpawn[1]] = "."


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

def chargeSprint():
    terminalClear()
    print("Charging sprint.")
    sleep(1)
    print("Charging sprint..")
    sleep(1)
    print("Charging sprint...")

def grabStunGun(y, x):
    animatronicMap[y][x] = "."
    global stunCount
    stunCount += 1
    print(f"You collected one stun gun ammo! You currently have {stunCount}")

def fireStun():
    terminalClear()
    global stunCount
    if stunCount < 1:
        print("You don't have any stuns!")
        printMap()
        return
    dist = ((fredPos[0]-playerPos[0])**2 + (fredPos[1]-playerPos[1])**2)**(1/2)
    chance = 100 - 30 * math.log(dist) + dist
    if dist > 30:
        chance = 0
    if random.randint(1, 100) < round(chance):
        global stunned
        stunned = True
        print("Stunned!")
    else:
        if round(chance) < 0:
            print(f"You missed with a 0% chance! Try firing closer!")
        else:
            print(f"You missed with a {round(chance)}% chance!")
    printMap()
    stunCount-=1

def playerTurn():
    grabbedStunGun = False
    global knockedOut
    if knockedOut:
        knockedOut = False
        return
    move = "defined"
    while not move in ["w", "a", "s", "d", "fire", "sprint", "help"]:
        print(f"You can sprint with 'sprint', learn how this works with 'help'.")
        if stunCount >= 1:
            move = input("What direction do you want to go? (wasd), or would you like to use a stun gun (fire) ").lower()
        else:
            move = input("What direction do you want to go? (wasd) ").lower()
        if move == "w":
            if animatronicMap[playerPos[0]-1][playerPos[1]] != "." or [playerPos[0]-1, playerPos[1]] == fredPos:
                if animatronicMap[playerPos[0]-1][playerPos[1]] == "г":
                    grabbedStunGun = True
                    break
                move = "defined"
                continue
        if move == "a":
            if animatronicMap[playerPos[0]][playerPos[1]-1] != "." or [playerPos[0], playerPos[1]-1] == fredPos:
                if animatronicMap[playerPos[0]][playerPos[1]-1] == "г":
                    grabbedStunGun = True
                    break
                move = "defined"
                continue
        if move == "s":
            if animatronicMap[playerPos[0]+1][playerPos[1]] != "." or [playerPos[0]+1, playerPos[1]] == fredPos:
                if animatronicMap[playerPos[0]+1][playerPos[1]] == "г":
                    grabbedStunGun = True
                    break
                move = "defined"
                continue
        if move == "d":
            if animatronicMap[playerPos[0]][playerPos[1]+1] != "." or [playerPos[0], playerPos[1]+1] == fredPos:
                if animatronicMap[playerPos[0]][playerPos[1]+1] == "г":
                    grabbedStunGun = True
                    break
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
    
    if move == "fire":
        fireStun()
        playerTurn()
        return
    
    global sprint
    if move == "sprint" and not sprint:
        sprint = True
        chargeSprint()

    elif move == "sprint" and sprint:
        playerTurn()
        return

    terminalClear()

    if grabbedStunGun:
        grabStunGun(playerPos[0], playerPos[1])
    #printMap()
    #playerTurn()

def fredTurn():
    dy = playerPos[0] - fredPos[0]
    dx = playerPos[1] - fredPos[1]

    space = [animatronicMap[fredPos[0]-1][fredPos[1]] == ".", animatronicMap[fredPos[0]][fredPos[1]+1] == ".", animatronicMap[fredPos[0]+1][fredPos[1]] == ".", animatronicMap[fredPos[0]][fredPos[1]-1] == "."]
    up = space[0]
    right = space[1]
    down = space[2]
    left = space[3]
    #UP RIGHT DOWN LEFT

    dirs = 0
    for bool in space:
        if bool:
            dirs += 1
    
    if dirs == 0:
        print("woah! no movy")
    
    if dirs == 1:
        for b, bool in enumerate(space):
            if bool:
                if b == 0:
                    fredPos[0] -= 1
                elif b == 1:
                    fredPos[1] += 1
                elif b == 2:
                    fredPos[0] += 1
                elif b == 3:
                    fredPos[1] -= 1
                
                return

    if abs(dy) > abs(dx) and dy < 0:
        if up:
            fredPos[0] -= 1
            return
        #dy = 0
    if abs(dy) > abs(dx) and dy > 0:
        if down:
            fredPos[0] += 1
            return
        #dy = 0
    if abs(dy) < abs(dx) and dx < 0:
        if left:
            fredPos[1] -= 1
            return
        #dx = 0
    if abs(dy) < abs(dx) and dx > 0:
        if right:
            fredPos[1] += 1
            return
        #dx = 0
    

    if dy == 0:
        if dx > 0 and not right:
            if up and down:
                if random.randint(0,1) == 0:
                    fredPos[0]-=1
                else:
                    fredPos[0]+=1
                return
            
            if up:
                fredPos[0] -= 1
            
            if down:
                fredPos[0]+=1
            
            return
        
        if dx < 0 and not left:
            if up and down:
                if random.randint(0,1) == 0:
                    fredPos[0]-=1
                else:
                    fredPos[0]+=1
                return
            
            if up:
                fredPos[0] -= 1
            
            if down:
                fredPos[0]+=1
            
            return
        
    if dx == 0:
        if dy > 0 and not down:
            if left and right:
                if random.randint(0,1) == 0:
                    fredPos[1]-=1
                else:
                    fredPos[1]+=1
                return
            
            if left:
                fredPos[1] -= 1
            
            if right:
                fredPos[1]+=1
            
            return
        if dy < 0 and not up:
            if left and right:
                if random.randint(0,1) == 0:
                    fredPos[1]-=1
                else:
                    fredPos[1]+=1
                return
            
            if left:
                fredPos[1] -= 1
            
            if right:
                fredPos[1]+=1
            
            return


    #if abs(dy) == abs(dx):
    #    print("woah")

    if dx > 0 and dy > 0:
        if (not right and down) or (right and not down):
            if right:
                fredPos[1] += 1
                return
            if down:
                fredPos[0] += 1
                return

        if not right and not down:
            if abs(dy) == abs(dx):
                #Go left or up
                if random.randint(0, 1) == 0:
                    fredPos[0] -= 1
                else:
                    fredPos[1] -= 1
            #else go in specific
            elif abs(dy) > abs(dx):
                fredPos[1] -= 1
            elif abs(dx) > abs(dy):
                fredPos[0] -= 1

        if right and down:
            #Go right or down
            if random.randint(0, 1) == 0:
                fredPos[0] += 1
            else:
                fredPos[1] += 1
            
    if dx > 0 and dy < 0:
        if (not right and up) or (right and not up):
            if right:
                fredPos[1] += 1
                return
            if up:
                fredPos[0] -= 1
                return
        
        if not right and not up:
            if abs(dy) == abs(dx):
                #Go left or down
                if random.randint(0, 1) == 0:
                    fredPos[0] += 1
                else:
                    fredPos[1] -= 1

            elif abs(dy) > abs(dx):
                fredPos[1] -= 1
            elif abs(dx) > abs(dy):
                fredPos[0] += 1

        if right and up:
            #Go right or up
            if random.randint(0, 1) == 0:
                fredPos[0] -= 1
            else:
                fredPos[1] += 1

    if dx < 0 and dy > 0:
        if (not left and down) or (left and not down):
            if left:
                fredPos[1] -= 1
                return
            if down:
                fredPos[0] += 1
                return
        
        if not left and not down:
            if abs(dy) == abs(dx):
                #Go right or up
                if random.randint(0, 1) == 0:
                    fredPos[0] -= 1
                else:
                    fredPos[1] += 1

            elif abs(dy) > abs(dx):
                fredPos[1] += 1
            elif abs(dx) > abs(dy):
                fredPos[0] -= 1

        if left and down:
            #Go left or down
            if random.randint(0, 1) == 0:
                fredPos[0] += 1
            else:
                fredPos[1] -= 1


    if dx < 0 and dy < 0:
        if (not left and up) or (left and not up):
            if left:
                fredPos[1] -= 1
                return
            if up:
                fredPos[0] -= 1
                return
        
        if not left and not up:
            if abs(dy) == abs(dx):
                #Go right or down
                if random.randint(0, 1) == 0:
                    fredPos[0] += 1
                else:
                    fredPos[1] += 1

            elif abs(dy) > abs(dx):
                fredPos[1] += 1
            elif abs(dx) > abs(dy):
                fredPos[0] += 1

        if left and up:
            #Go left or up
            if random.randint(0, 1) == 0:
                fredPos[0] -= 1
            else:
                fredPos[1] -= 1

def checkGameOver():
    global fredPos
    global playerPos
    if fredPos == playerPos:
        return True

def terminalClear():
    os.system('cls' if os.name == 'nt' else 'clear')

def turn():
    printMap()
    if random.randint(1, 10) == 10:
        charge = True
        print("Fred is going to sprint, making SEVEN moves unless stunned.")
    else:
        charge = False
    
    sprintPrint = ""
    global sprintMeter

    if sprintMeter>0:
        sprintPrint +="\033[32m█"
    if sprintMeter>1:
        sprintPrint +="\033[31m█"
    if sprintMeter>2:
        sprintPrint +="\033[30m█"
    if sprintMeter>3:
        sprintPrint +="\033[34m█"
    if sprintMeter>4:
        sprintPrint +="\033[35m█"
    if sprintMeter>5:
        sprintPrint +="\033[36m█"
    if sprintMeter>6:
        sprintPrint +="\033[37m█"
    
    sprintPrint+="\003[30m "
    print(sprintPrint)
    global sprint
    if sprint:
        for i in range(sprintMeter):
            if i ==0:
                playerTurn()
                continue
            printMap()
            playerTurn()
        sprintMeter-=1
        if sprintMeter == 0:
            sprint = False
    else:
        sprintMeter+=1
        playerTurn()
    global stunned
    if not stunned:
        global over
        if charge:
            for i in range(7):
                fredTurn()
                if checkGameOver():
                    over = True
                    return
        else:
            for i in range(2):
                fredTurn()
                if checkGameOver():
                    over = True
                    return
    else:
        if random.randint(1, 3) == 3:
            stunned = False

terminalClear()
createMap()

while not over:
    turn()

terminalClear()
print("         _______________\n        |               |\n        |               |\n        |               |\n        |               |\n--------                 --------\n|                               |\n|                               |\n---------------------------------\n       |                 |\n       |   O         O   |\n       |                 |\n       |                 |\n       |      -----      |")
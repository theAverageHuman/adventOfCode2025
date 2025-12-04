file = open("input.txt")

grid = file.read().splitlines()
swapGrid = grid.copy()

def wallRemoveIteration():
    total = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == '@':
                nearbyRolls = 0
                if scan(x-1, y+1):
                    nearbyRolls += 1
                if scan(x, y+1):
                    nearbyRolls += 1
                if scan(x+1, y+1):
                    nearbyRolls += 1
                if scan(x+1, y):
                    nearbyRolls += 1
                if scan(x+1, y-1):
                    nearbyRolls += 1
                if scan(x, y-1):
                    nearbyRolls += 1
                if scan(x-1, y-1):
                    nearbyRolls += 1
                if scan(x-1, y):
                    nearbyRolls += 1
            
                if(nearbyRolls < 4):
                    total += 1
                    listBuffer = list(swapGrid[y]).copy()
                    listBuffer[x] = 'x'
                    swapGrid[y] = "".join(listBuffer)
    return total

def scan(x, y):
    hasRoll = False
    if(y >= 0) & (y < len(grid)):
        if(x >= 0) & (x < len(grid[y])):
            if grid[y][x] == '@':
                #print('(', x, ',', y, ') has a roll')
                hasRoll = True
    return hasRoll

sum = 0
numOfRolls = 10000

while numOfRolls != 0:
    numOfRolls = wallRemoveIteration()
    sum += numOfRolls
    grid = swapGrid.copy()
    
    #print(numOfRolls)
    #for i in range(0, len(grid)):
        #print(grid[i])

print(sum)

file.close()

import math

file = open("test.txt")

junctionBoxes = []
for line in file:
    junctionBoxes.append(line.strip().split(','))

for i in range(0, len(junctionBoxes)):
    otherCoords = junctionBoxes.copy()
    otherCoords.pop(i)

    minDist = 999999
    currentCoord = []
    for coord in otherCoords:
        currentDist = math.sqrt((int(junctionBoxes[i][0])-int(coord[0]))**2 + 
                                (int(junctionBoxes[i][1])-int(coord[1]))**2 + 
                                (int(junctionBoxes[i][2])-int(coord[2]))**2) 
        if currentDist < minDist:
            minDist = currentDist
            currentCoord = coord
    print(junctionBoxes[i])
    print(currentCoord)

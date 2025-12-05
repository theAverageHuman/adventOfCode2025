file = open("input.txt")

freshRanges = []
#IDs = []
rangesDone = False

for line in file:
    #print(line)
        
    if line == '\n':
        rangesDone = True
    elif rangesDone == False:
        freshRanges.append(line.replace('\n', '').split("-"))

#print(len(freshRanges))

#print(IDs)

freshRanges = sorted(freshRanges, key=lambda x: int(x[0]))

def consolidate(mergedRanges):
    global freshRanges

    blendedRanges = []
    hasMerged = False

    for i in range(1, len(freshRanges)):
        #print(freshRanges[i-1][1], " : ", freshRanges[i][0])
        if int(freshRanges[i-1][1]) > int(freshRanges[i][0]):
            mergedRanges.append([freshRanges[i-1][0], freshRanges[i][1]])
        
            if blendedRanges.count(i) == 0:
                blendedRanges.append(i)
            if blendedRanges.count(i-1) == 0:
                blendedRanges.append(i-1)

            hasMerged = True

    blendedRanges = sorted(blendedRanges, reverse=True)
    #print(blendedRanges)
    for i in blendedRanges:
        #print(len(mergedRanges))
        #print(i)
        #print(mergedRanges[i])
        mergedRanges.pop(i)

    mergedRanges = sorted(mergedRanges, key=lambda x: int(x[0]))
    #print(mergedRanges)
    freshRanges = mergedRanges.copy()
    return hasMerged
 
#print(freshRanges)

while consolidate(freshRanges.copy()) == True:
    magicNum = 0

total = 0
for rangee in freshRanges:
    total += len(range(int(rangee[0]), int(rangee[1])+1))
print(total)

file.close()


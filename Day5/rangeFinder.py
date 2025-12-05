file = open("test.txt")

def consolidate():
    for i in range(1, len(freshRanges)):
        #print(freshRanges[i-1][1], " : ", freshRanges[i][0])
        if int(freshRanges[i-1][1]) > int(freshRanges[i][0]):
            mergedRanges.append([freshRanges[i-1][0], freshRanges[i][1]])
        
            if blendedRanges.count(i) == 0:
                blendedRanges.append(i)
            if blendedRanges.count(i-1) == 0:
                blendedRanges.append(i-1)

    #print(blendedRanges)
    for i in blendedRanges:
        mergedRanges.pop(i)

    mergedRanges = sorted(mergedRanges, key=lambda x: int(x[0]))

   

freshRanges = []
#IDs = []
rangesDone = False

for line in file:
    #print(line)
        
    if line == '\n':
        rangesDone = True
    elif rangesDone == False:
        freshRanges.append(line.replace('\n', '').split("-"))

#print(IDs)

freshRanges = sorted(freshRanges, key=lambda x: int(x[0]))
mergedRanges = freshRanges.copy()

blendedRanges = []

for i in range(1, len(freshRanges)):
    #print(freshRanges[i-1][1], " : ", freshRanges[i][0])
    if int(freshRanges[i-1][1]) > int(freshRanges[i][0]):
        mergedRanges.append([freshRanges[i-1][0], freshRanges[i][1]])
        
        if blendedRanges.count(i) == 0:
            blendedRanges.append(i)
        if blendedRanges.count(i-1) == 0:
            blendedRanges.append(i-1)

#print(blendedRanges)
for i in blendedRanges:
    mergedRanges.pop(i)

mergedRanges = sorted(mergedRanges, key=lambda x: int(x[0]))

print(freshRanges)
print(mergedRanges)
file.close()


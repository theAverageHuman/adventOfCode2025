file = open("input.txt")

freshRanges = []
IDs = []
rangesDone = False

for line in file:
    #print(line)
        
    if line == '\n':
        rangesDone = True
    elif rangesDone:
        IDs.append(line.replace('\n', ' '))
    else:
        freshRanges.append(line.replace('\n', '').split("-"))

#print(freshRanges)
#print(IDs)

count = 0
for ID in IDs:
    inRange = False

    for ranges in freshRanges:
        if (int(ID) >= int(ranges[0])) & (int(ID) <= int(ranges[1])):
            inRange = True
    if inRange:
        count += 1

print(count)
file.close()

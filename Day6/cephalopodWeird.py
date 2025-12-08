file = open("input.txt")
grid = []
columns = []
operatorLocs = []
operations = []

maxLength = 0
for line in file:
    if len(line) > maxLength:
        maxLength = len(line)

#print(maxLength)

file.seek(0)
for line in file:
    grid.append(line.ljust(maxLength, " "))

#for line in grid:
    #print("/" + line + "/")

for i in range(0, maxLength):
    thinColumn = ""
    for row in grid:
        thinColumn = thinColumn + row[i]
    columns.append(thinColumn.rstrip())

for x in range(0, len(columns)):
    if len(columns[x]) > 0:
        if (columns[x][len(columns[x])-1] == "+") or (columns[x][len(columns[x])-1] == "*"):
            operatorLocs.append(x)
operatorLocs.append(len(columns)-1)
#print(operatorLocs)

for i in range(1, len(operatorLocs)):
    currentOp = []
    for line in grid:
        currentOp.append(line[operatorLocs[i-1]:operatorLocs[i]])
    currentOp[len(currentOp)-1] = currentOp[len(currentOp)-1].rstrip()
    #print(currentOp)
    operations.append(currentOp)

totalSum = 0
for equation in operations:
    actualNums = []
    #print(equation)
    #print(len(equation[0]))

    for i in range(0, len(equation[0])):
        digits = ""
        for numLoc in range(0, len(equation)-1):
            digits += equation[numLoc][i]
        #print(digits)
        actualNums.append(digits.strip())

    sum = 0
    match equation[len(equation)-1]:
        case '*':
            base = 1
            for num in actualNums:
                if num.isnumeric():
                    #print(num + "*")
                    base *= int(num)
            sum = base
        case '+':
            total = 0
            for num in actualNums:
                if num.isnumeric():
                    #print(num + "+")
                    total += int(num)
            sum = total
    #print(sum)
    totalSum += sum
print(totalSum)
    

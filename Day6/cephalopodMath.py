file = open("input.txt")
grid = []
equations = []

for line in file:
    grid.append(line.split())

#for column in grid:
    #print(column)

for i in range(0, len(grid[0])):
    question = []
    for row in grid:
        question.append(row[i])
    equations.append(question)

grandTotal = 0

for question in equations:
    #print(question)

    finalNum = 0
    match question[len(question)-1]:
        case '*':
            mult = 1
            for num in question:
                if num.isnumeric():
                    mult = mult*int(num)
            finalNum = mult
        case '+':
            total = 0
            for num in question:
                if num.isnumeric():
                    total += int(num)
            finalNum = total
    #print(finalNum)
    grandTotal += finalNum

print(grandTotal)

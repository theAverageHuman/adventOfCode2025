import re

file = open("test.txt")
grid = []
equations = []

for line in file:
    grid.append(re.split(r('\s+'), line))

for column in grid:
    print(column)
'''
for i in range(0, len(grid[0])):
    question = []
    for row in grid:
        question.append(row[i])
    equations.append(question)

grandTotal = 0

def getNumbers(question):
    maxLen = 0
    for digits in question:
        if len(digits) > maxLen:
            maxLen = len(digits)
    
    numbers = []
    for i in range(0, maxLen):
        newDigits = ""
        for digits in question:
            if i < len(digits):
                if digits[len(digits)-i-1].isnumeric():
                    newDigits = newDigits + digits[len(digits)-i-1]
        numbers.append(newDigits)
    return numbers


for question in equations:
    #print(question)

    finalNum = 0
    match question[len(question)-1]:
        case '*':
            mult = 1
            for num in getNumbers(question):
                mult = mult*int(num)
            finalNum = mult
        case '+':
            total = 0
            for num in getNumbers(question):
                total += int(num)
            finalNum = total
    #print(finalNum)
    grandTotal += finalNum

print(grandTotal)
getNumbers(equations[0])'''

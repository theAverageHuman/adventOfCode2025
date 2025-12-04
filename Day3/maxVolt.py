file = open("test.txt")

batteryBanks = file.read().splitlines()

total = 0

for bank in range(0, len(batteryBanks)):
    max = 0
    maxLoc = 0
    for i in range(0, len(batteryBanks[bank])):
        if int(batteryBanks[bank][i]) > max:
            max = int(batteryBanks[bank][i])
            maxLoc = i
    doubleDigits = str(max)

    batteryBanks[bank] = batteryBanks[bank][maxLoc:]
    print(batteryBanks[bank])
    
    max = 0
    maxLoc = 0
    for i in range(0, len(batteryBanks[bank])):
        if int(batteryBanks[bank][i]) > max:
            max = int(batteryBanks[bank][i])
            maxLoc = i
    doubleDigits += str(max)
    #print(doubleDigits)

    total += int(doubleDigits)

print(total)

file.close()

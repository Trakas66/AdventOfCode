file = open(r'../day2.txt')
input = file.readlines()
file.close()

def getIsIncreasing(line):
    numInc, numDec = 0, 0
    for i in range(3):
        if line[i] < line[i+1]:
            numInc += 1
        elif line[i] > line[i+1]:
            numDec += 1
    if numInc > numDec:
        return True
    return False

def checkFollowSequence(num1, num2, isIncreasing):
    if isIncreasing and num1 >= num2:
        return False
    if not isIncreasing and num1 <= num2:
        return False
    return True

def checkIsSafe(isIncreasing, line):
    numRemoved, i = 0, 0
    while i < (len(line)-1):
        isValid = True
        if abs(line[i] - line[i+1]) > 3:
            isValid = False
        elif not checkFollowSequence(line[i], line[i+1], isIncreasing):
            isValid = False

        if not isValid:
            if numRemoved == 1:
                return False
            
            numRemoved = 1
            if i == len(line)-2:
                return True
            elif abs(line[i] - line[i+2]) <= 3 and checkFollowSequence(line[i], line[i+2], isIncreasing):
                i += 2
                continue
            elif i == 0:
                i += 1
                continue
            elif abs(line[i-1] - line[i+1]) <= 3 and checkFollowSequence(line[i-1], line[i+1], isIncreasing):
                continue
            else:
                return False
        else:
            i += 1
    return True

def isSafe(line):
    isIncreasing = getIsIncreasing(line)
    return checkIsSafe(isIncreasing, line)

totalSafe = 0
for line in input:
    line = line.split()
    line = [int(x) for x in line]

    if isSafe(line):
        totalSafe += 1

print(totalSafe)

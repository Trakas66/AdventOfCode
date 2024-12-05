sum = 0
gearbox = []
line = "new"
while line != "":
    line = input()
    gearbox.append(line)
gearbox.pop(-1)

def getNum(i, j):
    start = 0
    end = 0
    loop = True
    while loop:
        if (j+start-1) >= 0 and gearbox[i][j+start-1].isnumeric():
            start -= 1
        elif (j+end+1) < len(gearbox[i]) and gearbox[i][j+end+1].isnumeric():
            end += 1
        else:
            loop = False
    num = 0
    for k in range(start, end+1):
        num *= 10
        num += int(gearbox[i][j+k])
    return num

for i in range(len(gearbox)):
    for j in range(len(gearbox[i])):
        if gearbox[i][j] != '*':
            continue
        isGear = False
        checkDiagUp = True
        checkDiagDown = True
        nums = []

        if i > 0:
            if gearbox[i-1][j].isnumeric():
                checkDiagUp = False
                nums.append(getNum(i-1, j))
        else:
            checkDiagUp = False

        if i < len(gearbox)-1:
            if gearbox[i+1][j].isnumeric():
                checkDiagDown = False
                nums.append(getNum(i+1, j))
        else:
            checkDiagDown = False

        if j > 0:
            if gearbox[i][j-1].isnumeric():
                nums.append(getNum(i, j-1))

        if j < len(gearbox[i])-1:
            if gearbox[i][j+1].isnumeric():
                nums.append(getNum(i, j+1))

        if checkDiagUp:
            for k in [-1, 1]:
                if (j+k) < 0 or (j+k) > len(gearbox[i-1]):
                    continue
                if gearbox[i-1][j+k].isnumeric():
                    nums.append(getNum(i-1, j+k))

        if checkDiagDown:
            for k in [-1, 1]:
                if (j+k) < 0 or (j+k) > len(gearbox[i+1]):
                    continue
                if gearbox[i+1][j+k].isnumeric():
                    nums.append(getNum(i+1, j+k))
        
        if len(nums) == 2:
            gearRatio = nums[0] * nums[1]
            sum += gearRatio

print(sum)

import itertools

sum = 0

def checkConfig(line, nums):
    count = 0
    numCount = 0
    for i in range(len(line)):
        if line[i] == "#":
            count += 1
        else:
            if count > 0:
                if nums[numCount] == count:
                    numCount += 1
                    count = 0
                else:
                    return False
    if count > 0:
        if numCount < len(nums):
            if nums[numCount] == count:
                numCount += 1
                count = 0
    if numCount == len(nums):
        return True
    return False

while 1:
    line = input()
    if line == "":
        break
    parts = line.split()
    nums = parts[1].strip().split(",")
    nums = [(lambda x: int(x))(x) for x in nums]
    line = parts[0]
    marks = []
    numDamaged = 0
    for i in range(len(line)):
        if line[i] == "?":
            marks.append(i)
        elif line[i] == "#":
            numDamaged += 1
    for i in range(len(nums)):
        numDamaged -= nums[i]
    numDamaged = 0 - numDamaged

    combs = list(itertools.combinations(marks, numDamaged))
    for i in range(len(combs)):
        newLine = ""
        for j in range(len(line)):
            if j in combs[i]:
                newLine += "#"
            elif j in marks:
                newLine += "."
            else:
                newLine += line[j]
        if checkConfig(newLine, nums):
            sum += 1

print(sum)

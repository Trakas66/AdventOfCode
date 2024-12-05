sum = 0
line = "new"
while True:
    line = input().split(": ")
    if line[0] == "":
        break

    allNums = line[1].split("|")
    winNums = [(lambda x: int(x))(x) for x in allNums[0].strip().split()]
    nums = [(lambda x: int(x))(x) for x in allNums[1].strip().split()]

    cValue = 0

    for num in nums:
        if num in winNums:
            if cValue == 0:
                cValue = 1
            else:
                cValue *= 2

    sum += cValue

print(sum)

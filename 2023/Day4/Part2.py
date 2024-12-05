sum = 0
line = "new"
cards = {}
while True:
    line = input().split(": ")
    if line[0] == "":
        break

    gameNum = int(line[0].split()[1])

    if gameNum not in cards:
        cards[gameNum] = 1
    else:
        cards[gameNum] += 1
    
    allNums = line[1].split("|")
    winNums = [(lambda x: int(x))(x) for x in allNums[0].strip().split()]
    nums = [(lambda x: int(x))(x) for x in allNums[1].strip().split()]

    value = 0

    for num in nums:
        if num in winNums:
            value += 1
            if (gameNum + value) not in cards:
                cards[gameNum+value] = cards[gameNum]
            else:
                cards[gameNum+value] += cards[gameNum]

    sum += cards[gameNum]

print(sum)

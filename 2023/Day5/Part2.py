seeds = []
line = input().split(":")[1].strip().split()
for i in range(0, len(line), 2):
    seeds.append((int(line[i]), int(line[i+1])))
dicts = [{} for i in range(7)]


def findSeeds(num):
    for i in range(len(seeds)):
        if seeds[i][0] <= num and seeds[i][0] + seeds[i][1] >= num:
            return True
    return False

def getPrevious(index, num):
    for key, item in dicts[index].items():
        if item[0] <= num and item[0] + item[1] >= num:
            return key + num - item[0] + 1
    return -1

def checkAnswer(num):
    for i in range(6, -1, -1):
        pNum = getPrevious(i, num)
        if pNum != -1:
            num = pNum
    if findSeeds(num):
        return True
    else:
        return False

dictsi = -1
numBlank = 0

while 1:
    line = input()
    if line == "":
        numBlank += 1
        if numBlank == 2:
            break
        continue
    else:
        numBlank = 0

    if ":" in line:
        dictsi += 1
        continue

    nums = [(lambda x: int(x))(x) for x in line.split()]
    dicts[dictsi][nums[1]] = (nums[0], nums[2])

i = 52210644
found = False
while not found:
    if checkAnswer(i):
        print(i)
        found = True
    else:
        i += 1

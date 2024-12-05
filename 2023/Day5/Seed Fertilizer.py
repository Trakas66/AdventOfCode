seeds = [(lambda x: int(x))(x) for x in input().split(":")[1].strip().split()]
valid = [True for i in range(len(seeds))]
line = input()
numBlank = 0

while 1:
    line = input()
    if ":" in line:
        valid = [True for i in range(len(seeds))]
        continue
    if line == "":
        numBlank += 1
        if numBlank == 2:
            break
        else:
            continue

    numBlank = 0

    nums = [(lambda x: int(x))(x) for x in line.split()]
    for i in range(len(seeds)):
        if valid[i] and seeds[i] >= nums[1] and seeds[i] < nums[1] + nums[2]:
            seeds[i] = nums[0] + (seeds[i]-nums[1])
            valid[i] = False

print(min(seeds))

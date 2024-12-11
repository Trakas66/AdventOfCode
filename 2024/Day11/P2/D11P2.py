file = open(r'../day11.txt')
input = file.read().strip()
file.close()

stones = [int(stone) for stone in input.split()]
nums = {}
for i in range(len(stones)):
    if stones[i] in nums:
        nums[stones[i]] += 1
    else:
        nums[stones[i]] = 1

for _ in range(75):

    newNums = {}
    for key in nums:
        if key == 0:
            if 1 in newNums:
                newNums[1] += nums[key]
            else:
                newNums[1] = nums[key]
        elif len(str(key)) % 2 == 0:
            length = len(str(key))
            key1 = int(str(key)[:int(length/2)])
            key2 = int(str(key)[int(length/2):])
            if key1 in newNums:
                newNums[key1] += nums[key]
            else:
                newNums[key1] = nums[key]
            if key2 in newNums:
                newNums[key2] += nums[key]
            else:
                newNums[key2] = nums[key]
        else:
            key3 = key*2024
            if key3 in newNums:
                newNums[key3] += nums[key]
            else:
                newNums[key3] = nums[key]
    nums = newNums

total = 0
for _, value in nums.items():
    total += value

print(total)

file = open(r'../day7.txt')
input = file.readlines()
file.close()

def checkForSolution(total, nums, result, i):
    if i == len(nums):
        if total == result:
            return True
        else:
            return False
    if total > result:
        return False
    concat = int(str(total) + str(nums[i]))
    return checkForSolution(total + nums[i], nums, result, i+1) or checkForSolution(total * nums[i], nums, result, i+1) or checkForSolution(concat, nums, result, i+1)

total = 0
for line in input:
    line = line.strip().split(':')
    nums = [int(x) for x in line[1].split()]
    result = int(line[0])
    if checkForSolution(nums[0], nums, result, 1):
        total += result

print(total)

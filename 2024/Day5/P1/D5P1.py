file = open(r'../day5.txt')
input = file.readlines()
file.close()

depend = {}
i = 0
line = input[i].strip()
while line != "":
    nums = line.split('|')
    if nums[1] in depend:
        depend[nums[1]].append(nums[0])
    else:
        depend[nums[1]] = [nums[0]]
    i += 1
    line = input[i].strip()
i += 1

total = 0
while i < len(input):

    line = input[i].strip().split(',')
    found = []
    for num in line:
        if num in depend:
            isValid = True
            for d in depend[num]:
                if d in line and not d in found:
                    isValid = False
                    break
            if not isValid:
                break
        found.append(num)

    if len(found) == len(line):
        middle = int(len(found) / 2)
        total += int(found[middle])

    i += 1

print(total)

file = open(r'../day5.txt')
input = file.readlines()
file.close()

def fixLine(line, depend):

    i = 0
    found = []
    while i < len(line):
        if line[i] not in depend:
            found.append(line[i])
            i += 1
            continue
        for num in depend[line[i]]:
            if num in line and num not in found:
                line.remove(num)
                line.insert(i, num)
                break
        else:
            found.append(line[i])
            i += 1
    
    return line

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

invalid = []
while i < len(input):

    found = []
    line = input[i].strip().split(',')
    for num in line:
        if num in depend:
            isValid = True
            for d in depend[num]:
                if d in line and not d in found:
                    isValid = False
                    break
            if not isValid:
                invalid.append(line)
                break
        found.append(num)

    i += 1

total = 0
for line in invalid:
    line = fixLine(line, depend)

    middle = int(len(line)/2)
    total += int(line[middle])

print(total)

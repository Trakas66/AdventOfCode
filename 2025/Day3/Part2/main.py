filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

sum = 0

for line in input:
    maxNums = [int(line[i]) for i in range(12)]
    length = len(line)

    for i in range(12, length):
        num = int(line[i])

        for j in range(11):
            if maxNums[j] < maxNums[j+1]:
                for k in range(j, 11):
                    maxNums[k] = maxNums[k+1]
                maxNums[-1] = num
                break
        else:
            if num > maxNums[-1]:
                maxNums[-1] = num
    
    joltage = ""
    for i in range(12):
        joltage += str(maxNums[i])
    joltage = int(joltage)
    sum += joltage

print(sum)
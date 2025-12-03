filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

sum = 0

for line in input:
    max1 = int(line[0])
    max2 = int(line[1])
    length = len(line)

    for i in range(2, length):
        num = int(line[i])

        if max2 > max1:
            max1 = max2
            max2 = num
        elif num > max2:
            max2 = num
    
    sum += int(str(max1) + str(max2))

print(sum)
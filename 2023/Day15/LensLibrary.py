sum = 0

line = input().split(",")

for i in range(len(line)):
    currentValue = 0
    for j in range(len(line[i])):
        currentValue += ord(line[i][j])
        currentValue *= 17
        currentValue = currentValue % 256
    sum += currentValue

print(sum)

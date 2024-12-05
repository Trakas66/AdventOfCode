sum = 0
galaxies = []
row = 0
colCount = {}
colNum = 0
scale = 1000000

while 1:
    line = input()
    if line == "":
        break
    colNum = len(line)
    count = 0
    for i in range(len(line)):
        if line[i] == "#":
            galaxies.append((row, i))
            count += 1
            if i in colCount:
                colCount[i] += 1
            else:
                colCount[i] = 1
    if count == 0:
        row += scale
    else:
        row += 1

for i in range(colNum-1, -1, -1):
    if i in colCount:
        continue
    for j in range(len(galaxies)):
        if galaxies[j][1] >= i:
            galaxies[j] = (galaxies[j][0], galaxies[j][1]+scale-1)

for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        dist = abs(galaxies[j][0]-galaxies[i][0]) + abs(galaxies[j][1]-galaxies[i][1])
        sum += dist

print(sum)

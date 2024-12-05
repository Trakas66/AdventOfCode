sum = 0
gearbox = []
line = "new"
while line != "":
    line = input()
    gearbox.append(line)
gearbox.pop(-1)

num = 0
inNum = False
validNum = False
for i in range(len(gearbox)):
    for j in range(len(gearbox[i])):
        if gearbox[i][j].isnumeric():
            if inNum:
                num *= 10
                num += int(gearbox[i][j])
            else:
                num = int(gearbox[i][j])
                inNum = True
            if not validNum:
                for k in range(-1,2):
                    for l in range(-1,2):
                        if (i+k) < 0 or (i+k) >= len(gearbox):
                            continue
                        elif (j+l) < 0 or (j+l) >= len(gearbox[i+k]):
                            continue
                        if (not gearbox[i+k][j+l].isnumeric()) and gearbox[i+k][j+l] != '.':
                            validNum = 1
                            break
                    else:
                        continue
                    break
        else:
            if validNum:
                sum += num
            inNum = False
            validNum = False

print(sum)

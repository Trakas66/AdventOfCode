sum = 0
cubes = {"red":0, "blue":0, "green":0}
line = "new"
num = 0
while 1:
    
    cubes["red"] = 0
    cubes["blue"] = 0
    cubes["green"] = 0
    line = input().split(" ")
    if len(line) < 2:
        break
    ID = int(line[1][:-1])

    for i in range(2, len(line)):
        if line[i].isnumeric():
            num = int(line[i])
            continue
        if i != len(line)-1:
            if num > cubes[line[i][:-1]]:
                cubes[line[i][:-1]] = num
        else:
            if num > cubes[line[i]]:
                cubes[line[i]] = num

    if cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14:
        sum += ID

print(sum)

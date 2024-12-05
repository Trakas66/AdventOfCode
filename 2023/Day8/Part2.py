import math

count = 0
seq = []
myMap = {}
current = []
found = []

line = input()
for char in line:
    if char == "L":
        seq.append(0)
    else:
        seq.append(1)

line = input() #empty line

while 1:
    line = input()
    if line == "":
        break

    keys = line.split(" = ")
    keys[1] = keys[1].strip("()").split(", ")

    myMap[keys[0]] = (keys[1][0], keys[1][1])
    if keys[0][-1] == "A":
        current.append(keys[0])

while 1:
    endLoop = True
    n = count % len(seq)
    for i in range(len(current)-1, -1, -1):
        current[i] = myMap[current[i]][seq[n]]
        if current[i][-1] != "Z":
            endLoop = False
        else:
            current.pop(i)
            found.append(count+1)
    count += 1
    if endLoop:
        break
lcm = 1
for num in found:
    lcm = math.lcm(lcm, num)

print(lcm)

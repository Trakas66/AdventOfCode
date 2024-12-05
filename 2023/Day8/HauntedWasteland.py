count = 0
seq = []
myMap = {}

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


current = "AAA"
while current != "ZZZ":
    n = count % len(seq)
    current = myMap[current][seq[n]]
    count += 1

print(count)

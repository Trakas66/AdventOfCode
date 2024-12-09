file = open(r'../day9.txt')
input = file.read()
file.close()

mem = []
fid = 0
isFile = True
for num in input:
    num = int(num)
    if isFile:
        for i in range(num):
            mem.append(fid)
        fid += 1
        isFile = False
    else:
        for i in range(num):
            mem.append(-1)
        isFile = True

free = 0
cur = len(mem)-1
while free < cur:
    while mem[free] != -1:
        free += 1
    while mem[cur] == -1:
        cur -= 1
    if free < cur:
        mem[free] = mem[cur]
        mem[cur] = -1

total = 0
i = 0
while mem[i] != -1:
    total += mem[i] * i
    i += 1

print(total)

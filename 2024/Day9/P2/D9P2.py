file = open(r'../day9.txt')
input = file.read()
file.close()

mem = []
fid = 0
isFile = True
for num in input:
    num = int(num)
    if isFile:
        mem.append((num, fid))
        fid += 1
        isFile = False
    else:
        mem.append((num, -1))
        isFile = True

free = 0
low = 0
cur = len(mem)
while cur > low:
    cur -= 1
    if mem[cur][1] == -1:
        continue
    size = mem[cur][0]
    while mem[low][1] != -1:
        low += 1
    free = low
    while free < cur and (mem[free][1] != -1 or mem[free][0] < size):
        free += 1
    if free == cur:
        continue
    temp = mem[cur]
    mem[free] = (mem[free][0] - size, mem[free][1])
    mem[cur] = (size, -1)
    mem.insert(free, temp)

total = 0
count = 0
for item in mem:
    if item[1] == -1:
        count += item[0]
        continue
    for i in range(item[0]):
        total += item[1] * count
        count += 1

print(total)

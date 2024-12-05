sum = 0
seqs = []

while 1:
    seqs = []
    line = input()
    if line == "":
        break
    line = line.split()
    seqs.append([(lambda x: int(x))(x) for x in line])
    i = 0
    while 1:
        new = []
        for j in range(len(seqs[i])-1):
            new.append(seqs[i][j+1]-seqs[i][j])
        seqs.append(new)
        if all(x == 0 for x in new):
            break
        i += 1
    num = 0
    for j in range(i, -1, -1):
        num += seqs[j][-1]
    sum += num

print(sum)

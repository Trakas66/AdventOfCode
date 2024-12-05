sum = 0
patterns = []

def compareCols(pattern, col1, col2):
    count = 0
    for i in range(len(pattern)):
        if pattern[i][col1] != pattern[i][col2]:
            count += 1
    return count

def compareRows(row1, row2):
    count = 0
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            count += 1
    return count

pattern = []
while 1:
    line = input()
    if line == "":
        if len(pattern) == 0:
            break
        patterns.append(pattern)
        pattern = []
        continue
    pattern.append(line)

for pattern in patterns:
    found = False
    #rows
    for i in range(len(pattern)-1):
        count = compareRows(pattern[i], pattern[i+1])
        if count < 2:
            a,b=i-1,i+2
            sym = True
            while a >= 0 and b < len(pattern):
                count += compareRows(pattern[a], pattern[b])
                if count > 1:
                    sym = False
                    break
                a -= 1
                b += 1
            if sym and count == 1:
                sum += (100*(i+1))
                found = True
                break
    if found:
        continue
    #columns
    for i in range(len(pattern[0])-1):
        count = compareCols(pattern, i, i+1)
        if count < 2:
            a,b=i-1,i+2
            sym = True
            while a >= 0 and b < len(pattern[0]):
                count += compareCols(pattern, a, b)
                if count > 1:
                    sym = False
                    break
                a -= 1
                b += 1
            if sym and count == 1:
                sum += i + 1
                break

print(sum)

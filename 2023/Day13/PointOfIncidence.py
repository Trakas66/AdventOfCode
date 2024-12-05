sum = 0
patterns = []

def compareCols(pattern, col1, col2):
    for i in range(len(pattern)):
        if pattern[i][col1] != pattern[i][col2]:
            return False
    return True

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
        if pattern[i] == pattern[i+1]:
            a,b=i-1,i+2
            sym = True
            while a >= 0 and b < len(pattern):
                if pattern[a] != pattern[b]:
                    sym = False
                    break
                a -= 1
                b += 1
            if sym:
                sum += (100*(i+1))
                found = True
                break
    if found:
        continue
    #columns
    for i in range(len(pattern[0])-1):
        if compareCols(pattern, i, i+1):
            a,b=i-1,i+2
            sym = True
            while a >= 0 and b < len(pattern[0]):
                if not compareCols(pattern, a, b):
                    sym = False
                    break
                a -= 1
                b += 1
            if sym:
                sum += i + 1
                break

print(sum)

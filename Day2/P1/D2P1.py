file = open(r'../day2.txt')
input = file.readlines()
file.close()

totalSafe = 0
for line in input:
    line = line.split()
    line = [int(x) for x in line]
    
    if line[0] < line[1]:
        isIncreasing = True
    else:
        isIncreasing = False
        
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            break
        if abs(line[i] - line[i+1]) > 3:
            break
        if isIncreasing and line[i] > line[i+1]:
            break
        if not isIncreasing and line[i] < line[i+1]:
            break
    else:
        totalSafe += 1

print(totalSafe)

file = open(r'../ex1.txt')
input = file.readlines()
file.close()

totalSafe = 0
for line in input:
    line = line.split()
    line = [int(x) for x in line]
    print(line)
    

print(totalSafe)

file = open(r'../day1.txt')
input = file.readlines()
file.close()
list1, list2 = [], []

for line in input:
    line = line.split()
    list1.append(int(line[0]))
    list2.append(int(line[1]))

list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print(total)

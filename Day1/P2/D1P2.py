file = open(r'../day1.txt')
input = file.readlines()
file.close()
list1, list2 = [], {}

for line in input:
    line = line.split()
    list1.append(int(line[0]))
    if int(line[1]) in list2:
        list2[int(line[1])] += 1
    else:
        list2[int(line[1])] = 1

total = 0
for i in range(len(list1)):
    if list1[i] in list2:
        total += (list1[i] * list2[list1[i]])

print(total)

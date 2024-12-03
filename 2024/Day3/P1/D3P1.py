import re

file = open(r'../day3.txt')
input = file.read()
file.close()

muls = re.findall('mul\([0-9]+,[0-9]+\)', input)

total = 0
for mul in muls:
    mul = re.sub('[mul()]', '', mul)
    mul = mul.split(',')
    total += int(mul[0]) * int(mul[1])

print(total)

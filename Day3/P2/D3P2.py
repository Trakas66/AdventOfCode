import re

file = open(r'../day3.txt')
input = file.read()
file.close()

items = re.findall("(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))", input)
#items return in format ('mul(x,y)', 'do()', 'don't()')

total = 0
enable = True
for item in items:
    if item[1] == "do()":
        enable = True
    elif item[2] == "don't()":
        enable = False
    elif not enable:
        continue
    else:
        mul = re.sub('[mul()]', '', item[0])
        mul = mul.split(',')
        total += int(mul[0]) * int(mul[1])

print(total)

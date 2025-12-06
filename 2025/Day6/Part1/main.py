filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

for i in range(len(input)):
    input[i] = input[i].split()

total = 0
for i in range(len(input[0])):
    if input[-1][i] == '+':
        mul = False
        res = 0
    else:
        mul = True
        res = 1
    for j in range(len(input)-1):
        num = int(input[j][i])
        if mul:
            res *= num
        else:
            res += num
    total += res

print(total)
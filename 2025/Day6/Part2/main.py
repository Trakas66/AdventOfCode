filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

input[-1] = input[-1].split()

total = 0
counter = 0
for i in range(len(input[-1])):
    if input[-1][i] == '*':
        mul = True
        res = 1
    else:
        mul = False
        res = 0
    
    while 1:
        if counter >= len(input[0]):
            total += res
            break
        num = ""
        for j in range(len(input)-1):
            if input[j][counter] != " ":
                num += input[j][counter]
        counter += 1
        if num != "":
            num = int(num)
            if mul:
                res *= num
            else:
                res += num
        else:
            total += res
            break

print(total)
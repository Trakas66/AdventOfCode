sum = 0
line = "new"

while line != "":
    line = input()
    num1 = 0
    num2 = 0

    for i in range(len(line)):
        char = line[i]
        if char.isnumeric():
            num1 = char
            break
    for i in range(len(line)-1, -1, -1):
        char = line[i]
        if char.isnumeric():
            num2 = char
            break
    
    string = str(num1) + str(num2)
    sum += int(string)

print(sum)

filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

num = 50
passw = 0

for line in input:
    i = int(line[1:])
    passw += int(i / 100)
    i %= 100

    if line[0] == "L":
        if num == 0 and i != 0:
            num = 100
        num -= i
    elif line[0] == "R":
        num += i
    else:
        print("idk")
    
    if num < 1 or num > 99:
        passw += 1
        num %= 100

print(passw)


# < 6603
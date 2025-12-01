filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

num = 50
passw = 0

for line in input:
    i = int(line[1:])

    if line[0] == "L":
        num = (num - i) % 100
    elif line[0] == "R":
        num = (num + i) % 100
    else:
        print("idk")
    
    if num == 0:
        passw += 1

print(passw)
filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split(",")

sum = 0
found = []

for line in input:
    rangeNum = line.split("-")
    start, end = int(rangeNum[0]), int(rangeNum[1])

    for length in range(1, int(len(rangeNum[1])/2)+2):
        num = "1" + "0"*(length-1)
        while len(num) == length:
            for i in range(2, int(len(rangeNum[1])/length)+1):
                check = int(num*i)
                if check > end:
                    break
                elif check >= start and check not in found:
                    sum += check
                    found.append(check)
            num = str(int(num)+1)

print(sum)
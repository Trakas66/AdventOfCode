filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split(",")

sum = 0

for line in input:
    rangeNum = line.split("-")
    start, end = int(rangeNum[0]), int(rangeNum[1])

    valid = [int(n/2) for n in range(len(rangeNum[0]), len(rangeNum[1])+1) if n % 2 == 0]

    for length in valid:
        num = "1" + "0" * (length-1)
        while not len(num) > length:
            check = int(num + num)
            if check > end:
                break
            elif start <= check:
                sum += check
            num = str(int(num)+1)

print(sum)
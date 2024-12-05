nums = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
        "seven":7, "eight":8, "nine":9, "ten":10}
sum = 0
line = "new"
while line != "":
    line = input()
    num1 = 0
    num2 = 0
    
    for i in range(len(line)):
        if line[i].isnumeric():
            num1 = line[i]
            break
        for j in range(3, 7):
            if (i+j) > len(line):
                continue
            if line[i:i+j] in nums:
                num1 = nums[line[i:i+j]]
                break
        else:
            continue
        break
            
    for i in range(len(line)-1, -1, -1):
        if line[i].isnumeric():
            num2 = line[i]
            break
        for j in range(3, 7):
            if (i+j) > len(line):
                continue
            if line[i:i+j] in nums:
                num2 = nums[line[i:i+j]]
                break
        else:
            continue
        break
            
    num = str(num1) + str(num2)
    sum += int(num)

print(sum)
    

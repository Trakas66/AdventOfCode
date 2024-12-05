product = 1
times = []
records = []

line = input().split(":")
nums = line[1].strip().split()
for i in range(len(nums)):
    times.append(int(nums[i]))

line = input().split(":")
nums = line[1].strip().split()
for i in range(len(nums)):
    records.append(int(nums[i]))

for i in range(len(times)):
    minT = 0
    maxT = 0
    for j in range(times[i]+1):
        distance = j * (times[i]-j)
        if distance > records[i]:
            if minT == 0:
                minT = j
            maxT = j
        elif minT != 0:
            break

    n = maxT - minT + 1
    product *= n

print(product)

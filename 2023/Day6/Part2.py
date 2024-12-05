time = ""
record = ""

line = input().split(":")
nums = line[1].strip().split()
for i in range(len(nums)):
    time += nums[i]
time = int(time)

line = input().split(":")
nums = line[1].strip().split()
for i in range(len(nums)):
    record += nums[i]
record = int(record)

#(time-t1)t1 > record
#t1(time) - t1^2 > record
#-t1^2 + t1(time) - record > 0
minT = int((-time + (time**2 - 4*record)**0.5)/(-2)) + 1
maxT = int((-time - (time**2 - 4*record)**0.5)/(-2))

n = maxT - minT + 1

print(int(n))

sum = 0

def createRegEx(nums):
    regex = f"((\#|\?){{{nums[0]}}})"
    for i in range(1, len(nums)):
        regex += "((\.|\?)+)"
        regex += f"((\#|\?){{{nums[i]}}})"
    return regex


while 1:
    line = input()
    

file = open(r'../day4.txt')
input = file.readlines()
file.close()

letters = ['M', 'S']

def checkA(i, j):
    if input[i-1][j-1] in letters and input[i+1][j+1] in letters and input[i-1][j-1] != input[i+1][j+1]:
        if input[i-1][j+1] in letters and input[i+1][j-1] in letters and input[i-1][j+1] != input[i+1][j-1]:
            return 1
    return 0

total = 0
for i in range(1, len(input)-1):
    for j in range(1, len(input[i])-1):
        if input[i][j] != 'A':
            continue
        total += checkA(i, j)

print(total)


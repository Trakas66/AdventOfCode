file = open(r'../day4.txt')
input = file.readlines()
file.close()

letters = ['X', 'M', 'A', 'S']

#current i and j position
#d is a direction vector in the direction we're checking ex. (0,1)
#n is the index of the next letter we're looking for
def checkLine(i, j, d, n):
    i += d[0]
    j += d[1]
    if input[i][j] != letters[n]:
        return False
    if n == 3:
        return True
    return checkLine(i, j, d, n+1)

height, width = len(input), len(input[0])
total = 0
for i, line in enumerate(input):
    for j in range(len(line)):
        if line[j] != letters[0]:
            continue

        #call checkLine on all valid directions
        if j < width-3:
            if checkLine(i, j, (0, 1), 1):
                total += 1
            if i > 2:
                if checkLine(i, j, (-1, 1), 1):
                    total += 1
            if i < height-3:
                if checkLine(i, j, (1, 1), 1):
                    total += 1
        if j > 2:
            if checkLine(i, j, (0, -1), 1):
                total += 1
            if i > 2:
                if checkLine(i, j, (-1, -1), 1):
                    total += 1
            if i < height-3:
                if checkLine(i, j, (1, -1), 1):
                    total += 1
        if i > 2:
            if checkLine(i, j, (-1, 0), 1):
                total += 1
        if i < height-3:
            if checkLine(i, j, (1, 0), 1):
                total += 1

print(total)

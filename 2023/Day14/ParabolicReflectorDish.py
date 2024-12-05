sum = 0
board = []
rocks = []

row = 0
while 1:
    line = input()
    if line == "":
        break
    new = []
    for i in range(len(line)):
        if line[i] == "O":
            rocks.append((row, i))
        new.append(line[i])
    board.append(new)
    row += 1

for rock in rocks:
    x, y = rock[0], rock[1]
    board[x][y] = "."
    while x > 0:
        if board[x-1][y] == "#" or board[x-1][y] == "O":
            break
        x -= 1
    board[x][y] = "O"
    sum += len(board) - x

print(sum)

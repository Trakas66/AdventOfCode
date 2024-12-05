sum = 0
boxes = {x:[] for x in range(256)}

file = open("input.txt", "r")
line = file.read().split(",")

def hashStep(line):
    currentValue = 0
    for i in range(len(line)):
        currentValue += ord(line[i])
        currentValue *= 17
        currentValue = currentValue % 256
    return currentValue

def getIndex(item, box):
    box = boxes[box]
    for i in range(len(box)):
        if box[i][0] == item[0]:
            return i
    return -1

for i in range(len(line)):
    symbol = 0
    for j in range(len(line[i])):
        if line[i][j] in ['-', '=']:
            symbol = j
            break
    box = hashStep(line[i][:symbol])
    if line[i][symbol] == '-':
        item = (line[i][:symbol], 0)
        index = getIndex(item, box)
        if index != -1:
            boxes[box].pop(index)
    elif line[i][symbol] == '=':
        item = (line[i][:symbol], int(line[i][symbol+1]))
        index = getIndex(item, box)
        if index == -1:
            boxes[box].append(item)
        else:
            boxes[box][index] = item

for box in boxes:
    for i in range(len(boxes[box])):
        lens = boxes[box][i]
        focusP = (1+box)*(i+1)*lens[1]
        sum += focusP

print(sum)

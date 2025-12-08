from math import sqrt

filename = "input.txt"

with open(f"../{filename}", "r") as file:
    input = file.read().split("\n")

for i in range(len(input)):
    input[i] = input[i].split(",")
    for j in range(len(input[i])):
        input[i][j] = int(input[i][j])

def get_distance_box(boxes):
    return boxes[2]

def get_distance(box1, box2):
    x2 = (box1[0]-box2[0])**2
    y2 = (box1[1]-box2[1])**2
    z2 = (box1[2]-box2[2])**2
    return sqrt(x2 + y2 + z2)

def get_closest_list(boxes):
    boxlist = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            dist = get_distance(boxes[i], boxes[j])
            boxlist.append((i, j, dist))
    boxlist.sort(key=get_distance_box)
    return boxlist

boxlist = get_closest_list(input)
circuits = []
for _ in range(1000):
    box_circuits = [None, None]
    boxes = boxlist.pop(0)
    for i in range(len(circuits)):
        if boxes[0] in circuits[i]:
            box_circuits[0] = i
        if boxes[1] in circuits[i]:
            box_circuits[1] = i
    if box_circuits == [None, None]:
        circuits.append([boxes[0], boxes[1]])
    elif box_circuits[0] == box_circuits[1]:
        continue
    elif box_circuits[0] == None:
        circuits[box_circuits[1]].append(boxes[0])
    elif box_circuits[1] == None:
        circuits[box_circuits[0]].append(boxes[1])
    else:
        for num in circuits[box_circuits[1]]:
            circuits[box_circuits[0]].append(num)
        circuits.pop(box_circuits[1])

biggest = [0, 0, 0]
for circuit in circuits:
    for i in range(3):
        if len(circuit) > biggest[i]:
            for j in range(2, i, -1):
                biggest[j] = biggest[j-1]
            biggest[i] = len(circuit)
            break

product = biggest[0]*biggest[1]*biggest[2]
print(product)
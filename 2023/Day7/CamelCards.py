import functools

sum = 0
cardNum = {"T":10, "J":11, "Q":12, "K":13, "A":14}
hands = []

def getCardNum(card):
    if card.isnumeric():
        return int(card)
    else:
        return cardNum[card]

def checkHand(hand):
    cards = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1

    if len(cards) == 1:
        return 6
    elif len(cards) == 2:
        for card in cards:
            if cards[card] == 1 or cards[card] == 4:
                continue
            break
        else:
            return 5
        return 4
    elif len(cards) == 3:
        kind3 = False
        for card in cards:
            if cards[card] == 3:
                kind3 = True
                break
        if kind3:
            return 3
        return 2
    elif len(cards) == 4:
        return 1
    return 0

def compareHand(hand1, hand2):
    str1 = checkHand(hand1[0])
    str2 = checkHand(hand2[0])
    if str1 > str2:
        return 1
    elif str2 > str1:
        return -1
    for i in range(5):
        num1 = getCardNum(hand1[0][i])
        num2 = getCardNum(hand2[0][i])
        if num1 > num2:
            return 1
        elif num2 > num1:
            return -1


while 1:
    line = input()
    if line == "":
        break
    hands.append(tuple(line.split()))

hands.sort(key=functools.cmp_to_key(compareHand))

for i in range(len(hands)):
    sum += int(hands[i][1]) * (i+1)

print(sum)

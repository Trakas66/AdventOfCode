import functools

sum = 0
cardNum = {"T":10, "J":0, "Q":12, "K":13, "A":14}
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

    numJoker = 0

    if "J" in cards:
        numJoker = cards["J"]
        del cards["J"]
        high = 0
        highCard = 0
        for card in cards:
            if cards[card] > high:
                high = cards[card]
                highCard = card
        if highCard != 0:
            cards[highCard] += numJoker
        elif numJoker == 5:
            return 6

    kind3 = False
    pair = False
    pair2 = False

    for card in cards:
        if cards[card] == 5:
            return 6
        elif cards[card] == 4:
            return 5
        elif cards[card] == 3:
            kind3 = True
        elif cards[card] == 2 and pair:
            pair2 = True
        elif cards[card] == 2:
            pair = True

    if kind3 and pair:
        return 4

    if kind3:
        return 3

    if pair2:
        return 2

    if pair:
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
    return 0


while 1:
    line = input()
    if line == "":
        break
    hands.append(tuple(line.split()))

hands.sort(key=functools.cmp_to_key(compareHand))

for i in range(len(hands)):
    sum += int(hands[i][1]) * (i+1)

print(sum)

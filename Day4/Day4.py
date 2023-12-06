#Method calculates value of cards. 1 point for a winning number and then double for each subsequent winning number.
def calcValue(numWins):

    cardValue = 0
    if numWins >= 1:
        cardValue += 1
    if numWins > 1:
        winIndex = 1
        while winIndex < numWins:
            cardValue = cardValue * 2
            winIndex += 1
    return cardValue

#Open, read file and split into indivdual numbers of both sets
f = open("day4.txt")
scratchCards = []
for line in f:
    parts = line.split("|")
    parts[0] = parts[0].split(":")
    parts[0][1] = parts[0][1].split()
    parts[1] = parts[1].split()
    scratchCards.append([parts[0][0], parts[0][1], parts[1]])

totalWins =0
totalCardValue =0
cardCounter =[]
totalCards = 0
# Init list with all cards and a counter
for card in scratchCards:
    cardCounter.append([card, 1])

cardIndex = 0
for card in scratchCards:
    numWins =0
    for drawNum in card[2]:
        for winNum in card[1]:
            #print(drawNum, winNum)
            if int(drawNum) == int(winNum):
                numWins+=1

    print(card[0], '#', cardCounter[cardIndex][1], 'wins',numWins)
    winCounter = 1
    while winCounter < numWins+1:

        try:
            cardCounter[cardIndex + winCounter][1] += cardCounter[cardIndex][1]
            totalCards += cardCounter[cardIndex][1]
            print(cardCounter[cardIndex + winCounter])
        except IndexError:
            pass
        winCounter+=1

    #print(cardCounter)
    cardValue = calcValue(numWins)
    totalWins += numWins
    totalCardValue += cardValue
    cardIndex+=1


#print(totalCardValue)
print(totalCards+len(cardCounter))

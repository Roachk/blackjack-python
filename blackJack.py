import random

deck = ['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','k','k']
playerOneHand = []
dealerHand = []
players = [playerOneHand, dealerHand]

def dealCards():
    deckLength = len(deck)
    randomNumberGenerator = random.randint(0, deckLength)
    cardPick = deck[randomNumberGenerator]
    del deck[randomNumberGenerator]
    #print(randomNumberGenerator)
    #print(cardPick)
    return cardPick

def startGame():
    for i in range(len(players)):
        #print(i)
        for k in range(len(players)):
            #print(players[k])
            players[k].append(dealCards())
    for i in range(len(players)):
        print('Player ' + str((i + 1)) + ' showing')
        print(players[i])

print("Welcome to Kevin's Blackjack\nWould you like to play?\n(y)es (n)o (r)ules")
playerStart = input()

if playerStart == 'y':
    print('Dealing Cards')
    startGame()
else:
    print('Goodbye')



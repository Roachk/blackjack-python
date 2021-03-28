import random

#deck = ['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K']
#Test Desk
deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K']

#List to hold players hands
playerOneHand = []
dealerHand = []
tempDealerHand = []

#List to do math with
playerOneHandMath = []
dealerHandMath = []

players = [playerOneHand, dealerHand]
playerMath = [playerOneHandMath, dealerHandMath]

def twentyOneChecker(hand):
    handTotal = 0
    for i in range(0, len(hand)):
        handTotal = handTotal + int(hand[i])
        print(handTotal)

def dealCards():
    deckLength = len(deck)
    randomNumberGenerator = random.randint(0, deckLength)
    cardPick = deck[randomNumberGenerator]
    del deck[randomNumberGenerator]
    #print(randomNumberGenerator)
    #print(cardPick)
    return cardPick

def startGame():
    #This for for loop simulates a 21 dealer dealing cards to each player one at a time.
    for i in range(len(players)):
        #print(i)
        for k in range(len(players)):
            #print(players[k])
            players[k].append(dealCards())
            playerMath[k] = players[k]
            
    global tempDealerHand
    tempDealerHand = dealerHand
    del tempDealerHand[0]
    tempDealerHand.insert(0,'*')
    
    #This for loop shows the cards of each player
    for i in range(len(players)):
        if players[i] == players[-1]:
            print('Dealer is showing')
            print(tempDealerHand)
        else:
            print('Player ' + str((i + 1)) + ' is showing')
            print(players[i])
        #sets playerMath list equal to the players list
        
    #Converts the players hands to numbers ie J = 10, Q = 10 ...
    
    #Checks if a player or dealer has 21
    #for x in range(len(players)):
        #print(players[x])
        #handTotal = twentyOneChecker(players[x])
        #input()

print("Welcome to Kevin's Blackjack\nWould you like to play?\n(y)es (n)o (r)ules")
playerStart = input()

if playerStart == 'y':
    print('Dealing Cards')
    startGame()
else:
    print('Goodbye')


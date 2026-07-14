#program to simulat different betting strategies and the payoff with craps
from random import randint
# create a dice rolling simulation

class Die:
    """A class representing a single die."""
    
    def __init__(self, sides=6):
        """Initialize the die with a given number of sides (default is 6)."""
        self.sides = sides

    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.sides)
    
die1 = Die()
die2 = Die()

"""
Pass Line / come
2, 3, 12 - lose
4, 5, 6, 8, 9, 10 - continue
7, 11 - win even money

Don't pass/ don't come
2, 3, 12 win 1:1
4, 5, 6, 8, 9, 10 - continue
7, 11 - lose

Place Bets
6 - 8 - pay 7:6
5 - 9 - Pay 7:5
4 - 10 - pay 9 : 5

Odds bets
4, 10 - 2:1
5, 9 - 3:2
6,8 - 6:5

Buy Bets: Pays true mathematical odds (2:1 on 4/10, 3:2 on 5/9, 6:5 on 6/8), but you must pay a 5% commission (vig) to the house to make the bet

Single Role Bets
Any Craps (2, 3, or 12): Pays 7 to 1.
Any Seven: Pays 4 to 1.
Ace-Deuce (3) or Eleven (Yo): Pays 15 to 1.
Aces (2) or Midnight (12): Pays 30 to 1.

Field Bet: 
Pays 1 to 1 on 3, 4, 9, 10, and 11. 
Pays 2 to 1 (or sometimes 3 to 1) on 2 or 12.

Hardways (multi-roll)
Hard 4 or 10 pay 7:1
Hard 6 or Hard 8 pay 9:1

Payouts for Place Lose Bets
The standard payouts for betting against a number are:
Against the 4 or 10: Pays 5 to 11
Tip: Bet in multiples of $11 to win $5.
Against the 5 or 9: Pays 5 to 8
Tip: Bet in multiples of $8 to win $5.
Against the 6 or 8: Pays 4 to 5
Tip: Bet in multiples of $5 to win $4.
"""

# create a come out roll
# create a simulation to roll until the point is made or craps
# keep bets simple

#global variables
startingAmount = 1000
wager = 5
workingPoint = 0
pointOn = False
betDict = {
    "4": 0,
    "5": 0,
    "6": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "odds": True,
    "oddsBet": 0
}

payout = {
    "4": 1.8,
    "5": 1.4,
    "6": 1.16667,
    "8": 1.16777,
    "9": 1.4,
    "10": 1.8
}

oddsBets = {
    "4": 2,
    "5": 1.5,
    "6": 1.2,
    "8": 1.2,
    "9": 1.5,
    "10": 2

}

standardWager = {
    "4": 5,
    "5": 5,
    "6": 5,
    "8": 5,
    "9": 5,
    "10": 5
}

standardLineWager = {
    "4": 5,
    "5": 5,
    "6": 6,
    "8": 6,
    "9": 5,
    "10": 5
}

bettingStrategy = "aggressive"
betlist = ["4","5","6","8","9","10"]
carryOver = True
rolls = []
currentState = []

def comeout():
    newPoint = die1.roll() + die2.roll()
    if newPoint == 2 or newPoint == 3 or newPoint == 12:
        print("Craps you lose")
        startingAmount -= wager
    elif newPoint == 7 or newPoint == 11:
        print("winner")
        startingAmount += wager
    else:
        workingPoint = newPoint
        pointOn = True
    return workingPoint

def setWager(rollPoint):
    # if betting strategy is aggressive - buy odds and the place
    strPoint = str(rollPoint)
    if bettingStrategy == "aggressive" and carryOver:
        for bet in betlist:
            if bet != strPoint:
                betDict[bet] = standardLineWager[bet]
                startingAmount -= standardLineWager[bet]
    if betDict["odds"]:
        betDict["oddsBet"] = wager
        startingAmount -= wager

def workingRoll(rollPoint):
    #rollPoint is the working roll amount
    #shoot a new roll
    newPoint = die1.roll() + die2.roll()
    compPoint = str(newPoint)

    if newPoint == 7:

        print("ah craps")
        for bet in betlist:
            betDict[bet] = 0
            betDict["oddsBet"] = 0
            pointOn = False
            carryOver = False
    elif newPoint == rollPoint:
        startingAmount += wager
        startingAmount += standardLineWager[compPoint] * oddsBets[compPoint]
        pointOn = False
        carryOver = True
    elif rollPoint != 2 or rollPoint != 3 or rollPoint != 11 or rollPoint != 12:
            startingAmount += standardLineWager[compPoint] * payout[compPoint]



for x in range(100):
    if pointOn:
        workingRoll(workingPoint)
    else:
        workingPoint = comeout()
        setWager(workingPoint)
    print(startingAmount)



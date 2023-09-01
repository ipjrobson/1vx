import random
import pyinputplus as pyip
from tabulate import tabulate

dc = 0 # the difficulty of the throw
p1w = 0 # player 1 wins
p1l = 0 # player 2 losses
p2w = 0 # player 2 wins
p2l = 0 # player 2 losses
p1Diff = 0 # player 1 difference between the roll and the dc
p2Diff = 0 # player 2 difference between the roll and the dc
p1Record = ['Player1 Rolls']
p2Record = ['Player2 Rolls']
globalDiff = 0
critical = False

def checkDie(roll,diff,bonus):
    if roll < (dc + diff):        
        global globalDiff
        globalDiff = dc - roll
        return False
    elif roll - bonus == 20:
        # print('CRITICAL STRIKE''\n')
        global critcal
        critcal = True
        return True
    elif roll >= dc:
        # print('You pass the check ','\n')
        return True

# users input their bonuses

p1Bonus = pyip.inputNum('Player 1 what is your dex modifier?''\n' )
p2Bonus = pyip.inputNum('Player 2 what is your dex modifier?''\n' )

# input the difficulty of the roll

dc = pyip.inputNum('What is the difficulty of the throw ''\n')
print('\n')

# players roll their dice

while p1l < 3 and p2l < 3:
    p1 = random.randint(1,20) + p1Bonus
    if (checkDie(p1,p1Diff,p1Bonus)) == True:
        p1w += 1
    else:
        p1l += 1
    p1Diff = globalDiff
    
    if critical == True:
        p2l += 1
    critical = False
    p1Record.append(p1)
    p2 = random.randint(1,20) + p2Bonus
    if (checkDie(p2,p2Diff,p2Bonus)) == True:
        p2w += 1
    else:
        p2l += 1
    p2Diff = globalDiff
    globalDiff = 0
    if critical == True:
        p1l += 1
    critical = False
    p2Record.append(p2)

record = [p1Record],[p2Record]
print(tabulate((record)))
print('Player 1 wins ' + str(p1w) + ' Player 1 losses ' + str(p1l))
print('Player 2 wins ' + str(p2w) + ' Player 2 losses ' + str(p2l))

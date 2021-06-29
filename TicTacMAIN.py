import BoardClass
import PlayerClass
import CPUClass

b = BoardClass.Board()

opponent = b.chooseOpponent()
b.printBoard()

p1 = PlayerClass.Player()

if opponent == '1':
    p2 = PlayerClass.Player()
else:
    p2 = CPUClass.CPU()

turnNum = 0

while turnNum < b.gridSize:
    if turnNum % 2 == 0:
        playerChoice = p1.moveSelection(b.gridList)
    else:
        playerChoice = p2.moveSelection(b.gridList)
    b.markSelection(turnNum, playerChoice)
    b.printBoard()
    b.checkForWin()


    if b.gameOver == True:
        break

    turnNum += 1

if turnNum >= b.gridSize:
    print ("DRAW")

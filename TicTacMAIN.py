import BoardClass

b = BoardClass.Board(4,4)
b.listInit()

b.printBoard() #Make init function

turnNum = 0

while turnNum < b.gridSize:
    b.markSelection(turnNum)
    b.printBoard()
    b.checkForWin()


    if b.gameOver == True:
        break

    turnNum += 1

if turnNum >= 9:
    print ("DRAW")

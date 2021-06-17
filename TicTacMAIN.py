import BoardClass

b = BoardClass.Board(3,3)
b.listInit()

b.printBoard() #Make init function

turnNum = 0

while turnNum < 9:
    b.markSelection(turnNum)
    b.printBoard()
    b.checkForWin()


    if b.gameOver == True:
        break

    turnNum += 1

if turnNum >= 9:
    print ("DRAW")

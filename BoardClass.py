#look up sets


class Board:

    def __init__ (self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.gridSize = columns * rows
        self.gridList = []
        self.gameOver = False

    def listInit(self):
        idx = 1
        for i in range(self.rows):
            #Too much mutation?
            newList = []
            for j in range(self.columns):
                newList.append(j+idx)
            self.gridList.append(newList)
            idx += self.columns

    def printBoard(self):
        for item in self.gridList:
            print (*item, sep = " | ")
            
    def checkForTurn(self, idx):
        if idx % 2 == 0:
            return "X"
        else:
            return "O"
        
    def userSelection(self):
        userInput = int(input('Please enter a number'))
        return userInput

    def markSelection(self, turnNumber):
        playerToken = self.checkForTurn(turnNumber)
        playerChoice = self.userSelection()
        for i in range(len(self.gridList)):
            for j in range(len(self.gridList[i])):
                if self.gridList[i][j] == playerChoice:
                    self.gridList[i][j] = playerToken

    def winLogic(self,anySet):
            if len(anySet) == 1:
                print(str(anySet)+' WINNER')
                self.gameOver = True
        

    def checkForWin(self):
        #Horizontal Wins
        for item in self.gridList:
            seOne = set(item)
            self.winLogic(seOne)
        #Vertical Wins
        for j in range(self.columns):
            seTwo = set() #Vertical



                
            for i in range(self.rows):
                seTwo.add(self.gridList[i][j])
            #This is janky


        for j in range(1): # I don't understand why this is needed, but it doesn't work without
            #Also I think this only works for square boards where the win condition = the length of the board
            seThree = set() #diagonal forward
            seFour = set() #diagonal backward
            idx = 0
            for i in range(self.rows):
                seThree.add(self.gridList[i][j+idx])
                seFour.add(self.gridList[i][j+self.columns-1-idx])
                idx += 1

                
            self.winLogic(seTwo)
            self.winLogic(seThree)
            self.winLogic(seFour)
        #Diagonal Wins

        '''seThree = {self.gridList[0][0], self.gridList[1][1], self.gridList[2][2]}
        self.winLogic(seThree)
        seFour = {self.gridList[2][0], self.gridList[1][1], self.gridList[0][2]}
        self.winLogic(seFour)'''
        
        
        
            

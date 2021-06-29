
class Board:

    def listInit(self):
        idx = 1
        for i in range(self.rows):
            #Too much mutation?
            newList = []
            for j in range(self.columns):
                newList.append(j+idx)
            self.gridList.append(newList)
            idx += self.columns

    def __init__ (self):
        self.columns = 3
        self.rows = 3
        self.gridSize = 9
        self.gridList = [] #Nested list
        self.gameOver = False
        self.listInit()

    def chooseOpponent(self):
        while 1:
            userInput = input('''Would you like to play against an AI or a human?
Enter 1 for Human or 2 for AI.''')
            if userInput != '1' and userInput != '2':
                print ("Please input either 1 or 2")
                continue
            elif userInput == '1':
                print('You have chosen to play against a human.')
                return userInput
            elif userInput == '2':
                print('You have chosen to play against an AI')
                return userInput



    def printBoard(self):
        for item in self.gridList:
            print(*item, sep = " | ")
            
    def checkForTurn(self, idx):
        return 'O' if idx % 2 else 'X'
        

    def markSelection(self, turnNumber, playerChoice):
        playerToken = self.checkForTurn(turnNumber)
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
            self.winLogic(seTwo)


            #This is janky

            seThree = set() 
            seFour = set() 
            idx = 0
            for i in range(self.rows):
                seThree.add(self.gridList[i][i])
                seFour.add(self.gridList[i][self.columns-1-i])
                idx += 1

        self.winLogic(seThree)
        self.winLogic(seFour)
        
        
            

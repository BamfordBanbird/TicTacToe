
class Player:

    def moveSelection(self, gridList):
        while True:
            while 1:
                try:
                    userInput = int(input("Please input a number:"))
                    break
                
                except:
                    print ("Selections must be numbers only.")
                    continue
            if 0<userInput<=9:
                #Not sure how to pinpoint where we're going concisely
                for i in range(3):
                    for j in gridList[i]:
                        if j == userInput:
                            return userInput
                #Only prints if above fails
                print("Please select a number that hasn't been chosen already")
            else:
                print ("Please input a number between 1 and 9")

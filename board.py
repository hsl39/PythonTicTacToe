class Space:
    def __init__(self, x, y):
        self.value = " "
        self.coord = [x,y]
    def setValue(self, value):
        self.value = value
    def printSpace(self):
        print("[" + self.value + "]", end = "")
    def getXCoord(self):
        return self.coord[0]
    def getYCoord(self):
        return self.coord[1]

class Board:
    #Tic Tac Toe does not have dynamic board sizes, 3x3 by default.
    def __init__(self):
       self.spaces = []
       #Index starts at 1 for clarity
       for x in range(1,4):
           for y in range(1,4):
               self.spaces.append( Space(x,y) )

    def printBoard(self):
        currRow = 0
        #This is pretty gross, but it works
        print("  1  2  3", end= "")
        for x in self.spaces:
            if(x.getXCoord() > currRow):
                #Print a new line on new row
                print("\n" + str(currRow), end = "")
                currRow += 1
            x.printSpace()
    
    def winCheck(self):
        return


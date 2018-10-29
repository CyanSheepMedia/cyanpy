#cyanpy - a collection of small but useful functions that I need quite often.

#cyanpy is designed for use with different other libraries.
import pygame

#This functions saves a dictionary to a file. 
def dictToFile(aDict, fileName):
    file = open(fileName, 'w')
    file.write(str(aDict))
    file.close()

#This functions loads a dictionary from a file.
def fileToDict(fileName):
    file = open(fileName, 'r')
    aDict = eval(file.read())
    file.close
    return aDict

#This functions saves the list to a file.
def listToFile(aList, fileName):
    file = open(fileName, 'w')
    for x in range(0, len(aList)):
        if x == int(len(aList)-1):
            file.write(str(aList[x]))
        else:
            file.write(str(aList[x]) + str('\n'))
    file.close
            
#This functions loads a list from a file.
def fileToList(fileName):
    file = open(fileName,'r')
    aList = file.readlines()
    for x in range(0, len(aList)):
        aList[x] = aList[x].strip('\n')
    file.close
    return aList

#This function is a binary search. Works the same as the linear search only is fast when doing really large lists.
#I admit this function looks messy and could probably be more efficient.
def binarySearch(aList, searchItem):
    findWord = True
    midPoint = int(len(aList)/2)
    halfOfList = aList
    checkVal = int(0)
    checkWord = halfOfList[midPoint]
    while findWord == True:
        if searchItem == checkWord:
            return True
        else:
            if len(halfOfList) == int(1):
                return False
            elif len(halfOfList) == int(2):
                if halfOfList[0] == searchItem:
                    return True
                elif halfOfList[1] == searchItem:
                    return True
                else:
                    return False
            elif len(checkWord) == int(checkVal):
                halfOfList = halfOfList[midPoint:]
                midPoint = int(len(halfOfList) / 2)
                checkWord = halfOfList[midPoint]
                checkVal = int(0)
            elif len(searchItem) == int(checkVal):
                halfOfList = halfOfList[:midPoint]
                midPoint = int(len(halfOfList) / 2)
                checkWord = halfOfList[midPoint]
                checkVal = int(0)
            elif ord(searchItem[checkVal]) < ord(checkWord[checkVal]):
                halfOfList = halfOfList[:midPoint]
                midPoint = int(len(halfOfList) / 2)
                checkWord = halfOfList[midPoint]
                checkVal = int(0)
            elif ord(searchItem[checkVal]) > ord(checkWord[checkVal]):   
                halfOfList = halfOfList[midPoint:]
                midPoint = int(len(halfOfList) / 2)
                checkWord = halfOfList[midPoint]
                checkVal = int(0)
            elif ord(searchItem[checkVal]) == ord(checkWord[checkVal]):
                checkVal = checkVal + 1
            else:
                checkVal = int(0)
                
#This function is a linear search. Tells if an item is in a list.
def linearSearch(aList, searchItem):
    for x in range(0, len(aList)):
        if searchItem == aList[x]:
            return True
    return False

#Works out the factor increase between the values of a base list and another list.
#Returns a list with the scale factor of each point of data. Lists have to be the same length.
def scaleFactor(baseList, actualList):
    scaleFactors = []
    for x in range(0, len(actualList)):
        scale = actualList[x] / baseList[x]
        scaleFactors.append(scale)
    return scaleFactors

# //PYGAME FUNCTIONS//
#The following functions are designed for use with Pygame.

#This function allows you to print text into a box.
class textBox:
    def __init__(self, boxLocation, boxSize):
        self.boxLocation = boxLocation
        self.boxSize = boxSize
        self.currentTopLine = int(0)

    #No scroll is to be used if the text is short enough to fit within the decided box.
    def noScroll(self, screen, text, font, fontSize, colour):
        textFont = pygame.font.Font(font + '.ttf', fontSize)
    
        #First creates a list of all the words in the text.
        wordsList = []
        textLength = len(text)
        currentWord = str('')
        for x in range(0, textLength):
            if text[x] == str(' '):
                wordsList.append(currentWord)
                currentWord = str('')
            else:
                currentWord = currentWord + text[x]
                if x == int(textLength - 1):
                    wordsList.append(currentWord)
                    currentWord = str('')

        #Then works out which words should go into each line. Based on the width of the box.
        numOfWords = len(wordsList)
        currentLine = str('')
        linesList = []
        for x in range(0, numOfWords):
            wordWidth, wordHeight = textFont.size(wordsList[x])
            currentLineWidth, currentLineHeight = textFont.size(currentLine) 
            if int(currentLineWidth + wordWidth) <= self.boxSize[0]:
                currentLine = currentLine + wordsList[x] + str(' ')
                if x == int(numOfWords - 1):
                    linesList.append(currentLine)
            else:
                linesList.append(currentLine)
                currentLine = wordsList[x] + str(' ')

        #Finally blits all the lines to the screen.
        numOfLines = len(linesList)
        for x in range(0, numOfLines):
            textSurface = textFont.render(linesList[x], True, colour)
            screen.blit(textSurface, (self.boxLocation[0], int(self.boxLocation[1] + int(wordHeight * x))))

        pygame.display.update()

    def clickScroll(self, screen, text, font, fontSize, colour, pos, mouse):
        textFont = pygame.font.Font(font + '.ttf', fontSize)
    
        #First creates a list of all the words in the text.
        wordsList = []
        textLength = len(text)
        currentWord = str('')
        for x in range(0, textLength):
            #print(x, textLength)
            if text[x] == str(' '):
                wordsList.append(currentWord)
                currentWord = str('')
            else:
                currentWord = currentWord + text[x]
                if x == int(textLength - 1):
                    wordsList.append(currentWord)
                    currentWord = str('')

        #Then works out which words should go into each line. Based on the width of the box.
        numOfWords = len(wordsList)
        currentLine = str('')
        linesList = []
        for x in range(0, numOfWords):
            wordWidth, wordHeight = textFont.size(wordsList[x])
            currentLineWidth, currentLineHeight = textFont.size(currentLine) 
            if int(currentLineWidth + wordWidth) <= self.boxSize[0]:
                currentLine = currentLine + wordsList[x] + str(' ')
                if x == int(numOfWords - 1):
                    linesList.append(currentLine)
            else:
                linesList.append(currentLine)
                currentLine = wordsList[x] + str(' ')
                if x == int(numOfWords - 1):
                    linesList.append(currentLine)
                    
        #Next we work out which lines to blit.
        numOfLinesToBlit = int(self.boxSize[1] / wordHeight)
    
        for x in range(self.currentTopLine, int(numOfLinesToBlit + self.currentTopLine)):
            if x < len(linesList):
                textSurface = textFont.render(linesList[x], True, colour)
                screen.blit(textSurface, (self.boxLocation[0], int(self.boxLocation[1] + int(wordHeight * (x - self.currentTopLine)))))

        #Finally the controls for the text box.
        #[Left Side, Top Side, Right Side, Bottom Side]
        topHalfCoords = [self.boxLocation[0], self.boxLocation[1], int(self.boxLocation[0] + self.boxSize[0]), int(self.boxLocation[1] + int(self.boxSize[1] / 2))]
        bottomHalfCoords = [self.boxLocation[0], int(self.boxLocation[1] + int(self.boxSize[1] / 2) + 1), int(self.boxLocation[0] + self.boxSize[0]), int(self.boxLocation[1] + self.boxSize[1])]

        #We need to define the colours and coords for the arrows.
        #For the arrow colour
        arrowColour = [0,0,0]
        if colour[0] < 128:
            arrowColour[0] = colour[0] + 60
        else:
            arrowColour[0] = colour[0] - 60
        if colour[1] < 128:
            arrowColour[1] = colour[1] + 60
        else:
            arrowColour[1] = colour[1] - 60
        if colour[2] < 128:
            arrowColour[2] = colour[2] + 60
        else:
            arrowColour[2] = colour[2] - 60

        #Next is the arrow coords
        distanceFromEdge = int(self.boxSize[1] * 0.03)
        centerOfBox = int(self.boxLocation[0] + (self.boxSize[0] / 2))

        topArrow1 = (centerOfBox, int(self.boxLocation[1] + distanceFromEdge))
        topArrow2 = (int(centerOfBox - distanceFromEdge), int(self.boxLocation[1] + (distanceFromEdge * 2)))
        topArrow3 = (int(centerOfBox + distanceFromEdge), int(self.boxLocation[1] + (distanceFromEdge * 2)))
        topArrowCoords = (topArrow1, topArrow2, topArrow3)

        bottomArrow1 = (centerOfBox, int(self.boxLocation[1] + self.boxSize[1] - distanceFromEdge))
        bottomArrow2 = (int(centerOfBox - distanceFromEdge), int(self.boxLocation[1] + self.boxSize[1] - (distanceFromEdge * 2)))
        bottomArrow3 = (int(centerOfBox + distanceFromEdge), int(self.boxLocation[1] + self.boxSize[1] - (distanceFromEdge * 2)))
        bottomArrowCoords = (bottomArrow1, bottomArrow2, bottomArrow3)

        #THe actual mouse controls.
        if pos[0] >= topHalfCoords[0] and pos[1] >= topHalfCoords[1] and pos[0] <= topHalfCoords[2] and pos[1] <= topHalfCoords[3]:
            pygame.draw.polygon(screen, arrowColour, (topArrowCoords))
            if mouse == (1,0,0):
                if self.currentTopLine > int(0):
                    self.currentTopLine = self.currentTopLine - 1
                    
        if pos[0] >= bottomHalfCoords[0] and pos[1] >= bottomHalfCoords[1] and pos[0] <= bottomHalfCoords[2] and pos[1] <= bottomHalfCoords[3]:
            pygame.draw.polygon(screen, arrowColour, (bottomArrowCoords))
            if mouse == (1,0,0):
                if self.currentTopLine < int(len(linesList) - numOfLinesToBlit):
                    self.currentTopLine = self.currentTopLine + 1
        pygame.display.update()

    def typeText(self, screen, text, font, fontSize, colour, pos, mouse):
        print(text)

#Allows for different kind of mouse(1,0,0) positions.
class betterMouse:
    def __init__(self):
        self.lastMouse = (0,0,0)
        
    def oneClick(self, mouse):
        if mouse != self.lastMouse:
            self.lastMouse = mouse
            return mouse
        else:
            return (0,0,0)

#Allows you to easily make as many buttons as you want.
class texturedButton:
    def __init__(self, button, buttonHover):
        self.buttons = {'button': button,
                        'buttonHover': buttonHover
                        }
        self.activeButton = ('button')
        self.buttonCoords = (0,0)
        self.buttonSize = self.buttons['button'].get_rect().size

    def update(self, screen, coords):
        self.buttonCoords = coords
        screen.blit(self.buttons[self.activeButton], self.buttonCoords)

    #Tests if the button is being hovered and also pressed.
    def buttonHover(self, pos, mouse):
        if pos[0] > self.buttonCoords[0] and pos[0] < int(self.buttonSize[0] + self.buttonCoords[0]) and pos[1] > self.buttonCoords[1] and pos[1] < int(self.buttonSize[1] + self.buttonCoords[1]):
            self.activeButton = ('buttonHover')
            if mouse == (1,0,0):
                return True
            else:
                return False
        else:
            self.activeButton = ('button')
            return False

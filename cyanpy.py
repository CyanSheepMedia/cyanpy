#cyanpy - a collection of small but useful functions that I need quite often.

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
    print(str(len(aList)))
    file = open(fileName, 'w')
    for x in range(0, len(aList)):
        if x == int(len(aList)-1):
            file.write(aList[x])
        else:
            file.write(aList[x] + str('\n'))
    file.close
            
#This functions loads a list from a file.
def fileToList(fileName):
    file = open(fileName,'r')
    aList = file.readlines()
    file.close
    return aList

#Works out the factor increase between the values of a base list and another list.
#Returns a list with the scale factor of each point of data. Lists have to be the same length.
def scaleFactor(baseList, actualList):
    scaleFactors = []
    for x in range(0, len(actualList)):
        scale = actualList[x] / baseList[x]
        scaleFactors.append(scale)
    return scaleFactors

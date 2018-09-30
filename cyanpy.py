#cyanpy - a collection of small but useful functions that I need quite often.

#This functions save a dictionary to a file. 
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

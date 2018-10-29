# Documentation

## Contents
[*dictToFile*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#dicttofiledict-filename)    
[*fileToDict*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#filetodictfilename)   
[*listToFile*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#listtofilelist-filename)    
[*fileToList*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#filetolistfilename)      
[*scaleFactor*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#scalefactorbaselist-actuallist)

### dictToFile(*dict*, *fileName*)
	Converts the dictionary into a string and stores it into a file.
	
### fileToDict(*fileName*)
	Opens a file and returns its contents as a dictionary.

### listToFile(*list*, *fileName*)
	Adds each value of a list into a new line in a file. 
	
### fileToList(*filename*)
	Opens a file returns each line as a single value of a list.
	
### scaleFactor(*baseList*, *actualList*)
	Finds the scale factor from the base list to the actual list. 
	Returns another list of all the scale factors.
	Both lists have to be the same length.

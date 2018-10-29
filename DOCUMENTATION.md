# Documentation

## Contents
[*dictToFile*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#dicttofiledict-filename)    
[*fileToDict*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#filetodictfilename)   
[*listToFile*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#listtofilelist-filename)    
[*fileToList*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#filetolistfilename)   
[*binarySearch*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#binarySearchlist-searchItem)     
[*linearSearch*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#linearSearchlist-searchItem)    
[*scaleFactor*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#scalefactorbaselist-actuallist)

### dictToFile(*dict*, *fileName*)
	Converts the dictionary into a string and stores it into a file.
	
### fileToDict(*fileName*)
	Opens a file and returns its contents as a dictionary.

### listToFile(*list*, *fileName*)
	Adds each value of a list into a new line in a file. 
	
### fileToList(*filename*)
	Opens a file returns each line as a single value of a list.
	
### binarySearch(*list*, *searchItem*)
	Requires a list and a string.
	Performs a binary search on the list, looking for the string.
	Returns True if the string is found.
	Returns False if the string is nout found.
	Best for longer lists. 
	
### linearSearch(*list*, *searchItem*)
	Requires a list and a string.
	Performs a linear search on the list, looking for the string.
	Returns True if the string is found.
	Returns False if the string is nout found.
	Best for shorter lists. 
	
### scaleFactor(*baseList*, *actualList*)
	Finds the scale factor from the base list to the actual list. 
	Returns another list of all the scale factors.
	Both lists have have the same number of values.

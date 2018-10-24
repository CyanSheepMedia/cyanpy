# Documentation

## Contents
[*dictToFile*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#dicttofiledict-filename)    
[*fileToDict*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#filetodictfilename)    
[*scaleFactor*](https://github.com/CyanSheepMedia/cyanpy/blob/master/DOCUMENTATION.md#scalefactorbaselist-actuallist)

## Standalone Functions
### dictToFile(*dict*, *fileName*)
	Converts the dictionary into a string and stores it into a file.
	
### fileToDict(*fileName*)
	Opens a file and returns its contents as a dictionary.

### scaleFactor(*baseList*, *actualList*)
	Finds the scale factor from the base list to the actual list. 
	Returns another list of all the scale factors.
	Both lists have to be the same length.

## Pygame Text Boxes
## textBox(*boxLocation*, *boxSize*)
	pygame.font needs to be initialised.
	This function is to define a new textBox object. 
	boxLocation is the top left corner location of your box. Has to be integer.
	boxSize is how large you want your box in pixels. Has to be integer.
	
	exampleVar = cyanpy.textBox((0,0), (640, 480))
	
## noScroll(*screen*, *text*, *font*, *fontSize*, *colour*)
	This form of text box is meant to be used if you know the text will not overflow 
	*screen* is the variable that defines your pygame display.
	*text* is the text you want to be blitted to the screen. Has to be a string.
	*font* is the font you want to be used. Don't add the ".ttf". Has to be string.
	*fontSize* is the size you want the text to be. Has to be an integer.
	*colour* is the colour you want the text to be. Has to be RBG values like this ((255), (255), (255))
	
	exampleVar.noScroll(screen, text, str('arial'), int(50), ((124),(87),(32)))
	

## clickScroll()

	exampleVar.clickScroll(screen, text, str('freesansbold'), int(25), (0,0,0), pos, mouseB)

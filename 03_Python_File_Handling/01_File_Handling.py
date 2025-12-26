

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"""


"""
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""


# >>>>> SYNTAX <<<<< # :

f = open("demofile.txt") 

f = open("demofile.txt", "rt")

''' Because "r" for read, and "t" for text are the default values, you do not need to specify them. '''
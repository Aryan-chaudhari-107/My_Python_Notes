
''' 
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.
'''


import re
''' Search the string to see if it starts with "The" and ends with "Spain": '''

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("yes, we have a match!") 
else:
    print("nooooo!!")


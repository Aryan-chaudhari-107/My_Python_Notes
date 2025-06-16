
''' The findall() function returns a list containing all matches. '''


# Return a list containing every occurrence of "ai":
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) # Output: ['ai', 'ai']


'''
The list contains the matches in the order they are found.

If no matches are found, an empty list is returned:
'''


# Check if "Portugal" is in the string:
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) # Output: None
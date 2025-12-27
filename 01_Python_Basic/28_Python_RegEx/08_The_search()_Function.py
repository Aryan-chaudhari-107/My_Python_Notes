
# >>>>> SEARCH() FUNCTION <<<<< # :
'''
The search() function searches the string for a match, and 
returns a Match object if there is a match.

If there is more than one match, only the first occurrence 
of the match will be returned:
'''


# Search for the first white-space character in the string:
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
# Output: The first white-space character is located in position: 3


''' If no matches are found, the value None is returned: '''


# Make a search that returns no match:
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) # Outpout: None




# >>>>> MATCH OBJECT <<<<< # :
''' A Match Object is an object containing information about the search and the result. '''
''' Note: If there is no match, the value None will be returned, instead of the Match Object. '''


# The search() function returns a Match object:
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object (<re.Match object; span=(5, 7), match='ai'>)


''' The Match object has properties and methods used to retrieve information about 
the search, and the result: '''


#1: .span() returns a tuple containing the start-, and end positions of the match.
'''Print the position (start- and end-position) of the first match occurrence. '''

# Search for an upper case "S" character in the beginning of a word, and print its position:
import re

txt = "The Rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) # Output: (12, 17) S start at 12



#2: .string returns the string passed into the function

# The string property returns the search string:
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) 
print(x.string) # Output: The rain in Spain



#3: .group() returns the part of the string where there was a match
''' Print the part of the string where there was a match.
The regular expression looks for any words that starts with an upper case "S": '''

# Search for an upper case "S" character in the beginning of a word, and print the word:
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
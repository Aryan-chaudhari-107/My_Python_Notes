""" 
STRINGS (IMMUTABLE):
Once a string is created, you cannot change its contents.
Any operation that modifies a string will create a new string instead. 
"""

# >>>>> UPPER CASE <<<<< # :
a = "Hello, World!"
print(a.upper()) # Output: HELLO, WORLD!



# >>>>> LOWER CASE <<<<< # :
a = "HELLO, WORLD!"
print(a.lower()) # Output: hello, world!



# >>>>> REMOVE WHITESPACE <<<<< # :
''' The strip() method removes any whitespace from the beginning or the end: '''
a = "     Hello, World!       "
print(a.strip()) # Output: Hello, World!



# >>>>> REPLACE STRING <<<<< # :
a = "Hello, World!"
print(a.replace("Hello", "hiii")) # Output: hiii, World!



# >>>>> SPLITE STRING <<<<< # :
''' The split() method returns a list where the text
between the specified separator becomes the list items. '''
a = "Hello, World!"
print(a.split(",")) # Output: ['Hello', ' World!']
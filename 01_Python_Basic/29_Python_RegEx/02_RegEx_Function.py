
'''
[FUNCTION]              [DESCRIPTION]

findall	            Returns a list containing all matches (Use When You Need All Matches)
search	            Returns a Match object if there is a match anywhere in the string (Use When You Need The First Match)
split	            Returns a list where the string has been split at each match
sub	                Replaces one or many matches with a string
'''

#1:
import re

text = "I have 2 cats, 3 dogs, and 10 fish."
matches = re.findall(r"\d+", text)  # Finds all numbers
print(matches)  # Output: ['2', '3', '10']


#2:
import re

text = "Contact us at support@mail.com or info@mail.com."
match = re.search(r"\S+@\S+", text)  # Finds the first email
print(match.group())  # Output: support@mail.com



#3:
import re

text = "Hello, world! Welcome to Python."
words = re.split(r"[ ,!]+", text)  # Splits by spaces and punctuation
print(words)  # Output: ['Hello', 'world', 'Welcome', 'to', 'Python.']


#4:
import re

text = "I love cats and dogs."
new_text = re.sub(r"cats|dogs", "pets", text)  # Replace words
print(new_text)  # Output: I love pets and pets.

''' A set is a set of characters inside a pair of square brackets 
[] with a special meaning: '''

'''
[SETS]                  [DESCRIPTION]

[arn]	          Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	          Returns a match for any lower case character, alphabetically between a and n	
[^arn]	          Returns a match for any character EXCEPT a, r, and n	

[0123]	          Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	          Returns a match for any digit between 0 and 9	
[0-5][0-9]	      Returns a match for any two-digit numbers from 00 and 59	

[a-zA-Z]	      Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	              In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

'''


#1: Check if the string has any a, r, or n characters:
import re
txt = "The rain in Spain"

x = re.findall("[arn]", txt)
print(x) # Output: ['r', 'a', 'n', 'n', 'a', 'n']



#2: Check if the string has any characters between a and n:
import re
txt = "The rain in Spain"

x = re.findall("[a-n]", txt)
print(x) # Output: ['h', 'e', 'a', 'i', 'n', 'i', 'n', 'a', 'i', 'n']



#3: Check if the string has other characters than a, r, or n:
import re
txt = "The rain in Spain"

x = re.findall("[^arn]", txt)
print(x) # Output: ['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']



#4: Check if the string has any 0, 1, 2, or 3 digits:
import re
txt = "The rain in Spain"

x = re.findall("[0123]", txt)

if x:
  print(x)
else:
  print("No match") # Output: [No match] cuz there no digit in txt



#5: Check if the string has any digits:
import re
txt = "8 times before 11:45 AM"

x = re.findall("[0-9]", txt)
print(x) # Output: ['8', '1', '1', '4', '5']



#6: Check if the string has any two-digit numbers, from 00 to 59:
import re
txt = "8 times before 11:45 AM"

x = re.findall("[0-5][0-9]", txt)
print(x)  # Output: ['11', '45']



#7: Check if the string has any characters from a to z lower case, and A to Z upper case:
import re
txt = "8 times before 11:45 AM"

x = re.findall("[a-zA-Z]", txt)
print(x) # Output: ['t', 'i', 'm', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'A', 'M']



#8: Check if the string has any + characters:
import re
txt = "8 times before 11:45 AM"

x = re.findall("[+]", txt)

if x:
   print(x)
else:
   print("No match") # Output: No match
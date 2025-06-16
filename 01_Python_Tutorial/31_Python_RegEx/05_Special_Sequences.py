
''' A special sequence is a \ followed by one of the characters in the list 
below, and has a special meaning: '''

'''
[CHARACTER]          [DESCRIPTION]                                                                                                                          [EXAMPLE]

\A	             Returns a match if the specified characters are at the beginning of the string	                                                            "\AThe"	
\Z	             Returns a match if the specified characters are at the end of the string	                                                                "Spain\Z"

\b	             Returns a match where the specified characters are at the beginning or at the end of a word                                                r"\bain"
  (the "r" in the beginning is making sure that the string is being treated as a "raw string")                                             	            r"ain\b"

\B	             Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word                             r"\Bain"
  (the "r" in the beginning is making sure that the string is being treated as a "raw string")	                                                            r"ain\B"

\d	             Returns a match where the string contains digits (numbers from 0-9)	                                                                    "\d"	
\D	             Returns a match where the string DOES NOT contain digits	                                                                                "\D"

\s	             Returns a match where the string contains a white space character	                                                                        "\s"	
\S	             Returns a match where the string DOES NOT contain a white space character	                                                                "\S"

\w	             Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	             Returns a match where the string DOES NOT contain any word characters	"\W"	
'''


#1: Check if the string starts with "The":
import re
txt = "The rain in Spain"

x = re.findall("\AThe", txt)
print(x)

if x:
  print("Yes, there is a match!") # Output: Yes, there is a match!
else:
  print("No match")



#2: Check if the string ends with "Spain":
import re
txt = "The rain in Spain"

x = re.findall("Spain\Z", txt)
print(x)

if x:
  print("Yes, there is a match!") # 
else:
  print("No match")



#3:

#>> Check if "ain" is present at the "beginning" of a WORD:
import re
txt = "The rain in Spain"

x = re.findall(r"\bain", txt)
print(x)

if x:
  print("Yes, ain present at the begging!")
else:
  print("No, ain is not present at the begging!") # Output: No, ain is not present at the begging!


#>> Check if "ain" is present at the "end" of a WORD:
import re
txt = "The rain in Spain"

x = re.findall(r"ain\b", txt)
print(x)

if x:
  print("Yes, ain is present at the end!") # Output: Yes, ain is present at the end!
else:
  print("No, ain is not present at the end!")



#4: 

#>> Check if "ain" is present, but NOT at the beginning of a word:
import re 
txt = "The rain in Spain"

x = re.findall(r"\Bain", txt)
print(x)

if x:
  print("True, ain is not present at the begging!") # Output: True, ain is not present at the begging!
else:
  print("Flase, ain is present at the begging!")


#>> Check if "ain" is present, but NOT at the end of a word:
import re
txt = "The rain in Spain"

x = re.findall(r"ain\B", txt)
print(x)

if x:
  print("True, ain is not present at the end!")
else:
  print("Flse, ain is present at the end!") # Output: Flse, ain is present at the end!



#5: 

#>> Check if the string contains any digits (numbers from 0-9):
import re
txt = "The rain in Spain"

x = re.findall("\d", txt)
print(x)

if x:
  print("Yes contain")
else:
  print("Not contain") # Output: Not contain


#>> string doesnt contain a digit (Reverse of "\d")
import re
txt = "The rain in Spain"

x = re.findall("\D", txt)
print(x)

if x:
  print("True, not contain") # Output: True, not contain
else:
  print("Flase, it's contain")



#6:

#>> Return a match at every white-space character:
import re
txt = "The rain in Spain"

x = re.findall("\s", txt)
print(x) # Output: [' ', ' ', ' ']


#>> Return a match at every NON white-space character:
import re
txt = "The rain in Spain"

x = re.findall("\S", txt)
print(x) # Output: ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']




#6:

#>> Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
import re
txt = "The rain in Spain"

x = re.findall("\w", txt)
print(x) # Output: ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']


#>> Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
import re
txt = "The rain in Spain"

x = re.findall("\W", txt)
print(x) # Output: [' ', ' ', ' ']

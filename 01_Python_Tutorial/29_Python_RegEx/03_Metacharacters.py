

# Metacharacters are characters with a special meaning: 
'''
[CHARACTER]           [DESCRIPTION EXAMPLE TRY IT]                       [EXAMPLE]

[]	              A set of characters	                                    "[a-m]"	

\	                Signals a special sequence 
(can also be used to escape special characters)	                          "\d"

^	                Starts with	                                            "^hello"
$	                Ends with	                                              "planet$"	

.	                Any character (except newline character)	              "he..o"	
*	                Zero or more occurrences	                              "he.*o"	
+	                One or more occurrences	                                "he.+o"	
?	                Zero or one occurrences	                                "he.?o"	
{}	              Exactly the specified number of occurrences	            "he.{2}o"	

|	                Either or	                                              "falls|stays"

()	              Capture and group
'''



#1: Find all lower case characters alphabetically between "a" and "m":
import re
txt = "The rain in Spain"

x = re.findall("[a-m]", txt)
print(x) # Output: ['h', 'e', 'a', 'i', 'i', 'a', 'i']



#2: Find all digit characters:
import re
txt = "That will be 59 dollars"

x = re.findall("\d", txt)
print(x) # Output: ['5', '9']



#3: Check if the string starts with 'hello':
import re
txt = "hello planet"

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")



#4: Check if the string ends with 'planet':
import re
txt = "hello planet"

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
  


#5: Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
import re
txt = "hello planet"

x = re.findall("h...o", txt)
y = re.findall("pl...t", txt)
print(x) # Output: ["hello"]
print(y) # Output: ["planet"]



#6: Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
import re
txt = "hello planet"

x = re.findall("he.*o", txt)
print(x) # Output: ["hello"]



#7: Search for a sequence that starts with "he", followed by 1 or more (any) characters, and an "o":
import re
txt = "hello planet"

x = re.findall("he.+o", txt)
print(x) # Output: ["hello"]



#8: Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
import re
txt = "hello planet"

x = re.findall("he.?o", txt)
print(x) 
'''This time we got no match, because there were not zero, not one, but 
two characters between "he" and the "o". '''
 


#9: Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
import re
txt = "hello planet"

x = re.findall("he.{2}o", txt)
print(x) # Output: ["hello"]



#10: Check if the string contains either "falls" or "stays":
import re
txt = "The rain in Spain falls mainly in the plain!"

x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# >>>>> ESCAPE CHARACTERS <<<<< # :

# CODE                       RESULT
# \'	        ::          Single Quote	
# \\	        ::          Backslash	
# \n	        ::          New Line	
# \r	        ::          Carriage Return	
# \t	        ::          Tab	
# \b	        ::          Backspace	
# \f	        ::          Form Feed	
# \ooo	        ::          Octal value	
# \xhh	        ::          Hex value

''' To insert characters that are illegal in a 
string, use an escape character. '''

''' An escape character is a backslash \ 
followed by the character you want to insert. '''

txt = "We are the so-called "Vikings" from the north."
print (txt) # Error

txt = "We are the so-called \"Vikings\" from the north."
print (txt) # Output: We are the so-called "Vikings" from the north.

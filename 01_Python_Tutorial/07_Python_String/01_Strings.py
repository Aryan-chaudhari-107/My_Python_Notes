
# >>>>> STRINGS <<<<< # :
''' Strings in python are surrounded by either single 
quotation marks, or double quotation marks. '''

""" ('hello' is the same as "hello".) """

print("Hello")
print('Hello')



# >>>>> QUOTES INSIDE QUOTES <<<<< # :
''' You can use quotes inside a string, as long as 
they don't match the quotes surrounding the string. '''

print("It's alright")
print("He is called 'BUNNY'")
print('He is called "BUNNY"')



# >>>>> ASSIGN STRING TO A VARIABLE <<<<< # :
a = "Hello"
print(a)



# >>>>> MULTILINE STRINGS <<<<< # :
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) # we can also use single quote



# >>>>> STRINGS ARE ARRAYS <<<<< # :
''' strings in Python are arrays of bytes 
representing unicode characters. '''

''' However, Python does not have a character data type, 
a single character is simply a string with a length of 1. '''

''' Square brackets can be used to access elements of the string. '''

a = "Hello, World!"
print(a[1]) # Output: e



# >>>>> LOOPING THROUGH A STRING <<<<< # :
''' Since strings are arrays, we can loop through 
the characters in a string, with a for loop. '''

for x in "banana":
  print(x)
# Output: b
#         a
#         n
#         a
#         n 
#         a



# >>>>> STRING LENGTH <<<<< # :
a = "Hello, World!"
print(len(a)) # Output: 13



# >>>>> CHECK STRING <<<<< # :
''' To check if a certain phrase or character is 
present in a string, we can use the keyword "in". '''

txt = "The best things in life are free!"
print("free" in txt) # Output: True

""" (Use it in an if statement) """

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")



# >>>>> CHECK NOT <<<<< # :
txt = "The best things in life are free!"
print("expensive" not in txt) # Output: True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# >>>>> ACCESS ITEMS <<<<< # :
#1: positive
''' Print the second item in the tuple: '''

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # Output: banana

#2: negative 
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # Output: cherry



# >>>>> RANGE OF INDEXES <<<<< # :
''' When specifying a range, the return value will be a new tuple with the specified items. '''

''' Return the third, fourth, and fifth item: '''

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # Output: ['cherry', 'orange', 'kiwi']

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) # Output: ['apple', 'banana', 'cherry', 'orange']

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']



# >>>>> RANGE OF NEGATIVE INDEXES <<<<< # :
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # Output: ['orange', 'kiwi', 'melon']



# >>>>> CHECK IF ITEM EXISTS <<<<< # :
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")





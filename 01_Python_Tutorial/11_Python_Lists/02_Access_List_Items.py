
# >>>>> ACCESS ITEMS <<<<< # :
#1: positive
''' Print the 2 item of the list: '''

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # Output: banana

#2: negative
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # Output: cherry



# >>>>> RANGE OF INDEXES <<<<< # :
''' When specifying a range, the return value will be a new list with the specified items. '''

''' Return the third, fourth, and fifth item: '''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # Output: ['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # Output: ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']



# >>>>> RANGE OF NEGATIVE INDEXES <<<<< # :
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # Output: ['orange', 'kiwi', 'melon']



# >>>>> CHECK IF ITEM EXISTS <<<<< # :
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
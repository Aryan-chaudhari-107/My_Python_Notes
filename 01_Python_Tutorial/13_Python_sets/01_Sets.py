
# >>>>> SET EX. <<<<< # :
thisset = {"apple", "banana", "cherry"}
print(thisset)

''' Set items are unordered, unchangeable, and do not allow 
duplicate values. '''

''' Once a set is created, you cannot change its items, but you 
can remove items and add new items. '''



# >>>>> DUPLICATES ARE NOT ALLOWED <<<<< # :
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # Output: {'cherry', 'banana', 'apple'}

''' Note: The values (True and 1), (False and 0) are considered the same value 
in sets, and are treated as duplicates: '''

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) # Output: {True, 2, 'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", 0, False, True}
print(thisset) # Output: {0, 'apple', 'banana, True, 'cherry'}



# >>>>> SET LENGTH <<<<< # :
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) # Output: 3



# >>>>> SET ITEMS - DATA TYPES <<<<< # :
''' Set items can be of any data type: '''

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

''' A set can contain different data types: '''

set1 = {"abc", 34, True, 40, "male"}



# >>>>> SET TYPE() <<<<< # :
myset = {"apple", "banana", "cherry"}
print(type(myset))



# >>>>> THE SET() CONSTRUCTOR <<<<< # :
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
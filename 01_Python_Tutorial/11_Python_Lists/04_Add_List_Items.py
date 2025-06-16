
# >>>>> APPEND ITEMS <<<<< # :
''' To add an item to the end of the list, use the append() method: '''

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



# >>>>> INSERT ITEMS <<<<< # :
''' To insert a new list item, without replacing any of the existing values, 
we can use the insert() method. '''

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # Output: ['apple', 'banana', 'watermelon', 'cherry']



# >>>>> EXTEND LIST <<<<< # :
''' To append elements from another list to the current list, 
use the extend() method. '''

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']



# >>>>> ADD ANY ITERABLE TO LIST <<<<< # :
''' The extend() method does not have to append lists, 
you can add any iterable object (tuples, sets, dictionaries etc.). '''

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']


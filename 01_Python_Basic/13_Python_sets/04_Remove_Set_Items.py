
# >>>>> REMOVE() METHOD <<<<< # :
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset) # Output: {'apple', 'cherry'}

''' Note: If the item to remove does not exist, remove() 
will raise an error. '''



# >>>>> DISCARD() METHOD <<<<< # :
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

print(thisset) # Output: {'apple', 'cherry'}

''' Note: If the item to remove does not exist, discard()
will NOT raise an error. '''



# >>>>> POP() METHOD <<<<< # :
''' You can also use the pop() method to remove an item, but 
this method will remove a random item, so you cannot be sure 
what item that gets removed. '''

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) # Output: apple

print(thisset) # Output: {'cherry', 'banana'}






# >>>>> REMOVE SPECIFIED ITEM <<<<< # :
''' Remove "banana": '''

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # Output: ['apple', 'cherry']


''' If there are more than one item with the specified value, 
the remove() method removes the first occurrence: '''

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) # Output: ['apple', 'cherry', 'banana', 'kiwi']



# >>>>> REMOVE SPECIFIED INDEX <<<<< # :
''' The pop() method removes the specified index. '''

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # Output: ['apple', 'cherry']

''' If you do not specify the index, the pop() method removes the last item. '''

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # Output: ['apple', 'banana']



# >>>>> REMOVE SPECIFIED INDEX WITH "del" <<<<< # :
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # Output: ['banana', 'cherry']

''' Delete the entire list: '''

thislist = ["apple", "banana", "cherry"]
del thislist



# >>>>> CLEAR THE LIST <<<<< # :
''' The clear() method empties the list. '''

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # Output: []

# >>>>> ADD() METHOD <<<<< # :
''' Add an item to a set, using the add() method: '''  

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # Output: {'banana', 'apple', 'cherry', 'orange'}



# >>>>> UPDATE() METHOD <<<<< # :
''' Add elements from tropical into thisset: '''

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset) # Output: {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}



# >>>>> ADD ANY ITERABLE TO SET <<<<< # :
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)

print(thisset) # Output: {'banana', 'cherry', 'apple', 'orange', 'kiwi'}
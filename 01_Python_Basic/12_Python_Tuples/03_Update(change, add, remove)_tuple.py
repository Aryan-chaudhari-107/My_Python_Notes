

# >>>>> CHANGE TUPLE VALUES <<<<< # :
''' Once a tuple is created, you cannot change its values. 
Tuples are unchangeable, or immutable as it also is called. '''

''' But there is a workaround. You can convert the tuple into a list, 
change the list, and convert the list back into a tuple. '''

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # Output: ("apple", "kiwi", "cherry")



# >>>>> ADD ITEMS <<<<< # :
''' Since tuples are immutable, they do not have a built-in append() method 
but there are other ways to add items to a tuple. '''

#1: Convert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple= tuple(y)

print(thistuple) # Output: ('apple', 'banana', 'cherry', 'orange')

#2:  Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) # Output: ('apple', 'banana', 'cherry', 'orange')



# >>>>> REMOVE ITEMS <<<<< # :
''' Tuples are unchangeable, so you cannot remove items from it but you 
can use the same workaround as we used for changing and adding tuple items:'''

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

''' Or you can delete the tuple completely: '''
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
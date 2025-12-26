
''' 
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of 
the methods __iter__() and __next__().
'''

# Iterator vs Iterable
''' Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers 
which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator: 
'''

mytuple = ("apple", "banana", "cherry") # This is ITERABLE
myit = iter(mytuple) # Creating an INERATOR from the ITERABLE

print(next(myit)) # Output: apple 
print(next(myit)) # Output: banana
print(next(myit)) # Output: cherry    


''' Even strings are iterable objects, and can return an iterator: '''
mystr = "banana"
myit = iter(mystr)

print(next(myit)) # Output: b
print(next(myit)) # Output: a
print(next(myit)) # Output: n
print(next(myit)) # Output: a
print(next(myit)) # Output: n
print(next(myit)) # Output: a
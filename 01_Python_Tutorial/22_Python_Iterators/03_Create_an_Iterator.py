
''' To create an object/class as an iterator you have to implement 
the methods __iter__() and __next__() to your object. '''

'''  
The __iter__() method, you can do operations (initializing etc.),
but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the 
next item in the sequence.
'''

#1:
class mynum:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a 
        self.a += 1
        return x
    
myclass = mynum()
myiter = iter(myclass) # using ITERATOR (you can also use 'myiter = iter(mynum())')

print(next(myiter)) # Output: 1
print(next(myiter)) # Output: 2
print(next(myiter)) # Output: 3
print(next(myiter)) # Output: 4
print(next(myiter)) # Output: 5


#2: THIS IS ALSO CORRECT
class mynum:
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        x = self.a 
        self.a += 1
        return x
    
myclass = mynum()
myiter = iter(myclass) # using ITERATOR (u can also use 'myiter = iter(mynum())')

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

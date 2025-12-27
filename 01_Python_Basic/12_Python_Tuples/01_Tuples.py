
# >>>>> TUPLE EX. <<<<< # :
thistuple = ("apple", "banana", "cherry")
print(thistuple) # Output: ('apple', 'banana', 'cherry')

''' Tuple items are ordered, unchangeable, and allow duplicate values. '''

''' Tuple items are indexed, the first item has index [0], 
the second item has index [1] etc. '''



# >>>>> ALLOW DUPLICATES <<<<< # :
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) 



# >>>>> TUPLE LENGTH <<<<< # :
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # Output: 3



# >>>>> CREATE TUPLE WITH ONE ITEM <<<<< # :
''' One item tuple, remember the comma: '''

thistuple = ("apple",)
print(type(thistuple)) # Output: <class 'tuple'>

#NOT a tuple
thistuple = ("apple")  
print(type(thistuple)) # Output: <class 'str'>



# >>>>> TUPLE ITEMS - DATA TYPES <<<<< # :
''' Tuple items can be of any data type: '''

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

''' A tuple can contain different data types: '''

tuple1 = ("abc", 34, True, 40, "male")



# >>>>> TUPLE TYPE() <<<<< # :
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # Output: <class 'tuple'>



# >>>>> THE TUPLE() CONSTRUCTOR <<<<< # :
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
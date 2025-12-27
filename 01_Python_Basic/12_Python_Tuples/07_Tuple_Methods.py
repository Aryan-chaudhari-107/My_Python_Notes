

'''
[METHOD]                   [DESCRIPTION]

count()	   ::     Returns the number of times a specified value occurs in a tuple
index()    :: 	  Searches the tuple for a specified value and returns the position of where it was found

'''

fruits = ("apple", "banana", "cherry", "apple")
print(fruits.count("apple")) # Output: 2

fruits = ("apple", "banana", "cherry")
print(fruits.index("banana")) # Output: 1
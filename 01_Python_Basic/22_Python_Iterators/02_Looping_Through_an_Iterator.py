
''' We can also use a for loop to ITERATE through an ITERABLE object: '''

#1:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

#2:
mystr = "banana"
for x in mystr:
  print(x)

''' The for loop actually creates an iterator object and executes the 
next() method for each loop.'''

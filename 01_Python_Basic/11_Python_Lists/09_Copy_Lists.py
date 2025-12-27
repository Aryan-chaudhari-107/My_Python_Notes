
# >>>>> COPY() METHOD <<<<< # :
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) 



#  >>>>> LIST() METHOD <<<<< # :
''' Another way to make a copy is to use the built-in method list(). '''

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) 



# >>>>> SLICE OPERATOR <<<<< # :
''' You can also make a copy of a list by using the : (slice) operator. '''

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
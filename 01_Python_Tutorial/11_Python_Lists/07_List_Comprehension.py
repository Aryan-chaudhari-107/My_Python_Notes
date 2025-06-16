
# >>>>> LIST COMPREHENSION <<<<< # :
#1: without comprehension
''' List comprehension offers a shorter syntax when you want 
to create a new list based on the values of an existing list. '''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist) # Output: ['apple', 'banana', 'mango']


#2: with comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)  # Output: ['apple', 'banana', 'mango']



# >>>>> CONDITION <<<<< # :
#1
''' The condition is like a filter that only accepts the items that evaluate to True. '''

''' Only accept items that are not "apple": '''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits if x != "apple"]

print(newlist2)  # Output: ["banana", "cherry", "kiwi", "mango"]

''' The condition if x != "apple"  will return True for all elements other than "apple"
making the new list contain all fruits except "apple". '''

#2
''' The condition is optional and can be omitted: '''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits]
print(newlist2) # Output: ["apple", "banana", "cherry", "kiwi", "mango"] 



# >>>>> ITERABLE <<<<< # :
''' The iterable can be any iterable object, like a list, tuple, set etc. '''

''' You can use the range() function to create an iterable: '''
newlist3 = [x for x in range(10)] # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(newlist3)

''' Accept only numbers lower than 5: '''
newlist3 = [x for x in range(10) if x < 5]
print(newlist3) # Output: [0, 1, 2, 3, 4,]



# >>>>> EXPRESSION <<<<< # :
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist4 = [x.upper() for x in fruits]
print(newlist4) # Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

''' You can set the outcome to whatever you like: '''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist4 = ['hello' for x in fruits]
print(newlist4) # Output: ["hello", "hello", "hello", "hello", "hello"]

''' The expression can also contain conditions, not like a filter, 
but as a way to manipulate the outcome: '''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist4 = [x if x != "banana" else "orange" for x in fruits] 
# Output: ["apple", "orange", "cherry", "kiwi", "mango"]
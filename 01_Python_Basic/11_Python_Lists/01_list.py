
# >>>>> LIST EX.<<<<< # :
''' Lists are used to store multiple items in a single variable. '''

thislist = ["apple", "banana", "cherry"]
print(thislist)

''' List items are indexed, the first item has index [0],
the second item has index [1] etc. '''



# >>>>> ALLOW DUPLICATES <<<<< # :
''' Since lists are indexed, lists can have items with the same value: '''

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)



# >>>>> LIST LENGTH <<<<< # :
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # Output: 3



# >>>>> LIST ITEMS - DATA TYPES <<<<< # :
''' List items can be of any data type: '''

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

''' A list can contain different data types: '''

list1 = ["abc", 34, True, 40, "male"]



# >>>>> LIST TYPE() <<<<< # :
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # Output: <class 'list'>



# >>>>> THE LIST() CONSTRUCTOR <<<<< # :
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) 
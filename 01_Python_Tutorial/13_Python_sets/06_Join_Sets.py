
# >>>>> UNION() METHOD <<<<< # :
''' Returns a new set. '''
#1
''' The union() method returns all items from both sets. '''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) # Output: {3, 'b', 2, 1, 'a', 'c'}

#2
''' You can use the | operator instead of the union() method. '''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3} 

set3 = set1 | set2
print(set3) # Output: {'a', 2, 1, 'c', 'b', 3}

#3
''' Join multiple sets with the union() method: '''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) # Output: {'a', 1, cherry, 'c', banana, apple, Elena, John, 2, 'b', 3}

#4
''' Join multiple sets with the | operator: '''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset) # Output: {'b', Elena, 1, 2, 'c', 3, John, banana, apple, cherry, 'a'}



# >>>>> JOIN A SET AND A TUPLE <<<<< # :
''' The union() method allows you to join a set with other data types,
like lists or tuples. The result will be a set. '''

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z) # Output: {'c', 'a', 1, 2, 'b', 3}

""" Note: The  | operator only allows you to join sets with sets, and not with other 
data types like you can with the union() method. """



# >>>>> UPDATE() METHOD <<<<< # :
''' It will change the original set instead of returning a new set. '''

''' The update() method inserts all items from one set into another. '''

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3} 

set1.update(set2)
print(set1) # Output: {'c', 'a', 1, 2, 'b', 3}

""" Note: Both union() and update() will exclude any duplicate items. """



# >>>>> INTERSECTION() METHOD <<<<< # :
''' Returns a new set. '''
#1
''' Keep ONLY the duplicates'''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) # Output: {'apple'}

#2
''' You can use the & operator instead of the intersection() method. '''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) # Output: {'apple'}

""" Note: The & operator only allows you to join sets with sets, and not 
with other data types like you can with the intersection() method. """



# >>>>> INTERSECTION_UPDATE() MATHOD <<<<< # :
''' It will change the original set instead of returning a new set. '''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)  # Output: {'apple'}


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3) # Output: {False, 1, 'apple'}



# >>>>> DIFFERENCE() MATHOD <<<<< # :
''' Return a new set. '''
#1
''' The difference() method will contain only the items from the first
set that are not present in the other set. '''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3) # Output: {'banana', 'cherry'}

#2
''' You can use the - operator instead of the difference() method. '''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) # Output: {'banana', 'cherry'}

""" Note: The - operator only allows you to join sets with sets, 
and not with other data types like you can with the difference() method. """


# >>>>> DIFFERENCE_UPDATE() MATHOD <<<<< # :
''' It will change the original set instead of returning a new set. '''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1) # # Output: {'banana', 'cherry'}



# >>>>> SYMMETRIC_DIFFERENCE() METHOD <<<<< # :
''' Return new set '''
#1
''' The symmetric_difference() method will keep only the elements that 
are NOT present in both sets. '''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) # Output: {'google', 'banana', 'microsoft', 'cherry'}

#2
''' You can use the ^ operator instead of the symmetric_difference() method. '''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3) # Output: {'google', 'banana', 'microsoft', 'cherry'}

""" Note: The ^ operator only allows you to join sets with sets, and not 
with other data types like you can with the symmetric_difference() method. """



# >>>>> SYMMETRIC_DIFFERENCE_UPDATE() METHOD <<<<< # :
''' It will change the original set instead of returning a new set. '''

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1) # Output: {'google', 'banana', 'microsoft', 'cherry'}
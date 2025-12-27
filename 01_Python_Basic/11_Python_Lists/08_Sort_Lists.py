
# >>>>> SORT LIST ALPHANUMERICALLY <<<<< # :
''' List objects have a sort() method that will sort the list 
alphanumerically, ascending, by default: '''

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # Output: [23, 50, 65, 82, 100]



# >>>>> SORT DESCENDING <<<<< # :
''' To sort descending, use the keyword argument reverse = True: '''

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # Output: [100, 82, 65, 50, 23]



# >>>>> CUSTOMIZE SORT FUNCTION <<<<< # :
''' You can also customize your own function by using the
keyword argument key = function. '''

def myfunc(n):
    return abs(n - 50)
    
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) # Sorted by distance to 50 (smallest to largest):
print(thislist) # Output: [50, 65, 23, 82, 100]



# >>>>> CASE INSENSITIVE SORT <<<<< # :
''' By default the sort() method is case sensitive, resulting in all 
capital letters being sorted before lower case letters: '''

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # Output: ['Kiwi', 'Orange', 'banana', 'cherry']

''' So if you want a case-insensitive sort function, use str.lower as a key function: '''

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # Output: ['banana', 'cherry', 'Kiwi', 'Orange']



# >>>>> REVERSE ORDER <<<<< # :
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # Output: ['cherry', 'Kiwi', 'Orange', 'banana']
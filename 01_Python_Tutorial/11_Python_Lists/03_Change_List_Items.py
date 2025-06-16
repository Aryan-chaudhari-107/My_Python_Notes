
# >>>>> CHANGE LIST ITEM <<<<< # :
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # Output: ['apple', 'blackcurrant', 'cherry']



# >>>>> CHANGE A RANGE OF ITEM VALUES <<<<< # :
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']



# >>>>> INSERT MORE ITEMS THAN YOU REPLACE <<<<< # :
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # Output: ['apple', 'blackcurrant', 'watermelon', 'cherry']



# >>>>> INSERT LESS ITEMS THAN YOU REPLACE <<<<< # :
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # Output: ['apple', 'watermelon']


# >>>>> LOOP THROUGH A DICTIONARY <<<<< # :
''' Print all key names in the dictionary, one by one: '''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) 
# Output: brand
#         model 
#         year

''' Print all values in the dictionary, one by one: '''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x]) 
# Output: Ford 
#         Mustang
#         1964



# >>>>> VALUE() METHOD <<<<< # :
''' You can also use the values() method to return values of a dictionary: '''

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
# Output: Ford 
#         Mustang
#         1964



# >>>>> KEY() METHOD <<<<< # :
''' You can use the keys() method to return the keys of a dictionary: '''

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
# Output: brand
#         model 
#         year



# >>>>> ITEM() MELTHOD <<<<< # :
''' Loop through both keys and values, by using the items() method: '''

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
# Output: brand Ford
#         model Mustang
#         year 1964

# >>>>> ACCESS ITEMS <<<<< # :
''' You can access the items of a dictionary by 
referring to its key name, inside square brackets: '''

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["model"]) # Output: Mustang

''' There is also a method called get() that will give you the same result '''

print(thisdict.get("year")) # Output: 1964



# >>>>> GET KEYS <<<<<< # :
''' The keys() method will return a list of all the keys in the dictionary. '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x) # Output: dict_keys(['brand', 'model', 'year'])



# >>>>> GET VALUES <<<<<< # :
''' The values() method will return a list of all the values in the dictionary. '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x) # Output: dict_values(['Ford', 'Mustang', 1964])



# >>>>> GET ITEMS <<<<<< # :
''' The items() method will return each item in a dictionary, as tuples in a list. '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)
# Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])



# >>>>> CHECK IF KEY EXISTS <<<<< # :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# >>>>> DICTIONARY EX. <<<<< # :
''' Dictionaries are used to store data values in key:value pairs. '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

''' A dictionary is a collection which is ordered*, changeable and do not allow duplicates. '''



# >>>>> DUPLICATES ARE NOT ALLOWED <<<<< # :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}



# >>>>> DICTIONARY LENGTH <<<<< # :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict)) # Output: 3



# >>>>> DICTIONARY ITEMS - DATA TYPES <<<<< # :
''' The values in dictionary items can be of any data type: '''

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}



# >>>>> DICTIONARY TYPE() <<<<< # :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) # Output: <class 'dict'>



# >>>>> THE DICT() CONSTRUCTOR <<<<< # :
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) # Output: {'name': 'John', 'age': 36, 'country': 'Norway'}

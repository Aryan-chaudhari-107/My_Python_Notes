
# >>>>> CHANGE VALUE <<<<< # :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}



# >>>>> UPDATE DICTIONARY <<<<< # :
''' The argument must be a dictionary, or an iterable 
object with key:value pairs. '''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

''' 
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.
'''

# >>>>> JSON IN PYTHON <<<<< # :
''' Python has a built-in package called json, which can be used to work with JSON data. '''

import json



# >>>>> PARSE JSON - CONVERT FROM JSON TO PYTHON <<<<< # :
''' If you have a JSON string, you can parse it by using the json.loads() method. '''

import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) # Output: 30



# >>>>> CONVERT FROM PYTHON TO JSON <<<<< # :
''' If you have a Python object, you can convert it into a JSON string by using 
the json.dumps() method. '''

import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) # Output: {"name": "John", "age": 30, "city": "New York"}



# >>>>> PYTHON OBJECTS ARE CONVERTED INTO THE JSON(JAVASCRIPT) EQUIVALENT <<<<< # :
''' 
[PYTHON]	    [JSON]

dict	        Object
list	        Array
tuple	        Array
str	          String
int	          Number
float	        Number
True	        true
False	        false
None	        null
'''


import json

print(json.dumps({"name": "John", "age": 30}))   # Output: {"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"]))          # Output: ["apple", "bananas"]
print(json.dumps(("apple", "bananas")))          # Output: ["apple", "bananas"]
print(json.dumps("hello"))                       # Output: "hello"
print(json.dumps(42))                            # Output: 42
print(json.dumps(31.76))                         # Output: 31.76
print(json.dumps(True))                          # Output: true
print(json.dumps(False))                         # Output: false
print(json.dumps(None))                          # Output: null

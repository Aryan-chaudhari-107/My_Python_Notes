
''' You can choose to import only parts from a module, by using the from keyword. '''

from Mymodule import person1

print(person1["name"]) # Output: John 
 
""" Note: When importing using the from keyword, do not use the module name 
when referring to elements in the module. 

Example: person1["age"], not mymodule.person1["age"] """
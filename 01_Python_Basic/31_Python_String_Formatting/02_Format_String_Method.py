
# >>>>> STRING FORMAT <<<<< # :
#1:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#2:
txt = "The price is {} dollars".format(49)
print(txt)

#3:
""" You can add parameters inside the curly brackets to specify how to convert the value: """
txt = "The price is {:.2f} dollars".format(49)
print(txt)



# >>>>> MULTIPLE VALUES <<<<< # :
#1:

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#2:
myorder = "I want {} pieces of item number {} for {:.2f} dollars.".format(3,567,49)
print(myorder)



# >>>>> INDEX NUMBERES <<<<< # :
#1:
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#2:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))



# >>>>> NAMED INDEXES <<<<< #:
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
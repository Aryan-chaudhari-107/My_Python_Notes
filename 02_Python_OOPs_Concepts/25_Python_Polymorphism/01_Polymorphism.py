
''' The word "polymorphism" means "many forms", and in programming it refers 
to methods/functions/operators with the same name that can be executed on many 
objects or classes '''



# >>>>> FUNCTION POLYMORPHISM <<<<< # :
''' An example of a Python function that can be used on different 
objects is the len() function. '''

#1: String
x = "Hello World!"
print(len(x))

#2: Tuple
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

#3: Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",  
  "year": 1964
}
print(len(thisdict))



# >>>>> CLASS POLYMORPHISM <<<<< # :
''' Polymorphism is often used in Class methods, where we can have multiple 
classes with the same method name. '''

#1:
class CreditCard:
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card."

class PayPal:
    def pay(self, amount):
        return f"Paid ₹{amount} using PayPal."

class Cash:
    def pay(self, amount):
        return f"Paid ₹{amount} in cash."

# Using polymorphism
payment_methods = [CreditCard(), PayPal(), Cash()]
for method in payment_methods:
    print(method.pay(500))  # Output varies based on the payment method

'''
# You can also use this Polymorphism
cc = CreditCard()
p = PayPal()
c = Cash()
for method in (cc,p,c):
   print(method.pay(500))
'''



#2:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

# Using polymorphism
vehical = [Car("Ford", "Mustang"), Boat("Ibiza", "Touring 20"), Plane("Boeing", "747")]
for x in vehical:
   print(x.brand)
   print(x.model)
   x.move()

'''
# You can also use this 
c = Car("Ford", "Mustang")       # Create a Car objecta
b = Boat("Ibiza", "Touring 20")  # Create a Boat object
p = Plane("Boeing", "747")       # Create a Plane object

for x in (c, b, p):
  print(x.brand)
  print(x.model)
  x.move() # Output: Drive!, Sail!, Fly!'''



# >>>>> INHERITANCE CLASS POLYMORPHISM <<<<< # :
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
# Output: Ford
#         Mustang
#         Move!
#         Ibiza
#         Touring 20
#         Sail!
#         Boeing
#         747
#         Fly!


''' 
class definitions cannot be empty, but if you for some reason have a class definition with no 
content, put in the pass statement to avoid getting an error.
'''

class horse:
    def make_sound(self):
        pass                  # Placeholder for future implementation

class Dog:
    def make_sound(self):
        print("Woof! Woof!")

class Cat:
    def make_sound(self):
        print("Meow!")

# Creating objects 
h = horse()
d = Dog()
c = Cat()

# Calling methods
h.make_sound()  # Empty
d.make_sound()  # Output: Woof! Woof!
c.make_sound()  # Output: Meow!
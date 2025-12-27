
# >>>>> CONVERSION <<<<< # :
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))



# >>>>> COMPLEX NUMBER TO INT OR FLOAT <<<<< # : 
n = 3 + 5j

real_part = int(n.real)
print(real_part) # Output: 3

imaginary_part = int(n.imag)
print(imaginary_part) # Output: 5

m = 3 + 5j

real_part = float(m.real)
print(real_part) # Output: 3.0

imaginary_part = float(m.imag)
print(imaginary_part) # Output: 5.0
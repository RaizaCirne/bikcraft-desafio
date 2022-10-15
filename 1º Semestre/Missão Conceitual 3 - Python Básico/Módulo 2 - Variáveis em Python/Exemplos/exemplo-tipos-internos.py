print(type(1_000_000))  # Tipo int
print(type(2+3+1))      # Tipo int
print(type(2+3+1.0))    # Tipo float

# Se a base for float, o resultado também será

print(2**3)            # 8
print(type(2**3))      # Tipo int
print(type(2.0**3))    # Tipo float

w = 2+5j
print(type(w))         # Tipo complex

a = 2 < 3
print(type(a))          # Tipo bool

print(not(2 < 3))       # Operador not
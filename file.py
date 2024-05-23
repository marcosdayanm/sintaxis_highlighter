# <regresa ek mayor de a o b
import random


def mayor(a, b):
  if a > b:
    return a - b
  else:
    return b - a

# ¿Par o non?
for i in range(10):
  if i % 2 == 0:
    print("Par: " + str(i))
  else:
    print("Impar: " + str(i))

# ¿Es un entero?
try:
  x = int("123")
except ValueError:
  print("Valor no es un entero")

# Es un volado
while random.randint(0, 1) == 0:
  print("Random")

# Ésta es una clase
class MiClase:
  def __init__(self, valor):
    self.valor = valor

def metodo_clase(self):
  return self.valor

obj = MiClase("Hola")
print(obj.metodo())
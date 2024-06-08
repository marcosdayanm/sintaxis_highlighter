# Pide al usuario un número
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Muestra la tabla de multiplicar del número del 1 al 10
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

# Pide al usuario la cantidad de números
cantidad = int(input("¿Cuántos números quieres promediar? "))

# Lista para almacenar los números
numeros = []

# Obtiene los números del usuario
for i in range(cantidad):
    numero = float(input(f"Introduce el número {i + 1}: "))
    numeros.append(numero)

# Calcula la media aritmética
media = sum(numeros) / len(numeros)

# Muestra el resultado
print("La media aritmética es", media)

def convertir_a_celsius(temperatura, unidad_origen):
    if unidad_origen == 'F':
        return (temperatura - 32) * 5/9
    elif unidad_origen == 'K':
        return temperatura - 273.15
    else:
        return temperatura

def convertir_a_fahrenheit(temperatura, unidad_origen):
    if unidad_origen == 'C':
        return (temperatura * 9/5) + 32
    elif unidad_origen == 'K':
        return (temperatura - 273.15) * 9/5 + 32
    else:
        return temperatura

def convertir_a_kelvin(temperatura, unidad_origen):
    if unidad_origen == 'C':
        return temperatura + 273.15
    elif unidad_origen == 'F':
        return (temperatura - 32) * 5/9 + 273.15
    else:
        return temperatura

def main():
    print("Conversor de temperatura")
    temperatura = float(input("Introduce la temperatura: "))
    unidad_origen = input("Introduce la unidad de origen (C, F, K): ").upper()

    if unidad_origen not in ['C', 'F', 'K']:
        print("Unidad no reconocida.")
        return

    print("1. Convertir a Celsius")
    print("2. Convertir a Fahrenheit")
    print("3. Convertir a Kelvin")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        print(f"Resultado: {convertir_a_celsius(temperatura, unidad_origen):.2f} C")
    elif opcion == '2':
        print(f"Resultado: {convertir_a_fahrenheit(temperatura, unidad_origen):.2f} F")
    elif opcion == '3':
        print(f"Resultado: {convertir_a_kelvin(temperatura, unidad_origen):.2f} K")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

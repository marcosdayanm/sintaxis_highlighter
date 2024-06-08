def agregar_contacto(contactos, nombre, telefono):
    contactos[nombre] = telefono

def eliminar_contacto(contactos, nombre):
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado.")
    else:
        print("El contacto no existe.")

def buscar_contacto(contactos, nombre):
    if nombre in contactos:
        print(f"El número de {nombre} es {contactos[nombre]}")
    else:
        print("Contacto no encontrado.")

def mostrar_contactos(contactos):
    for nombre, telefono in contactos.items():
        print(f"{nombre}: {telefono}")

def main():
    contactos = {}

    while True:
        print("\n1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            agregar_contacto(contactos, nombre, telefono)
        elif opcion == '2':
            nombre = input("Nombre del contacto a eliminar: ")
            eliminar_contacto(contactos, nombre)
        elif opcion == '3':
            nombre = input("Nombre del contacto a buscar: ")
            buscar_contacto(contactos, nombre)
        elif opcion == '4':
            mostrar_contactos(contactos)
        elif opcion == '5':
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()

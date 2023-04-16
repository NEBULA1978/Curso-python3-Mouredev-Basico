# Asignar un valor a la variable antes de utilizarla
language = "Python"
number = "32543"

# Menú principal
while True:
    print("Menú principal:")
    print("1. Mostrar el valor de 'language'")
    print("2. Mostrar el valor de 'number'")
    print("3. Convertir 'language' a mayúsculas")
    print("4. Cambiar el valor de 'number'")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    # Estructura case para manejar las diferentes opciones del menú
    if opcion == "1":
        print(f"El valor de 'language' es {language}")
    elif opcion == "2":
        print(f"El valor de 'number' es {number}")
    elif opcion == "3":
        language = input("Introduzca el valor de 'language': ")
        print(f"El valor de 'language' en mayúsculas es {language.upper()}")
    elif opcion == "4":
        number = int(input("Introduzca el valor de 'number': "))
        print(f"El valor de 'number' ha sido cambiado a {number}")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor seleccione una opción válida.")

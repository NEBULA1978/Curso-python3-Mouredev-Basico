while True:
    print("¿Qué resultado quieres obtener?")
    print("1. Resultado de la condición del primer if")
    print("2. Resultado de la condición del segundo if")
    print("3. Resultado de la condición con if, elif y else")
    print("4. Resultado de la condición con inspección de valor")
    print("5. Salir del programa")

    opcion = input("Ingresa el número de la opción que deseas: ")

    if opcion == "1":
        my_condition = False
        if my_condition:
            print("Se ejecuta la condición del if")
        else:
            print("No se ejecuta la condición del if")
    elif opcion == "2":
        my_condition = 5 * 5
        if my_condition == 10:
            print("Se ejecuta la condición del segundo if")
        else:
            print("No se ejecuta la condición del segundo if")
    elif opcion == "3":
        my_condition = int(input("Ingresa un número: "))
        if my_condition > 10 and my_condition < 20:
            print("Es mayor que 10 y menor que 20")
        elif my_condition == 25:
            print("Es igual a 25")
        else:
            print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")
    elif opcion == "4":
        my_string = input("Ingresa una cadena de texto: ")
        if not my_string:
            print("La cadena de texto es vacía")
        else:
            print("La cadena de texto no es vacía")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Ingresa un número del 1 al 5.")

while True:
    print("¿Qué resultado quieres obtener?")
    print("1. Resultado de la condición del primer if")
    print("2. Resultado de la condición del segundo if")
    print("3. Resultado de la condición con if, elif y else")
    print("4. Resultado de la condición con inspección de valor")
    print("5. Salir del programa")

    opcion = input("Ingresa el número de la opción que deseas: ")

    if opcion == "1":
        my_condition = input("Ingresa un valor para my_condition: ")
        if my_condition:
            print("Se ejecuta la condición del if")
        else:
            print("No se ejecuta la condición del if")
    elif opcion == "2":
        my_condition = input("Ingresa un valor para my_condition: ")
        if my_condition == "10":
            print("Se ejecuta la condición del segundo if")
        else:
            print("No se ejecuta la condición del segundo if")
    elif opcion == "3":
        my_condition = int(input("Ingresa un número para my_condition: "))
        if my_condition > 10 and my_condition < 20:
            print("Es mayor que 10 y menor que 20")
        elif my_condition == 25:
            print("Es igual a 25")
        else:
            print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")
    elif opcion == "4":
        my_string = input("Ingresa una cadena de texto para my_condition: ")
        if not my_string:
            print("La cadena de texto es vacía")
        else:
            print("La cadena de texto no es vacía")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Ingresa un número del 1 al 5.")

# En este código, después de que el usuario selecciona una opción, el programa solicita al usuario que ingrese un valor para my_condition utilizando la función input(). El valor ingresado por el usuario se almacena en la variable my_condition, que luego se utiliza en la evaluación de la condición correspondiente.

# En la opción 1, el programa evalúa si my_condition es verdadero o falso en un if . Si my_condition es verdadero, se muestra un mensaje que dice "Se ejecuta la condición del if". De lo contrario, se muestra un mensaje que dice "No se ejecuta la condición del if".

# En la opción 2, el programa evalúa si my_condition es igual a "10" en un if . Si my_condition es igual a "10", se muestra un mensaje que dice "Se ejecuta la condición del segundo if". De lo contrario, se muestra un mensaje que dice "No se ejecuta la condición del segundo if".

# En la opción 3, el programa le pide al usuario que ingrese un número utilizando la función int(input()) y luego evalúa my_condition en una serie de condiciones utilizando if , elif y else.

# En la opción 4, el programa le pide al usuario que ingrese una cadena de texto utilizando la función input() y luego evalúa si my_condition está

import random

# Define the dictionary
my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

# Get a random order for the keys and values
items = list(my_dict.items())
random.shuffle(items)

# Print the shuffled keys and ask the user to match the values
print("Bienvenido al juego de coincidencia de diccionario!")
print("Las claves y valores han sido mezclados. Adivina el valor correspondiente de cada clave.")

for key, value in items:
    shuffled_values = list(my_dict.values())
    random.shuffle(shuffled_values)
    options = shuffled_values[:4]  # Get four random values
    options.append(value)  # Add the correct value
    random.shuffle(options)  # Shuffle the options

    print(f"{key}: ")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    answer = input("Selecciona una opción (1-5): ")
    if options[int(answer)-1] == value:
        print("¡Correcto!")
    else:
        print(f"Incorrecto. El valor correcto era {value}")

print("Juego terminado.")

# Este programa es un juego de adivinanza que utiliza un diccionario de Python. El programa mezcla aleatoriamente las claves y valores del diccionario, y luego pide al usuario que adivine el valor correspondiente de cada clave.

# Primero, el programa crea un diccionario con varias claves y valores. Luego, el programa usa la función items() del diccionario para obtener una lista de tuplas de cada clave y valor en el diccionario. El programa mezcla aleatoriamente esta lista de tuplas utilizando la función shuffle() del módulo random.

# Luego, el programa entra en un bucle for que itera a través de cada tupla de clave-valor en la lista mezclada. En cada iteración del bucle, el programa crea una lista de valores mezclados aleatoriamente del diccionario y selecciona cuatro de ellos al azar. Luego, el programa agrega el valor correcto correspondiente a la clave actual a esta lista de valores y los mezcla nuevamente.

# El programa muestra al usuario la clave actual y los cinco valores mezclados (cuatro aleatorios y el valor correcto). Luego, el usuario selecciona una opción utilizando la entrada de teclado. Si el usuario selecciona la opción correcta, el programa imprime un mensaje de confirmación. Si el usuario selecciona una opción incorrecta, el programa imprime un mensaje de error y muestra el valor correcto.

# Después de que todas las claves hayan sido adivinadas, el programa imprime un mensaje de finalización del juego.

# En resumen, el programa es un juego de adivinanza que utiliza un diccionario de Python y mezcla aleatoriamente las claves y valores para aumentar la dificultad del juego.
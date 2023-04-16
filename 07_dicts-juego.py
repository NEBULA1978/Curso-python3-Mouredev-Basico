import random

# Define the dictionary
my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

# Get a random order for the keys
keys = list(my_dict.keys())
random.shuffle(keys)

# Print the shuffled keys and ask the user to match the values
print("Bienvenido al juego de coincidencia de diccionario!")
print("El orden de las claves ha sido mezclado. Adivina el valor correspondiente de cada clave.")

for key in keys:
    value = input(f"{key}: ")
    if str(my_dict[key]) == value:
        print("¡Correcto!")
    else:
        print(f"Incorrecto. El valor correcto era {my_dict[key]}")

print("Juego terminado.")

# Este programa es un juego de adivinanza que utiliza un diccionario de Python. El programa mezcla aleatoriamente las claves del diccionario y luego pide al usuario que adivine el valor correspondiente de cada clave.

# Primero, el programa crea un diccionario con varias claves y valores. Luego, el programa usa la función keys() del diccionario para obtener una lista de las claves en el diccionario. El programa mezcla aleatoriamente esta lista de claves utilizando la función shuffle() del módulo random.

# Luego, el programa entra en un bucle for que itera a través de cada clave mezclada aleatoriamente en la lista. En cada iteración del bucle, el programa muestra al usuario la clave actual y solicita que ingrese el valor correspondiente a esa clave utilizando la entrada de teclado.

# Si el valor ingresado por el usuario coincide con el valor almacenado en el diccionario para esa clave, el programa imprime un mensaje de confirmación. Si el valor ingresado por el usuario no coincide con el valor almacenado en el diccionario, el programa imprime un mensaje de error y muestra el valor correcto.

# Después de que todas las claves hayan sido adivinadas, el programa imprime un mensaje de finalización del juego.

# En resumen, el programa es un juego de adivinanza que utiliza un diccionario de Python y mezcla aleatoriamente las claves para aumentar la dificultad del juego. El programa solicita al usuario que ingrese los valores correspondientes a cada clave y proporciona comentarios sobre la precisión de las respuestas del usuario.
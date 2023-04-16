import random
import time

# Define the dictionary of ages
ages_dict = {
    "Pedro": 35,
    "Juan": 25,
    "Maria": 28,
    "Sofia": 30,
    "Carlos": 40
}

# Select a random age from the dictionary
name = random.choice(list(ages_dict.keys()))
age = ages_dict[name]

# Ask the user to guess the value until they get it right or until 5 seconds elapse
print(f"Adivina la edad de {name} (entre 25 y 40):")
start_time = time.time()
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time >= 5:
        print("Tiempo agotado.")
        break
    guess = input("Edad: ")
    if guess.strip() == "":
        continue
    try:
        guess_int = int(guess)
    except ValueError:
        print("Ingresa una edad válida.")
        continue
    if guess_int == age:
        print("¡Correcto!")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")
        
print("Juego terminado.")

# El programa es un juego de adivinanza basado en diccionarios de Python. Primero, el programa crea dos diccionarios de ejemplo y los imprime en pantalla. Luego, el programa muestra una serie de claves y valores aleatorios de uno de los diccionarios, y le pide al usuario que adivine el valor correspondiente a cada clave. Si el usuario adivina correctamente, el programa imprime un mensaje de confirmación y pasa a la siguiente clave. Si el usuario adivina incorrectamente, el programa imprime un mensaje de error y continúa con la siguiente clave. Después de que todas las claves hayan sido adivinadas, el programa imprime un mensaje de finalización del juego.

# Luego, el programa tiene una sección que pide al usuario que adivine la edad de una persona seleccionada aleatoriamente de un diccionario de edades. El programa muestra el nombre de la persona y le pide al usuario que adivine su edad. Si el usuario adivina correctamente, el programa imprime un mensaje de confirmación y finaliza el juego. Si el usuario no adivina correctamente después de 5 segundos, el programa imprime un mensaje de tiempo agotado y pregunta al usuario si desea volver a jugar. El juego continúa hasta que el usuario elija no volver a jugar.
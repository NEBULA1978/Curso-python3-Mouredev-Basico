import random

# Función para generar un número aleatorio
def generate_random_number():
    return random.randint(1, 100)

# Función para pedir al usuario que adivine el número
def ask_for_guess():
    return int(input("Ingresa un número entre 1 y 100: "))

# Función para verificar si el número es correcto
def check_guess(guess, secret_number):
    if guess == secret_number:
        print("¡Adivinaste el número! ¡Felicidades!")
        return True
    elif guess < secret_number:
        print("El número es mayor.")
        return False
    else:
        print("El número es menor.")
        return False

# Función para imprimir la tabla de multiplicar de un número
def print_multiplication_table(number):
    print(f"Tabla de multiplicar del {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Función principal que utiliza las funciones anteriores
def main():
    # Generamos un número aleatorio
    secret_number = generate_random_number()

    # Pedimos al usuario que adivine el número
    for i in range(5):
        guess = ask_for_guess()
        if check_guess(guess, secret_number):
            break
        elif i == 4:
            print(f"Lo siento, el número era {secret_number}. Has agotado tus intentos.")

    # Imprimimos la tabla de multiplicar del número
    print_multiplication_table(secret_number)

# Ejecutamos la función principal
main()

# En este ejemplo, hemos dividido el código en cuatro funciones más pequeñas:

#     generate_random_number(): esta función es la misma que antes, y se utiliza para generar un número aleatorio.

#     ask_for_guess(): esta función pide al usuario que ingrese un número entre 1 y 100, y lo retorna.

#     check_guess(guess, secret_number): esta función verifica si el número ingresado por el usuario (guess) es igual al número secreto generado por la función generate_random_number() (secret_number). Si son iguales, muestra un mensaje de felicitaciones y retorna True. Si el número ingresado es menor que el número secreto, muestra un mensaje indicando que el número es mayor y retorna False. Si el número ingresado es mayor que el número secreto, muestra un mensaje indicando que el número es menor y retorna False.

#     print_multiplication_table(number): esta función es la misma que antes, y se utiliza para imprimir la tabla de multiplicar del número pasado como argumento.

# Luego, en la función main(), utilizamos estas funciones para ejecutar el programa:

#     Generamos un número aleatorio utilizando la función generate_random_number().

#     Pedimos al usuario que adivine el número utilizando un bucle for que llama a las funciones ask_for_guess() y check_guess(). Si el usuario adivina el número, salimos del bucle utilizando la palabra clave break. Si el usuario agota sus 5 intentos, mostramos el número secreto utilizando la función print().

#     Imprimimos la tabla de multiplicar del número utilizando la función print_multiplication_table().
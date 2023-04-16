import random

# Generamos un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Jugador tiene 5 intentos para adivinar el número
intentos_restantes = 5

# Bucle while para los intentos
while intentos_restantes > 0:
    print(f"Tienes {intentos_restantes} intentos restantes.")
    # Pedimos al jugador que ingrese un número
    numero_usuario = int(input("Ingresa un número entre 1 y 100: "))
    if numero_usuario == numero_secreto:
        print("¡Adivinaste el número! ¡Felicidades!")
        break  # Salimos del bucle while
    elif numero_usuario < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    intentos_restantes -= 1
else:
    print(f"Lo siento, el número era {numero_secreto}. Has agotado tus intentos.")

print("¡Gracias por jugar!")

# Bucle for para imprimir la tabla de multiplicar del número secreto
print(f"Tabla de multiplicar del {numero_secreto}:")
for i in range(1, 11):
    print(f"{numero_secreto} x {i} = {numero_secreto * i}")

# En este juego, el programa genera un número aleatorio entre 1 y 100, y el jugador tiene 5 intentos para adivinarlo. El programa le irá indicando si el número ingresado es mayor o menor que el número secreto.

# Si el jugador adivina el número, el programa sale del bucle while y le muestra un mensaje de felicitaciones. Si el jugador agota sus 5 intentos, el programa sale del bucle while y le muestra el número secreto.

# Luego, el programa utiliza un bucle for para imprimir la tabla de multiplicar del número secreto. En este caso, el bucle for itera sobre los números del 1 al 10, y en cada iteración imprime el resultado de multiplicar el número secreto por el número actual del bucle.
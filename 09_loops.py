# While

my_condition = 0

while my_condition < 10:
    print(my_condition)  # Imprime 0, 2, 4, 6, 8
    my_condition += 2
else:
    print("Mi condición es mayor o igual que 10")  # Imprime "Mi condición es mayor o igual que 10"

print("La ejecución continúa")  # Imprime "La ejecución continúa"

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")  # Imprime "Se detiene la ejecución"
        break
    print(my_condition)  # Imprime 11, 12, 13, 14

print("La ejecución continúa")  # Imprime "La ejecución continúa"

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)  # Imprime los elementos de la lista: 35, 24, 62, 52, 30, 30, 17

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)  # Imprime los elementos de la tupla: 35, 1.77, "Brais", "Moure", "Brais"

my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)  # Imprime los elementos del conjunto: "Brais", "Moure", 35

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element)  # Imprime las claves del diccionario: "Nombre", "Apellido", "Edad", 1
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")  # No se ejecuta

print("La ejecución continúa")  # Imprime "La ejecución continúa"

for element in my_dict:
    print(element)  # Imprime las claves del diccionario: "Nombre", "Apellido", "Edad", 1
    if element == "Edad":
        continue
    print("Se ejecuta")  # Imprime "Se ejecuta" para todas las claves excepto "Edad"
else:
    print("El bluce for para diccionario ha finalizado")  # Imprime "El bluce for para diccionario ha finalizado"
    


# # Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=23822

# ### Loops ###

# # While

# my_condition = 0

# while my_condition < 10:
#     print(my_condition)
#     my_condition += 2
# else:  # Es opcional
#     print("Mi condición es mayor o igual que 10")

# print("La ejecución continúa")

# while my_condition < 20:
#     my_condition += 1
#     if my_condition == 15:
#         print("Se detiene la ejecución")
#         break
#     print(my_condition)

# print("La ejecución continúa")

# # For

# my_list = [35, 24, 62, 52, 30, 30, 17]

# for element in my_list:
#     print(element)

# my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

# for element in my_tuple:
#     print(element)

# my_set = {"Brais", "Moure", 35}

# for element in my_set:
#     print(element)

# my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

# for element in my_dict:
#     print(element)
#     if element == "Edad":
#         break
# else:
#     print("El bluce for para diccionario ha finalizado")

# print("La ejecución continúa")

# for element in my_dict:
#     print(element)
#     if element == "Edad":
#         continue
#     print("Se ejecuta")
# else:
#     print("El bluce for para diccionario ha finalizado")

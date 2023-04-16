# Definición

def my_function():
    print("Esto es una función")


my_function()  # Imprime "Esto es una función"
my_function()  # Imprime "Esto es una función"
my_function()  # Imprime "Esto es una función"

# Función con parámetros de entrada/argumentos

def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)  # Imprime 12
sum_two_values(54754, 71231)  # Imprime 125985
sum_two_values("5", "7")  # Genera un TypeError
sum_two_values(1.4, 5.2)  # Imprime 6.6

# Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)  # Imprime None

my_result = sum_two_values_with_return(10, 5)
print(my_result)  # Imprime 15

# Función con parámetros de entrada/argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure", name="Brais")  # Imprime "Brais Moure"

# Función con parámetros de entrada/argumentos por defecto

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")  # Imprime "Brais Moure Sin alias"
print_name_with_default("Brais", "Moure", "MoureDev")  # Imprime "Brais Moure MoureDev"

# Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "MoureDev")  # Imprime <class 'tuple'> y "HOLA", "PYTHON", "MOUREDEV"
print_upper_texts("Hola")  # Imprime <class 'tuple'> y "HOLA"
    


# # Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=26619

# ### Functions ###

# # Definición

# def my_function():
#     print("Esto es una función")


# my_function()
# my_function()
# my_function()

# # Función con parámetros de entrada/argumentos


# def sum_two_values(first_value: int, second_value):
#     print(first_value + second_value)


# sum_two_values(5, 7)
# sum_two_values(54754, 71231)
# sum_two_values("5", "7")
# sum_two_values(1.4, 5.2)

# # Función con parámetros de entrada/argumentos y retorno


# def sum_two_values_with_return(first_value, second_value):
#     my_sum = first_value + second_value
#     return my_sum


# my_result = sum_two_values(1.4, 5.2)
# print(my_result)

# my_result = sum_two_values_with_return(10, 5)
# print(my_result)

# # Función con parámetros de entrada/argumentos por clave


# def print_name(name, surname):
#     print(f"{name} {surname}")


# print_name(surname="Moure", name="Brais")

# # Función con parámetros de entrada/argumentos por defecto


# def print_name_with_default(name, surname, alias="Sin alias"):
#     print(f"{name} {surname} {alias}")


# print_name_with_default("Brais", "Moure")
# print_name_with_default("Brais", "Moure", "MoureDev")

# # Función con parámetros de entrada/argumentos arbitrarios


# def print_upper_texts(*texts):
#     print(type(texts))
#     for text in texts:
#         print(text.upper())


# print_upper_texts("Hola", "Python", "MoureDev")
# print_upper_texts("Hola")

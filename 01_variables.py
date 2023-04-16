# Creamos una variable de tipo string y la imprimimos
my_string_variable = "My String variable"
print(my_string_variable)  # Output: My String variable

# Creamos una variable de tipo int y la imprimimos
my_int_variable = 5
print(my_int_variable)  # Output: 5

# Convertimos la variable de tipo int a str y la imprimimos
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)  # Output: 5
print(type(my_int_to_str_variable))  # Output: <class 'str'>

# Creamos una variable de tipo bool y la imprimimos
my_bool_variable = False
print(my_bool_variable)  # Output: False

# Concatenamos varias variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)  # Output: My String variable 5 False
print("Este es el valor de:", my_bool_variable)  # Output: Este es el valor de: False

# Usamos la función len para obtener la longitud de la variable my_string_variable
print(len(my_string_variable))  # Output: 18

# Creamos varias variables en una sola línea y las imprimimos
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)  # Output: Me llamo: Brais Moure . Mi edad es: 35 . Y mi alias es: MoureDev

# Pedimos al usuario que introduzca su nombre y su edad
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)  # Output: El valor introducido por el usuario como nombre
print(age)  # Output: El valor introducido por el usuario como edad

# Asignamos un valor numérico a una variable que antes tenía un valor string
name = 35
age = "Brais"
print(name)  # Output: 35
print(age)  # Output: Brais

# Asignamos diferentes tipos de valor a una misma variable
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))  # Output: <class 'float'>

# Definición de tuplas
my_tuple = tuple()
my_other_tuple = ()
print(my_tuple)  # ()
print(type(my_tuple))  # <class 'tuple'>
print(my_other_tuple)  # ()
print(type(my_other_tuple))  # <class 'tuple'>

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)
print(my_tuple)  # (35, 1.77, 'Brais', 'Moure', 'Brais')
print(type(my_tuple))  # <class 'tuple'>
print(my_other_tuple)  # (35, 60, 30)
print(type(my_other_tuple))  # <class 'tuple'>

# Acceso a elementos y búsqueda
print(my_tuple[0])  # 35
print(my_tuple[-1])  # 'Brais'
# print(my_tuple[4]) IndexError: tuple index out of range
# print(my_tuple[-6]) IndexError: tuple index out of range

print(my_tuple.count("Brais"))  # 2
print(my_tuple.index("Moure"))  # 3
print(my_tuple.index("Brais"))  # 2

# Concatenación
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)  # (35, 1.77, 'Brais', 'Moure', 'Brais', 35, 60, 30)

# Subtuplas
print(my_sum_tuple[3:6])  # ('Moure', 'Brais', 35)

# Conversión a lista y modificación
my_tuple = list(my_tuple)
print(type(my_tuple))  # <class 'list'>

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)  # (35, 'Azul', 1.77, 'Brais', 'MoureDev')
print(type(my_tuple))  # <class 'tuple'>

# Eliminación
# del my_tuple[2] TypeError: 'tuple' object does not support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined


# # Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=14711

# ### Tuples ###

# # Definición

# my_tuple = tuple()
# my_other_tuple = ()

# my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
# my_other_tuple = (35, 60, 30)

# print(my_tuple)
# print(type(my_tuple))

# # Acceso a elementos y búsqueda

# print(my_tuple[0])
# print(my_tuple[-1])
# # print(my_tuple[4]) IndexError
# # print(my_tuple[-6]) IndexError

# print(my_tuple.count("Brais"))
# print(my_tuple.index("Moure"))
# print(my_tuple.index("Brais"))

# # my_tuple[1] = 1.80 'tuple' object does not support item assignment

# # Concatenación

# my_sum_tuple = my_tuple + my_other_tuple
# print(my_sum_tuple)

# # Subtuplas

# print(my_sum_tuple[3:6])

# # Tupla mutable con conversión a lista

# my_tuple = list(my_tuple)
# print(type(my_tuple))

# my_tuple[4] = "MoureDev"
# my_tuple.insert(1, "Azul")
# my_tuple = tuple(my_tuple)
# print(my_tuple)
# print(type(my_tuple))

# # Eliminación

# # del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

# del my_tuple
# # print(my_tuple) NameError: name 'my_tuple' is not defined

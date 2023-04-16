# Definición
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda
print(my_dict[1]) # 1.77
print(my_dict["Nombre"]) # Brais

print("Moure" in my_dict) # False
print("Apellido" in my_dict) # True

# Inserción
my_dict["Calle"] = "Calle MoureDev"
print(my_dict) # {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Kotlin', 'Swift', 'Python'}, 1: 1.77, 'Calle': 'Calle MoureDev'}

# Actualización
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"]) # Pedro

# Eliminación
del my_dict["Calle"]
print(my_dict) # {'Nombre': 'Pedro', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Kotlin', 'Swift', 'Python'}, 1: 1.77}

# Otras operaciones
print(my_dict.items()) # dict_items([('Nombre', 'Pedro'), ('Apellido', 'Moure'), ('Edad', 35), ('Lenguajes', {'Kotlin', 'Swift', 'Python'}), (1, 1.77)])
print(my_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1])
print(my_dict.values()) # dict_values(['Pedro', 'Moure', 35, {'Kotlin', 'Swift', 'Python'}, 1.77])

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict) # {'Nombre': None, 1: None, 'Piso': None}
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict) # {'Nombre': None, 1: None, 'Piso': None}
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict) # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print(my_new_dict) # {'Nombre': 'MoureDev', 'Apellido': 'MoureDev', 'Edad': 'MoureDev', 'Lenguajes': 'MoureDev', 1: 'MoureDev'}

my_values = my_new_dict.values()
print(type(my_values)) # <class 'dict_values'>

print(my_new_dict.values()) # dict_values(['MoureDev', 'MoureDev', 'MoureDev', 'MoureDev', 'MoureDev'])
print(list(dict.fromkeys(list(my_new_dict.values())).keys())) # ['MoureDev']
print(tuple(my_new_dict)) # ('Nombre', 'Apellido', 'Edad', '


# # Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

# ### Dictionaries ###

# # Definición

# my_dict = dict()
# my_other_dict = {}

# print(type(my_dict))
# print(type(my_other_dict))

# my_other_dict = {"Nombre": "Brais",
#                  "Apellido": "Moure", "Edad": 35, 1: "Python"}

# my_dict = {
#     "Nombre": "Brais",
#     "Apellido": "Moure",
#     "Edad": 35,
#     "Lenguajes": {"Python", "Swift", "Kotlin"},
#     1: 1.77
# }

# print(my_other_dict)
# print(my_dict)

# print(len(my_other_dict))
# print(len(my_dict))

# # Búsqueda

# print(my_dict[1])
# print(my_dict["Nombre"])

# print("Moure" in my_dict)
# print("Apellido" in my_dict)

# # Inserción

# my_dict["Calle"] = "Calle MoureDev"
# print(my_dict)

# # Actualización

# my_dict["Nombre"] = "Pedro"
# print(my_dict["Nombre"])

# # Eliminación

# del my_dict["Calle"]
# print(my_dict)

# # Otras operaciones

# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())

# my_list = ["Nombre", 1, "Piso"]

# my_new_dict = dict.fromkeys((my_list))
# print(my_new_dict)
# my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
# print((my_new_dict))
# my_new_dict = dict.fromkeys(my_dict)
# print((my_new_dict))
# my_new_dict = dict.fromkeys(my_dict, "MoureDev")
# print((my_new_dict))

# my_values = my_new_dict.values()
# print(type(my_values))

# print(my_new_dict.values())
# print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
# print(tuple(my_new_dict))
# print(set(my_new_dict))

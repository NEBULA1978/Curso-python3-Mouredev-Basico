# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)  # Imprime <class '__main__.MyEmptyPerson'>
print(MyEmptyPerson())  # Imprime <__main__.MyEmptyPerson object at 0x7f68be993850>

# Clase con constructor, funciones y propiedades privadas y públicas

class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)  # Imprime "Brais Moure (Sin alias)"
print(my_person.get_name())  # Imprime "Brais"
my_person.walk()  # Imprime "Brais Moure (Sin alias) está caminando"

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)  # Imprime "Brais Moure (MoureDev)"
my_other_person.walk()  # Imprime "Brais Moure (MoureDev) está caminando"
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)  # Imprime "Héctor de León (El loco de los perros)"

my_other_person.full_name = 666
print(my_other_person.full_name)  # Imprime 666
    


# # Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

# ### Classes ###

# # Definición

# class MyEmptyPerson:
#     pass  # Para poder dejar la clase vacía


# print(MyEmptyPerson)
# print(MyEmptyPerson())

# # Clase con constructor, funciones y popiedades privadas y públicas


# class Person:
#     def __init__(self, name, surname, alias="Sin alias"):
#         self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
#         self.__name = name  # Propiedad privada

#     def get_name(self):
#         return self.__name

#     def walk(self):
#         print(f"{self.full_name} está caminando")


# my_person = Person("Brais", "Moure")
# print(my_person.full_name)
# print(my_person.get_name())
# my_person.walk()

# my_other_person = Person("Brais", "Moure", "MoureDev")
# print(my_other_person.full_name)
# my_other_person.walk()
# my_other_person.full_name = "Héctor de León (El loco de los perros)"
# print(my_other_person.full_name)

# my_other_person.full_name = 666
# print(my_other_person.full_name)

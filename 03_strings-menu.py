"""
Módulo que implementa un menú para trabajar con dos cadenas de texto,
permitiendo al usuario ver sus longitudes y agregar palabras a ellas.
"""


class StringHandler:
    """
    Clase que maneja dos cadenas de texto y permite realizar operaciones
    básicas como obtener la longitud y agregar palabras.
    """

    def __init__(self):
        self.my_string = "Mi String"
        self.my_other_string = 'Mi otro String'

    def print_len_my_string(self):
        print("Longitud de my_string:", len(self.my_string))

    def print_len_my_other_string(self):
        print("Longitud de my_other_string:", len(self.my_other_string))

    def add_word_to_my_string(self):
        word = input("Ingrese la palabra que desea añadir a my_string: ")
        self.my_string += " " + word
        print("my_string actualizado:", self.my_string)

    def add_word_to_my_other_string(self):
        word = input("Ingrese la palabra que desea añadir a my_other_string: ")
        self.my_other_string += " " + word
        print("my_other_string actualizado:", self.my_other_string)


def main_menu(handler):
    print("Ingrese el número de la opción deseada:")
    options = [
        "Longitud de my_string",
        "Longitud de my_other_string",
        "Añadir palabra a my_string",
        "Añadir palabra a my_other_string",
        "Salir"
    ]

    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    try:
        choice = int(input())
    except ValueError:
        print("Opción inválida. Por favor, ingrese un número.")
        return

    if choice == 1:
        handler.print_len_my_string()
    elif choice == 2:
        handler.print_len_my_other_string()
    elif choice == 3:
        handler.add_word_to_my_string()
    elif choice == 4:
        handler.add_word_to_my_other_string()
    elif choice == 5:
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida. Por favor, ingrese un número dentro del rango de opciones.")


if __name__ == "__main__":
    string_handler = StringHandler()
    while True:
        main_menu(string_handler)
        input("Presione Enter para continuar...")


# EJEMPLO2

# class StringHandler:
#     def __init__(self):
#         self.my_string = "Mi String"
#         self.my_other_string = 'Mi otro String'

#     def print_len_my_string(self):
#         print("Longitud de my_string:", len(self.my_string))

#     def print_len_my_other_string(self):
#         print("Longitud de my_other_string:", len(self.my_other_string))

#     def add_word_to_my_string(self):
#         word = input("Ingrese la palabra que desea añadir a my_string: ")
#         self.my_string += " " + word
#         print("my_string actualizado:", self.my_string)

#     def add_word_to_my_other_string(self):
#         word = input("Ingrese la palabra que desea añadir a my_other_string: ")
#         self.my_other_string += " " + word
#         print("my_other_string actualizado:", self.my_other_string)


# def main_menu(handler):
#     print("Ingrese el número de la opción deseada:")
#     options = [
#         "Longitud de my_string",
#         "Longitud de my_other_string",
#         "Añadir palabra a my_string",
#         "Añadir palabra a my_other_string",
#         "Salir"
#     ]

#     for i, option in enumerate(options):
#         print(f"{i + 1}. {option}")

#     try:
#         choice = int(input())
#     except ValueError:
#         print("Opción inválida. Por favor, ingrese un número.")
#         return

#     if choice == 1:
#         handler.print_len_my_string()
#     elif choice == 2:
#         handler.print_len_my_other_string()
#     elif choice == 3:
#         handler.add_word_to_my_string()
#     elif choice == 4:
#         handler.add_word_to_my_other_string()
#     elif choice == 5:
#         print("Saliendo del programa...")
#         exit()
#     else:
#         print("Opción inválida. Por favor, ingrese un número dentro del rango de opciones.")


# if __name__ == "__main__":
#     string_handler = StringHandler()
#     while True:
#         main_menu(string_handler)
#         input("Presione Enter para continuar...")

# EJEMPLO2

# def print_len_my_string():
#     my_string = "Mi String"
#     print("Longitud de my_string:", len(my_string))


# def print_len_my_other_string():
#     my_other_string = 'Mi otro String'
#     print("Longitud de my_other_string:", len(my_other_string))


# def main_menu():
#     print("Ingrese el número de la opción deseada:")
#     options = [
#         "Longitud de my_string",
#         "Longitud de my_other_string",
#         "Salir"
#     ]

#     for i, option in enumerate(options):
#         print(f"{i + 1}. {option}")

#     try:
#         choice = int(input())
#     except ValueError:
#         print("Opción inválida. Por favor, ingrese un número.")
#         return

#     if choice == 1:
#         print_len_my_string()
#     elif choice == 2:
#         print_len_my_other_string()
#     elif choice == 3:
#         print("Saliendo del programa...")
#         exit()
#     else:
#         print("Opción inválida. Por favor, ingrese un número dentro del rango de opciones.")


# if __name__ == "__main__":
#     while True:
#         main_menu()
#         input("Presione Enter para continuar...")

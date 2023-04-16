class StringHandler:
    """
    Clase que maneja una cadena de texto llamada language y permite realizar
    operaciones básicas como obtener la longitud, agregar palabras y realizar
    diversas operaciones de string.
    """

    def __init__(self):
        self.language = "python"

    def unpack_and_print_characters(self):
        a, b, c, d, e, f = self.language
        print(a)  # p
        print(e)  # o

    def slice_and_print_language(self):
        language_slice = self.language[1:3]
        print(language_slice)  # yt

        language_slice = self.language[1:]
        print(language_slice)  # ython

        language_slice = self.language[-2]
        print(language_slice)  # o

        language_slice = self.language[0:6:2]
        print(language_slice)  # pto

    def reverse_and_print_language(self):
        reversed_language = self.language[::-1]
        print(reversed_language)  # nohtyp

    def perform_language_operations(self):
        print(self.language.capitalize())  # Python
        print(self.language.upper())  # PYTHON
        print(self.language.count("t"))  # 1
        print(self.language.isnumeric())  # False
        print("1".isnumeric())  # True
        print(self.language.lower())  # python
        print(self.language.lower().isupper())  # False
        print(self.language.startswith("Py"))  # False
        print("Py" == "py")  # False


def main_menu(handler):
    print("Ingrese el número de la opción deseada:")
    options = [
        "Desempacar e imprimir caracteres",
        "Dividir e imprimir language",
        "Invertir e imprimir language",
        "Realizar operaciones en language",
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
        handler.unpack_and_print_characters()
    elif choice == 2:
        handler.slice_and_print_language()
    elif choice == 3:
        handler.reverse_and_print_language()
    elif choice == 4:
        handler.perform_language_operations()
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

def mostrar_diccionario(diccionario):
    for key, value in diccionario.items():
        print(f"{key}: {value}")

def agregar_elemento(diccionario):
    clave = input("Ingresa la clave del nuevo elemento: ")
    valor = input("Ingresa el valor del nuevo elemento: ")
    diccionario[clave] = valor
    print("Elemento agregado correctamente.")

def actualizar_elemento(diccionario):
    clave = input("Ingresa la clave del elemento a actualizar: ")
    if clave in diccionario:
        valor = input(f"Ingresa el nuevo valor para la clave '{clave}': ")
        diccionario[clave] = valor
        print(f"El elemento '{clave}' ha sido actualizado correctamente.")
    else:
        print(f"La clave '{clave}' no existe en el diccionario.")
def eliminar_elemento(diccionario):
    clave = input("Ingresa la clave del elemento a eliminar: ")
    if clave in diccionario:
        del diccionario[clave]
        print("Elemento eliminado correctamente.")
    else:
        print("La clave seleccionada no existe en el diccionario.")

def menu(diccionario):
    while True:
        print("¿Qué acción deseas realizar?")
        print("1. Mostrar diccionario")
        print("2. Agregar elemento")
        print("3. Actualizar elemento")
        print("4. Eliminar elemento")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_diccionario(diccionario)
        elif opcion == "2":
            agregar_elemento(diccionario)
        elif opcion == "3":
            actualizar_elemento(diccionario)
        elif opcion == "4":
            eliminar_elemento(diccionario)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

mi_diccionario = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35}

menu(mi_diccionario)

# Este es un código que define un menú de opciones para interactuar con un diccionario en Python. Las opciones disponibles son las siguientes:

#     Mostrar diccionario: muestra todas las claves y valores del diccionario.
#     Agregar elemento: permite agregar un nuevo elemento al diccionario, solicitando la clave y el valor al usuario.
#     Actualizar elemento: permite actualizar el valor de una clave existente en el diccionario, solicitando la clave y el nuevo valor al usuario.
#     Eliminar elemento: permite eliminar un elemento del diccionario, solicitando la clave al usuario.
#     Salir: termina la ejecución del programa.

# El diccionario inicial se define en la variable mi_diccionario, y se pasa como argumento a la función menu() para que el usuario pueda interactuar con él.

# Cada función del menú utiliza métodos específicos de los diccionarios de Python para realizar las operaciones correspondientes (mostrar, agregar, actualizar y eliminar elementos). El bucle while en la función menu() se ejecuta hasta que el usuario selecciona la opción "Salir" (opción 5).

# Ejemplo2
nombre_buscado = "Brais"
archivo = "/ruta/al/archivo.txt"

with open(archivo, "r") as f:
    lineas = f.readlines()

for linea in lineas:
    nombres = linea.split()
    if nombre_buscado in nombres:
        print(f"Se encontró el nombre '{nombre_buscado}' en la línea '{linea.strip()}'")

# En este ejemplo, primero definimos el nombre que queremos buscar (nombre_buscado) y la ruta al archivo que queremos leer (archivo). Luego, abrimos el archivo en modo lectura ("r") utilizando el comando open() y leemos todas las líneas del archivo utilizando el método readlines().

# Después, recorremos cada línea del archivo utilizando un bucle for. En cada iteración del bucle, dividimos la línea en una lista de palabras utilizando el método split(), y luego verificamos si el nombre buscado está presente en esa lista utilizando el operador in. Si se encuentra el nombre, imprimimos un mensaje indicando en qué línea se encontró el nombre.

# Ten en cuenta que este código supone que cada línea del archivo contiene varios nombres separados por espacios en blanco. Si el archivo contiene una estructura diferente, como por ejemplo un nombre por línea, entonces tendrás que ajustar el código en consecuencia.
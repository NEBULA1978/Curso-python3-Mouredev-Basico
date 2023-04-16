import os

while True:
    print("¿Qué resultado quieres obtener?")
    print("1. Listar archivos .py")
    print("2. Listar archivos .sh")
    print("3. Listar archivos .txt")
    print("4. Listar archivos .blend")
    print("5. Salir del programa")

    opcion = input("Ingresa el número de la opción que deseas: ")

    if opcion == "1":
        directorio = input("Ingresa la ruta del directorio a buscar: ")
        archivos = os.listdir(directorio)
        archivos_py = [archivo for archivo in archivos if archivo.endswith(".py")]
        print(f"Archivos .py en {directorio}:")
        for archivo in archivos_py:
            print(archivo)
    elif opcion == "2":
        directorio = input("Ingresa la ruta del directorio a buscar: ")
        archivos = os.listdir(directorio)
        archivos_sh = [archivo for archivo in archivos if archivo.endswith(".sh")]
        print(f"Archivos .sh en {directorio}:")
        for archivo in archivos_sh:
            print(archivo)
    elif opcion == "3":
        directorio = input("Ingresa la ruta del directorio a buscar: ")
        archivos = os.listdir(directorio)
        archivos_txt = [archivo for archivo in archivos if archivo.endswith(".txt")]
        print(f"Archivos .txt en {directorio}:")
        for archivo in archivos_txt:
            print(archivo)
    elif opcion == "4":
        directorio = input("Ingresa la ruta del directorio a buscar: ")
        archivos = os.listdir(directorio)
        archivos_blend = [archivo for archivo in archivos if archivo.endswith(".blend")]
        print(f"Archivos .blend en {directorio}:")
        for archivo in archivos_blend:
            print(archivo)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Ingresa un número del 1 al 5.")

# Para permitir al usuario buscar archivos con extensiones específicas(.py, .sh, .txt, .blend) en cada opción, puedes utilizar la biblioteca os de Python y su función listdir(). La función listdir() devuelve una lista de los archivos y directorios en el directorio especificado.

# Luego puedes usar la función endswith() de Python para verificar si la extensión del archivo coincide con una de las extensiones específicas(.py, .sh, .txt, .blend).

# En este código, el usuario ingresa la ruta del directorio que desea buscar en cada opción. Luego, la función listdir() se utiliza para obtener una lista de los archivos y directorios en el directorio especificado.

# Después, se utiliza la función endswith() para verificar si la extensión del archivo coincide con una de las extensiones específicas(.py, .sh, .txt, .blend). Los archivos que coinciden con la extensión se agregan a una lista de archivos específicos(.py, .sh, .txt, .blend).

# Finalmente, se muestra una lista de los archivos encontrados en el directorio especificado que coinciden con la extensión específica. Si no se encuentran archivos que coincidan con la extensión específica, se muestra un mensaje que dice que no se encontraron archivos con esa extensión en el directorio especificado.

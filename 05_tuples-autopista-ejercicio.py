# Definición de tarifas utilizando tuplas
tarifas = (("tipo1", 20), ("tipo2", 40), ("tipo3", 60))

# Inicializar variables
total_recaudado = 0
continuar = True

# Función para obtener tarifa por tipo de vehículo


def obtener_tarifa(tipo):
    for t in tarifas:
        if t[0] == tipo:
            return t[1]
    return None


# Menú de entrada y cálculo de recaudación
while continuar:
    print("Ingrese el tipo de vehículo:")
    print("1. Tipo 1")
    print("2. Tipo 2")
    print("3. Tipo 3")
    print("4. Salir")
    opcion = int(input())

    if opcion == 1:
        tarifa = obtener_tarifa("tipo1")
        total_recaudado += tarifa
        print(f"Vehículo de tipo 1 ha pagado {tarifa} unidades.")
    elif opcion == 2:
        tarifa = obtener_tarifa("tipo2")
        total_recaudado += tarifa
        print(f"Vehículo de tipo 2 ha pagado {tarifa} unidades.")
    elif opcion == 3:
        tarifa = obtener_tarifa("tipo3")
        total_recaudado += tarifa
        print(f"Vehículo de tipo 3 ha pagado {tarifa} unidades.")
    elif opcion == 4:
        continuar = False
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

print(f"Total recaudado: {total_recaudado} unidades.")

# Sí, en mi primera respuesta, el ejemplo utilizaba un diccionario para almacenar las tarifas de los tipos de vehículos. Los diccionarios son útiles cuando tienes pares clave-valor, como en este caso, donde cada tipo de vehículo tiene una tarifa asociada.

# En el primer ejemplo, el diccionario de tarifas se veía así:

# python

# tarifas = {"tipo1": 20, "tipo2": 40, "tipo3": 60}

# En la segunda respuesta, modifiqué el ejemplo para utilizar tuplas, como solicitaste. La estructura de datos con tuplas se ve así:

# python

# tarifas = (("tipo1", 20), ("tipo2", 40), ("tipo3", 60))

# Ambas estructuras de datos se pueden utilizar para almacenar y acceder a las tarifas asociadas con cada tipo de vehículo, aunque la forma de acceder a los valores difiere. Los diccionarios son más eficientes para buscar valores por clave, mientras que las tuplas son inmutables y tienen un menor costo de memoria.

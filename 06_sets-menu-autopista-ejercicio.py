# Definición de tarifas utilizando un diccionario
tarifas = {"tipo1": 20, "tipo2": 40, "tipo3": 60}

# Conjunto de tipos de vehículos únicos
tipos_vehiculos = set(tarifas.keys())

# Inicializar variables
total_recaudado = 0
continuar = True

# Diccionario para llevar registro del conteo de vehículos
conteo_vehiculos = {tipo: 0 for tipo in tipos_vehiculos}

# Menú de entrada y cálculo de recaudación
while continuar:
    print("Ingrese el tipo de vehículo:")
    for i, tipo in enumerate(tipos_vehiculos, start=1):
        print(f"{i}. {tipo}")
    print("4. Salir")

    opcion = int(input())

    if opcion in range(1, len(tipos_vehiculos) + 1):
        tipo_seleccionado = list(tipos_vehiculos)[opcion - 1]
        tarifa = tarifas[tipo_seleccionado]
        total_recaudado += tarifa
        conteo_vehiculos[tipo_seleccionado] += 1
        print(f"Vehículo de {tipo_seleccionado} ha pagado {tarifa} unidades.")
    elif opcion == len(tipos_vehiculos) + 1:
        continuar = False
    else:
        print(
            f"Opción no válida. Por favor, ingrese un número entre 1 y {len(tipos_vehiculos) + 1}.")

# Encontrar el tipo de vehículo con más y menos pasos
tipo_mas_pasos = max(conteo_vehiculos, key=conteo_vehiculos.get)
tipo_menos_pasos = min(conteo_vehiculos, key=conteo_vehiculos.get)

print(f"Total recaudado: {total_recaudado} unidades.")
print(
    f"El tipo de vehículo que ha pasado más veces es {tipo_mas_pasos} con {conteo_vehiculos[tipo_mas_pasos]} pasos.")
print(
    f"El tipo de vehículo que ha pasado menos veces es {tipo_menos_pasos} con {conteo_vehiculos[tipo_menos_pasos]} pasos.")


# EJEMPLO2

# Definición de tarifas utilizando un diccionario
# tarifas = {"tipo1": 20, "tipo2": 40, "tipo3": 60}

# # Conjunto de tipos de vehículos únicos
# tipos_vehiculos = set(tarifas.keys())

# # Inicializar variables
# total_recaudado = 0
# continuar = True

# # Menú de entrada y cálculo de recaudación
# while continuar:
#     print("Ingrese el tipo de vehículo:")
#     for i, tipo in enumerate(tipos_vehiculos, start=1):
#         print(f"{i}. {tipo}")
#     print("4. Salir")

#     opcion = int(input())

#     if opcion in range(1, len(tipos_vehiculos) + 1):
#         tipo_seleccionado = list(tipos_vehiculos)[opcion - 1]
#         tarifa = tarifas[tipo_seleccionado]
#         total_recaudado += tarifa
#         print(f"Vehículo de {tipo_seleccionado} ha pagado {tarifa} unidades.")
#     elif opcion == len(tipos_vehiculos) + 1:
#         continuar = False
#     else:
#         print(
#             f"Opción no válida. Por favor, ingrese un número entre 1 y {len(tipos_vehiculos) + 1}.")

# print(f"Total recaudado: {total_recaudado} unidades.")


# Un conjunto(set) no es la mejor estructura de datos para este caso, ya que los conjuntos no admiten elementos duplicados ni tienen un orden establecido. Sin embargo, podemos utilizar un conjunto para almacenar los tipos de vehículos únicos y un diccionario para almacenar las tarifas asociadas a cada tipo de vehículo. Aquí tienes un ejemplo modificado que utiliza un conjunto para los tipos de vehículos y un diccionario para las tarifas:

# En este ejemplo, el conjunto tipos_vehiculos se construye a partir de las claves del diccionario tarifas. El menú se genera dinámicamente utilizando un bucle for, que itera sobre los elementos del conjunto y muestra las opciones disponibles. La variable opcion se compara con el rango de opciones válidas, y se selecciona el tipo de vehículo y la tarifa correspondiente en función de la opción ingresada por el usuario.

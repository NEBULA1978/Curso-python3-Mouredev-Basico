# Definición de tarifas
tarifas = {"tipo1": 20, "tipo2": 40, "tipo3": 60}

# Inicializar variables
total_recaudado = 0
continuar = True

# Menú de entrada y cálculo de recaudación
while continuar:
    print("Ingrese el tipo de vehículo:")
    print("1. Tipo 1")
    print("2. Tipo 2")
    print("3. Tipo 3")
    print("4. Salir")
    opcion = int(input())

    if opcion == 1:
        total_recaudado += tarifas["tipo1"]
        print(f"Vehículo de tipo 1 ha pagado {tarifas['tipo1']} unidades.")
    elif opcion == 2:
        total_recaudado += tarifas["tipo2"]
        print(f"Vehículo de tipo 2 ha pagado {tarifas['tipo2']} unidades.")
    elif opcion == 3:
        total_recaudado += tarifas["tipo3"]
        print(f"Vehículo de tipo 3 ha pagado {tarifas['tipo3']} unidades.")
    elif opcion == 4:
        continuar = False
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

print(f"Total recaudado: {total_recaudado} unidades.")

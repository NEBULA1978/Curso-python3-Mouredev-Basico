#!/bin/bash

opciones=(
    "Mostrar directorio:|ls"
    "Mostrar calendario:|cal"
    "Mostrar fecha y hora:|date"
    "Ejecutar 00_helloworld.py:|python3 00_helloworld.py"
    "Ejecutar 01_variables.py:|python3 01_variables.py"
    "Ejecutar 02_operators.py:|python3 02_operators.py"
    "Ejecutar 03_strings.py:|python3 03_strings.py"
    "Ejecutar 04_lists.py:|python3 04_lists.py"
    "Ejecutar 05_tuples.py:|python3 05_tuples.py"
    "Ejecutar 06_sets.py:|python3 06_sets.py"
    "Ejecutar 07_dicts.py:|python3 07_dicts.py"
    "Ejecutar 07_dicts-juego.py:|python3 07_dicts-juego.py"
    "Ejecutar 07_dicts-juego-random.py:|python3 07_dicts-juego-random.py"
    "Ejecutar 07_dicts-juego-random-automatico.py:|python3 07_dicts-juego-random-automatico.py"
    "Ejecutar 07_dicts-menu.py:|python3 07_dicts-menu.py"
    "Ejecutar 08_conditionals.py:|python3 08_conditionals.py"
    "Ejecutar 08_conditionals-menu.py:|python3 08_conditionals-menu.py"
    "Ejecutar 09_loops.py:|python3 09_loops.py"
    "Ejecutar 09_loops-juego.py:|python3 09_loops-juego.py"
    "Ejecutar 10_functions.py:|python3 10_functions.py"
    "Ejecutar 10_functions-juego.py:|python3 10_functions-juego.py"
    "Ejecutar 11_classes.py:|python3 11_classes.py"
    "Ejecutar 11_classes-circulo.py:|python3 11_classes-circulo.py"
    "Ejecutar 12_exceptions.py:|python3 12_exceptions.py"
    "Ejecutar 13_modules.py:|python3 13_modules.py"
    "Ejecutar codigo.py:|python3 codigo.py"
    "Ejecutar my_module.py:|python3 my_module.py"
    "Ejecutar tabla multiplicar.py:|python3 tabla_multiplicar.py"
    "Salir:|exit 0"
)

# Recorrer la lista y reemplazar "|" por ";"
for i in "${!opciones[@]}"; do
    opciones[$i]="${opciones[$i]/\|/;}"
    if [[ "${opciones[$i]}" != *"exit"* ]]; then
        opciones[$i]="${opciones[$i]} ; echo \"Presiona Enter para continuar...\" ; read ; clear"
    fi
done

# Imprimir las opciones actualizadas
for opcion in "${opciones[@]}"; do
    echo "$opcion"
done

# RESULTADO CONSOLA:
# <◂> ./cabiarpipe-puntocoma-ultimo-solo-nomArchivo.sh
# Mostrar directorio:;ls ; echo "Presiona Enter para continuar..." ; read ; clear
# Mostrar calendario:;cal ; echo "Presiona Enter para continuar..." ; read ; clear
# Mostrar fecha y hora:;date ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 00_helloworld.py:;python3 00_helloworld.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 01_variables.py:;python3 01_variables.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 02_operators.py:;python3 02_operators.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 03_strings.py:;python3 03_strings.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 04_lists.py:;python3 04_lists.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 05_tuples.py:;python3 05_tuples.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 06_sets.py:;python3 06_sets.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 07_dicts.py:;python3 07_dicts.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 07_dicts-juego.py:;python3 07_dicts-juego.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 07_dicts-juego-random.py:;python3 07_dicts-juego-random.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 07_dicts-juego-random-automatico.py:;python3 07_dicts-juego-random-automatico.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 07_dicts-menu.py:;python3 07_dicts-menu.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 08_conditionals.py:;python3 08_conditionals.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 08_conditionals-menu.py:;python3 08_conditionals-menu.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 09_loops.py:;python3 09_loops.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 09_loops-juego.py:;python3 09_loops-juego.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 10_functions.py:;python3 10_functions.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 10_functions-juego.py:;python3 10_functions-juego.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 11_classes.py:;python3 11_classes.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 11_classes-circulo.py:;python3 11_classes-circulo.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 12_exceptions.py:;python3 12_exceptions.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar 13_modules.py:;python3 13_modules.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar codigo.py:;python3 codigo.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar my_module.py:;python3 my_module.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Ejecutar tabla multiplicar.py:;python3 tabla_multiplicar.py ; echo "Presiona Enter para continuar..." ; read ; clear
# Salir:;e
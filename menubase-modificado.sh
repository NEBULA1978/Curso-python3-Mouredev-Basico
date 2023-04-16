#!/bin/bash

opciones=(
"Mostrar directorio:;ls ; cat"
"Mostrar calendario:;cal ; cat"
"Mostrar fecha y hora:;date ; cat"
"Ejecutar 00_helloworld.py:;python3 00_helloworld.py ; cat"
"Ejecutar 01_variables.py:;python3 01_variables.py ; cat"
"Ejecutar 02_operators.py:;python3 02_operators.py ; cat"
"Ejecutar 03_strings.py:;python3 03_strings.py ; cat"
"Ejecutar 04_lists.py:;python3 04_lists.py ; cat"
"Ejecutar 05_tuples.py:;python3 05_tuples.py ; cat"
"Ejecutar 06_sets.py:;python3 06_sets.py ; cat"
"Ejecutar 07_dicts.py:;python3 07_dicts.py ; cat"
"Ejecutar 07_dicts-juego.py:;python3 07_dicts-juego.py ; cat"
"Ejecutar 07_dicts-juego-random.py:;python3 07_dicts-juego-random.py ; cat"
"Ejecutar 07_dicts-juego-random-automatico.py:;python3 07_dicts-juego-random-automatico.py ; cat"
"Ejecutar 07_dicts-menu.py:;python3 07_dicts-menu.py ; cat"
"Ejecutar 08_conditionals.py:;python3 08_conditionals.py ; cat"
"Ejecutar 08_conditionals-menu.py:;python3 08_conditionals-menu.py ; cat"
"Ejecutar 09_loops.py:;python3 09_loops.py ; cat"
"Ejecutar 09_loops-juego.py:;python3 09_loops-juego.py ; cat"
"Ejecutar 10_functions.py:;python3 10_functions.py ; cat"
"Ejecutar 10_functions-juego.py:;python3 10_functions-juego.py ; cat"
"Ejecutar 11_classes.py:;python3 11_classes.py ; cat"
"Ejecutar 11_classes-circulo.py:;python3 11_classes-circulo.py ; cat"
"Ejecutar 12_exceptions.py:;python3 12_exceptions.py ; cat"
"Ejecutar 13_modules.py:;python3 13_modules.py ; cat"
"Ejecutar codigo.py:;python3 codigo.py ; cat"
"Ejecutar my_module.py:;python3 my_module.py ; cat"
"Ejecutar tabla multiplicar.py:;python3 tabla_multiplicar.py ; cat"
"Salir:;exit 0"
)

while true; do
    clear
    echo "Ingrese el número de la opción deseada:"
    for i in "${!opciones[@]}"; do
        echo "$i. ${opciones[$i]%%|*}" # Imprimimos el índice de la opción y su nombre (sin el comando correspondiente).
    done
    read -r opcion

    # Validamos que la opción ingresada sea un número válido dentro del rango de opciones.
    if [[ "$opcion" =~ ^[0-9]+$ ]] && [ "$opcion" -ge 0 ] && [ "$opcion" -lt ${#opciones[@]} ]; then
        clear
        comando="${opciones[$opcion]#*|}" # Obtenemos el comando correspondiente a la opción seleccionada.
        eval "$comando"                   # Ejecutamos el comando.
        echo ""
        echo "Presione Enter para continuar..."
        read
    else
        echo "Opción inválida. Presione Enter para continuar..."
        read
    fi
done

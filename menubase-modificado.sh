#!/bin/bash

opciones=(
"Mostrar directorio:;ls"
"Mostrar calendario:;cal"
"Mostrar fecha y hora:;date"
"Ejecutar 00_helloworld.py:;python3 00_helloworld.py ; cat 00_helloworld.py"
"Ejecutar 01_variables.py:;python3 01_variables.py ; cat 01_variables.py"
"Ejecutar 02_operators.py:;python3 02_operators.py ; cat 02_operators.py"
"Ejecutar 03_strings.py:;python3 03_strings.py ; cat 03_strings.py"
"Ejecutar 04_lists.py:;python3 04_lists.py ; cat 04_lists.py"
"Ejecutar 05_tuples.py:;python3 05_tuples.py ; cat 05_tuples.py"
"Ejecutar 06_sets.py:;python3 06_sets.py ; cat 06_sets.py"
"Ejecutar 07_dicts.py:;python3 07_dicts.py ; cat 07_dicts.py"
"Ejecutar 07_dicts-juego.py:;python3 07_dicts-juego.py ; cat 07_dicts-juego.py"
"Ejecutar 07_dicts-juego-random.py:;python3 07_dicts-juego-random.py ; cat 07_dicts-juego-random.py"
"Ejecutar 07_dicts-juego-random-automatico.py:;python3 07_dicts-juego-random-automatico.py ; cat 07_dicts-juego-random-automatico.py"
"Ejecutar 07_dicts-menu.py:;python3 07_dicts-menu.py ; cat 07_dicts-menu.py"
"Ejecutar 08_conditionals.py:;python3 08_conditionals.py ; cat 08_conditionals.py"
"Ejecutar 08_conditionals-menu.py:;python3 08_conditionals-menu.py ; cat 08_conditionals-menu.py"
"Ejecutar 09_loops.py:;python3 09_loops.py ; cat 09_loops.py"
"Ejecutar 09_loops-juego.py:;python3 09_loops-juego.py ; cat 09_loops-juego.py"
"Ejecutar 10_functions.py:;python3 10_functions.py ; cat 10_functions.py"
"Ejecutar 10_functions-juego.py:;python3 10_functions-juego.py ; cat 10_functions-juego.py"
"Ejecutar 11_classes.py:;python3 11_classes.py ; cat 11_classes.py"
"Ejecutar 11_classes-circulo.py:;python3 11_classes-circulo.py ; cat 11_classes-circulo.py"
"Ejecutar 12_exceptions.py:;python3 12_exceptions.py ; cat 12_exceptions.py"
"Ejecutar 13_modules.py:;python3 13_modules.py ; cat 13_modules.py"
"Ejecutar codigo.py:;python3 codigo.py ; cat codigo.py"
"Ejecutar my_module.py:;python3 my_module.py ; cat my_module.py"
"Ejecutar tabla multiplicar.py:;python3 tabla_multiplicar.py ; cat tabla_multiplicar.py"
"Salir:;exit 0; cat"
)

while true; do
    for i in "${!opciones[@]}"; do
        printf "%d. %s\n" $((i+1)) "${opciones[$i]%%:*}"
    done

    echo "Introduce una opción:"
    read opcionSeleccionada

    case $opcionSeleccionada in
        [1-9]|[1-2][0-9]|3[0-9])
            comando=$(echo "${opciones[$opcionSeleccionada-1]}" | cut -d';' -f2-)
            echo "Ejecutando: $comando"
            $comando
            ;;
        $((${#opciones[@]})))
            echo "Saliendo del programa..."
            exit 0
            ;;
        *)
            echo "Opción inválida, vuelve a intentarlo."
            ;;
    esac

done

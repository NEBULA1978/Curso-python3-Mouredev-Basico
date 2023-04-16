#!/bin/bash

while true; do
    # Mostrar menú
    clear
    echo -e "\e[1;32mMENU SCRIPT V.1\e[0m"
    echo ""
    echo "1. Mostrar directorio"
    echo "2. Mostrar calendario"
    echo "3. Mostrar fecha y hora"
    echo "4. Ejecutar 00_helloworld.py"
    echo "5. Ejecutar 01_variables.py"
    echo "6. Ejecutar 02_operators.py"
    echo "7. Ejecutar 03_strings.py"
    echo "8. Ejecutar 04_lists.py"
    echo "9. Ejecutar 05_tuples.py"
    echo "10. Ejecutar 06_sets.py"
    echo "11. Ejecutar 07_dicts.py"
    echo "12. Ejecutar 07_dicts-juego.py"
    echo "13. Ejecutar 07_dicts-juego-random.py"
    echo "14. Ejecutar 07_dicts-juego-random-automatico.py"
    echo "15. Ejecutar 07_dicts-menu.py"
    echo "16. Ejecutar 08_conditionals.py"
    echo "17. Ejecutar 08_conditionals-menu.py"
    echo "18. Ejecutar 09_loops.py"
    echo "19. Ejecutar 09_loops-juego.py"
    echo "20. Ejecutar 10_functions.py"
    echo "21. Ejecutar 10_functions-juego.py"
    echo "22. Ejecutar 11_classes.py"
    echo "23. Ejecutar 11_classes-circulo.py"
    echo "24. Ejecutar 12_exceptions.py"
    echo "25. Ejecutar 13_modules.py"
    echo "26. Ejecutar codigo.py"
    echo "27. Ejecutar my_module.py"
    echo "28. Ejecutar tabla multiplicar.py"
    echo "29. Salir"
    echo ""

    # Leer la opción seleccionada
    read -r opcion

    # Selección de opción
    case $opcion in
    1)
        echo -e "\nMostrando directorio:"
        ls
        read -r -s -p "Presione Enter para continuar..."
        ;;
    2)
        echo -e "\nMostrando calendario:"
        cal
        read -r -s -p "Presione Enter para continuar..."
        ;;
    3)
        echo -e "\nMostrando fecha y hora:"
        date
        read -r -s -p "Presione Enter para continuar..."
        ;;
    4)
        echo -e "\nEjecutando 00_helloworld.py:"
        python3 00_helloworld.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    5)
        echo -e "\nEjecutando 01_variables.py:"
        python3 01_variables.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    6)
        echo -e "\nEjecutando 02_operators.py:"
        python3 02_operators.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    7)
        echo -e "\nEjecutando 03_strings.py:"
        python3 03_strings.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    8)
        echo -e "\nEjecutando 04_lists.py:"
        python3 04_lists.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    9)
        echo -e "\nEjecutando 05_tuples.py:"
        python3 05_tuples.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    10)
        echo -e "\nEjecutando 06_sets.py:"
        python3 06_sets.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    11)
        echo -e "\nEjecutando 07_dicts-juego.py:"
        python3 07_dicts-juego.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    12)
        echo -e "\nEjecutando 08_conditionals.py:"
        python3 08_conditionals.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    13)
        echo -e "\nEjecutando 09_loops-juego.py:"
        python3 09_loops-juego.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    14)
        echo -e "\nEjecutando 10_functions-juego.py:"
        python3 10_functions-juego.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    15)
        echo -e "\nEjecutando 11_classes-circulo.py:"
        python3 11_classes-circulo.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    16)
        echo -e "\nEjecutando 12_exceptions.py:"
        python3 12_exceptions.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    17)
        echo -e "\nEjecutando 13_modules.py:"
        python3 13_modules.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    18)
        echo -e "\nEjecutando tabla_multiplicar.py:"
        python3 "tabla_multiplicar.py"
        read -r -s -p "Presione Enter para continuar..."
        ;;
    19)
        echo -e "\nEjecutando 01_variables.py:"
        python3 01_variables.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    20)
        echo -e "\nEjecutando 02_operators.py:"
        python3 02_operators.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    21)
        echo -e "\nEjecutando 04_lists.py:"
        python3 04_lists.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    22)
        echo -e "\nEjecutando 05_tuples.py:"
        python3 05_tuples.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    23)
        echo -e "\nEjecutando 06_sets.py:"
        python3 06_sets.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    24)
        echo -e "\nEjecutando 11_classes.py:"
        python3 11_classes.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    25)
        echo -e "\nEjecutando 11_classes-circulo.py:"
        python3 11_classes-circulo.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    26)
        echo -e "\nEjecutando 12_exceptions.py:"
        python3 12_exceptions.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    27)
        echo -e "\nEjecutando 10_functions.py:"
        python3 10_functions.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    28)
        echo -e "\nEjecutando 10_functions-juego.py:"
        python3 10_functions-juego.py
        read -r -s -p "Presione Enter para continuar..."
        ;;
    29)
        echo "¡Hasta luego!"
        exit 0
        ;;

    *)
        echo -e "\nOpción inválida..."
        sleep 1
        ;;
    esac
done

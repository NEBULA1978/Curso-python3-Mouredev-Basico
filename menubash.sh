#!/bin/bash

python_files=(
    "00_helloworld.py"
    "01_variables.py"
    "02_operators.py"
    "03_strings.py"
    "04_lists.py"
    "05_tuples.py"
    "06_sets.py"
    "07_dicts-juego.py"
    "08_conditionals.py"
    "09_loops-juego.py"
    "10_functions-juego.py"
    "11_classes-circulo.py"
    "12_exceptions.py"
    "13_modules.py"
    "tabla_multiplicar.py"
    "11_classes.py"
    "10_functions.py"
)

for file in "${python_files[@]}"; do
    echo -e "\nEjecutando ${file}:"
    python3 "${file}"
    more cat "${file}"
    read -r -s -p "Presione Enter para continuar..."
done

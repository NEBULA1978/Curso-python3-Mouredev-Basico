#!/bin/bash

python_files=$(find . -maxdepth 1 -type f -name "*.py")

for file in $python_files; do
    if [ -e "${file}" ]; then
        echo -e "\nEjecutando ${file}:"
        python3 "${file}"
        more cat "${file}"
        read -r -s -p "Presione Enter para continuar..."
    else
        echo -e "\nArchivo ${file} no encontrado, saltando..."
    fi
done

# La línea python_files=$(find . -maxdepth 1 -type f -name "*.py") utiliza el comando find para buscar archivos con la extensión .py en el directorio actual y almacenarlos en la variable python_files. Veamos cada parte de este comando:

#     find .: El comando find busca archivos y directorios en el sistema de archivos. El punto . indica que la búsqueda debe comenzar desde el directorio actual.

#     -maxdepth 1: Esta opción limita la búsqueda a una profundidad máxima de 1. Esto significa que solo se buscarán archivos y directorios en el directorio actual, sin adentrarse en subdirectorios.

#     -type f: Esta opción limita la búsqueda a archivos regulares, excluyendo directorios, enlaces simbólicos y otros tipos de archivos especiales.

#     -name "*.py": Esta opción indica que solo se deben buscar archivos cuyos nombres coincidan con el patrón *.py. En otras palabras, solo se buscarán archivos con la extensión .py.

# Finalmente, python_files=$(...) asigna el resultado del comando find a la variable python_files.

# //////////////////////////
# //////////////////////////

# SIN COMPROBACION ERROR
# python_files=$(find . -maxdepth 1 -type f -name "*.py")

# for file in $python_files; do
#     echo -e "\nEjecutando ${file}:"
#     python3 "${file}"
#     cat "${file}"
#     read -r -s -p "Presione Enter para continuar..."
# done

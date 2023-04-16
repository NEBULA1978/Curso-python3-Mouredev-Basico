# Operadores Aritméticos

# Operaciones con enteros
print(3 + 4)  # suma: 7
print(3 - 4)  # resta: -1
print(3 * 4)  # multiplicación: 12
print(3 / 4)  # división: 0.75
print(10 % 3)  # módulo: 1
print(10 // 3)  # división entera: 3
print(2 ** 3)  # potencia: 8
print(2 ** 3 + 3 - 7 / 1 // 4)  # orden de operaciones: 9.0

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")  # concatenación: Hola Python ¿Qué tal?
print("Hola " + str(5))  # concatenación de texto con número convertido a texto: Hola 5

# Operaciones mixtas
print("Hola " * 5)  # repetición de cadena: Hola Hola Hola Hola Hola 
print("Hola " * (2 ** 3))  # repetición de cadena con potencia: Hola Hola Hola Hola Hola Hola Hola Hola 
my_float = 2.5 * 2
print("Hola " * int(my_float))  # repetición de cadena con número decimal convertido a entero: Hola Hola 

# Operadores Comparativos

# Operaciones con enteros
print(3 > 4)  # mayor que: False
print(3 < 4)  # menor que: True
print(3 >= 4)  # mayor o igual que: False
print(4 <= 4)  # menor o igual que: True
print(3 == 4)  # igual que: False
print(3 != 4)  # diferente que: True

# Operaciones con cadenas de texto
print("Hola" > "Python")  # comparación lexicográfica: False
print("Hola" < "Python")  # comparación lexicográfica: True
print("aaaa" >= "abaa")  # comparación lexicográfica: False (ordenación alfabética por ASCII)
print(len("aaaa") >= len("abaa"))  # comparación de longitud: False (cuenta caracteres)
print("Hola" <= "Python")  # comparación lexicográfica: True
print("Hola" == "Hola")  # comparación de igualdad: True
print("Hola" != "Python")  # comparación de diferencia: True

# Operadores Lógicos

# Basado en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")  # and: False
print(3 > 4 or "Hola" > "Python")  # or: True
print(3 < 4 and "Hola" < "Python")  # and: True
print(3 < 4 or "Hola" > "Python")  # or: True
print(3 < 4 or ("Hola" > "Python" and 4 == 4))  # and, or y paréntesis: True
print(not (3 > 4))  # negación: True

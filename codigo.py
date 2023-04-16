
#print("Hola\nmi nombre es Ramon")
#print("mi nombre es Ramon")

#numero =10
#numero =10.56#ejecuta el ultimo en pantalla
#print(Hola mundo)
#print(numero)#el valor de la variable
#print(type(numero))

#cadena = 'a'
#cadena = "Estoy'estudiando'"#salga en pantallacon comillas
#cadena = 'Estoy"estudiando"'

#print(cadena)
#print(type(cadena))

#valor = True
#valor = False#ejecuta en pantallala ultima
#print(valor)
#print(type(valor))

#num1 = 10
#num2 = 6.7
#suma = num1+num2 * 10 /6#variable suma le hemos almacenado otras dos variables
#primero multiplica num2 * 10 luego divide resultado num2*10 / 6 y luego suma num1
#suma = (num1+num2) * 10 /6#si queremos que primero ejecute la suma ponemos parentesis
#resultado = (num1+num2) * 10 /6#mostrar texto en pantalla asi

#print("El resultado es: ",resultado)#cuantomas prints de 1 igual mas salidas
#print(suma)
#print(type(suma))
#print(suma)
#print(suma)

#Python permite eltipado dinamico variable
#puede ser de entero a estream o cualquier tipo de dato
'''
#comentario multilinea
el tipado dinamico es que una variablepuede contener diferentes tipos de datos a lo largo del programa

'''

#valor = 10

#print(valor)

#valor = "Ramon"
#print(valor)

#operadores aritmeticos

#resultado = 10 +5

#print(resultado)

#num1 = 2
#num2 = 5

#operadores aritmeticos python
#prioridad
# 1ºParentesis  2ºexponenciacion  3º(multiplicacion , 4ºdivision y modulo%) y por ultimo  5 ºsuma resta

#resultado = num1 + num2
#resultado = num1 - num2
#resultado = num1 * num2
#resultado = num1 / num2
#resultado = num1 // num2#añado//para no tener restos de decimales 3.33333
#resultado = num1 % num2# modulo tanto por 100 meda el resto de 10/3 residuo1
#resultado = num1 ** num2# 2 elevado a 5igual a 32
#solo ejecuta el ultimo de los 5 operadores aritmeticos ahorala de abajo

#resultado = 3**3 * (13/5-(2*4))

#print(resultado)

#operadores relacionales:
#seutilizan para establecer una relacion entre2 valores.
#compara estos valores y da verdadero o falso
#tienen el mismo nivel de prioridad en su evaluacion.
#los operadores relacionales tinene menos prioridad que los  1º aritmeticos
#se ejecutan de izquierda a derecha
# mayor que ,menor que mayor o igual que , menor o igual que , diferente admiracion igual , == igual
#me devuelven verdadero y falso

#resultado = 10 > 20
#resultado = 10 != 20
#resultado = 10 <= 10# es menor o igual
#resultado = 10 >= 10


#si 10 es diferente de 20 true

#print(resultado)


#a = 10
#b = 20
#c = 30

##resultado = a+b == c

#print(resultado)


#operadores logicos
#permite construir expreisones logicas como resultados bolesanos

#and conjuncion

#Or disyuncion

#Negacion not

#AND operador solo true y true verdadero demas combinaciones falsas

#OR basta con que haya un solo veradero para verdadero solo false y false falso

#operador negacion si a un valor verdadero le ponemos not (True) hace falso Falso
#operador negacion si a un valor verdadero le ponemos not (False) hace falso true

# Prioridad de operadores1º NOT 2º AND 3º OR

#prioridadde operadores engeneral
#1º () 2º ** 3º *,/mod%,not 4º +,-,and 5º mayor,menor == adimarion= mayor = menor= or

#a = 10
#b = 15
#c = 20
#resultado = ((a>b)) and ((b<c))#uno falso falso
#resultado = ((a>b)) or ((b<c))#uno verdadero verdadero
#resultado = not((a>b)) or ((b<c))
#print(resultado)

#operadores de asignacion

#a = 0 si no declaro la variable python no sabe a que aumentar restar *,etc
#a = 0


#a = a + 5 lo mismo que abajo
#a += 5# suma en asignacion
#a -= 2# resta en asignacion
#a *= 3# multiplicacion en asignacion
#a /= 3# division en asignacion
#a **=2# potencia  en asignacion
#a %=2# modulo  en asignacion 9/2residuo1

#print(a)


#Salidas de datos


#nombre ="Ramon"
#edad = 22

#print("Hola",nombre,"tienes",edad,"años")
#print("Hola {} tienes {} años".fonrmat(nombre,edad))#lo mismo que anterior pero mas comodo
#print(f"Hola {nombre} tienes {edad} años")#otra forma ultima mas moderna


#Entradade datos

#nombre = input("Digite su nombre: ")

#print(f"Hola {nombre}")#guardar datos de tipo cadena

#numero= float(input("Digite su numero: "))
#numero= int(input("Digite su numero: "))# guardar valor entero en nuestra variable numero
#se guarda en valor cadena pero lo vas a transformar a entero con int y()
#print(f"El numero es {numero+1}")#guardar datos de tipo cadena suma uno al valor que añadamos

#Funciones integradas

#n = int("10")
#n = float("10.8")

#n = str(10.98)# devuelve valor cadena

#valor entero a binario
#n = bin(10)
#valor hexadecimal
#n = hex(10)
#valor binario a entero
#n = int("0b1010",2)en base 2
#valor hexadecimal a entero
#n = int("0xa",16)#en base 16
#sacar valor absoluto de un numero ,es la distancia de un numero hacia 0 siempre en positivo
#n = abs(-8)
# round redondea un munero
#n = round(5.4)#seredodeasiemp`rehacialo que tenga mas cerca
# funcion len se le tiene que pasar como argumento unacadena
#n = len("Ramon")
#print(n)

#ejerc 3 intercambiar el valor de 2variables

a = input("a -> ")
b = input("b -> ")

a ,  b = b , a#dentrode a se tienen almacenar el valor de b y en b almacenar el valor de a

print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de a es: {b}")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Creamos un círculo con radio 5
my_circle = Circle(5)

# Imprimimos el área y la circunferencia del círculo
print(f"El área del círculo es: {my_circle.area()}")
print(f"La circunferencia del círculo es: {my_circle.circumference()}")

# Creamos otro círculo con radio 10
my_other_circle = Circle(10)

# Imprimimos el área y la circunferencia del otro círculo
print(f"El área del otro círculo es: {my_other_circle.area()}")
print(f"La circunferencia del otro círculo es: {my_other_circle.circumference()}")


# En este ejemplo, hemos creado una clase llamada Circle que representa un círculo. La clase tiene un constructor que recibe el radio del círculo y lo guarda en una propiedad radius. Además, la clase tiene dos métodos: area() y circumference(), que calculan el área y la circunferencia del círculo, respectivamente.

# Luego, en la función principal, hemos creado dos objetos de la clase Circle: uno con radio 5 (my_circle) y otro con radio 10 (my_other_circle). Hemos utilizado los métodos area() y circumference() de estos objetos para imprimir el área y la circunferencia de los círculos.

# La salida del programa sería algo como:

# El área del círculo es: 78.53981633974483
# La circunferencia del círculo es: 31.41592653589793
# El área del otro círculo es: 314.1592653589793
# La circunferencia del otro círculo es: 62.83185307179586

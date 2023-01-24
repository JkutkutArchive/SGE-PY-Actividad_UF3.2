# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    shapes.py                                            ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/01/24 12:59:25 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/01/24 13:43:03 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from math import sqrt

def ft_ask_int(question: str) -> int:
    while True:
        try:
            return int(input(question))
        except:
            print("El número no es válido.")

def ft_ask_natural_int(question: str) -> int:
    while True:
        r = ft_ask_int(question)
        if r > 0:
            return r
        print("El número tiene que ser natural mayor que 0.")

'''
Escribe una clase llamada Poligono() que genera objetos de polígono de 3 o
más lados.
Al crear un objeto, en el constructor __init__ ( ), se indica el número de
lados que va a tener y se crea una lista que va a tener ese número de elementos
cuyos valores iniciales serán 0.

La clase Poligono() tendrá un método llamado darlados( ) que le pedirá al
usuario que introduzca uno a uno los valores de todos los lados.

La clase Polígono() tendrá otro método llamado verlados( ) que mostrará uno a
uno los valores introducidos de todos los lados.

Se va a crear una clase llamada Triangulo() que hereda de la clase  Poligono().
Al crear un objeto triangulo, se invoca al constructor de la clase Poligono()
al que se indica el número de lados = 3.

La clase Triangulo() tendrá un método area( ) que calcule y muestre el área
del triángulo.
Puede ser cualquier tipo de triángulo. Puedes usar la fórmula de Herón.

La clase Triangulo() tendrá un método perimetro( ) que calcule y muestre
el perímetro del triángulo (suma de sus lados).

Crea dos objetos de la clase Triangulo() y muestra el resultado de ejecutar
todos los métodos tanto de la clase Polígono() como de la clase Triangulo().
'''
class Poligono:
    def __init__(self, n: int):
        self.lados = [0 for _ in range(n)]
        self.darLados() # No tienen sentido que un polígono no tenga 
        # los valores definidos

    def darLados(self) -> None:
        print(f"Introduce los lados del {self.__class__.__name__}:")
        for i in range(len(self.lados)):
            self.lados[i] = ft_ask_natural_int(f"- {i + 1:02}º lado: ")

    def verLados(self) -> None:
        print(f"Los lados del {self.__class__.__name__} son: ", end="")
        print(*self.lados, sep=", ")

    def area(self) -> int:
        raise Exception("Not implemented")

    def perimetro(self) -> int:
        return sum(self.lados)

class Triangulo(Poligono):
    def __init__(self):
        Poligono.__init__(self, 3)

    def area(self) -> int:
        s = self.perimetro()
        a, b, c = self.lados
        return sqrt(s * (s - a) * (s - b) * (s - c))

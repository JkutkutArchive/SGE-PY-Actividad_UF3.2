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
#    Updated: 2023/01/24 13:12:07 by Jkutkut            '-----------------'    #
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

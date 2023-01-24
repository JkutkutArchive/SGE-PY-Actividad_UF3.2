# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    main.py                                              ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/01/24 10:33:08 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/01/24 13:38:43 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from typing import Callable
from uf2_1 import *
from shapes import Triangulo, Poligono

def ft_print_title(n: int) -> None:
    print(f"\n\n          Ej{n:02}")

def ft_attempt(ft: Callable, args: tuple) -> None:
    try:
        ft(*args)
    except TypeError as e:
        # print(e)
        return
    raise Exception(f"{ft.__name__}({', '.join(args)}) didn't throw an exception")

if __name__ == "__main__":
    # Ej1
    ft_print_title(1)
    print(ft_generar_n_caracteres(42, 'h'))
    ft_attempt(ft_generar_n_caracteres, (-2, "s"))
    ft_attempt(ft_generar_n_caracteres, (5, "sadf"))
    ft_attempt(ft_generar_n_caracteres, (5, ""))

    # Ej2
    ft_print_title(2)
    print(ft_histograma([5, 3, 0, 1, 10, 42]))
    ft_attempt(ft_histograma, [['a', 0]])
    ft_attempt(ft_histograma, [[-2, 0]])
    ft_attempt(ft_histograma, [[3, 1, None]])

    # Ej3
    ft_print_title(3)
    cubo = lambda e: e ** 3
    print(ft_funcionLista(cubo, [3, 2, 1, 0]))

    # Ej4
    ft_print_title(4)
    print(ft_palabrasLongitud("hola caracola qué tal estás"))
    print(ft_palabrasLongitud("hhola hola hola hola hola ola ola qué tal estás"))
    ft_attempt(ft_palabrasLongitud, [None])
    ft_attempt(ft_palabrasLongitud, [0])
    ft_attempt(ft_palabrasLongitud, [[]])
    ft_attempt(ft_palabrasLongitud, [tuple()])

    # Ej5
    ft_print_title(5)
    print(ft_calificaPalabras(
        {'aa': 3.2, 'bb': 5, 'cc': 7.0, 'dd': 8, 'ee': 9.1, 'dd': 10}
    ))

    # Ej Poligono
    ft_print_title('Polígono')
    p3 = Triangulo()
    p3.verLados()
    print(f"Área: {p3.area()} u²")
    print(f"Perímetro: {p3.perimetro()} u")

    print("\n")
    p3_2 = Triangulo()
    p3_2.verLados()
    print(f"Área: {p3_2.area()} u²")
    print(f"Perímetro: {p3_2.perimetro()} u")

    print("\n")
    p8 = Poligono(8)
    p8.verLados()

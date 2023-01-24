# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    uf2.py                                               ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/01/24 10:25:59 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/01/24 11:29:09 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from typing import Callable

def ft_generar_n_caracteres(n: int, c: str) -> str:
    '''
    Escribe una función generar_n_caracteres(n, carácter) a la que se le pasa
    un número entero n y un carácter. Devolverá el carácter multiplicado por
    n.
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
    Tantas x como indique el número.
    '''
    if type(n) != int or n < 0:
        raise TypeError("n should be a positive number!")
    if type(c) != str or len(c) != 1:
        raise TypeError("c should be a character!")
    return "".join([c for _ in range(n)])

def ft_histograma(lst: list) -> str:
    '''
    Crea una función llamada histograma(lista_números) a la que se le pasa
    una lista de números enteros. Se mostrará un histograma cuyas columnas
    midan el valor de los números.
    '''
    try:
        return "\n".join([ft_generar_n_caracteres(e, '*') for e in lst])
    except TypeError as error:
        raise TypeError("The elements in the lists must be positive numbers!")

def ft_funcionLista(ft: Callable, lst: list) -> list:
    '''
    Escribe una función funcionLista(función, lista) que reciba otra función
    creada anteriormente y una lista, y devuelva otra lista con el resultado
    de aplicar la función dada a cada uno de los elementos de la lista.
    Por ejemplo, la función que se le pasa calcula el cubo de un número.
    La lista que se pasa es una lista de números enteros.
    A cada número de la lista se le aplica la función y se calculará el
    cubo de todos ellos, mostrándolos en otra lista nueva.
    Si la lista que se pasara fuera [1,2,3,4,5] la función
    devolvería [1,8,27,64,125]
    '''
    # return list(map(ft, lst))
    return [ft(e) for e in lst]

def ft_palabrasLongitud(txt: str) -> dict:
    '''
    Escribe una función palabrasLongitud(frase) que reciba una frase y devuelva
    un diccionario con las palabras que contiene y su longitud.
    Por ejemplo, la función recibe la frase ‘Hola y adiós’ y devuelve un
    diccionario de la forma {‘Hola’:4, ‘y’:1, ‘adiós’:5}
    '''
    if type(txt) != str:
        raise TypeError("The txt must be a string!")
    d = dict()
    for w in set(txt.split(" ")):
        d[w] = len(w)
    return d

def ft_calificaPalabras(input_dict: dict) -> dict:
    '''
    Escribe una función calificaPalabras(diccionario) que reciba un diccionario
    con las asignaturas y las notas numéricas de un alumno y devuelva otro
    diccionario con las asignaturas en mayúsculas y las calificaciones
    correspondientes a las notas con palabras.

    El criterio será el siguiente:  nota <5 → Suspenso;  
    5 <= nota < 7 → Aprobado; 7 <= nota < 9 → Notable;
    9 <= nota <=10 → Sobresaliente.
    La nota no puede sobrepasar 10.

    Por ejemplo, la función recibe el diccionario {'Android':8.2, 'Hilos':5,
    'Python':9.3, 'Interfaces':4.4}
    y devuelve el diccionario {'ANDROID’:’Notable’,  ‘HILOS’:’Aprobado’,
    ‘PYTHON’:’Sobresaliente’, ‘INTERFACES’:’Suspenso’ }
    '''
    d = dict()
    for k, v in input_dict.items():
        if v < 0 or v > 10:
            raise TypeError("All marks must be numbers in range [0, 10]!")
        nota = 'Suspenso'
        if 5 <= v < 7:
            nota = 'Aprobado'
        elif 7 <= v < 9:
            nota = 'Notable'
        else:
            nota = 'Sobresaliente'
        d[k.upper()] = nota
    return d

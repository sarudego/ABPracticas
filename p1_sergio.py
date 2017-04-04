#Python 2
"""
Problema del viajante de comercio.
Listado de ciudades con una distancia conocida entre si.
1. Implementar los esquemas algoritmos mediante:
    Fuerza Bruta
    Algoritmo voraz
    Programacion dinamica
    Ramificacion y poda
2. Calcular y comparar tiempos de ejecucion para distintas entradas
"""
"""import numpy as np"""
from itertools import permutations
import math
import operator
#Para ejemplo 
"""points  = [[0, 0], [1,5], [2,3], [20, 3],
     [5, 3], [0, 17], [9, 3], [10, 8],
     [6, 2], [13, 5], [0, 2], [12, 11],
     [8, 9], [8, 1], [9, 11], [0,19]
    ]
"""
points = [[0, 0], [1, 5], [5, 3], [8, 1]]
matriz = [[0, 10, 15],
          [5, 0, 9],
          [6, 13, 0]]


def getDistance(point1, point2):
    """
    distancia = raiz((x2-x1)^2 + (y2-y1)^2)
    """
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

""" 
comprueba la distancia entre dos puntos desde el punto inicial
pasando por sus vecinos hasta llegar al punto final
obteniendo la distancia minima para el camino
"""
# implementar
def checkPath(point1, point2):
    cost = []
    for i in points:
        dist = getDistance(i, i)
        # hacer if para comprobar distancia minima
        # cost.append = dist

# genera el diccionario de costes
def genCost(lst):
    permu = list(permutations(lst))
    cst,tup = [], []
    cstd = {}
    for i in lst:
        for j in lst:
            cst.append(getDistance(i, j))
            tup.append(tuple(i))
            tup.append(tuple(j))
            # print(tup)
            k = tuple(tup)
            cstd[k] = getDistance(i, j)
            tup = []
    cstdsort = sorted(cstd.items(), key=operator.itemgetter(0))
    for i in cstdsort:
        print(i)


""" codigo obtenido de http://edupython.blogspot.com.es/2016/06/combinaciones-permutaciones-y-otras.html"""
def inserta(x, lst, i):
    return lst[:i] + [x] + lst[i:]

""" codigo obtenido de http://edupython.blogspot.com.es/2016/06/combinaciones-permutaciones-y-otras.html"""
def inserta_multiple(x, lst):
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]

""" codigo obtenido de http://edupython.blogspot.com.es/2016/06/combinaciones-permutaciones-y-otras.html"""
def permuta(puntos):
    if len(puntos) == 0:
        return [[]]
    return sum([inserta_multiple(puntos[0], s)
                for s in permuta(puntos[1:])],
               [])

""" codigo obtenido de http://edupython.blogspot.com.es/2016/06/combinaciones-permutaciones-y-otras.html"""    
def imprime_ordenado(c):
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)


def fuerzaBruta(inicio, puntos):
    puntos = permuta(puntos)
    lst = []
    sol = []
    print puntos
    for i in puntos:
        if i[0] == inicio:
            lst.append(i)
            print lst
    """for i in lst:
        menor = 10000
        suma = 0
        for j in i:
            if j.next() != None:
                suma += sum(getDistance(j, j.next()))
            else:
                suma += sum(getDistance(j, inicio))
        if sum < menor:
            menor = suma
            sol = i
    print sol"""
            

def fuerzaMatriz(inicio, matriz):
    vertices = []
    lst = []
    num = 1
    for i in matriz:
        vertices.append(num)
        num += 1
    vertices = permuta(vertices)
    #print vertices
    for i in vertices:
        if i[0] == inicio:
            lst.append(i)
    print lst
    print "\n"
    for i in lst:
        suma = 0
        for j in range(len(i)):
            if j+1 < len(i):
                suma += matriz[i[j]-1][i[j+1]-1]
            else:
                suma += matriz[i[j]-1][inicio-1]
        print i
        print suma
        print "\n"
            
fuerzaMatriz(1, matriz)
#genCost(points)

#checkPath(points[0], points[1])
# print(getDistance(points[1], points[2]))




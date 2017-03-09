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
import numpy as np
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
points = [[0, 0], [1, 5], [5, 3]]


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
        dist = getDistance(points[i], points[i+1])
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



genCost(points)

# checkPath(points[0], points[1])
# print(getDistance(points[1], points[2]))




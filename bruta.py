"""
Problema del viajante de comercio implementado mediante fuerza bruta.
Indica cual es el camino mas corto y la secuencia de nodos que lo genera.
"""

import auxi
import itertools

def fuerzaMatriz(matriz):
    inicio = 1
    vertices = []
    lst = []
    num = 2

    for i in matriz:
        if num <= len(matriz):
            vertices.append(num)
            num += 1
    c = [float("inf"),vertices]
    for x in itertools.permutations(vertices):
        suma = matriz[inicio-1][x[0]-1]
        for j in range(len(x)):
            if j+1 < len(x):
                suma += matriz[x[j]-1][x[j+1]-1]
            else:
                suma += matriz[x[j]-1][inicio-1]
        if suma < c[0]:
            c[0] = suma
            c[1] = x
    camino = "1-"
    for i in c[1]:
        camino += str(i) + "-"
    camino += "1"
    print "El camino optimo es: " + str(camino)
    print "Con distancia " + repr(c[0])


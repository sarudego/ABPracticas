"""
Problema del viajante de comercio implementado mediante fuerza bruta.
Obtiene todos los caminos posibles e indica cual es el mas corto.
"""

import auxi

def fuerzaMatriz(matriz):
    inicio = 1
    vertices = []
    lst = []
    num = 1
    
    for i in matriz:
        vertices.append(num)
        num += 1
    vertices = auxi.permuta(vertices)
    
    for i in vertices:
        if i[0] == inicio:
            lst.append(i)
    caminos = []
    for i in lst:
        suma = 0
        for j in range(len(i)):
            if j+1 < len(i):
                suma += matriz[i[j]-1][i[j+1]-1]
            else:
                suma += matriz[i[j]-1][inicio-1]
        c = [suma, i]
        caminos.append(c)
    c = min(caminos)
    camino = ""
    for i in c[1]:
        camino += str(i) + "-"
    camino += "1"
    print "El camino optimo es: " + str(camino)
    print "Con distancia " + repr(c[0])



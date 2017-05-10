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
    print lst
    print "\n"
    caminos = []
    print "Los caminos posibles son: "
    for i in lst:
        suma = 0
        for j in range(len(i)):
            if j+1 < len(i):
                suma += matriz[i[j]-1][i[j+1]-1]
            else:
                suma += matriz[i[j]-1][inicio-1]
        print repr(i) + " con distancia " + repr(suma)
        c = [suma, i]
        caminos.append(c)
    c = min(caminos)
    print "\n"
    print "El camino optimo es: " + repr(c[1])
    print "Con distancia " + repr(c[0])


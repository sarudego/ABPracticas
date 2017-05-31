"""
Problema del viajante de comercio implementado mediante un algoritmo voraz.
Indica cual es el camino mas corto y la secuencia de nodos que lo genera.
"""

def voraz(matriz):
    inicio = 1
    nodos = len(matriz)
    solucion = []
    solucion.append(1)
    coste = 0
    s = []
    for i in range(nodos):
        s.append(i+1)
    s.remove(1)
    while (len(s) != 0):
        minimo = 9999;
        for i in s:
            if matriz[inicio-1][i-1] < minimo:
                minimo = matriz[inicio-1][i-1]
                sol = i;
        solucion.append(sol)
        coste += minimo
        inicio = sol
        s.remove(sol)
    coste += matriz[sol-1][0]
    camino = ""
    for i in solucion:
        camino += str(i) + "-"
    camino += "1"
    print "El camino mas corto Algoritmo Voraz es: " + str(camino)
    print "Con distancia " + str(coste)    
    

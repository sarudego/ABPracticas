def inicializarS(nodos, n):
    s = []
    for i in range(nodos):
        s.append(n)
    return s

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
    solucion.append(1)
    coste += matriz[sol-1][0]
    print "El camino mas corto en Algoritmos voraces es: " + str(solucion)
    print "Con distancia " + str(coste)
    
    

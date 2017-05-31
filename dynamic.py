"""
Problema del viajante de comercio implementado mediante programacion dinamica.
Indica cual es el camino mas corto y la secuencia de nodos que lo genera.
"""

"""
Funcion que inicia listas de una longitud dada y con un valor dado en todas 
sus posiciones
"""
def inicializarM(nodos, v):
    col = 2**(nodos)
    gtab = [v] * nodos
    for i in range (nodos):
        gtab[i] =  [v] * col
    return gtab        

"""
Funcion que convierte un conjunto de nodos en un numero para poder indexar
mediante conjuntos de nodos
"""
def toNumber(s):
    number = 0b0
    for i in s:
        x = 0b1 << i-1
        number = number | x
    return number
     

def dinamica(matriz):
    s = []
    i = 1
    nodos =  len(matriz)
    while (i < nodos):
        i += 1
        s.append(i)
    gtab = inicializarM(nodos, -1)
    path = inicializarM(nodos, None)
    coste = g(0, s, matriz, gtab, path)
    camino = c(0, s, path)
    print "El camino mas corto en Programacion Dinamica es: " + str(camino)
    print "Con distancia " + str(coste)

"""
Funcion que rellena la matriz de distancias y devuelve la distancia minima
"""
def g(i, s, matriz, gtab, camino):
    distancia = 0
    if len(s) == 0:
        return matriz[i][0]
    else:
        if (gtab[i][toNumber(s)] >= 0):
            return gtab[i][toNumber(s)]
        else:
            masCorto = 999999
            for j in s:
                ns = s[:]
                ns.remove(j)
                distancia = matriz[i][j-1] + g(j-1, ns, matriz, gtab, camino)
                if distancia < masCorto:
                    masCorto =  distancia
                    camino [i][toNumber(s)] = j
            gtab[i][toNumber(s)] = masCorto
            return masCorto

"""
Funcion que calcula el camino recorrido para el minimo coste encontrado
"""
def c(i, s, camino):
    p = []
    p.append(1)
    while len(s) != 0:
        j =  camino[i][toNumber(s)]
        p.append(j)
        s.remove(j)
        i = j-1
    p.append(1)
    return p

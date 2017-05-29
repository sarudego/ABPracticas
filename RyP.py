

def setinf(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 0:
                matriz[i][j] = float("inf")

def minfila(matriz, i):
    minimo = float("inf")
    for j in range(len(matriz)):
        if matriz[i][j] < minimo:
            minimo = matriz[i][j]
    if minimo == float("inf"):
        minimo = 0
    return minimo

def mincol(matriz, i):
    minimo = float("inf")
    for j in range(len(matriz)):
        if matriz[j][i] < minimo:
            minimo = matriz[j][i]
    if minimo == float("inf"):
        minimo = 0
    return minimo
       
def reduccion(matriz):
    cost = 0
    inf = float("inf")
    for i in range(len(matriz)):
        fmin = minfila(matriz,i)
        cost += fmin
        for j in range(len(matriz)):
            if matriz[i][j] != inf:
                matriz[i][j] = matriz[i][j] - fmin
    
    for i in range(len(matriz)):
        cmin = mincol(matriz, i)
        cost += cmin
        for j in range(len(matriz)):
            if matriz[j][i] != inf:
                matriz[j][i] = matriz[j][i] - cmin
    return cost

def factible(nodo, matriz):
    for i in range(1, len(matriz)):
        if matriz[nodo][i] != float("inf"):
            return False
    return True

def poda(ini, fin, matriz, coste):
    cost = coste
    cost += matriz[ini][fin]
    reducida = [x[:] for x in matriz]
    reducida[fin][ini] = float("inf")
    for i in range(len(matriz)):
        reducida[ini][i] = float("inf")
    for i in range(len(matriz)):
        reducida[i][fin] = float("inf")
    cost += reduccion(reducida)
    return cost


def RamPoda(matriz, nodo):
    u = float("inf")
    setinf(matriz)
    q = []
    q.append([reduccion(matriz), nodo, matriz, str(nodo+1)])
    while len(q) != 0:
        xcurso = min(q)
        q.remove(xcurso)
        for i in (range(1, len(matriz))):
            nmatriz = [x[:] for x in xcurso[2]]
            if nmatriz[xcurso[1]][i] != float("inf"):
                if poda(xcurso[1], i, xcurso[2], xcurso[0]) <= u:
                    for j in range(len(matriz)):
                        nmatriz[xcurso[1]][j] = float("inf")
                        nmatriz[j][i] = float("inf")
                    nmatriz[i][xcurso[1]] = float("inf")
                    reduccion(nmatriz)
                    q.append([poda(xcurso[1], i, xcurso[2], xcurso[0]), i, nmatriz, xcurso[3] + "-" + str(i+1)])
                    if (factible(i, xcurso[2]) == True) and (xcurso[0] < u):
                        u = xcurso[0]
                if (len(q) == 0) or (min(q)[0] >= u):
                    sol = [poda(xcurso[1], i, xcurso[2], xcurso[0]), xcurso[3] + "-" + str(i+1) + "-1"]
                    q = []
    print "El camino mas corto en Ramifacion y Poda es: " + str(sol[1])
    print "Con coste: " + str(sol[0])
                
                        

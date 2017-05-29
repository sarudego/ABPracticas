"""
Funciones auxiliares
"""


""" codigo obtenido de http://www.forosdelweb.com/f130/duda-novato-967713/"""
def leerArchivo(archivo):
        f = open(archivo)
        data = f.read().strip()
        f.close()
        matriz = [[int(num) for num in line.strip().split()] for line in data.split('\n')]
        return matriz

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
def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

""" codigo obtenido de http://edupython.blogspot.com.es/2016/06/combinaciones-permutaciones-y-otras.html"""    
def combinaciones(c, n):
    return [s for s in potencia(c) if len(s) == n]

def imprime(matriz):
    for i in matriz:
        print i
    print " "
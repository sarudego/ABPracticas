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

def imprime(matriz):
    for i in matriz:
        print i
    print " "
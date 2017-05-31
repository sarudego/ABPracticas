'''
Created on 28 de may. de 2017

@author: Sergio
'''
import random
import sys

minimo = int(float(sys.argv[1]))
maximo = int(float(sys.argv[2]))

def matrices(x):
    matriz = []
    for i in range(x):
        matriz.append([])
        for j in range(x):
            if i == j:
                matriz[i].append(0)
            else:
                matriz[i].append(random.randrange(1,99,1))
    return matriz

def escribir(x):
    if x<10:
        nombre = "Pruebas/m0"+ str(x) + ".tsp"
    else:
        nombre = "Pruebas/m" + str(x) + ".tsp"
    f = open(nombre, "w")
    m = matrices(x)
    for i in m:
        for j in i:
            f.write(str(j) + " ")
        f.write("\n")


for i in range(minimo,maximo):
    escribir(i)
escribir(maximo)


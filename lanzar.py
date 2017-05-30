#!/usr/bin python2.7

import os
from os import listdir
import time
"""
En RyP, hasta 26x26
En P.D, hasta 23x23
"""

opt = ['fb','av','pd','rp']
dire = listdir('Pruebas')
dire.sort()
for i in range(60, 5, -1):
    dire.pop(i)

ficheros_grandes = listdir('Pruebas')
ficheros_grandes.sort(reverse=True)
for i in range(60, 54, -1):
    ficheros_grandes.pop(i)
ficheros_grandes.sort()
ficheros_din = listdir('Pruebas')
ficheros_din.sort()
for i in range(60, 19, -1):
    ficheros_din.pop(i)
ficheros_din.sort(reverse=True)
for i in range(19, 15, -1):
    ficheros_din.pop(i)
ficheros_din.sort()

"""
ejecucion hasta 10x10
"""
outfile = open('tiempos.txt', 'w') # Indicamos el valor 'w'.
for i in opt:
    if (i == "fb"):
        print "Se va a ejecutar el algoritmo de \"Fuerza Bruta\" con ficheros de prueba"
    elif (i == "av"):
        print "Se va a ejecutar el algoritmo de \"Algoritmos Voraces\" con ficheros de prueba"
    elif (i == "pd"):
        print "Se va a ejecutar el algoritmo de \"Programacion Dinamica\" con ficheros de prueba"
    else:
        print "Se va a ejecutar el algoritmo de \"Ramificacion y Poda\" con ficheros de prueba"
    outfile.write("Ejecucion de " + i + "\n")
    for j in dire:
        print "Se va a ejecutar el fichero... " + j
        start_time = time.time()
        os.system('python tsp.py ' + i + ' ' + 'Pruebas/' +j)
        tiempo = (time.time() - start_time)
        outfile.write("El fichero " + j + " ha costado " + str(tiempo) + " segundos\n")
        print "Ha costado " + str(tiempo) + " segundos"
        print ""
    outfile.write("\n")
    print ""
    print ""

print "Ahora las matrices de 10x10 hasta 20x20... se toman su tiempo..."
opt2 = ['av','pd','rp']
outfile.write("\n\nAhora ficheros grandes...\n")
for i in opt2:
    outfile.write("\nEjecucion de " + i + "\n")
    if (i == "av"):
        print "Se va a ejecutar el algoritmo de \"Algoritmos Voraces\" con ficheros de prueba"
        for j in ficheros_grandes:
            print "Se va a ejecutar el fichero... " + j
            start_time = time.time()
            os.system('python tsp.py ' + i + ' ' + 'Pruebas/' +j)
            tiempo = (time.time() - start_time)
            outfile.write("El fichero " + j + " ha costado " + str(tiempo) + " segundos\n")
            print "Ha costado " + str(tiempo) + " segundos"
            print ""
    elif (i == "pd"):
        print "Se va a ejecutar el algoritmo de \"Programacion Dinamica\" con ficheros de prueba"
        for j in ficheros_din:
            print "Se va a ejecutar el fichero... " + j
            start_time = time.time()
            os.system('python tsp.py ' + i + ' ' + 'Pruebas/' +j)
            tiempo = (time.time() - start_time)
            outfile.write("El fichero " + j + " ha costado " + str(tiempo) + " segundos\n")
            print "Ha costado " + str(tiempo) + " segundos"
            print ""
    else:
        print "Se va a ejecutar el algoritmo de \"Ramificacion y Poda\" con ficheros de prueba"
        for j in ficheros_grandes:
            print "Se va a ejecutar el fichero... " + j
            start_time = time.time()
            os.system('python tsp.py ' + i + ' ' + 'Pruebas/' +j)
            tiempo = (time.time() - start_time)
            outfile.write("El fichero " + j + " ha costado " + str(tiempo) + " segundos\n")
            print "Ha costado " + str(tiempo) + " segundos"
            print ""
    print ""
    print ""

outfile.close()
# print dire
# print ficheros_grandes
# print ficheros_din


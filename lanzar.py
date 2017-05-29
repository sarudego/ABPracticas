#!/usr/bin python2.7

import os
from os import listdir
import time

opt = ['fb','av','pd','rp']
dire = listdir('Pruebas')
dire.sort()
dire.pop(16) # fichero 20
dire.pop(15) # fichero 19
dire.pop(14) # fichero 18
dire.pop(13) # fichero 17
dire.pop(12) # fichero 16
dire.pop(11) # fichero 15
dire.pop(10) # fichero 14
dire.pop(9) # fichero 13
dire.pop(8) # fichero 12
dire.pop(7) # fichero 11
dire.pop(6) # fichero 10
ficheros_grandes = listdir('Pruebas')
ficheros_grandes.sort(reverse=True)
ficheros_grandes.pop(16)
ficheros_grandes.pop(15)
ficheros_grandes.pop(14)
ficheros_grandes.pop(13)
ficheros_grandes.pop(12)
ficheros_grandes.pop(11)
ficheros_grandes.sort()
for i in opt:
    if (i == "fb"):
        print "Se va a ejecutar el algoritmo de \"Fuerza Bruta\" con ficheros de prueba"
    elif (i == "av"):
        print "Se va a ejecutar el algoritmo de \"Algoritmos Voraces\" con ficheros de prueba"
    elif (i == "pd"):
        print "Se va a ejecutar el algoritmo de \"Programacion Dinamica\" con ficheros de prueba"
    else:
        print "Se va a ejecutar el algoritmo de \"Ramificacion y Poda\" con ficheros de prueba"
    for j in dire:
        print "Se va a ejecutar el fichero... " + j
        start_time = time.time()
        os.system('python tsp.py ' + i + ' ' + 'Pruebas/' +j)
        tiempo = (time.time() - start_time)
        print "Ha costado " + str(tiempo) + " segundos"
        print ""
    print ""
    print ""

print "Ahora las matrices de 10x10 hasta 20x20... se toman su tiempo..."
opt2 = ['av','pd','rp']
for i in opt2:
    if (i == "av"):
        print "Se va a ejecutar el algoritmo de \"Algoritmos Voraces\" con ficheros de prueba"
    elif (i == "pd"):
        print "Se va a ejecutar el algoritmo de \"Programacion Dinamica\" con ficheros de prueba"
    else:
        print "Se va a ejecutar el algoritmo de \"Ramificacion y Poda\" con ficheros de prueba"
    for j in ficheros_grandes:
        print "Se va a ejecutar el fichero... " + j
        start_time = time.time()
        os.system('python tsp.py ' + i + ' ' + 'Pruebas/' +j)
        tiempo = (time.time() - start_time)
        print "Ha costado " + str(tiempo) + " segundos"
        print ""
    print ""
    print ""

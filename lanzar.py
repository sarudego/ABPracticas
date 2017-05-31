#!/usr/bin python2.7

import os
from os import listdir
import time
"""
Limits:
In Brute, until 13x13
In RyP, until 26x26
In P.D, until 23x23
In Voraz, we don't reach the limit...
"""

opt = ['fb','av','pd','rp']

files_small = []
files_medium = []
files_large = []
for i in listdir('Pruebas'):
    if i == "m128.tsp" or i == "m256.tsp" or i == "m512.tsp" or i == "m1024.tsp" or i == "m2048.tsp":
        files_large.append(i)
    elif i == "m04.tsp" or i == "m05.tsp" or i == "m06.tsp" or i == "m07.tsp" or i == "m08.tsp" or i == "m09.tsp":
        files_small.append(i)
    else:
        files_medium.append(i)
files_small.sort()
files_medium.sort()
files_large.sort()


outfile = open('tiempos.txt', 'w') # Indicamos el valor 'w'.
def execute_time(alg,i):
    print "Se va a ejecutar el fichero... " + i
    start_time = time.time()
    os.system('python tsp.py ' + alg + ' ' + 'Pruebas/' +i)
    tiempo = (time.time() - start_time)
    outfile.write("El fichero " + i + " ha costado " + str(tiempo) + " segundos\n")
    print "Ha costado " + str(tiempo) + " segundos"
    print ""

def bruta(alg):
    for i in files_small:
        execute_time(alg,i)
    for i in files_medium[:6]:
        execute_time(alg,i)

def voraz(alg):
    for i in files_small:
        execute_time(alg,i)
    for i in files_medium:
        execute_time(alg,i)
    for i in files_large:
        execute_time(alg,i)

def dinamica(alg):
    for i in files_small:
        print ""
    for i in files_medium[:14]:
        execute_time(alg,i)

def poda(alg):
    for i in files_small:
        execute_time(alg,i)
    for i in files_medium[:17]:
        execute_time(alg,i)

for i in opt:
    outfile.write("Ejecucion de " + i + "\n")
    if (i == "fb"):
        print "Ejecucion de \"Fuerza Bruta\" con ficheros de prueba:"
        bruta(i)
    elif (i == "av"):
        print "Ejecucion de \"Algoritmos Voraces\" con ficheros de prueba:"
        voraz(i)
    elif (i == "pd"):
        print "Ejecucion de \"Programacion Dinamica\" con ficheros de prueba:"
        dinamica(i)
    else:
        print "Ejecucion de \"Ramificacion y Poda\" con ficheros de prueba:"
        poda(i)

outfile.close()
# print files_small
# print files_medium
# print files_large

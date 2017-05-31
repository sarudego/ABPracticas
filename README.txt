La implementación se ha realizado en python, asi que no es necesaria compilación.

Para ejecutar un determinado algoritmo sobre un grafo se debe ejecutar:
./tsp algoritmo ruta
	
	algoritmo:
		fb - fuerza bruta
		av - algoritmo voraz
		pd - programación dinámica
		rp - ramificación y poda
	
	ruta:
		donde se encuetra el archivo que contiene el grafo

	Ejemplo:
		./tsp fb /pruebas/m08.tsp
-------------------------------------------------------------------------------------------------------------------------------------

Para crear los archvios que continene los grafos se debe ejecutar el archivo matrices.py de la siguiente forma:

python matrices.py [minimo] [maximo]
	minimo = número de filas y columnas de la matriz mas pequeña que se quiere generar
	maximo = número de filas y columnas de la matriz mas grande que se quiere generar

Las matrices generadas se guardaran en la carpeta Pruebas que se encuentra en este mismo direcctorio.
-------------------------------------------------------------------------------------------------------------------------------------

Es posible ejecutar un fichero de manera que se comprueben de manera automática
los ficheros en la carpeta Pruebas.

Para ello unicamente es necesario ejecutar el fichero "lanzar.py" con:
"python lanzar.py".

Esto irá ejecutando los distintos algoritmos con grafos de distintos tamaños,
desde 4x4 hasta 2048x2048, pero debido al tipo de algoritmo,en alguno se ha 
limitado el tamaño de grafo a ejecutar, debido a quedarse el ordenador sin memoria

Imprimirá por consola los resultados y guardará la ejecución en un fichero llamado
"tiempos.txt" mostrando el tiempo que de ejecución de cada algoritmo con cada
fichero..

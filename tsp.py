import sys
import p1
import auxi
import dynamic


opt = sys.argv[1]
archivo = sys.argv[2]



if opt == "fb":
    matriz = auxi.leerArchivo(archivo)
    print matriz
    p1.fuerzaMatriz(matriz)
elif opt == "av":
    print "Aun no se ha implementado el algoritmo voraz"
elif opt == "pd":
    print "Aun no se ha implementado la programacion dinamica"
    matriz = auxi.leerArchivo(archivo)
    dynamic.dinamica(matriz)
elif opt == "rp":
    print "Aun no se ha implementado la ramificacion y poda"
else:
    print "No se a elegido un esquema valido"
import sys
import bruta, dynamic, voraz, auxi, RyP


opt = sys.argv[1]
archivo = sys.argv[2]

if opt == "fb":
    try:
        matriz = auxi.leerArchivo(archivo)
    except:
        print "No se ha podido leer archivo"
        print "Compruebe que la ruta esta bien escrita"
    else:
        bruta.fuerzaMatriz(matriz)
elif opt == "av":
    try:
        matriz = auxi.leerArchivo(archivo)
    except:
        print "No se ha podido leer archivo"
        print "Compruebe que la ruta esta bien escrita"
    else:
        voraz.voraz(matriz)
elif opt == "pd":
    try:
        matriz = auxi.leerArchivo(archivo)
    except:
        print "No se ha podido leer archivo"
        print "Compruebe que la ruta esta bien escrita"
    else:
        dynamic.dinamica(matriz)
elif opt == "rp":
    try:
        matriz = auxi.leerArchivo(archivo)
    except:
        print "No se ha podido leer archivo"
        print "Compruebe que la ruta esta bien escrita"
    else:
        RyP.RamPoda(matriz, 0)
else:
    print "No se a elegido un esquema valido"

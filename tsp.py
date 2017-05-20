import sys
import p1, dynamic, voraz, auxi


opt = sys.argv[1]
archivo = sys.argv[2]

if opt == "fb":
    try:
        matriz = auxi.leerArchivo(archivo)
    except:
        print "No se ha podido leer archivo"
        print "Compruebe que la ruta esta bien escrita"
    else:
        p1.fuerzaMatriz(matriz)
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
    print "Aun no se ha implementado la ramificacion y poda"
else:
    print "No se a elegido un esquema valido"
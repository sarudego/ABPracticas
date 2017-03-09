#Python 3

"""
Problema de la mochila:
    Tenemos un conjunto N de objetos
    cada objeto tiene un peso P y un valor V
    y queremos llenar una mochila con capacidad C
    maximizando el beneficio
"""

listado = {"1": [10, 80],
        "2": [16, 60],
        "3": [30, 100],
        "4": [20, 15],
        "5": [12, 10]}


C = 60 # capacidad
res = C
sol = {}
for i in listado:
    p = listado[i][0]
    v = listado[i][1]
    print("objeto {} con un peso de {} y beneficio de {}".format(i, p, v))

    if listado[i][0] <= res:
        sol[i] = [p, v]
        res = res - sol[i][0]

for i in sol:
    p = sol[i][0]
    v = sol[i][1]
    print("Los objetos metidos son: {}, con un peso de {} y beneficio de {}".format(i, p, v))


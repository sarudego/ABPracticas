#Python 2
"""
Problema del viajante de comercio.
Listado de ciudades con una distancia conocida entre si.
1. Implementar los esquemas algoritmos mediante:
    Fuerza Bruta
    Algoritmo voraz
    Programacion dinamica
    Ramificacion y poda
2. Calcular y comparar tiempos de ejecucion para distintas entradas
"""
import doctest
import numpy as np
from itertools import permutations
import math
import operator
#Para ejemplo 
# np.array([1,2])
# points = [[0, 0], [1, 5], [5, 3]]
# points = np.random.random((3,3))

def distance(point1, point2):
    """
    distance = raiz((x2-x1)^2 + (y2-y1)^2)
    """
    return round(math.sqrt((point2[0] - point1[0])**2 + (point2[1] -
        point1[1])**2),2)


    def total_distance(points):
        """
    Returns the length of the path passing throught
    all the points in the given order.
    """
    # print(distance(points[0],points[1]))
    return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])


def optimized_travelling_salesman(points, start=None):
    """
    As solving the problem in the brute force way is too slow,
    this function implements a simple heuristic: always
    go to the nearest city.
    Even if this algoritmh is extremely simple, it works pretty well
    giving a solution only about 25% longer than the optimal one (cit. Wikipedia),
    and runs very fast in O(N^2) time complexity.
    """
    if start is None:
        start = points[0]
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path

def gen_cost(points):
    for i in points:
        for j in points:
            if i !=j:
                print("dist. between {} --> {} is {}".format(i,j,distance(i,j)))

def main():
    doctest.testmod()
    # points = [[0, 0], [1, 5.7], [2, 3], [3, 7],
             # [0.5, 9], [3, 5], [9, 1], [10, 5]]
    points = [[0, 0], [5,9], [3,8]]
    start_point = points[1]
    gen_cost(points)
    print("""The minimum distance to visit all the following points: {}
          starting at {}.
    The optimized algoritmh yields a path long {}.""".format(
        tuple(points),
        start_point,
        total_distance(optimized_travelling_salesman(points,start_point))))

    if __name__ == "__main__":
        main()



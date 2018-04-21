# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt

def closestpoint(point, route):
    dmin = float("inf")
    for p in route:
        d = math.sqrt((int(point[0]) - int(p[0]))**2 + (int(point[1]) - int(p[1]))**2)
        if d < dmin:
            dmin = d
            closest = p
    return closest, dmin

def graphplot(list):
    xlist = []
    ylist = []
    for x, y in list:
        xlist.append(x)
        ylist.append(y)

    plt.plot(xlist, ylist)
    plt.show()
    
def findpath(point, list):
    path = [point]
    sum = 0
    while len(list) >= 1:
        closest, dist = closestpoint(path[-1], list)
        path.append(closest)
        list.remove(closest)
        sum += dist
    # Go back the the beginning when done.
    closest, dist = closestpoint(path[-1], [point])
    path.append(closest)
    sum += dist
    return path, sum
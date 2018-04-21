# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 14:36:46 2018

@author: Dylan Tey
"""

import math
import random

def closestpoint(point, route):
    dmin = float("inf")
    for p in route:
        d = math.sqrt((int(point[0]) - int(p[0]))**2 + (int(point[1]) - int(p[1]))**2)
        if d < dmin:
            dmin = d
            closest = p
    return closest, dmin


file = open('wi29.tsp','r').read().splitlines()[7:-1]

list = []
for item in file:
    #print(item)
    num, x, y = item.split(" ")
    #print('x is ', float(x))
    #print('y is ', float(y))
    list.append([float(x), float(y)]) # int tuple list

random_number = random.randint(0, len(list)+1)

point = list.pop(random_number) # pop out the first item in the list

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

print("Optimal route:", path)
print("Length:", sum)
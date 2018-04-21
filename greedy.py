# -*- coding: utf-8 -*-


import time
import tsp_util

t0 = time.time()
file = open('qa194.tsp','r').read().splitlines()[7:-1]

list = []
for item in file:
    num, x, y = item.split(" ")
    list.append([float(x), float(y)]) # int tuple list

point = list.pop(0) # pop out the first item in the list

path, sum = tsp_util.findpath(point, list)
t1 = time.time()
total = t1 - t0

print("Optimal route:", path)
print("Length:", sum)
print("Time Take: %.3fs" %total)

# graph it
tsp_util.graphplot(path)
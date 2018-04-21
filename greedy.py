# -*- coding: utf-8 -*-


import tsp_util


file = open('wi29.tsp','r').read().splitlines()[7:-1]

list = []
for item in file:
    num, x, y = item.split(" ")
    list.append([float(x), float(y)]) # int tuple list

point = list.pop(0) # pop out the first item in the list

path, sum = tsp_util.findpath(point, list)

print("Optimal route:", path)
print("Length:", sum)

# graph it
tsp_util.graphplot(path)
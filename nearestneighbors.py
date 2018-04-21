# -*- coding: utf-8 -*-

import random
import tsp_util


file = open('qa194.tsp','r').read().splitlines()[7:-1]

list = []
for item in file:
    num, x, y = item.split(" ")
    list.append([float(x), float(y)]) # int tuple list

random_number = random.randint(0, len(list)+1)

point = list.pop(random_number) # pop out the first item in the list

path, sum = tsp_util.findpath(point, list)

print("Optimal route:", path)
print("Length:", sum)

# graph it
tsp_util.graphplot(path)
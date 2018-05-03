import sys
import math
import tsp_util
import clusters
import matplotlib
import random
import time


#MAIN-------------------------------
list = []
filename = 'wi29.tsp'

t0 = time.time()

#process file to get proper input
list = tsp_util.processFile(filename)

#build clusters and fillclusters():

firstCluster = []
firstList = []
secondCluster = []
secondList = []
thirdCluster= []
thirdList = []
fourthCluster = []
fourthList = []

firstCluster,secondCluster,thirdCluster,fourthCluster = clusters.findClusters(list)
firstCluster,secondCluster,thirdCluster,fourthCluster = clusters.FillClusters(firstCluster,secondCluster,thirdCluster,fourthCluster,list)
#Copy Lists so we still have them


firstList.extend(firstCluster)
secondList.extend(secondCluster)
thirdList.extend(thirdCluster)
fourthList.extend(fourthCluster)

#find optimal path in each clusters
sumList = []
sum = 0
print("\n first list is")
print(firstList)
firstList, sum = tsp_util.nearestNeighbor(firstList)
sumList.append(sum)
secondList, sum = tsp_util.nearestNeighbor(secondList)
sumList.append(sum)
thirdList, sum = tsp_util.nearestNeighbor(thirdList)
sumList.append(sum)
fourthList, sum = tsp_util.nearestNeighbor(fourthList)
sumList.append(sum)



#first sort the cluster, then get 2 max from each, shove into aggregate list
cities = []

firstCluster.sort()

if len(firstCluster) >= 2:
    cities.append(firstCluster.pop(0))
    cities.append(firstCluster.pop(-1))
    cities.append(firstCluster.pop(-1))
    cities.append([])
# doesnt pop if it's only one element


secondCluster.sort()

if len(secondCluster) >= 4:
    cities.append(secondCluster.pop(-1))
    cities.append(secondCluster.pop(0))
    cities.append(secondCluster.pop(-1))
    cities.append(secondCluster.pop(0))
    cities.append([])
# doesnt pop if it's only one element
elif len(secondCluster) >= 2:
    cities.append(secondCluster.pop(-1))
    cities.append(secondCluster.pop(0))
    cities.append([])
# doesnt pop if it's only one element


thirdCluster.sort()

if len(thirdCluster) >= 4:
    cities.append(thirdCluster.pop(-1))
    cities.append(thirdCluster.pop(0))
    cities.append(thirdCluster.pop(-1))
    cities.append(thirdCluster.pop(0))
    cities.append([])
# doesnt pop if it's only one element
elif len(thirdCluster) >= 2:
    cities.append(thirdCluster.pop(-1))
    cities.append(thirdCluster.pop(0))
    cities.append([])
# doesnt pop if it's only one element


fourthCluster.sort()

if len(fourthCluster) >= 2:
    cities.append(fourthCluster.pop(0))
    cities.append(fourthCluster.pop(0))
    cities.append([])
# doesnt pop if it's only one element




"""
firstCluster.sort()
cities.append(firstCluster.pop(-1))
cities.append(firstCluster.pop(-1))
cities.append(firstCluster.pop(0))
cities.append(firstCluster.pop(0))
secondCluster.sort()
cities.append(secondCluster.pop(-1))
cities.append(secondCluster.pop(-1))
cities.append(secondCluster.pop(0))
cities.append(secondCluster.pop(0))
thirdCluster.sort()
cities.append(thirdCluster.pop(-1))
cities.append(thirdCluster.pop(-1))
cities.append(thirdCluster.pop(0))
cities.append(thirdCluster.pop(0))
fourthCluster.sort()
cities.append(fourthCluster.pop(-1))
cities.append(fourthCluster.pop(-1))
cities.append(fourthCluster.pop(0))
cities.append(fourthCluster.pop(0))
"""

firstList = tsp_util.combineClusters(firstList,secondList,thirdList,fourthList,cities)

t1 = time.time()
total = t1 - t0

print("\n route:", firstList)
print(len(firstList))
sum = tsp_util.sumDistance(firstList)


print("Length:", sum)
print("Time Take: %.3fs" %total)

tsp_util.graphplot(firstList)

import sys
import timeit
import math
import tsp_util
import clusters
import matplotlib
import random


#MAIN-------------------------------
list = []
filename = 'qa194.tsp'

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
print("\n")
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


firstList = tsp_util.combineClusters(firstList,secondList,thirdList,fourthList,cities)


print("\n route:", firstList)

tsp_util.graphplot(firstList)

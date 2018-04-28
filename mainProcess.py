import sys
import timeit
import math
import tsp_util
import clusters


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

firstCluster,secondCluster,thirdCluster,fourthCluster = findClusters(list)
firstCluster,secondCluster,thirdCluster,fourthCluster = FillClusters(firstCluster,secondCluster,thirdCluster,fourthCluster,list)

#find optimal path in each clusters
sumList = []

firstList, sumList[0] = tsp_util.nearestNeighbor(firstCluster)
secondList, sumList[1] = tsp_util.nearestNeighbor(secondCluster)
thirdList, sumList[2] = tsp_util.nearestNeighbor(thirdCluster)
fourthList, sumList[3] = tsp_util.nearestNeighbor(fourthCluster)

#Connect the Clusters

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


firstList = tsp_util.combinedList(firstList,secondList,thirdList,fourthList,cities)

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 14:36:46 2018

@author: Dylan Tey
"""

import sys
import timeit
import math


def findClusters(list):
    a = []
    b = []
    c = []
    d = []

    #first find min/max from entire list
    minX = list[0][0]
    maxX = list[0][0]


    for iterator in range(0,len(list)):
        if minX > list[iterator][0]:
            minX = list[iterator][0]
        if maxX < list[iterator][0]:
            maxX = list[iterator][0]

    #find min/max for each subregion

    regionRange = int((maxX-minX)/4.0)

    aRegionMin = int(minX)
    aRegionMax = (aRegionMin + regionRange)-1

    bRegionMin = aRegionMax + 1
    bRegionMax = (bRegionMin + regionRange)-1

    cRegionMin = bRegionMax + 1
    cRegionMax = (cRegionMin + regionRange)-1

    dRegionMin = maxX-regionRange
    dRegionMax = maxX

    print(str(regionRange)+"")

    print ("\n")
    print(minX)

    print ("\n")
    print(maxX)


    print("\n + RegionA Max: "+str(aRegionMax))
    print("\n + RegionB Max: "+str(bRegionMax))
    print("\n + RegionC Max: "+str(cRegionMax))
    print("\n + RegionD Max: "+str(dRegionMax))
    print ("\n")
    #create 4 subregions
    a.append(aRegionMin)
    a.append(aRegionMax)
    b.append(bRegionMin)
    b.append(bRegionMax)
    c.append(cRegionMin)
    c.append(cRegionMax)
    d.append(dRegionMin)
    d.append(dRegionMax)

    return a, b, c, d

def FillClusters(a,b,c,d, list):

    minA = a[0]
    maxA = a[1]

    minB = b[0]
    maxB = b[1]

    minC = c[0]
    maxC = c[1]

    minD = d[0]
    maxD = d[1]

    alist = []
    blist = []
    clist = []
    dlist = []

    for iterator in range(0,len(list)):
        currentX = list[iterator][0]
        currentY = list[iterator][1]
        if currentX <= maxA:
            alist.append(list[iterator])
        elif currentX <= maxB:
            blist.append(list[iterator])
        elif currentX <= maxC:
            clist.append(list[iterator])
        else:
            dlist.append(list[iterator])



    print("\n + This is list a:")
    print(alist)
    print("\n + This is list b:")
    print(blist)
    print("\n + This is list c:")
    print(clist)
    print("\n + This is list d:")
    print(dlist)
    print("\n")

    return alist,blist,clist,dlist


#print(list)
#first,second,third,fourth = findClusterRange(list)
#first,second,third,fourth = FillClusters(first,second,third,fourth,list)

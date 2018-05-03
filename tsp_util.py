# -*- coding: utf-8 -*-

import math
import random
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
def sumDistance(list):
    sum = 0

    for coordinate in range(0,len(list)-1):
        pointA = list[coordinate]
        pointB = list[coordinate+1]


        # sqrt(c^2)= sqrt((a-a2)^2+(b-b2)^2)
        sum += math.sqrt((int(pointA[0]) - int(pointB[0]))**2 + (int(pointA[1]) - int(pointB[1]))**2)




    return sum
def processFile(filename):


    file = open(filename,'r').read().splitlines()[7:-1]

    list = []
    for item in file:
        num, x, y = item.split(" ")
        list.append([float(x), float(y)]) # int tuple list


    #file.close()

    return list

def nearestNeighbor(list):
    random_number = random.randint(0, len(list)-1)
    print(random_number)

    point = list.pop(random_number) # pop out random item from list

    path, sum = findpath(point, list)
    return path, sum

def greedy(list):
    point = list.pop(0) # pop out the first item in the list

    path, sum = findpath(point, list)
    return path, sum

def combineClusters(firstList,secondList,thirdList,fourthList, cities):


    #cities [0]amax[1]amax [2]amin[3]amin

    #cities [4]bmax [5]bmax [6]bmin [7min]

    #cities [8]cmax [9]cmax [10]cmin [11cmin]

    #cities [12]dmax [13]dmax [14]dmin [15]dmin

    #connect amax to bmin

    counter = 1
    iteratorOfList = 1
    print("cities")
    print(cities)
    for city in cities:
        if city == []:
            print("\n\n-----next list-----\n\n")
            iteratorOfList += 1
            counter += 1
            continue
        elif iteratorOfList == 1:
            continue
        elif counter == 1:
            print("\n\n-----iterator is %d-----\n\n" %iteratorOfList)
            print(city)
            print(firstList)
            firstList.remove(city)
            print("\n\n-----iterator is %d is successful-----\n\n" %iteratorOfList)
            iteratorOfList += 1
        elif counter == 2:
            print("\n\n-----iterator is %d-----\n\n" %iteratorOfList)
            print(city)
            print(secondList)
            secondList.remove(city)
            print("\n\n-----iterator is %d is successful-----\n\n" %iteratorOfList)
            iteratorOfList += 1
        elif counter == 3:
            thirdList.remove(city)
            iteratorOfList += 1
        elif counter == 4:
            fourthList.remove(city)
            iteratorOfList += 1

    counter = 1
    iteratorOfList = 1
    for city in cities:
        if city == []:
            if counter == 2:
                firstList.extend(secondList)
            elif counter == 3:
                firstList.extend(thirdList)
            elif counter == 4:
                firstList.extend(fourthList)
            iteratorOfList += 1
            counter += 1
        elif iteratorOfList == 1:
            continue
        elif counter == 1:
            firstList.append(city)
            iteratorOfList += 1
        elif counter == 2:
            secondList.append(city)
            iteratorOfList += 1
        elif counter == 3:
            thirdList.append(city)
            iteratorOfList += 1
        elif counter == 4:
            fourthList.append(city)
            iteratorOfList += 1

    firstList.append(cities[0])

    return firstList


"""
    firstList.remove(cities[0])
    firstList.remove(cities[1])
    secondList.remove(cities[4])
    secondList.remove(cities[5])
    secondList.remove(cities[6])
    secondList.remove(cities[7])
    thirdList.remove(cities[8])
    thirdList.remove(cities[9])
    thirdList.remove(cities[10])
    thirdList.remove(cities[11])
    fourthList.remove(cities[14])
    fourthList.remove(cities[15])


    firstList.append(cities[0])
    firstList.append(cities[6])
    firstList.append(cities[1])
    firstList.append(cities[7])

    firstList.extend(secondList)
    #ok up to this point
    firstList.append(cities[4])
    firstList.append(cities[10])
    firstList.append(cities[5])
    firstList.append(cities[11])

    firstList.extend(thirdList)

    firstList.append(cities[8])
    firstList.append(cities[14])
    firstList.append(cities[9])
    firstList.append(cities[15])

    firstList.extend(fourthList)
"""

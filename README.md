# The Plan


- use greedy method to figure out which one to start with based on number
- use nearest neighbor to create path in sub region

#process input file():
-spit out file with just x and y

#build clusters and fillclusters():
- process file with x, y
- find min and max x coordinate
- create 4 regions (or relative number based on 3 of total cities) based on x increment
- create min max for each sub region (4)
- spit out the arrays with cities separated in each

#process individual clusters():
- using nearest neighbor by randomly selecting initial city

#connect clusters ():
- by utilizing greedy method for lowest distance between two cities of adjacent sectors

#PrintPath():

#PlotPath:

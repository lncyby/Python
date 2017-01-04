#!/usr/bin/python

l = []

for x in range(0,10):
    l.append([])
    l[x].append(1)
    for y in range(1,x+1):
        num = l[x-1][y-1]+l[x-1][y]
        l[x].append(num)
    l[x].append(0)
for x in range(0,10):
    for y in range(x+1):
        print "%d"%l[x][y],
    print ""

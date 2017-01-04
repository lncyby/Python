#!/usr/bin/python

l = [[12,45,30,8],[3,18,60,15],[23,21,10,8]]
max = l[0][0]
for a in range(3):
    for b in range(4):
        if  l[a][b] > max:
            max = l[x][y]
            x = a
            y = b
print "max=%d, [%d][%d]"%(max,x,y)

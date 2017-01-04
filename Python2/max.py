#!/usr/bin/python

l = [[5,3,8,6],
     [4,7,2,9],
     [3,1,6,4]]

for i in range(3):
    line_max = max(l[i])
    k = l[i].index(line_max)
    num = l[i][k]
    for j in range(3):
        if l[j][k] > num:
            num = l[j][k]
    if num == line_max:
        print "l[%d][%d] = %d"%(i,k,num)

max = l[0][0]
x = y = 0
for i in range(3):
    for j in range(4):
        if l[i][j] > max:
            max = l[i][j]
            x = i
            y = j
print "l[%d][%d] = %d"%(x,y,max)

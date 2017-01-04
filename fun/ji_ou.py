#!/usr/bin/python

def fun(l):
    i = 0
    j = len(l) - 1
    
    while i < j:
        while l[i] % 2 != 0:
            i += 1
        while l[j] % 2 == 0:
            j -= 1

        l[i],l[j] = l[j],l[i]

l = [1,2,3,4,5,6,7,8,9,10]
print "before:",l

fun(l)
print "after:",l

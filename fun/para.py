#!/usr/bin/python

def fun(a):
    a = a[:]
    a[2] = 100
    print "fun:",a

l = [1,2,3,4,5]

print l

print "+++++++++++++++++++"

fun(l)

print l

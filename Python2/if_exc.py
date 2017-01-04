#!/usr/bin/python

a = input()
b = input()
c = input()

if a > b:
    a,b = b,a

if a > c:
    a,c = c,a

if b > c:
    b,c = c,b

print "a = %d,b = %d,c = %d"%(a,b,c)

#! /usr/bin/python

a = int(input())
b = int(input())
c = int(input())


if a > b:
    tmp = a
    a = b
    b = tmp

if a > c:
    tmp = a
    a = c
    c = tmp

if b > c:
    tmp = b
    b = c
    c = tmp

print("a = %d,b = %d,c = %d"%(a,b,c))

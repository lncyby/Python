#!/usr/bin/python

#输入三角形三条边求面积
import math

a = input()
b = input()
c = input()

if a + b < c or a + c < b or b + c < a:
    print "input error"
    exit()

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print "The area is %.2f"%area

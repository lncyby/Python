#!/usr/bin/python
#coding=utf-8

#求两个根
'''
name : lvze
mail :lvze@cainiaoketang.com
add:xxxx
tel:xxxx
'''

import math

a = input("a:") # a : input
b = input("b:")
c = input("c:")

q = b * b - 4 * a * c

#判断输入出错
if q < 0:
    print "没有根"
    exit()

x = -b /(a * 2)
#   求开方
y = math.sqrt(q)

x1 = x + y
x2 = x - y

print "x1:%.2f,x2:%.2f"%(x1,x2)

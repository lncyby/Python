#!/usr/bin/python
#coding=utf-8

#水仙花数

for i in range(100,1000):
    ge = i % 10
    shi = i / 10 % 10
    bai = i / 100

    if i == ge ** 3 + shi ** 3 + bai ** 3:
        print "%d "%i,

print ""

#!/usr/bin/python
#coding=utf-8

#²ÂÊıÓÎÏ·

import random

i = 0

while i < 4:
    print "******************************************************************"

    num = input("input 0-9:")
    xnum = random.randint(0,9)

    x = 3 - i

    if num == xnum:
        print "You are right!!"
        break
    elif num < xnum:
        print "small,is%d,remain%d"%(xnum,x)
    elif num > xnum:
        print "big,is%d,remain%d"%(xnum,x)
    
    print "******************************************************************"

    i += 1




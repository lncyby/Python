#!/usr/bin/python

def fun(a,b,c ):
    print a,b,c

fun(**{'a':1,'b':2,'c':3})
fun(*[1,2,3])

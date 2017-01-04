#!/usr/bin/python

class A(object):
    def __call__(self,x):
        print "x : "+str(x)

a = A()

a(2000)

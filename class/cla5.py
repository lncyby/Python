#!/usr/bin/python

class A():
    def fun(self,a):
        print a

class B(A):
    def fun(self,a,b):
        print a + b


b = B()

#b.fun(1)

b.fun(1,2)

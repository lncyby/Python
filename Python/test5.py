#!/usr/bin/python

class A(object):
    __name = "zhangsan"

class B(A):
    pass


b = B()
a = A()

#print b.__name
print a.__name

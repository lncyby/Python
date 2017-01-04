#!/usr/bin/python

class TestStaticMethod(object):
#    age = 10
    @staticmethod
    def foo():
#        print TestStaticMethod.age
        print "calling static method foo()"
#    foo = staticmethod(foo)

class TestClassMethod(object):
    @classmethod
    def foo(cls):
        print "calling class method foo()"
        print "class",cls.__name__
#    foo = classmethod(foo)


A = TestStaticMethod()
A.foo()

B = TestClassMethod()
B.foo()

TestStaticMethod.foo()
TestClassMethod.foo()

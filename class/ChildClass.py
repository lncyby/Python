#!/usr/bin/python
#coding=utf-8

class ParentClass():
    name = "老张"

    def func(self):
        print "老子有钱"

class ChildClass(ParentClass):
    name = "小张"
    def fun(self):
        print "哥也有钱"


child = ChildClass()

print child.name
child.func()
child.fun()

parent = ParentClass()

parent.fun()

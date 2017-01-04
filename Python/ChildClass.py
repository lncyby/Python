#!/usr/bin/python
#coding=utf-8

class ParentClass(object):
    name = '老张'
    def func(self):
        print "老子有钱"

class ChildClass(ParentClass):
    name = "小张"
    def func(self,s):
        print "哥也有钱%s"%s

child = ChildClass()

print child.name
child.func("$")

parent = ParentClass()
print parent.name

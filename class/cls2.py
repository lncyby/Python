#!/usr/bin/python
#coding=utf-8
__metaclass__ = type
class Person():

    print "This is a class"

    age = 10

    def __init__(self,name):     # __init__初始化
        print "init func"
        self.name = name

    def color(self,color):      # self 在类的方法必须有个额外的第一个参数
        print "%s is %s"%(self.name,color)

Lilei = Person('Lilei')

print Lilei.age

print Lilei.name

Lilei.color('black')

print "****************************8"


Hanmei = Person('Hanmei')

print Hanmei.age

print Hanmei.name

Hanmei.color('yellow')

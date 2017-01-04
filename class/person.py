#!/usr/bin/python
#coding=utf-8

class Person(object):

    age = 10

    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def color(self,color):
        print("%s is %s"%(self.name,color))

Lilei = Person('lilei')

print(Lilei.age)

Lilei.name = "Li"
Lilei.sex = 'man'  # 可以为这个对象增加属性

def fun():
    print "new fun"

Lilei.new = fun
Lilei.new()

print(Lilei.getName())

Lilei.color('black')

print(dir(Lilei))

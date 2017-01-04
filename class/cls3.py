#!/usr/bin/python
#coding=utf-8
class Person():
    age = 10

    def color(self,color): # 在类的方法必须有一个额外的第一个参数（self）
        print "%s is %s"%(self.name,color)


Lilei = Person()

print Lilei.age

Lilei.name = "Lilei"

print Lilei.name

Lilei.color('black')

print dir(Lilei)

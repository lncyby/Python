#!/usr/bin/python

class Animal(object):

    print "A new animal!!"

    def call(self,yell):
        self.yell = yell

class Dog(Animal):
    color = "yellow"

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

class Cat(Animal):
    color = "white"
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name


wang = Dog()
miao = Cat()

wang.setName("dahuang")
miao.setName("xiaomiao")

print wang.getName()
print miao.getName()

wang.call("wangwang")
print wang.yell
miao.call("miaomiao")
print miao.yell

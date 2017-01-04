#!/usr/bin/python
#coding=utf-8

# 定义一个类（动物）
class Animal(object):

    print "A new animal!!"    # 输出“一个新动物”

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

if __name__ == '__main__':
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

#!/usr/bin/python
#coding=utf-8

class Car(object):
    wheel = 4
    engine = None

    def __init__(self,name):
        self.name = name

    def fun(self):
        print "跑......"

class Bus(Car):
    zuo = 20
    color = "yellow"

class SUV(Car):
    def __init__(self,color):
        self.color = color
    def func(self):
        print "越野。。。。"

class SportsCar(Car):
    engine = 12

suv = SUV("red")
suv.func()
print suv.wheel,suv.engine

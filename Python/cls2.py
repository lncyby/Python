#!/usr/bin/python

class Person(object):
    print "class ......"
    
    def __new__(cls):
        print "new......"
        return object.__new__(cls)

    def __init__(self):
        print "init....."

    def color(self):
        print "color...."

    def __del__(self):
        print "del......"

Lilei = Person()
Lilei.color()

del Lilei

Hanmei = Person()
Hanmei.color()

#!/usr/bin/python

class Person(object):

    print "class ....."

    def __init__(self):      # 初始化一个函数
        print "init...."
    def __new__(cls):
        print "new ......"
        return object.__new__(cls)

    def color(self):
        print "color....."

    def __del__(self):
        print "del....."

Lilei = Person()

Lilei.color()

Hanmei = Person()

Hanmei.color()

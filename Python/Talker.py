#!/usr/bin/python

class Speaker(object):
    name = "mao"

class Calculator(Speaker):
    name = "luosifu"

    age = 88

class Talker(Speaker):
    name = "liyong"

    sex = 'man'

class TalkCalculator(Calculator,Talker):
#    name = "mengfei"
    pass

A = TalkCalculator()

print TalkCalculator.mro()

print A.name
print A.sex
print A.age

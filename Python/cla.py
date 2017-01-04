#!/usr/bin/python

#a = 10000
class Person(object):
    '''This is  a class'''
    age = 10
    name = "Lilei"

    def color(self,color):
        self.language = "English"
        print "%s is %s"%(self.name,color)
#    print a

#print age
Lilei = Person()
Hanmei = Person()
Lilei.sex = 'Man'
Hanmei.name = "Hanmei"
print Lilei.age
print Person.age
print Lilei.name
print Hanmei.age
print Lilei.sex
#print Person.sex
Lilei.color('black')
print Lilei.language
Hanmei.color('yellow')

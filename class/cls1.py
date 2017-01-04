#!/usr/bin/python

class Person():
    age = 10
    name = "Lilei"

    def color(self,color):
        print "%s is %s"%(self.name,color)

#age = 20

#print age

Lilei = Person()

print Lilei.age
print Lilei.name

Lilei.color('black')

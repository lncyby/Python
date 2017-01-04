class Person(object):
    age = 10

    def __init__(self,name):
        self.name = name

    def color(self,color):
        print "%s is %s"%(self.name,color)

Lilei = Person("Lilei")
Hanmei = Person("Hanmei")

Lilei.color("black")
Hanmei.color("yellow")
print dir(Lilei)

#!/usr/bin/python


class Bird1(object):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print "Aaaah"
            self.hungry = False
        else:
            print "No Thanks"
class Bird2(object):
    def __init__(self):
        self.call = "gugugu"

    def tall(self):
        print self.call

class SongBird(Bird1,Bird2):
    def __init__(self):
        super(SongBird,self).__init__()

    def eat(self):
        print "songbird eat"
    def tall(self):
        print "songbird talk"

niao = SongBird()
niao.eat()
niao.tall()

super(SongBird,niao).eat()
super(SongBird,niao).tall()

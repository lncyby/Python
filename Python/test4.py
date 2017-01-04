#!/usr/bin/python

class Student(object):
    def __init__(self):
        pass

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if value < 0 or value > 100:
            raise ValueError("score must between 0 -- 100")
        self.__score = value
s = Student()

s.score = 100  >> s.score(100)

print s.score  >>s.score()

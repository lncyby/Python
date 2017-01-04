#!/usr/bin/python

class Test(object):
    def __del__(self):
        print "del...."

    def __enter__(self):
        print "enter..."

    def __exit__(self,type,value,traceback):
        print "exit......"
        print type
        print value
        print traceback

    def do_something(self):
        return 1 / 0

with Test() as Thing:
    print "doing something"
#    Thing.do_something()

print "over"

#!/usr/bin/python

class MyError(Exception):
    pass

try:
    s = None
    if s is None:
        print "s is none"
        raise MyError("s is NoneType")
    print len(s)

except MyError as x:
    print "s has no lenght"
    print x

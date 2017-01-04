#!/usr/bin/python

def func():
    print "hello world!"

print "++++++++++++++++"
func()

f = func

f()
print type(f)

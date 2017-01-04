#!/usr/bin/python

def div(a,b):
    if b == 0:
        raise
    print "div test"
    return a / b

result = div(3,0)

print result
print "test over"

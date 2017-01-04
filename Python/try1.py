#!/usr/bin/python

def div(a,b):
    try:
        c =  a / b
        print "c:",c
    except (TypeError,ZeroDivisionError):
        print "zero can not be divsion or num error"
    else:
        print "else......"
    finally:
        print "finally...."
        
    return c



result = div(3,1)

print result
print "test over"

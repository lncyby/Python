#!/usr/bin/python
import traceback

def div(a,b):
    try:
        return a / b
    except (ZeroDivisionError,TypeError) as e:
#        print "zero can not be divsion"
        print e
        traceback.print_exc()
    else:
        print "else......"
    finally:
        print "finally...."




result = div(3,'c')

print result
print "test over"

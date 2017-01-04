#!/usr/bin/python

def div(a,b):
    try:
        c =  a / b
        print "c:",c
        return c
    except ZeroDivisionError:
        print "zero can not be divsion"
    except TypeError:
        print "Plaase input the right num"
    except:
        pass

result = div(3,'c')

print result
print "test over"

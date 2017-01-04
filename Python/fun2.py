#!/usr/bin/python
'''
def fun(a,b):
    print a,b
    a += 1
    b += 1
    print id(a),id(b)
    return a + b,a - b,a * b,a / b



x,y = 3,2
print id(x),id(y)
print "+++++++++++++++++++++++++++++++++++"
print fun(x,y)  #a = x  b = y

print x,y
'''
def fun(a):
    a.append(5)
    print a

l = [1,2,3,4]
a = l[:]
fun(a)
print "++++++++++++++++++++++++++++++"
print l

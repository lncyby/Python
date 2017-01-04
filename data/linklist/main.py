#!/usr/bin/python
from linklist import *

l = Linklist()

l.initlist([1,2,3,4,5])

l.show()

print l.getlength()

l.append(10)

l.show()

l.append(20)

l.show()

l.insert(2,30)
l.show()

l.delete(3)
l.show()
print l.index(30)
print l.getitem(4)
print l[4]

l[4] = 40

l.show()

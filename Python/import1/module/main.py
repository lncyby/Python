#!/usr/bin/python

import module1
import module2 as m

s = "main-->s..."

module1.b()
print m.s

m1 = module1.A()
m2 = m._C()

reload(module1)
m1.a()
m2.c()

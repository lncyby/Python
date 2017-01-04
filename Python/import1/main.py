import dir.dir1.module1
#from dir.dir1 import module2
from dir.dir1.module2 import C,d

m1 = dir.dir1.module1.A()

m1.a()

dir.dir1.module1.b()

#m2 = module2.C()
m2 = C()
m2.c()
#module2.d()
d()

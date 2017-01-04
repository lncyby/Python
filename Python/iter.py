class TestIter(object):
    def __init__(self,a):
        self.a = a

    def __iter__(self):
        return self

    def __next__(self):
        self.a += 1
        return self.a ** 2

I = TestIter(2)

#print (next(I))
#print (next(I))
#print (next(I))
#print (next(I))
print (I.__next__())
print (I.__next__())
print (I.__next__())

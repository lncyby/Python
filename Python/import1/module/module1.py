#!/usr/bin/python
print "module1...."
class A(object):
    print "module1->class A"
    def a(self):
        print "module1-->class A-->def a..."

def b():
    print "module1-->def b..."
    print "+++++++",__name__

print __name__

if __name__ == "__main__":
    print "dosomething..."

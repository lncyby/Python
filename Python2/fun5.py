def fun():
#    a = 3
#    b = 4
    global a
    a += 1
    print "in fun:",a,b
    num = 1000


a = 1
b = 2
fun()
print "out fun:",a,b
#print num

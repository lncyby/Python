#!/usr/bin/python

a = 1

def fun_out(N):
    a = 2
    def fun1(X):
        return X * N
    def fun2(X):
        return X / N

    if N != 0:
        return fun2
    else:
        return fun1

f = fun_out(0)

print f(4)

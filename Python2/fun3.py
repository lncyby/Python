#!/usr/bin/python
#coding=utf-8

#定义位置参数的函数
def fun(a,b):
    print a,b

#定义默认值传参
def fun1(a,b = 100,c = 1000):
    print a,b,c

#收集位置参数方式
def fun2(a ,*b):
    print a,b

#收集字典的方式
def fun3(a,**b):
    print a,b

def fun4(a,d = 100,*b,**c):
    print a,b,c,d

fun(1,2)
fun1(1,2)
fun2(1,2,3,4,5,6)
fun3(1,c = 2,b = 3)

fun4(1,2,3,4,5,b = 6,c = 7)

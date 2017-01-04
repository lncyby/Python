#!/usr/bin/python
#coding=utf-8

a = 5

def fun():
    global a    # 定义全局变量
    a += 1

fun()
print(a)

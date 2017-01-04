#!/usr/bin/python
#coding=utf-8
# a = input()

l = [ [1],[1,1] ]   # 定义一个列表

for i in range(2,10):      # 通过for 函数在 范围（2 ， a）中取值赋值给I
    # print l               #  输出l  在这里不需要输出。
    l.append([1,1])         # 在l 中添加一个
    for j in range(1,i):
        l[i].insert(j,(l[i-1][j-1]+l[i-1][j]))

for x in l:
    print x

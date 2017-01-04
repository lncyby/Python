#!/usr/bin/python
#coding=utf-8

for i in [1,2,3,4,5]:
    print i,

print ""
for i in (1,2,3,4,5):
    print i,
print ""

for i in {1,2,3,4,5}:
    print i,
print ""


for i in "hello":
    print i,
print ""


d =  {'a':1,'b':2,'c':3}   #变量取键
for i in d:   #变量取键
    print i,":",d[i],
print ""

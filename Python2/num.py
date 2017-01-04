#!/usr/bin/python

num = raw_input()
print type(num)

s = 0
for i in num:
    s = s * 10 + int(i)

print s
print type(s)

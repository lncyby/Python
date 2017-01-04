#!/usr/bin/python

def char(ch,s):
    n = len(s)
    i = 0
    num = 0

    while i<n:
        if s[i] == ch:
            num += 1
        i += 1
    return num
    
a = char('l','hello world')
print a

#!/usr/bin/python
#coding=utf-8

#质数

import math

flag = 1
for num in range(2,100):
	for i in range(2,int(math.sqrt(num))):
		if num % i == 0:
			flag = 0
			break
		else:
			flag = 1
	
	if flag == 1:
		print "%d"%num

#!/usr/bin/python
#coding=utf-8

def fun(l):				# 定义函数l
	l[3] = 100			# l的索引3 值为100
	print "fun:",l		# 打印函数 l

def fun1(a):			# 定义函数a
	a = 100				# a 赋值为100
	print "fun:",a		# 输出函数 a

l = [1,2,3,4,5]			# 定义列表 l

fun(l)					# 函数传参 l

print "main:",l			# 打印 l


a = 2					# a 赋值为 2

fun1(a)					# 函数传参 a

print "main:",a			# 打印 a

#!/usr/bin/python
#coding=utg-8

def func(a,b):    # 定义函数
#	a += 1
#	b += 1
	print a,b	#输出函数值 a ,b
	print id(a),id(b)  # 输出 a, b 的id 号

#func(1,2)

x,y = 5,6		# x,y 赋值
print id(x),id(y)	# 打印x , y 的id
func(x,y)		# 把x,y的值赋给a,b

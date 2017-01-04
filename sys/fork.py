#!/usr/bin/python
#coding=utf-8

import os,time  # 引用时间和操作系统模块

pid = os.fork()  # 创建进程

if pid < 0:  # os.fork()返回值小于零则创建失败
    print "create process failed"
elif pid == 0: # os.fork()返回值等于零创建成功
    print "This is child process",os.getpid() # 输出路径id
    print os.getppid()
    exit('hahahha')

else:
    time.sleep(0.1)  # 睡眠
    print os.waitpid(-1,os.WNOHANG)
    print "This is parent process",os.getpid()
    print pid
    while True:
        pass

print "+++++++++++++++++++"

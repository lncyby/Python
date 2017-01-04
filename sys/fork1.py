#!/usr/bin/python
#coding=utf-8

import os,time  # 引用时间，操作系统模块


pid = os.fork() # 创建进程

if pid < 0:  # 进程返回值 小于 0
    print "create process error"
elif pid == 0: # 进程返回值 等于 0
    pid = os.fork()

    if pid < 0:
        print "create process error"
    elif pid == 0:
        while True:
            time.sleep(1)  # 睡眠
            print "greatson do something"
    else:
        exit()
else:
    os.wait()
    while True:
        time.sleep(1)
        print "parent do something"

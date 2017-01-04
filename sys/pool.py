#!/usr/bin/python

from multiprocessing import Pool    # 管理进程
import os,time,random   # 引入操作系统，时间，random函数


def test(name):  # 定义一个函数
    print "start....."
    time.sleep(2)  # 睡眠 2 秒
    print "Task %s is run....."%name
    print "end...."



if __name__ == '__main__':
    print "parent pid : ",os.getpid()
    p = Pool(4)

    for i in range(5): # 便利取值1-5
        p.apply_async(test,args = (i,))    # i 赋值给 name

    p.close()
    p.join()

    print "All processs end"

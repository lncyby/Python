#! /usr/bin/python

#猜数游戏

import random

i = 0

while i < 4:
    print('************************************************')
    num = int(input("输入0-9任意数字:"))
    xnum = random.randint(0,9)

    x = 3 - i

    if num == xnum:
        print("猜对了！！！！")
        break
    elif num < xnum:
        print("猜小了 ，正确是%d，你还有%d次机会"%(xnum,x))
    elif num > xnum:
        print("猜大了 ，正确是%d，你还有%d次机会"%(xnum,x))

    print('************************************************')
    i += 1

#!/usr/bin/python
#coding=utf-8

#从终端输入日期判断是一年中的第几天
#日期格式2016-7-1

f_leap = 0
days = 0
DayMon = {'mon1':31,'mon2':28,'mon3':31,'mon4':30,'mon5':31,'mon6':30,'mon7':31,\
        'mon8':31,'mon9':30,'mon10':31,'mon11':30,'mon12':31}

data = raw_input("Enter as 2016-1-1>>")

data = data.split('-')

year = int(data[0])
mon = int(data[1])
day = int(data[2])

print "%d-%d-%d"%(year,mon,day)

if year < 0 or mon < 1 or mon > 12 or day < 0 or day > 31:
    print "Invalid data"
    exit()

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    f_leap = 1
    if mon == 2 and day > 29:
        print "Invalid data"
        exit()
elif mon == 2 and day > 28:
    print "Invalid data"
    exit()

if mon == 2 or mon == 4 or mon == 6 or mon == 9 or mon == 11:
    if day > 30:
        print "Invalid data"
        exit()

for i in range(1,mon):

    l = ['mon',str(i)]
    s = ''.join(l)
    days += DayMon[s]

days += day

if mon > 2:
    days += f_leap

print "days = ",days
                                        

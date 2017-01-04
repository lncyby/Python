#!/usr/bin/python
#coding=utf-8

# 创建一个类，为每次创建结点调用
class Node(object):
    def __init__(self,val,p = None):
        self.val = val
        self.next = p
        self.prior = p

class Linklist(object):
    def __init__(self):
        self.head = None    # 头结点为None

    # 初始链表
    def initlist(self,data):
        self.head = Node(0)
        p = self.head

        for i in data:
            node = Node(i)

            p.next = node
            node.prior = p
            p = p.next

        p.next = self.head
        self.head.prior = p

    def show(self):
        p = self.head.prior

        while p != self.head:
            print p.val,
            p = p.prior
        print ""

    def getlength(self):
        p = self.head
        length = 0
        while p.next != self.head:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def insert(self,index,value):
        if index < 0 or index > self.getlength():
            print "index is error"
            return

        p = self.head
        i = 0

        while p.next != self.head and i < index:
            p = p.next
            i += 1

        q = Node(value)

        q.next = p.next
        p.next.prior =  q
        p.next = q
        q.prior = p

    def delete(self,index):
        if self.is_empty() or index < 0 or index > self.getlength():
            print "index is error"
            return

        p = self.head
        i = 0

        while p.next != self.head and i < index:
            p = p.next
            i += 1

        if p.next == self.head:
            print "index is error"
        else:
            p.next = p.next.next
            p.next.prior = p

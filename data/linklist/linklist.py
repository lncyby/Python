#!/usr/bin/python

class Node(object):
    def __init__(self,val,next = None):
        self.value = val
        self.next = next


class Linklist(object):
    def __init__(self):
        self.head = None

    def __getitem__(self,key):
        if self.is_empty():
            print "linklist is empty"
            return
        else:
            return self.getitem(key)

    def __setitem__(self,key,value):
        if key < 0 or key > self.getlength():
            print "The given key is error"
            return
        else:
            self.delete(key)
            return self.insert(key,value)



    def initlist(self,data):
        self.head = Node(0)
        p = self.head

        for i in data:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):
        p = self.head
        length = 0
        while p.next != None:
            length += 1
            p = p.next
        return length

    def show(self):
        p = self.head.next

        while p != None:
            print p.value,
            p = p.next

        print ""

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = None

    def append(self,value):
        p = self.head
        while p.next != None:
            p = p.next
        p.next = Node(value)

    def insert(self,index,value):
        if index < 0 or index > self.getlength():
            print "index is error"
            return

        p = self.head

        i = 0
        while p.next != None and i < index:
            p = p.next
            i += 1

        q = Node(value)
        q.next = p.next
        p.next = q

        self.delete(index + 1)  # 调用函数delete删除坐标对应的数

    def delete(self,index):
        if self.is_empty() or index < 0 or index > self.getlength() - 1:
            print "index is error"
            return

        p = self.head
        i = 0
        while p.next != None and i < index:
            p = p.next
            i += 1

        if p.next == None:
            print "index is error"
        else:
            p.next = p.next.next

    def index(self,value):
        if self.is_empty():
            print "Linklist is empty"
            return
        p = self.head.next
        i = 0
        while p != None and not (p.value == value):
            p = p.next
            i += 1

        if p == None:
            return -1
        else:
            return i

    def getitem(self,index):
        if self.is_empty():
            print "link is empty"
            return
        i = 0
        p = self.head.next

        while p != None and i < index:
            i += 1
            p = p.next

        if p == None:
            print "target is noe exist"
        else:
            return p.value

#!/usr/bin/python

class Node(object):
    def __init__(self,val,next = None):
        self.value = val
        self.next = next


class Linklist(object):
    def __init__(self):
        self.head = None

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
        pass

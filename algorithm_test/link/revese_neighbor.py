'''
把链表相邻元素翻转，给定链表 1->2->3->4->5->6->7
翻转后链表变为 2 1 4 3 6 5 7
就地逆序
'''

class LNode():
    def __init__(self,x=None):
        self.data = x
        self.next = None

def reverseNear(head):
    cur = head.next
    pre = head
    next = None
    while cur != None and cur.next != None:
        next = cur.next.next#next这个时候就会指向3
        pre.next = cur.next
        cur.next.next = cur# 2指向1
        cur.next = next#1就会指向3
        pre = cur  #pre向前移动
        cur = next # cur向前移动

if __name__ == '__main__':
    i = 1
    head = LNode('head')
    tmp = None
    cur = LNode(i)
    head.next = cur
    while i < 7:
        i += 1
        tmp = LNode(i)
        cur.next = tmp
        cur = cur.next
    print('正序：')
    cur = head.next
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next
    print()
    print('相邻翻转：')
    reverseNear(head)
    cur = head.next
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next








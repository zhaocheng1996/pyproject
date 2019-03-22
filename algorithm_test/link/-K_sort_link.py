'''
找出单链表中的倒数第K个元素，例如给定单链表：1>2>3>4>5>6>7，则单链表的倒数第k=3个元素为5
顺序遍历一遍单链表，求出整个单链表的长度n，然后吧求倒数第k个元素转换为求顺数第n-k个元素，再去遍历一次单链表就可以得到结果。
方法二：快慢指针法
查找过程中，设置两个指针，让其中一个指针比另一个指针先移动k步，然后两个指针同时前移。直到先走的指针值为None时，另一个指针的位置就是要找的位置
注意：有头节点
'''

import random
class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createlink():
    i = 1
    head = LNode(None)
    tmp = None
    cur = head
    while i <= 6:
        #n = random.randint(0,6)
        tmp = LNode(i)
        cur.next = tmp
        cur = tmp#如果没有这个赋值就没法调整当前结点的位置了
        i += 1
    return head

def FindlastK(head,k):
    if head==None or head.next==None:
        return head
    # slow = LNode()
    # fast = LNode()
    slow = head.next
    fast = head.next
    i = 0
    while i<k and fast != None:
        fast = fast.next
        i += 1
    if i<k:
        return None
    while fast!=None:
        slow = slow.next
        fast = fast.next
    return slow.data

def PrintList(head):
    cur = head.next
    cur = head.next
    print('初试链表：')
    while cur != None:
       print(cur.data)
       cur = cur.next

head = createlink()
PrintList(head)
result = None
result = FindlastK(head,3)
if result != None:
    print(result)





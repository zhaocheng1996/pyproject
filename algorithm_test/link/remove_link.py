'''给定一个没有排序的链表，去掉其重复项，保留原顺序
思想，两层循环，外层循环，然后内层循环去找剩下的元素，一样的就删掉
'''
#创建一个随机的无序链表
import random
class LNode(object):
    def __init__(self,arg):
         self.data = arg
         self.next = None

def createlink(x):
    i = 1
    head = LNode(None)
    tmp = None
    cur = head
    while i <= x:
        n = random.randint(0,6)
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp#如果没有这个赋值就没法调整当前结点的位置了
        i += 1
    return head

def remove(head):
    '''有头节点'''
    if head.next is None or head is None:
        return head
    outCur = head.next# 外层的遍历
    innerCur = None #内层的当前结点
    innerPre = None #内层结点的当前结点的前驱结点
    while outCur is not None:
        # inner指向当前节点的后后继节点 用于遍历
        innerCur = outCur.next
        # 用来保存当前节点的前驱节点
        innerPre = outCur
        # 这里开始内部遍历，直到链表为空
        while innerCur is not None:
           if innerCur.data == outCur.data:
               #删除结点
                innerPre.next = innerCur.next
                innerCur = innerCur.next
           else:
               #继续遍历下一个结点
               innerPre = innerCur
               innerCur = innerCur.next
        #外层一个结点遍历结束后，下一个结点
        outCur = outCur.next
    return head

head = createlink(6)
cur = head.next
print('删除之前：')
while cur != None:
    print(cur.data)
    cur = cur.next

head = remove(head)
print('删除之后：')
cur = head.next
while cur != None:
    print(cur.data)
    cur = cur.next



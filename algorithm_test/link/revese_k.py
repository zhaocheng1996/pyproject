'''
K链表翻转
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
'''

class LNode():
    def __init__(self,x):
        self.data = x
        self.next = None

def reverse(head):
    if head == None or head.next == None:
        return
    pre = None  # 前驱节点
    cur = None  # 当前节点
    next = None  # 后继节点
    # 把链表首节点变为尾节点
    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next
    # 使当前遍历到的节点cur指向其前驱节点
    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
        cur = next
    cur.next = pre
    head.next = cur

    
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
    print('翻转：')
    reverse(head)
    cur = head.next
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next





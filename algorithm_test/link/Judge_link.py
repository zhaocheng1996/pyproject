'''
判断两个单链表是否交叉
交叉的意思是两个单链表存在完全重合的部分
1.hash法，先遍历head1，然后把结点的地址存下来，接着遍历head2，看里面的地址有没有一样的
2.首尾相接法。把两个链表首尾相接，看是否有环，环入口就是相交的结点
3.尾结点法。如果有交点，则两个单链表一点有相同的结尾，依次遍历两个链表，记录下长度n1，n2，长的先走n1-n2步，然后两个同时每步走1，相遇的第一点就是交点
'''

class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None


def Isintersect(head1,head2):
    cur1 = head1.next
    cur2 = head2.next
    n1,n2 = 0,0
    while cur1.next != None:
        cur1 = cur1.next
        n1 += 1
    while cur2.next != None:
        cur2 = cur2.next
        n1 += 1
    if cur1 == cur2:
        #长链表先走n1-n2步
        if n1 > n2:
            while n1 - n2>0:
                haed1 = head1.next
                n1 -= 1
        if n2 > n1:
            while n2 - n1>0:
                head2 = head2.next
                n2 -= 1
         #两个结点同时前进，找到相同结点
        while head1 != head2:
            head1 = head1.next
            head2 = head2.next
        return head1
    else:
        return None

if __name__ == '__main__':
    i = 1
    head1 = LNode(None)
    head1.next = None
    head2 = LNode(None)
    head2.next = None
    tmp = None
    cur = head1
    p = None
    while i<8:
        tmp = LNode(None)
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        if(i==5):
            p = tmp
        i += 1
    cur = head2
    i=1
    while i<5:
        tmp = LNode(None)
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
        #使它们相交于结点5
        cur.next = p
        interNode = Isintersect(head1,head2)
        if interNode==None:
            print('不相交')
        else:
            print('相交点为：'+str(interNode.data))











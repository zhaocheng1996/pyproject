'''检测一个较大的单链表是否有环
采用快慢指针：两个指向头节点的指针，fast和slow，一起从头结点开始往后遍历，fast每次移动两个节点，slow每次移动一个节点，
这样，如果存在环结构，那么fast指针在不断绕环过程中，肯定会追上slow指针。
然后环的入口点就是把快指针返回head，和慢指针在一起移动，再相遇的时候就是入环点
'''
class LNode():
    def __init__(self,x=None):
        self.data = x
        self.next = None

def findloop(head):
    fast = head
    slow = head
    loopexit = False
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast.data == slow.data:
            loopexit = True
            print(loopexit)
            break
    if loopexit == True:
        fast = head
        while fast.data != slow.data:
            fast = fast.next
            slow = slow.next
        print(slow.data)


node1 = LNode(1)
node2 = LNode(2)
node3 = LNode(3)
node4 = LNode(4)
node5 = LNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2
findloop(node1)










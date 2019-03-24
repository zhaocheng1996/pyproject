'''
实现一个算法来删除单链表中间的一个结点，只给出指向那个结点的指针。
例子：
输入：指向链表a->b->c->d->e中结点c的指针
结果：不需要返回什么，得到一个新链表：a->b->d->e

如果这个结点不是链表的最后一个结点，可以通过把其后继结点的数据复制到当前结点仲，然后删除后继结点的方法来实现
'''

class LNode:
    def __init__(self,x=None):
        self.data = x
        self.next = None

def printNode(head):
    cur = head
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next

def remove(p):
    if p == None or p.next == p:
        return False
    p.data = p.next.data
    tmp = p.next
    p.next = tmp.next
    return True

def getNewChart(list):
    if list:
        node = LNode(list.pop(0))
        node.next = getNewChart(list)
        return node

if __name__ == '__main__':
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    p = None
    while i<8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        if i==5:
            p = tmp
        i += 1
        print('删除结点'+str(p.data)+'前链表:'),
        printNode(head)
        result = remove(p)
        if result:
            print('删除后的是')
            printNode(head)






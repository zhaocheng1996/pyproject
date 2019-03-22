'''
给定两个单链表，链表的每个结点代表一位数，计算两个数的和。例如链表3-1-5，链表5-9-2，输出8-0-8
链表相加法：对结点中的值直接相加
给定两个单链表，链表的每个结点代表一位数，计算两个数的和。例如：输入链表（3->1->5）和链表（5->9->2)，输出：8->0->8,即513+295=808，注意个位数在链表头。
'''

"""链表"""


# 定义链表的结点
class LNode():
    def __init__(self):
        self.data = None  # 数据域
        self.next = None  # 指针域


# 链表相加
def addLink(head1, head2):
    # 判断链表是否为空
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    c = 0  # 用来记录进位
    sums = 0  # 用来记录两个结点相加的值
    p1 = head1.next  # 用来遍历h1
    p2 = head2.next  # 用来遍历h2
    resultHead = LNode()
    p = resultHead
    # 两链表进行相加
    while p1 is not None and p2 is not None:
        tmp = LNode()
        sums = p1.data + p2.data + c
        tmp.data = sums % 10  # 两结点相加的和
        c = sums // 10  # 进位
        p.next = tmp
        p = tmp
        p1 = p1.next
        p2 = p2.next
    if p1 is None:
        while p2 is not None:
            tmp = LNode()
            sums = p2.data + c
            tmp.data = sums % 10
            c = sums // 10
            p.next = tmp
            p = tmp
            p2 = p2.next
    #如果一个表长一个表短
    if p2 is None:
        while p1 is not None:
            tmp = LNode()
            sums = p1.data + c
            tmp.data = sums % 10
            c = sums // 10  # 取整
            p.next = tmp
            p = tmp
            p1 = p1.next
    # 如果计算完成后还有进位，则增加新的结点
    if c == 1:
        tmp = LNode
        tmp.data = c
        p.next = tmp
    return resultHead


if __name__ == "__main__":
    i = 1
    head1 = LNode()
    head2 = LNode()
    cur = head1
    # 构造第一个链表
    while i < 7:
        tmp = LNode()
        tmp.data = i + 2
        cur.next = tmp
        cur = tmp
        i += 1
    # 构造第二个链表
    cur = head2
    i = 9
    while i > 4:
        tmp = LNode()
        tmp.data = i
        cur.next = tmp
        cur = tmp
        i -= 1
    print("\nHead1:")
    cur = head1.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    print("\nHead2:")
    cur = head2.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
    # 相加后
    print("\n相加后：")
    cur = addLink(head1, head2)
    cur = cur.next
    while cur is not None:
        print(cur.data)
        cur = cur.next

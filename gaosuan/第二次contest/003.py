'''
链表区间逆序
Description
将单个链表的每K个节点之间逆序，打印出新链表；最后不足K的节点数不需要逆序；要求时间复杂度为O(n)，额外空间复杂度为O(1)。
Input
输入的每一行的值用空格隔开，第一个表示链表长度，中间为节点值，最后代表K。
Output
输出的每一行为新的链表，节点值用空格隔开，末尾不要空格。
Sample Input 1
8 1 2 3 4 5 6 7 8 3
8 a b c d e f g h 4
Sample Output 1
3 2 1 6 5 4 7 8
d c b a h g f e
'''

def test(a):
    b=a[2:-2].split()
    #print(b)
    K=int(a[-1])
    #print(K)
    number=int(a[0])
    #print(number)
    div=number//K
    for i in range(1,div+1):
       b[K*(i-1):K*i] = list(reversed(b[K*(i-1):K*i]))
    #print(b)
    print(" ".join(str(i) for i in b))
try:
    while True:
        a=input()
        test(a)
except EOFError:
    pass



# def reverseKNode2(head, k):
#     def reverse2(head, left, right):
#         pre = None
#         start = head
#         while head != right:
#             next = head.next
#             head.next = pre
#             pre = head
#             head = next
#         if left != None:
#             left.next = pre
#         start.next = right
#
#     if head == None or head.next() == None or k < 2:
#         return head
#     pre = None
#     cur = head
#     count = 0
#     while cur != None:
#         count += 1
#         next = cur.next
#         if count == k:
#             start = head if pre == None else pre.next
#             head = cur if pre == None else head
#             reverse2(start, pre, next)
#             pre = start
#             count = 0
#         cur = next
#     return head
#
# print(reverseKNode2(b,K))


'''
合并两个有序链表，合并完成后依然有序
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
思路：初始化两个链表头，其中一个表头用以记录两个单调递增链表比较后的结果，另一个用以返回结果。
用while循环：
①如果两个链表不为空，比较进行，并将小的那个赋给合并的链表头。小表头继续走一步，合并表头继续走一步。
②如果两个链表有其一为空，那么跳出循环，并将另一不为null的链表的后续部分赋给合并链表。
'''

class Solution:
    #非递归
    def Merge1(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        mainHead = pHead1 if pHead1.val <= pHead2.val else pHead2 #0 1 4
        secHead = pHead2 if mainHead == pHead1 else pHead1 # 1 3 5
        mergeHead = mainHead
        mainNext = mainHead.next# 这时候的maonNext已经是 1到4后面的
        while mainNext and secHead:
            if secHead.val <= mainNext.val:
                mainHead.next = secHead
                secHead = secHead.next
                mainHead.next.next = mainNext
                mainHead = mainHead.next
            else:
                mainHead = mainNext
                mainNext = mainNext.next
        if not mainNext:
            mainHead.next = secHead
        return mergeHead

    #递归
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return  pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2

    def getNewChart(self, list):
        if list:
            node = ListNode(list.pop(0))
            node.next = self.getNewChart(list)
            return node

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    list1 = [1, 3, 5]
    list2 = [0, 1, 4]
    testList1 = Solution().getNewChart(list1)
    testList2 = Solution().getNewChart(list2)
    final = Solution().Merge1(testList1, testList2)
    while final:
        print(final.val, end=" ")
        final = final.next






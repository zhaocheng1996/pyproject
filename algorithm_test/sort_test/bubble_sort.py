'''
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成
时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：稳定
'''

def bubble_sort(ilist):
    for i in range(len(ilist)):
        for j in range(i,len(ilist)):
            if ilist[i]>ilist[j]:
                ilist[i],ilist[j] = ilist[j],ilist[i]
    return ilist

blist = bubble_sort([4,5,6,7,3,2,6,9,8])
print(blist)






'''
插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，
算法适用于少量数据的排序；首先将第一个作为已经排好序的，然后每次从后的取出插入到前面并排序；
时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：稳定
'''

def insert_sort(ilist):
    for i in range(len(ilist)):
        for j in range(i):
            if ilist[i]<ilist[j]:
                ilist.insert(j,ilist.pop(i))
                break
    return ilist
list = insert_sort([4,5,6,7,3,2,6,9,8])
print(list)

'''
希尔排序：希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止
时间复杂度：O(n)
空间复杂度：O(n√n)
稳定性：不稳定
'''

def shell_sort(ilist):
    gap = len(ilist)
    while gap>1:
        gap = gap//2
        for i in range(gap,len(ilist)):
            for j in range(i%gap,i,gap):
                if ilist[i]<ilist[j]:
                    ilist[i],ilist[j] = ilist[j],ilist[i]
    return ilist


slist = shell_sort([4,5,6,7,3,2,6,9,8])
print(slist)




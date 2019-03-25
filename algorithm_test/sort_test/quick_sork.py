'''
快速排序：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列
时间复杂度：O(nlog₂n)
空间复杂度：O(nlog₂n)
稳定性：不稳定
'''

def quick_sort(ilist):
    if ilist == []:
       return []
    else:
        ifirst = ilist[0]
        iless = quick_sort([l for l in ilist[1:] if l<ifirst])
        imore = quick_sort([m for m in ilist[1:] if m>=ifirst])
        return iless + [ifirst] + imore

ilist = quick_sort([4,5,6,7,3,2,6,9,8])
print(ilist)




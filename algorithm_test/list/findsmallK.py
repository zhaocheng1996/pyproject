'''
找出数组中第k个大的数字
例如数组为[4,0,1,0,2,3],那么第3大的元素是2

解题思路：首先了解快排思想，即每次可以将一个元素放到最终位置上，
快速排序每次把一个元素交换到正确的位置，同时把左边的都放上大的，右边都放上小的。
这个算法每一次选取一个枢纽元，排序之后，查看枢纽元的位置。
如果它的位置大于K，就说明，要求出前面一个子序列的第K大的元素。
反之，如果小于K，就说明要求出在后面一个序列的第K - 前一个序列的长度个元素。
'''

# def quick_sork(array):
#     if array == []:
#         return [];
#     else:
#         ifirst = array[0]
#         array_l = quick_sork([l for l in array[1:] if l<ifirst])
#         print('array_l', array_l)
#         array_r = quick_sork([r for r in array[1:] if r>=ifirst])
#         index=len(array_l)
#         print(index)
#     return array_l+[ifirst]+array_r
#

def quicksort(num, low, high):  # 快速排序
    if low < high:
        location = partition(num, low, high)
        quicksort(num, low, location - 1)
        quicksort(num, location + 1, high)

#这个函数返回的是一次快速排序枢纽元的下标
def partition(num, low, high):
    pivot = num[low]
    while (low < high):
        while (low < high and num[high] > pivot):
            high -= 1
        while (low < high and num[low] < pivot):
            low += 1
        num[low],num[high] = num[high],num[low]
    num[low] = pivot
    return low

def findkth(num, low, high, k):  # 找到数组里第k个数
    index = partition(num, low, high)
    if index == k: return num[index]
    if index < k:
        return findkth(num, index + 1, high, k)
    else:
        return findkth(num, low, index - 1, k)


qlist = [2, 3, 1, 5, 4, 6]
# quicksort(pai, 0, len(pai) - 1)
print(findkth(qlist, 0, len(qlist) - 1, 3))









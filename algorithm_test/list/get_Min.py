'''
题目： 把一个数组最开始的若干个元素搬到数组的末尾，
我们称之数组的旋转。输入一个递增排序的数组的一个旋转，
输出旋转数组的最小元素。例如数组3，4, 5, 1, 2
为1,2,3, 4，5的一个旋转，该数组的最小值为 1
思路：使用二分查找
1、设置一个首部指针low,一个尾部指针high，以及一个最小值初始值minVal
2、求出中间坐标middle，若a[low]小于a[middle]，把low移到中间，
否则将high移到中间(因为这样中间某个部分就会有个降序)
3、循环2，直到 high-low = 1，则最小值为a[high]
特殊情况：当数组为空时返回0，当数组有大量重复时，使用for循环普通方法找最小值
'''

def get_min(list):
    high = len(list)-1
    low = 0
    mid = (low+high)/2
    if high == 0:
        return 0
    minvalue = list[low]
    while high-low > 1:
        mid = (low + high) // 2
        if list[low]<=list[mid]:
            low = mid
        elif list[low]>=list[mid]:
            high = mid
#        elif list[mid] == list[low]:
#             for i in range(1, len(list)):
#                 if list[i] < minVal:
#                     minVal = list[i]
#                     high = i
    minvalue = list[high]
    return minvalue

list = [5,1,2,3,4]
print(get_min(list))
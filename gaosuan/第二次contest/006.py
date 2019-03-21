'''
计数排序
Description
实现计数排序，通过多次遍历数组，统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。
Input
输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
Output
输出的每一行为排序结果，用空格隔开，末尾不要空格。
Sample Input 1
13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1
 3 3 9 12 24 29 34 49 51 56 78 84 100
'''

# def su_counting_algorithm(A, B, k):
#     C = list(range(k + 1))
#     for i in range(0, k + 1):
#         C[i] = 0
#     for j in range(0, len(A)):
#         C[A[j]] = C[A[j]] + 1
#     for i in range(1, k + 1):
#         C[i] = C[i] + C[i - 1]
#     for j in reversed(range(0, len(A))):
#         B[C[A[j]] - 1] = A[j]
#         C[A[j]] = C[A[j]] - 1
#     return B
#
#
# A = [2, 5, 3, 0, 2, 3, 0, 3]
# B = range(len(A))
# print(A)
# print(su_counting_algorithm(A, B, 5))
def counting_sort(collection):
    """
    计数排序
    算法思想：
    假设要排序的数组为 A = {1,0,3,1,0,1,1}这里最大值为3，最小值为0，
    那么我们创建一个数组C，长度为3+1-0=4。然后一趟扫描数组A，得到A中各个元素的总数，
    并保持到数组C的对应单元中。比如0 的出现次数为2次，则 C[0] = 2;1 的出现次
    数为4次，则C[1] = 4。C=[2,4,0,1]由于C 是以A的元素为下标的，所以这样一做，A中的元素在C
    中自然就成为有序的了,然后我们分别统计比0,1,3小的元素个数，如比1小（包括1）的元素有6个。更新
    C,C=[2,6,0,7]，更新C是为了保证排序稳定。然后把这个在C中的记录按每个元素的计数展开到输出数组B中，
    排序就完成了。 也就是B[0] 到 B[1] 为0, B[2] 到 B[5] 为1 这样依此类推。
    Examples:
    >>> counting_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # 输入为空，就返回空列表
    if collection == []:
        return []


    coll_len = len(collection)
    coll_max = max(collection)#返回最大值
    coll_min = min(collection)#返回最小值

    #计算待排序列表的元素数值区域长度，如4-9共9+1-4=6个数
    counting_arr_length = coll_max + 1 - coll_min
    counting_arr = [0] * counting_arr_length  #构造一个全为0列表


    for number in collection:
        counting_arr[number - coll_min] += 1  #统计列表中每个值出现的次数，


    #使counting_arr[i]存放<=i的元素个数，就是待排序列表中比某个值小的元素有多少个
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i-1]


    ordered = [0] * coll_len   #存放排序结果


    #使每个元素被放在ordered中正确的位置，升序
    for i in reversed(range(0, coll_len)): #reversed表示从下标最大的位置到0，为了使排序稳定
        ordered[counting_arr[collection[i] - coll_min]-1] = collection[i]#-1是因为下标从0开始的
        counting_arr[collection[i] - coll_min] -= 1 #每归位一个元素，就少一个元素

    return ordered


A = [24,3,56,34,3,78,12,29,49,84,51,9,100]
print(A)
A = counting_sort(A)
print(A)

try:
    while True:
        string = input().split()
        str1 = string[1:]
        str1_int = list(map(int, str1))
        #print(str1_int)
        str1_int=counting_sort(str1_int)
        #print(str1_int)
        print(" ".join(str(i) for i in str1_int))
except EOFError:
    pass



'''
非递归快排
Description
快速排序的核心思想是使用元素的值对数组进行划分。实现其非递归方案。
Input
输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
Output
输出的每一行为排序结果，用空格隔开，末尾不要空格。
Sample Input 1
 13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1
 3 3 9 12 24 29 34 49 51 56 78 84 100
'''

def quick_sort(arr):
    '''''
    模拟栈操作实现非递归的快速排序
    '''
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr)-1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)


def partition(arr, start, end):
    # 分区操作，返回基准线下标
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    # 此时start = end
    arr[start] = pivot
    return start

try:
    while True:
        string = input().split()
        str1 = string[1:]
        str1_int = list(map(int, str1))
        #print(str1_int)
        quick_sort(str1_int)
        print(" ".join(str(i) for i in str1_int))
except EOFError:
    pass








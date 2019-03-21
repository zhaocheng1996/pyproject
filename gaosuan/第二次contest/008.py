'''
非递归合并排序
Description
合并（归并）排序的核心思想是：每次从中间位置将数组分组再分别排序。请实现其非递归方案。
Input
输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
Output
输出的每一行为排序结果，用空格隔开，末尾不要空格。
Sample Input 1
13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1
3 3 9 12 24 29 34 49 51 56 78 84 100
'''

def merge(seq,low,mid,height):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    # 通过low,mid height 将[low:mid) [mid:height)提取出来
    left = seq[low:mid]
    right = seq[mid:height]
    #print('left:', left, 'right:', right)

    k = 0   #left的下标
    j = 0   #right的下标
    result = [] #保存本次排序好的内容
    #将最小的元素依次添加到result数组中
    while k < len(left) and j < len(right):
        if left[k] <= right[j]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[j])
            j += 1
    #将对比完后剩余的数组内容 添加到已排序好数组中
    result += left[k:]
    result += right[j:]
    #将原始数组中[low:height)区间 替换为已经排序好的数组
    seq[low:height] = result
    return seq

try:
    while True:
        string = input().split()
        str1 = string[1:]
        str1_int = list(map(int, str1))
        i = 1
        while i < len(str1_int):
            low = 0
            while low < len(str1_int):
                mid = low + i
                height = min(low + 2 * i, len(str1_int))
                if mid < height:
                    result=merge(str1_int, low, mid, height)
                low += 2 * i
            i *= 2
        print(" ".join(str(i) for i in result))
except EOFError:
    pass



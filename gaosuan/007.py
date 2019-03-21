
# 先升后降
# Description
# 从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的。
# Input输入时一个数组，数值通过空格隔开。
# Output输出筛选之后的数组，用空格隔开。如果有多种解雇哦，则一行一种结果。
#sample input 1 2 4 7 11 10 9 15 3 5 8 6  output 1 2 4 7 11 10 9 8 6


def maxseqRemoveNum(array):
    b = [1] * len(array)
    prevb = [-1] * len(array)

    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] < array[i] and b[i] < b[j] + 1:
                b[i] = b[j] + 1
                prevb[i] = j


    c = [1] * len(array)
    prevc = [-1] * len(array)
    for i in range(len(array) - 2, -1, -1):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[i] and c[i] < c[j] + 1:
                c[i] = c[j] + 1
                prevc[i] = j


    maxv = 0
    point = 0
    for i in range(len(array)):
        if b[i] + c[i] > maxv:
            maxv = b[i] + c[i]
            point = i


    result = []
    ppoint = point

    while (prevb[point] != -1):
        result.append(array[point])
        point = prevb[point]
    result.append(array[point])
    result.reverse()
    result.remove(array[ppoint])

    while prevc[ppoint] != -1:
        result.append(array[ppoint])
        ppoint = prevc[ppoint]
    result.append(array[ppoint])
    return result
if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    result = maxseqRemoveNum(arr)
    for i in result:
        print(i, end=' ')











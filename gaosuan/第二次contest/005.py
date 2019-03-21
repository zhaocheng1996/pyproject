'''
冒泡排序
Description
实现冒泡排序。
Input
输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
Output
输出的每一行为排序结果，用空格隔开，末尾不要空格。
Sample Input 1
13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1
 3 3 9 12 24 29 34 49 51 56 78 84 100
'''
def BubbleSort(numList):
    if not len(numList):
        return
    for i in range(len(numList)):
        for j in range(len(numList)-1):
            if numList[i] < numList[j]:
                numList[i], numList[j] = numList[j], numList[i]
    return numList

try:
    while True:
        string = input().split()
        str1 = string[1:]
        str1_int = list(map(int, str1))
        #print(str1_int)
        BubbleSort(str1_int)
        #print(str1_int)
        print(" ".join(str(i) for i in str1_int))
except EOFError:
    pass


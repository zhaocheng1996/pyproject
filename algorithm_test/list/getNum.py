'''
给定一个由n-1个整数组成的未排序的数组序列，其元素都是1到n中的不同的整数
请写出一个寻找数组序列中缺失整数的线性时间算法

第一种：数学法，把1到n的值算出来，然后减去这个序列
第二种：异或法
'''

def getNum1(list):
    n = len(list)+1
    sumn = 0
    for i in range(n+1):
        sumn += i
    res = sumn-sum(list)
    return res

list = [2,1,4,5]
print(getNum1(list))



'''
求集合的所有子集
根据数学性质分析，不难得知，子集个数 Sn 与原集合元素个数 n 之间的关系满足如下等 式： S
n=2^n一1。
'''

#迭代法
#每次迭代，都是上一次迭代的结果＋上次迭代结果中每个元素都加上当前迭代的元素
#＋当前迭代的元素

def getAllSubset(str):
    arr = []
    arr.append(str[0:1])
    i = 1
    while i<len(str):
        lens = len(arr)
        j = 0
        while j<lens:
            arr.append(arr[j]+str[i])#每个元素都加上当前迭代的元素
            j+=1
        arr.append(str[i:i+1])#加当前迭代的元素
        i+=1
    return arr

res = getAllSubset("abc")
print(res)#['a', 'ab', 'b', 'ac', 'abc', 'bc', 'c']
i = 0
while i<len(res):
    print(res[i])
    i+=1



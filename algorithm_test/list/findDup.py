'''
1-1000放在含有1001个元素的数组中，只有唯一的一个元素值重复，
其它均只出现一次．每个数组元素只能访问一次，
设计一个算法，将它找出来；不用辅助存储空间，

'''
#将1001个元素相加减去1，2，3....1000数列的和，得到的差就是重复的元素
def findDup1(array):
    lens = len(array)
    sum = 0
    for item in array:
        sum+=item
    count=0
    for i in range(lens):
        count+=i
    res=sum-count
    return res
array=[1,2,3,3,4,5]
print(findDup1(array))#3

#Hash法
#将字典中的key值都初始化为0，将原数组的元素逐一映射到该字典的key中，当对应的key中的value值为0时
#则置该key的value的值为1，当对应1的key的value的值为1时，则表明该位置在原来的数组中是重复的
def findDup2(array):
    # hashtable = {k:0 for k in array }
    # return hashtable
    lens = len(array)
    hashtable = dict()
    i=0
    while i<lens:
        hashtable[i]=0
        i+=1
    j=0
    while j<lens:
        if hashtable[array[j]]==0:
             hashtable[array[j]]=1
        else:
            return array[j]
        j+=1
array=[2,1,5,4,3,1]
print(findDup2(array))

#异或法，相同元素异或时，其运算结果为0，当相异元素异或时候，运算结果为非0
# 当任何数和0异或时，结果为该数
# 以数组(1,3,4,2,5,3)为例，(1^3^4^2^5^3)^(1^2^3^4^5)=(^1^1)^(2^2)^(3^3^3)^(4^4)^(5^5)=0^0^3^0^0
# def findDup3(array):
#     lens = len(array)
#     i=0
#     res=0
#     while i<lens:
#         res^= array[i]
#         i+=1
#     # return res
#     j=1
#     while j<lens:
#         res^=j
#         j+=1
#     return res
# array=[1,2,3,3,4,5]
# print(findDup3(array))




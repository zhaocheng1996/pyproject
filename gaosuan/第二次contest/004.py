'''
插入排序
Description
实现插入排序。
Input
输入的每一行代表一个数组，其中的值用空格隔开，第一个值表示数组的长度。
Output
输出排序的数组，用空格隔开，末尾不要空格。
Sample Input 1
13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1
3 3 9 12 24 29 34 49 51 56 78 84 100
'''

def inertsort(l):  #参数的传入，当想传入的是一个list时，直接传入一个变量就行了
    N=len(l)
    for x in range(1,N):
        a,b=x,x
        n=l[x]
        while n<l[a-1] and a-1>=0:
            a=a-1
            if a-1<0:
                a=0
        while b>a:
            l[b]=l[b-1]
            b=b-1
        l[a]=n

# l=[1,3,2,8,5,3,1]
# inertsort(l)
# print (l)

try:
    while True:
        string = input().split()
        str1 = string[1:]
        str1_int = list(map(int, str1))
        #print(str1_int)
        inertsort(str1_int)
        #print(str1_int)
        print(" ".join(str(i) for i in str1_int))
except EOFError:
    pass

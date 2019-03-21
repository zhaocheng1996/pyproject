'''
数组查询
Description
Given an array, the task is to complete the function which finds the maximum sum subarray, where you may remove atmost one element to get the maximum sum.
给定一个数组，任务是完成找到最大和子数组的函数，在那里你可以删除最多一个元素以获得最大总和。
Input
第一行为测试用例个数T；后面每两行表示一个用例，第一行为用例中数组长度N，第二行为数组具体内容。
Output
每一行表示对应用例的结果。
Sample Input 1
 1
5
1 2 3 -4 5
Sample Output 1
11
'''
# a=[1,2,3,-4,5]
# b=a[:0]
# c=a[1:]
# print(c)#[2,3,-4,5]
# print(b)#[]
# b=[]
# c=[]
# def f(a,n):
#     sum1 = []
#     for i in range(n):
#         b = a[:i]
#         c = a[i+1:]
#         result = sum(a[:i]) + sum(a[i+1:])
#         sum1.append(result)
#     print(max(sum1))
#
# a = [-2,-3,4,-1,-2,1,5,-3]
# f(a,len(a))

def maxSumSubarray(arr, n):
    sum = []
    temp_sum = 0
    for i in range(0, n):
        temp_sum = 0
        for j in range(0, n - i):
            temp_sum += arr[i+j]
            sum.append(temp_sum)

            if j > 1:
                for k in range(1, j):
                    temp_mis_sum = temp_sum - arr[i+j-k]
                    sum.append(temp_mis_sum)
    return max(sum)

T = int(input())
while T >0:
    T-= 1
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    print(maxSumSubarray(a,n))








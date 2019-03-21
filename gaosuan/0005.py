#子矩阵取值范围
#给定数组arr和整数num，求arr的子数组中满足：其最大值减去最小值的结果大于num的个数。
#input 输入的第一行为数组，每一个数用空格隔开，第二行为num
#sample input：3 6 4 3 2    2  output 6


# arr = [3,6,4,3,2]
# num  = 2
count = 0
arr = input()
arr_split = arr.split()
arr_split_int = list(map(int,arr_split))
num = int(input())

#import numpy as np
# arr = np.array(arr)
# print(arr.max())
# print(arr.min())

arr1 = []
count = 0
for i in range(len(arr_split_int)):
    for j in range(i+1,len(arr_split_int)):
        arr1 = arr_split_int[i:j+1]
        #arr1.append(arr[j])
        #print(arr1)
        #arr1 = np.array(arr1)
        if(max(arr1)-min(arr1)>num):
            count+=1
print(count)






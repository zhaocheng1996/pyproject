import numpy as np
arr = np.random.randint(20)#大于0小于20的随机整数
#print('arr20',arr)

arr2 = np.random.randint(2,20)#2到20之间
#print(arr2)

two_d_arr = np.array([[10,20,30], [40,50,60], [70,80,90]])
print('two_d_arr:',two_d_arr)
print(two_d_arr[1][2]) #The value 60 appears is in row index 1, and column index 2

print('two_d_arr[:1, :2]',two_d_arr[:1, :2])#[[10 20]]
print('two_d_arr[:2, 1:]',two_d_arr[:2, 1:])#第一个维度取前两个，第二个维度取后两个
#[[20, 30], [50, 60]]
#抓取任意一行或者一列
print('two_d_arr[0]:',two_d_arr[0])
print('two_d_arr[:2]',two_d_arr[:2])#This grabs everything before row 2 ([[10, 20, 30], [40, 50, 60]])



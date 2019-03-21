# 找到指定数组的给定区间的倒数第K小的数值
# 输入的第一行为数组，每个数用空格隔开；第二行是区间(第几个数到第几个数，两头均包含)，
# 两个值用用空格隔开；第三行为K值
#
# Sample Input 1 2 3 4 5 6 7
# 3 5
# 2
#
# Sample Output 4

arr = input()
print(arr)#arr是str
#arr = "1 2 3 4 5 6 7"
arr_split = arr.split()
arr_split_int = list(map(int,arr_split))
print(arr_split_int)
# min = 3
# max = 5
min_max = input()
min_max = min_max.split()
min = min_max[0]
max = min_max[1]
min = int(min)
max = int(max)
arr_choose = arr_split_int[min-1:max]
print(min,max)
#print(arr_choose)

k=input()
k = int(k)
arr_choose.sort()
print(arr_choose)
min = arr_choose[k-1]
print(min)


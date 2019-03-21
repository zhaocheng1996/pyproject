
# 输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字，统计这样两个数的对数。
# Input
# 输入第一行是数组，每一个数用空格隔开；第二行是数字和。
# Output输出这样两个数有几对
# inpput
# 1 2 4 7 11 0 9 15
# 11
# out
# 3

arr = input()
#arr = "1 2 4 7 11 0 9 15"
arr_split = arr.split()
arr_split_int = list(map(int,arr_split))
arr_split_int.sort()

sum = input()
sum = int(sum)
count=0
low = 0
heigh = len(arr_split_int)-1 #7

while low<heigh:
    if(arr_split_int[low] + arr_split_int[heigh] == sum):
        num1 = arr_split_int[low]
        num2 = arr_split_int[heigh]
        count+=1
        heigh-=1
        low+=1
    elif(arr_split_int[low] + arr_split_int[heigh] > sum):
        heigh=heigh-1
    else:
        low=low+1

print(count)

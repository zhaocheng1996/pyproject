# Python program for The painter's
# partition problem function to
# calculate sum between two indices
# in array
def sum(arr, frm, to):
    total = 0;
    for i in range(frm, to + 1):
        total += arr[i]
    return total


# for n boards and k partitions
def partition(arr, n, k):
    # base cases
    if k == 1:  # one partition
        return sum(arr, 0, n - 1)
    if n == 1:  # one board
        return arr[0]
    best = 100000000

    # find minimum of all possible
    # maximum k-1 partitions to
    # the left of arr[i], with i
    # elements, put k-1 th divider
    # between arr[i-1] & arr[i] to
    # get k-th partition
    for i in range(1, n + 1):
        best = min(best,
                   max(partition(arr, i, k - 1),
                       sum(arr, i, n - 1)))
    return best

# # Driver Code
# arr = [10, 20,30, 40]
# n = len(arr)
# k = 2
# print(partition(arr, n, k))

n = int(input())
result_list=[]
for i in range(0,n):
    k_v=input()
    k_v_item = k_v.strip().split()
    k = int(k_v[0])#2
    n = int(k_v[2])#4
    #print(k,n)
    arr = input()
    arr_tmp = arr.strip().split()
    list = []
    for tmp in arr_tmp:
        list.append(int(tmp))
    #print(list)
    #n = len(list)
    #print(len(list))
    result=partition(list, n, k)
    result_list.append(result)
for item in result_list:
    print(item)
# Sample Input 4 3 5 4 3 3 6 7
# 3
# SampleOutput 32

arr = input()
print(arr)
#arr = "4 3 5 4 3 3 6 7"
arr_split = arr.split()
arr_split_int = list(map(int,arr_split))
print(arr_split_int)
w = input()
w = int(w)

def getMaxWindow(arr, w):
    if arr == None or w < 1 or len(arr) < w:
        return
    deque = []
    res = []
    for i in range(len(arr)):
        while deque and arr[deque[-1]] <= arr[i]:
            deque.pop()
        deque.append(i)
        if deque[0] <= i - w:
            deque.pop(0)
        if i-w+1 >= 0:
            res.append(arr[deque[0]])
    return res

MaxWindow = getMaxWindow(arr_split_int,w)
result = sum(MaxWindow)
print(result)




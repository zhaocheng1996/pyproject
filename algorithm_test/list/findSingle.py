'''
找出数组中出现一次的数
'''

import copy
def findSingle(arr):
    b=arr.copy()
    i=0
    while i<len(arr):
        if arr[i] not in arr[i+1:]:#先找出重复的
            arr.pop(i)
            i-=1
        i+=1
    for each_b in b:
        if each_b not in arr:
            print(each_b,end=' ')
arr = [1,2,4,5,6,4,2]
#findSingle(arr)

def findSingle2(arr):
    hastable = dict()
    for item in arr:
         hastable[item]=arr.count(item)
    #print(hastable)#{1: 1, 2: 2, 4: 2, 5: 1, 6: 1}
    klist = list(hastable.keys())
    vlist = list(hastable.values())
    #print(klist)
    for i in range(len(vlist)):
        if vlist[i] == 1:
            print(klist[i],end=' ')

arr = [1,2,4,5,6,4,2]
findSingle2(arr)
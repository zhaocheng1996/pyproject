'''
数组中有N+2个数，其中，N个数出现了偶数次，2个数出现了奇数次(
这两个数字不用相等)，用O(1)的空间复杂度，找出这两个数。
思路，遍历出现一次的时候记录为1，当记录的values为1时候，代表以前出现过，变为0
遍历多次
'''

# def get_odd(olist):
#     hashtable = dict()
#     for i in olist:
#         hashtable[i] = olist.count(i)#{3: 1, 5: 2, 6: 2, 7: 1, 2: 2}
#     a=[]
#     values=hashtable.values()
#     #print(type(values))#<class 'dict_values'>
#     for each_v in hashtable.values():
#         if each_v%2 == 1:
#             print(list(hashtable.keys())[list(hashtable.values()).index(each_v)])
#             #return list(hashtable.keys())[list(hashtable.values()).index (each_v)]

def get_odd(olist):
    dic = dict()
    i = 0
    while i < len(olist):
        #字典中第一次出现这个数字
          if olist[i] not in dic:
              dic[olist[i]]=1
          #已经出现过了
          else:
              dic[olist[i]] = 0
          i+=1
    for k,v in dic.items():
        if v == 1:
            print(k,end=' ')

olist = [3,5,6,6,5,7,2,2]
get_odd(olist)




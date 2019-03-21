lis = [3,5,5,4,4]

# num = input()
# num = int(num)
# arr_num = input()
# arr_num = int(arr_num)
# arr = input()
# print(arr)#arr是str
# #arr = "1 2 3 4 5 6 7"
# arr_split = arr.split()
# arr_split_int = list(map(int,arr_split))
# arr_split_int = arr_split_int[0:arr_num]
# print('arr_split_int',arr_split_int)

def test1():
    # #进行去重
    # c = []
    # for i in lis:
    #     if i not in c:
    #         c.append(i)
    #进行统计，生成二维列表
    b = []
    for i in lis:
        num = 0
        for j in range(len(lis)):
            if lis[j] == i:
                num += 1
        a = []
        a.append(i)
        a.append(num)
        b.append(a)
    # 排序算法，按出现次数进行降序排列
    for i in range(len(b)):
        for j in range(i,len(b)):
            if b[i][1] < b[j][1]:
                temp = b[i]
                b[i] = b[j]
                b[j] = temp
    print(b)
    import numpy as np
    a = np.array(b)
    print(a.shape)
    c = a[:,0]
    print(c)#选取数组的第一列



# def test2():
#     # set进行去重，进行统计生成二维列表
#     b = []
#     for i in list(set(lis)):
#         num = 0
#         for j in range(len(lis)):
#             if lis[j] == i:
#                 num += 1
#         a = []
#         a.append(i)
#         a.append(num)
#         b.append(a)
#     # 排序算法，按出现次数进行降序排列
#     for i in range(len(b)):
#         for j in range(i,len(b)):
#             if b[i][1] < b[j][1]:
#                 temp = b[i]
#                 b[i] = b[j]
#                 b[j] = temp
#     print(b)
#
# def test3():
#     # 统计元素出现次数，元素为key，次数为value，生成字典
#     a = {}
#     for i in lis:
#         if i in a:
#             a[i] = a[i] + 1
#         else:
#             a[i] = 1
#     # 使用sorted对字典进行排序
#     b = sorted(a.items(),key=lambda item:item[1],reverse=True)
#     print(b)

import numpy as np

def test4():
    from  collections import Counter
    import operator
    #进行统计
    a = dict(Counter(lis))
    #进行排序
    b= dict(sorted(a.items(),key=lambda x:x[0]))#先按keys排序
    c= dict(sorted(b.items(), key=operator.itemgetter(1),reverse=True))#再按values排序
    print("c",c)
    #print("b",b)
    # 通过list将字典中的keys和values转化为列表
    keys = list(c.keys())
    print(keys)
    values = list(c.values())
    print(values)
    d = []
    for key in keys:
        for i in range(0,c[key]):#会根据这个key去找values
            d.append(str(key))
    print(" ".join(d))

#test1()
# test2()
# test3()
test4()




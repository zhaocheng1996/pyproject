'''
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)
组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
返回 enumerate(枚举) 对象。
'''


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))#[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
#从下标1开始
print(list(enumerate(seasons,start=1)))#[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

#如果对一个列表，既要遍历索引又要遍历元素时，首先可以这样写：
list1 = ["这", "是", "一个", "测试"]
for i in range (len(list1)):
    print(i ,list1[i])




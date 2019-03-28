'''
春天是鲜花的季节，水仙花就是其中最迷人的代表，数学上有个水仙花数，他是这样定义的：
“水仙花数”是指一个三位数，它的各位数字的立方和等于其本身，比如：153=1^3+5^3+3^3。
现在要求输出所有在m和n范围内的水仙花数。
输入
输入数据有多组，每组占一行，包括两个整数m和n（100<=m<=n<=999）。
输出
对于每个测试实例，要求输出所有在给定范围内的水仙花数，就是说，输出的水仙花数必须大于等于m,并且小于等于n，如果有多个，则要求从小到大排列在一行内输出，之间用一个空格隔开;
如果给定的范围内不存在水仙花数，则输出no;
每个测试实例的输出占一行。
样例输入
100 120
300 380
样例输出
no
370 371
'''

def daffodil(x):
    a = x//10**2
    b = (x-a*100)//10
    c = x%10
    if x==pow(a,3)+pow(b,3)+pow(c,3):
        return x
    else:
        return None

a = []
for item in range(100,120):
    if daffodil(item) == None:
        continue
    else:
       a.append(daffodil(item))
if len(a)==0:
    print('no')
else:
    for item in a:
        print(item,end=' ')




# while 1:
#     s=[int(x) for x in input().split()]
#     for item in range(s[0],s[1]+1):
#         if daffodil(item) == 'no':
#            print('no')
#            break
#         else:
#             print(daffodil(item),end=' ')



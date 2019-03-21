'''
KD树构造和查找
Description
对给定的点集合构造KD树，要求如下：将方差最大的维度作为当前的分割维度，将数据集在分割维度上排序后的中位数作为分割点。程序要检索给定点对应的最近的K个点的坐标。
Input
输入第一行为测试用例个数，后面为测试用例，每一个用例包含三行，第一行为点集合（点之间用逗号隔开，两个坐标用空格隔开），第二行为检索的点，第三行为K值。
Output
输出每一个用例的最近K个点，按照距离从小到大的顺序打印。
Sample Input 1 
 1
3 5,6 2,5 8,9 3,8 6,1 1,2 9
8.2 4.6
2
Sample Output 1
 8 6,9 3
'''

import math
# def cal_variance(lis: list) -> float:
#     mean = sum(lis) / len(lis)
#     var = sum([(i - mean) ** 2 for i in lis]) / len(lis)
#     return var
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
def to_int(n):
    return int(n) if n == int(n) else n
cases = int(input())
for _ in range(cases):
    pairs = []
    tmp = input().strip().split(',')
    for t in tmp:
        x, y = list(map(float, t.split()))
        pairs.append([x, y])

    a, b = list(map(float, input().strip().split()))
    k = int(input().strip())
    # print(str(pairs))

    # dis = [distance(p, [a, b]) for p in pairs]
    d = {}
    for index in range(len(pairs)):
        d[index] = distance([a, b], pairs[index])
    # print(d)
    d = sorted(d.items(), key=lambda l: l[1])
    s = ''
    for i in range(k):
        p = pairs[d[i][0]]
        s += str(to_int(p[0])) + ' ' + str(to_int(p[1])) + ','
    print(s[:len(s) - 1])


#子矩阵问题
# Description
# 给定一个矩形区域，每一个位置上都是1或0，求该矩阵中每一个位置上都是
# 1的最大子矩形区域中的1的个数。
# Input
# 输入的每一行是用空格隔开的0或1。
# Output
# 输出一个数值。
# Sample Input 1
# 1 0 1 1
# 1 1 1 1
# 1 1 1 0
# out
# 6

def get_max_num(arr):
    maxn = 0
    n = len(arr)
    m = len(arr[0])
    opt = [0 for _ in range(m)]#[0, 0, 0, 0]
    map = [[0 for _ in range(m)] for _ in range(n)]#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                map[i][j] = 1
            else:
                map[i][j] = -10000

    for i in range(n):
        for j in range(i, n):
            t = 0
            for k in range(m):
                if j == i:
                    opt[k] = map[i][k]
                else:
                    opt[k] += map[j][k]
                t += opt[k]
                if t < 0:
                    t = 0
                if maxn < t:
                    maxn = t
    return maxn

a = []
try:
    while True:
        e = [int(x) for x in input().split()]
        a.append(e)
except EOFError:
    pass
# print(a)
#
# a = [[1,0,1,1],
#      [1,1,1,1],
#      [1,1,1,0]]

#print(a.shape)
print(get_max_num(a))





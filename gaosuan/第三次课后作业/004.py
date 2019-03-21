'''
棋盘覆盖问题
Description
棋盘覆盖问题：给定一个大小为2^n2^n个小方格的棋盘，其中有一个位置已经被填充，现在要用一个L型（2*2个小方格组成的大方格中去掉其中一个小方格）形状去覆盖剩下的小方格。求出覆盖方案，即哪些坐标下的小方格使用同一个L型格子覆盖。注意：坐标从0开始。左上方的第一个格子坐标为(0,0)，第一行第二个坐标为(0,1)，第二行第一个为(1,0)，以此类推。
Input
输入第一行为测试用例个数，后面每一个用例有两行，第一行为n值和特殊的格子的坐标（用空格隔开），第二行为需要查找其属于同一个L型格子的格子坐标。
Output
输出每一行为一个用例的解，先按照行值从小到大、再按照列值从小到大的顺序输出每一个用例的两个坐标；用逗号隔开。
Sample Input 1 
 1
1 1 1
0 0
Sample Output 1
 0 1,1 0
'''

t = 0
def f(a, b, aa, bb, n, m):
    if n == 0:
        return
    global t
    t += 1
    tmp = t  # **
    k = n - 1
    l = 2 ** k
    # 特殊点在左上角
    if aa < a + l and bb < b + l:
        f(a, b, aa, bb, k, m)
    else:
        m[a + l - 1][b + l - 1] = tmp
        f(a, b, a + l - 1, b + l - 1, k, m)
    # 左下角
    if aa >= a + l and bb < b + l:
        f(a + l, b, aa, bb, k, m)
    else:
        m[a + l][b + l - 1] = tmp
        f(a + l, b, a + l, b + l - 1, k, m)
    # 右上角
    if aa < a + l and bb >= b + l:
        f(a, b + l, aa, bb, k, m)
    else:
        m[a + l - 1][b + l] = tmp
        f(a, b + l, a + l - 1, b + l, k, m)
    # 右下角
    if aa >= a + l and bb >= b + l:
        f(a + l, b + l, aa, bb, k, m)
    else:
        m[a + l][b + l] = tmp
        f(a + l, b + l, a + l, b + l, k, m)


cases = int(input())
for case in range(cases):
    n, aa, bb = list(map(
        int, input().strip().split()
    ))
    found_x, found_y = list(map(
        int, input().strip().split()
    ))
    length = 2 ** n
    m = [[0 for _ in range(length)] for _ in range(length)]
    # print(m)
    f(0, 0, aa, bb, n, m)
    # print(m)
    num = m[found_x][found_y]
    # print("num:  " + str(num))
    s = ''
    for i in range(length):
        for j in range(length):
            if m[i][j] == num and not (i == found_x and j == found_y):
                s += str(i) + ' ' + str(j) + ','
    print(s[:len(s) - 1])


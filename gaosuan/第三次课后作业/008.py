'''
拓扑排序解的个数
Description
给定有向无环图中所有边，计算图的拓扑排序解的个数。
Input
输入第一行为用例个数，后面每一行表示一个图中的所有边，边的起点和终点用空格隔开，边之间使用逗号隔开。
Output
输出拓扑排序解的个数。
Sample Input 1 
1
a c,b c,c d,d e,d f,e g,f g
Sample Output 1
4
'''

def is_ok(i: int):
    for j in range(n):
        if m[j][i] == 1 and visited[j] == 0:
            return False
    return True


def dfs(cnt: int):
    global num
    if cnt == n:
        num += 1
        return

    for i in range(n):
        if visited[i] == 0 and is_ok(i):
            visited[i] = 1
            dfs(cnt +1)
            visited[i] = 0


cases = int(input())
for case in range(cases):
    pairs = input().strip().split(',')
    s = set()
    for pair in pairs:
        x, y = pair.split()
        s.add(x)
        s.add(y)
    n = len(s)
    m = [[0 for _ in range(n)] for _ in range(n)]
    for pair in pairs:
        x, y = pair.split()
        m[ord(x) - ord('a')][ord(y) - ord('a')] = 1

    visited = [0] * n
    num = 0
    dfs(0)
    print(num)

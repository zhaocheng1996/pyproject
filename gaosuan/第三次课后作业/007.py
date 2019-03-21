'''
广度优先遍历图
Description
按照给定的起始顶点广度优先遍历图，每一次通过字母顺序选择顶点查找下一层邻接点，打印遍历顺序。
Input
输入第一行为测试用例个数，后面每一个用例用多行表示，用例第一行是节点个数n和开始顶点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
Output
输出遍历顺序，用空格隔开
Sample Input 1 
 1
4 a
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
Sample Output 1
 a b c d
'''

from queue import Queue


def f(v):
    q = Queue()
    res = v
    visited[v] = 1
    q.put(v)
    while not q.empty():
        v = q.get()
        for w in graph.adjacent(v):
            if visited[w] == 0:
                res += " " + w
                visited[w] = 1
                q.put(w)
    return res


class Graph(object):
    def __init__(self, v_list, m):
        self.v_list = v_list
        self.m = m
        self.num = len(self.v_list)

    def adjacent(self, v):
        lis = []
        for x in range(self.num):
            if self.m[v][x] == 1:
                lis.append(self.v_list[x])
        return lis


cases = int(input())
for case in range(cases):
    n, start = input().strip().split()
    n = int(n)
    v_list = input().strip().split()
    m = {}
    visited = {}
    for i in range(n):
        m[v_list[i]] = input().strip().split()
        m[v_list[i]].pop(0)
        m[v_list[i]] = list(map(int, m[v_list[i]]))
        visited[v_list[i]] = 0
    graph = Graph(v_list, m)
    print(f(start))

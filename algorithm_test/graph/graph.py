'''
实现一个图，图具体啥样看这个链接
https://www.jianshu.com/p/2c2cdcb9de9d
'''

import collections
import queue

g = collections.OrderedDict()
g['A'] = ['B', 'C', 'D']
g['B'] = ['A', 'E']
g['C'] = ['A', 'F']
g['D'] = ['A', 'G', 'H']
g['E'] = ['B', 'F']
g['F'] = ['E', 'C']
g['G'] = ['D', 'H', 'I']
g['H'] = ['G', 'D']
g['I'] = ['G']

#深度优先遍历
def DFSTraverse(g):
    visited = {}
    def DFS(v):
        print(v)
        visited[v] = True
        for adj in g[v]:
            if not visited.get(adj):
                DFS(adj)
    for v in g:
        if not visited.get(v):
            DFS(v)
DFSTraverse(g)











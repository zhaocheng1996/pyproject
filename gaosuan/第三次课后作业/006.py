'''
分治法解最近对问题
Description
最近对问题：使用分治算法解决最近对问题。
Input
第一行为测试用例个数。后面每一行表示一个用例，一个用例为一些平面上点的集合，点与点之间用逗号隔开，一个点的两个坐标用空格隔开。坐标值都是正数。
Output
对每一个用例输出两个距离最近的点（坐标使用空格隔开），用逗号隔开，先按照第一个坐标大小排列，再按照第二个坐标大小排列。如果有多个解，则按照每个解的第一个点的坐标排序，连续输出多个解，用逗号隔开。
Sample Input 1 
 1
1 1,2 2,3 3,4 4,5 5,1.5 1.5
Sample Output 1
 1 1,1.5 1.5,1.5 1.5,2 2
'''

import math
class Node_nearst(object):
    res = []
    dist = 100000  # 一个比较大的数

    def add(self, node_pair):
        node_pair = sorted(node_pair, key=lambda n: (n.x, n.y))
        # 判断是否重复添加
        for np in self.res:
            if node_pair[0].x == np[0].x and node_pair[0].y == np[0].y \
                    and node_pair[1].x == np[1].x and node_pair[1].y == np[1].y:
                return
        self.res.append(node_pair)

    def clear_add(self, node_pair):
        self.res.clear()
        node_pair = sorted(node_pair, key=lambda n: (n.x, n.y))
        self.res.append(node_pair)

    def sort(self):
        self.res = sorted(self.res, key=lambda np: (np[0].x, np[0].y))

    def print(self):
        s = ''
        for node_pair in self.res:
            n1, n2 = node_pair
            n1 = self.__toInt(n1)
            n2 = self.__toInt(n2)
            s += str(n1.x) + " " + str(n1.y) + ',' + str(n2.x) + " " + str(n2.y) + ','
        print(s[:len(s) - 1])

    def __toInt(self, n):
        x, y = n.x, n.y
        n.x = int(x) if x == int(x) else x
        n.y = int(y) if y == int(y) else y
        return n

node_nearst = Node_nearst()

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(n1, n2):
    return math.sqrt((n1.x - n2.x) ** 2 + (n1.y - n2.y) ** 2)


def isNearst(dist, n1, n2):
    if dist == node_nearst.dist:
        node_nearst.add([n1, n2])
    elif dist < node_nearst.dist:
        node_nearst.clear_add([n1, n2])
        node_nearst.dist = dist


def f(s, left, right):
    if right - left == 1:  # 仅两个点
        d = distance(s[left], s[right])
        isNearst(d, s[left], s[right])
        return d
    if right - left == 2:  # 仅三个点
        d1 = distance(s[left], s[left + 1])
        d2 = distance(s[left + 1], s[right])
        d3 = distance(s[left], s[right])
        min_d = min(d1, d2, d3)
        if d1 == min_d:
            isNearst(d1, s[left], s[left + 1])
        if d2 == min_d:
            isNearst(d1, s[left + 1], s[right])
        if d3 == min_d:
            isNearst(d1, s[left], s[right])
        return min_d

    mid = (right - left) // 2 + left
    d_left = f(s, left, mid)
    d_right = f(s, mid + 1, right)
    dist = min(d_left, d_right)

    inner_s = []
    for i in range(mid, left - 1, -1):
        if s[mid].x - s[i].x < dist:
            inner_s.append(s[i])
        else:
            break
    for i in range(mid + 1, right + 1):
        if s[i].x - s[mid].x < dist:
            inner_s.append(s[i])
        else:
            break
    # 按照 y 升序
    inner_s = sorted(inner_s, key=lambda n: n.y)
    for i in range(len(inner_s)):
        for j in range(i + 1, i + 7):  # 6个点
            if j < len(inner_s):
                if inner_s[j].y - inner_s[i].y >= dist:
                    break
                else:
                    d = distance(inner_s[j], inner_s[i])
                    if d <= dist:
                        #print(inner_s[j].x,inner_s[i].x)
                        isNearst(d, inner_s[j], inner_s[i])
                        dist = d
            else:
                break
    return dist

cases = int(input())
for case in range(cases):
    nodes = input().strip().split(',')
    s = []
    for node in nodes:
        x, y = list(map(float, node.split()))
        node = Node(x, y)
        s.append(node)
    # 按照 x 升序
    s = sorted(s, key=lambda n: n.x)
    f(s, 0, len(s) - 1)
    # print(node_nearst.dist)
    node_nearst.sort()
    node_nearst.print()


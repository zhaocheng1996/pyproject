'''
深度优先遍历
Description
按照给定的起始顶点深度优先遍历给定的无向图，尝试所有可能的遍历方式，打印遍历过程中出现的最大深度。
Input
输入第一行是用例个数，后面每个用例使用多行表示，用例的第一行是图中节点的个数n和起始点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
Output
输出深度优先遍历中遇到的最大深度。
Sample Input 1 
1
4 a
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
Sample Output 1
4
'''

def get_max(points: list, lines: list) -> int:
    line = lines[points[-1]]
    max = 1
    for i in range(1, len(line)):
        if line[i] == '1' and (i - 1) not in points:
            temp = points.copy()
            temp.append(i - 1)
            if get_max(temp, lines) + 1 > max:
                max = get_max(temp, lines) + 1
            del temp
    return max


case_num = int(input())
for i in range(case_num):
    arr = input().split(' ')
    line_num = int(arr[0])
    start = arr[1]
    not_used = input().split(' ')
    lines = []
    start_line = 0
    for j in range(line_num):
        line = input().split(' ')
        lines.append(line)
        if line[0] == start:
            start_line = j
        line[0] = j
    points = []
    points.append(start_line)
    # print(points)
    # print(lines)
    print(get_max(points, lines))

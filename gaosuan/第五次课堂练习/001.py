'''
Every house in the colony has at most one pipe going into it and at most one pipe going out of it. Tanks and taps are to be installed in a manner such that every house with one outgoing pipe but no incoming pipe gets a tank installed on its roof and every house with only an incoming pipe and no outgoing pipe gets a tap. Find the efficient way for the construction of the network of pipes.
殖民地中的每个房屋最多只有一根管子进入其中，最多只有一根管子从其中出来。储罐和水龙头的安装方式应使每个房屋都有一个输出管道，
但没有进水管道安装在其屋顶上，每个房屋只有一个输入管道，没有输出管道可以安装水龙头。找到构建管网的有效方法。
Input
The first line contains an integer T denoting the number of test cases. For each test case, the first line contains two integer n & p denoting the number of houses and number of pipes respectively. Next, p lines contain 3 integer inputs a, b & d, d denoting the diameter of the pipe from the house a to house b.Constraints:1<=T<=50，1<=n<=20，1<=p<=50，1<=a, b<=20，1<=d<=100
第一行包含一个整数T，表示测试用例的数量。对于每个测试用例，第一行包含两个整数n和p，分别表示房屋数量和管道数量。
接下来，p行包含3个整数输入a，b和d，d表示从房屋a到房屋b的管道直径。约束：1 <= T <= 50,1 <= n <= 20,1 <= p <= 50,1 <= a，b <= 20,1 <= d <= 100
Output
For each test case, the output is the number of pairs of tanks and taps installed i.e n followed by n lines that contain three integers: house number of tank, house number of tap and the minimum diameter of pipe between them.
对于每个测试用例，输出是安装的水箱和水龙头对的数量，即n后面包含三个整数的线：水箱的门牌号，水龙头的门牌号和它们之间的管道的最小直径。
Sample Input 1 
1
9 6
7 4 98
5 9 72
4 6 10
2 8 22
9 7 17
3 1 66
Sample Output 1
3
2 8 22
3 1 66
5 6 10
'''

from collections import defaultdict
def dfs(src, houses, pipes, visited):
    visited.add(src)
    sink = src
    mind = 999999
    for adj_h in houses[src]:
        mind = min(mind, pipes[src][adj_h])
        if adj_h not in visited:
            sink, tmp = dfs(adj_h, houses, pipes, visited)
            mind = min(mind, tmp)
    return sink, mind


def solve(houses, pipes):
    sources = set(houses.keys())
    houses_inv = defaultdict(set)
    for h in houses:
        for adj_h in houses[h]:
            houses_inv[adj_h].add(h)
            if adj_h in sources:
                sources.remove(adj_h)

    print(len(sources))
    while sources:
        src = sources.pop()
        sink, mind = dfs(src, houses, pipes, set())
        print(src, sink, mind)


for _ in range(int(input())):
    nohouses, nopipes = map(int, input().split())
    houses = defaultdict(set)
    pipes = defaultdict(dict)
    for p in range(nopipes):
        house_a, house_b, d = map(int, input().split())
        houses[house_a].add(house_b)
        pipes[house_a][house_b] = d
    solve(houses, pipes)



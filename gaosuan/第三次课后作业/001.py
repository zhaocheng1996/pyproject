'''
分配问题
Description
对给定的n个任务与n个人之间的成本矩阵完成成本最低的任务分配策略。
Input
输入：第一行为用例个数，之后为每一个用例；用例的第一行为任务个数，即n；用例的第二行为使用逗号隔开的人员完成任务的成本；每一个成本描述包括人员序号、任务序号和成本，使用空格隔开。人员序号和任务序号都是从1到n的整数，序号出现的次序没有固定规则。
Output
输出：每一个用例输出一行，从序号为1的人员开始，给出其分配的任务序号，使用空格隔开；使用逗号将多个解隔开。结果按照人员分配的任务序号大小排，第一个人员的任务序号大的放在前面，如果相同则看第二个人员的任务，以此类推。
Sample Input 1
 1
4
2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4
Sample Output 1
 2 1 3 4
'''

import itertools


def per(n):
    lis = [i for i in range(n)]
    res = []
    for r in itertools.permutations(lis, n):
        res.append(r)
    return res


def f(m, n):
    res = per(n)
    s = []
    for r in res:
        c = 0
        for i in range(n):
            c += m[i][r[i]]
        s.append(c)
    min_v = min(s)
    result = []
    for i in range(len(s)):
        if min_v == s[i]:
            result.append(list(map(lambda x: x + 1, res[i])))

    return result


def g(n):
    s = ''
    for i in range(n):
        s += 'x[' + str(i) + ']' + ','
    return s[:len(s) - 1]


cases = int(input())
for _ in range(cases):
    n = int(input())
    m = [[0 for _ in range(n)] for _ in range(n)]
    nn = input().strip().split(',')
    for p in nn:
        people, task, value = p.split()
        m[int(people) - 1][int(task) - 1] = int(value)
    res = f(m, n)
    res = sorted(res, key=lambda x: (eval(g(n))), reverse=True)
    s = ''
    for r in res:
        s += ' '.join(list(map(str, r))) + ','
    print(s[:len(s) - 1])


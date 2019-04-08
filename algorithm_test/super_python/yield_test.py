# encoding:UTF-8
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")
def call(i):
    return i * 2
# 使用for循环
for i in yield_test(5):
    print(i, ",")
'''
结果
0 ,
i= 0
2 ,
i= 1
4 ,
i= 2
6 ,
i= 3
8 ,
i= 4
do something.
end.
理解的关键在于：下次迭代时，代码从yield的下一跳语句开始执行。
如果去了yield的话
i= 0
i= 1
Traceback (most recent call last):
i= 2
i= 3
i= 4
do something.
end.
  File "E:/kaifaanzhuanglj/pyproject/algorithm_test/super_python/yield_test.py", line 12, in <module>
    for i in yield_test(5):
TypeError: 'NoneType' object is not iterable
这个程序就不再是一个可迭代的了
'''



#让我们看看比赛中4匹马可能到达终点的先后顺序的可能情况:
import itertools
horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)#<itertools.permutations object at 0xb754f1dc>
print(list(itertools.permutations(horses)))#[(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]

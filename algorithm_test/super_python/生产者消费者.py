#生产者消费者
import time
import queue
import threading

q = queue.Queue(10) #生成一个队列，用来存包子，最大数量为10

def productor(i):
    # 厨师2秒做一个包子
    while True:
        q.put("厨师%s做的包子！" % i)
        time.sleep(2)

def consumer(j):
    # 顾客不停地每秒吃一个包子
    while True:
        print("顾客 %s 吃了一个 %s"%(j,q.get()))
        time.sleep(1)

# 实例化了3个生产者（厨师）
for i in range(3):
    t = threading.Thread(target=productor, args=(i,))
    t.start()
# 实例化了10个消费者（顾客）
for j in range(10):
    v = threading.Thread(target=consumer, args=(j,))
    v.start()
'''
顾客 0 吃了一个 厨师0做的包子！
顾客 1 吃了一个 厨师1做的包子！
顾客 2 吃了一个 厨师2做的包子！
顾客 3 吃了一个 厨师2做的包子！
顾客 4 吃了一个 厨师0做的包子！
顾客 5 吃了一个 厨师1做的包子！
顾客 6 吃了一个 厨师1做的包子！
顾客 7 吃了一个 厨师0做的包子！
顾客 8 吃了一个 厨师2做的包子！
顾客 0 吃了一个 厨师1做的包子！
顾客 1 吃了一个 厨师0做的包子！
顾客 9 吃了一个 厨师2做的包子！
'''






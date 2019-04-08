'''
有两种方式来创建线程：一种是继承Thread类，并重写它的run()方法；
另一种是在实例化threading.Thread对象的时候，将线程要执行的任务函数作为参数传入线程。
'''

#第一种方法：
# import threading
#
# class MyThread(threading.Thread):
#     def __init__(self,thread_name):
#         #注意：一定要显式的调用父类的初始化函数。
#         super(MyThread,self).__init__(name=thread_name)
#     def run(self):
#         print('%s正在运行中....'%self.name)
#
# if __name__ == '__main__':
#     for i in range(10):
#     MyThread("thread-"+str(i)).start()
# 运行结果
# thread-0正在运行中....
# thread-1正在运行中....
# thread-2正在运行中....
# thread-3正在运行中....
# thread-4正在运行中....
# thread-5正在运行中....
# thread-6正在运行中....
# thread-7正在运行中....
# thread-8正在运行中....
# thread-9正在运行中....
#第二种方法
# import threading
# import time
#
# def show(arg):
#     time.sleep(1)
#     print('thread'+str(arg)+'running....')
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = threading.Thread(target=show,args=(i,))
#         t.start()
# thread0running....
# thread1running....
# thread4running....
# thread3running....
# thread2running....
# thread5running....
# thread7running....
# thread8running....
# thread6running....
# thread9running....

#在多线程执行过程中，有一个特点要注意，那就是每个线程各执行各的任务，不等待其它的线程，自顾自的完成自己的任务

# import time
# import threading
#
# def doWaiting():
#     print('start waiting:',time.strftime('%H:%M:%S'))
#     time.sleep(3)
#     print('stop waiting:',time.strftime('%H:%M:%S'))
#
# t = threading.Thread(target=doWaiting)
# t.start()
# # 确保线程t已经启动
# time.sleep(1)
# print('start job')
# print('end job')
# start waiting: 22:49:58
# start job
# end job
# stop waiting: 22:50:01
'''
Python默认会等待最后一个线程执行完毕后才退出。上面例子中，主线程没有等待子线程t执行完毕，而是啥都不管，继续往下执行它自己的代码，执行完毕后也没有结束整个程序，而是等待子线程t执行完毕，整个程序才结束
就是这个stop方法的子线程在主线程后执行完毕
'''
#主线程等子线程

# import time
# import threading
#
# def doWaiting():
#     print('start waiting:', time.strftime('%H:%M:%S'))
#     time.sleep(3)
#     print('stop waiting', time.strftime('%H:%M:%S'))
#
# t = threading.Thread(target=doWaiting)
# t.start()
# # 确保线程t已经启动
# time.sleep(1)
# print('start join')
# # 将一直堵塞，直到t运行结束。
# t.join()
# print('end join')

# start waiting: 22:54:39
# start join
# stop waiting 22:54:42
# end join

#我们还可以使用setDaemon(True)把所有的子线程都变成主线程的守护线程，
# 当主线程结束后，守护子线程也会随之结束，整个程序也跟着退出。
# import threading
# import time
#
# def run():
#     print(threading.current_thread().getName(),'开始工作')
#     time.sleep(2) #子线程停2s
#     print("子线程工作完毕")
#
# for i in range(3):
#     t = threading.Thread(target=run,)
#     t.setDaemon(True)
#     t.start()
#
# time.sleep(1)  #主程序停1秒
# print('主线程结束了！')
# print(threading.active_count()) #输出活跃的线程数

# Thread-1 开始工作
# Thread-2 开始工作
# Thread-3 开始工作
# 主线程结束了！
# 4




# import threading
# import time
# number = 0
# def plus():
#     global number       # global声明此处的number是外面的全局变量number
#     for _ in range(1000000):    # 进行一个大数级别的循环加一运算
#         number += 1
#     print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))
# for i in range(2):      # 用2个子线程，就可以观察到脏数据
#     t = threading.Thread(target=plus)
#     t.start()
# time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
# print("主线程执行完毕后，number = ", number)
# 子线程Thread-2运算结束后，number = 1124101
# 子线程Thread-1运算结束后，number = 1154389
# 主线程执行完毕后，number =  1154389
# 算同一个东西算出来的结果并不一样

#对于threading模块中的Thread类，本质上是执行了它的run方法。
# 因此可以自定义线程类，让它继承Thread类，然后重写run方法。

# import threading
# class MyThreading(threading.Thread):
#     def __init__(self,func,arg):
#         super(MyThreading,self).__init__()
#         self.func = func
#         self.arg = arg
#     def run(self):
#         self.func(self.arg)
# def my_func(args):
#     for i in range(10):
#         print(i)
# obj = MyThreading(my_func,123)
# obj.start()

# import threading
# #具体做啥事,写在函数中
# def run(number):
#     print(threading.currentThread().getName() + ' ')
#     print(number)
#
# if __name__ == '__main__':
#     for i in range(3):
#         #注意这,开始咯,指明具体的方法和方法需要的参数
#         my_thread = threading.Thread(target=run, args=(i,))
#         #一定不要忘记
#         my_thread.start()
'''
输出
Thread-1 
0
Thread-2 
1
Thread-3 
2
'''

import threading

mylock = threading.RLock()
num = 0


class WorkThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global num
        while True:
            mylock.acquire()
            print('\n%s locked, number: %d' % (self.t_name, num))
            if num >= 4:
                mylock.release()
                print('\n%s released, number: %d' % (self.t_name, num))
                break
            num += 1
            print('\n%s released, number: %d' % (self.t_name, num))
            mylock.release()


def test():
    thread1 = WorkThread('A-Worker')
    thread2 = WorkThread('B-Worker')
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    test()


















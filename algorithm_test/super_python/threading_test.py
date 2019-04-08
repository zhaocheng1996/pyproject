'''
threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
threading.currentThread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
run(): 用以表示线程活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。
'''

# import threading
# from time import ctime,sleep
#
# def music(func):
#     for i in range(2):
#         print("I was listening to %s. %s" % (func, ctime()))
#         sleep(1)
#
# def movie(func):
#         for i in range(2):
#             print("I was at the %s! %s" % (func, ctime()))
#             sleep(5)
#
# threads = []
# t1 = threading.Thread(target=music,args=(u'亏啊了',))
# threads.append(t1)
# t2 = threading.Thread(target=movie,args=(u'shadafa',))
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.start()
#
#     print ("all over %s" %ctime())

'''
I was listening to 亏啊了. Wed Mar 27 09:54:25 2019
I was at the shadafa! Wed Mar 27 09:54:25 2019
all over Wed Mar 27 09:54:25 2019
I was listening to 亏啊了. Wed Mar 27 09:54:26 2019
I was at the shadafa! Wed Mar 27 09:54:30 2019
'''

#构造线程类
#也可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：
import threading
import time
exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程："+self.name)
        print_time(self.name,self.counter,5)
        print("退出线程：" + self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s" %(threadName,time.ctime(time.time())))
        counter -= 1

#床罩新线程
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

#开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
'''
“等待该线程终止。”join方法
解释一下，是主线程等待子线程的终止。也就是说主线程的代码块中，如果碰到了t.join()方法，此时主线程需要等待（阻塞），等待子线程结束了(Waits for this thread to die.),才能继续执行t.join()之后的代码块。
'''
print("退出主线程")


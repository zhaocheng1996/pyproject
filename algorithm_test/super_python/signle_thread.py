from time import ctime,sleep
import threading

def music(func):
    for i in range(2):
        print("I was listening to %s. %s" %(func,ctime()))
        sleep(1)


def move(func):
    for i in range(2):
        print("I was at the %s %s" %(func,ctime()))
        sleep(5)


if __name__ == '__main__':
    music(u'快乐')
    move(u'我不是要深')
    print("all over %s" % ctime())
#计算函数使用时间的装饰器
import time

def decorate(fun):
    '''
    打印函数被调用的时间及调用次数
    '''
    count = 0
    def wrapper(*args, **kwargs):
        count=0
        start_time = time.time()
        data = fun(*args, **kwargs)
        stop_time = time.time()
        dt = stop_time - start_time
        count += 1
        print("被调用%d次，本次调用花费时间%f秒。" % (count, dt))
        return data

    return wrapper


@decorate
def demo():
    print("hello world!")
    time.sleep(0.5)


if __name__ == '__main__':
    for i in range(3):
        demo()
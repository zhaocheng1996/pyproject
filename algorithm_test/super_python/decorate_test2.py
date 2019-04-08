'''
测量时间的装饰器例子
'''
import time
#装饰的函数不带返回值
def display_time1(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print('total time:{:.4}s'.format(t2-t1))#:.4是保留四位小数
    return wrapper

#判断一个数是不是质数
def is_prime(num):
    if num<2:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

@display_time1
def prime_nums1():
    count = 0
    for i in range(2,10000):
        if is_prime(i):
            print(i)

#prime_nums()

#装饰带有返回值的函数
def display_time2(func):
    def wrapper():
        t1 = time.time()
        result= func()
        t2 = time.time()
        'total time:{:.4}s'
        print('total time:{:.4}s'.format(t2-t1))#:.4是保留四位小数
        return result
    return wrapper

#判断一个数是不是质数
def is_prime(num):
    if num<2:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

@display_time2
def prime_nums2():
    count = 0
    for i in range(2,10000):
        if is_prime(i):
            count+=1
    return count

# count = prime_nums2()
# print(count)

#装饰带有参数的函数
def display_time3(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print('tital time{:.4}s'.format(t2-t1))
        return result
    return wrapper

def is_prime(num):
    if num<2:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

@display_time3
def prime_nums3(maxnum):
    count = 0
    for i in range(2,maxnum):
        if is_prime(i):
            count+=1
    return count

res=prime_nums3(1000)
print(res)

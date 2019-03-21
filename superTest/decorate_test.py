#简单装饰器
def use_logging(func):

    def wrapper():
        print("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()                   # 执行foo()就相当于执行 wrapper()
# output： foo is running
        #  i am foo


#@语法糖装饰器
def use_logging(func):

    def wrapper():
        print("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

@use_logging
def foo():
       print('i am foo')

foo()                   # 执行foo()就相当于执行 wrapper,有了@就可以省去赋值






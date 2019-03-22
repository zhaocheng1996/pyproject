import sys #  模块，sys指向这个模块对象
import inspect
def foo(): pass # 函数，foo指向这个函数对象

class Cat(object): # 类，Cat指向这个类对象
    def __init__(self, name='kitty'):
        self.name = name
    def sayHi(self): #  实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print (self.name, 'says Hi!') # 访问名为name的字段，使用实例.name访问

cat = Cat() # cat是Cat类的实例对象

print (Cat.sayHi) # 使用类名访问实例方法时，方法是未绑定的(unbound)<function Cat.sayHi at 0x00000238529FF510>
print (cat.sayHi) # 使用实例访问实例方法时，方法是绑定的(bound)<bound method Cat.sayHi of <__main__.Cat object at 0x00000238526AA438>>
cat = Cat('kitty')

print (cat.name) # 访问实例属性
# kitty
print(cat.sayHi()) # 调用实例方法
# kitty says Hi!
print (dir(cat)) # 获取实例的属性名，以列表形式返回
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'sayHi']
if hasattr(cat, 'name'): # 检查实例是否有这个属性
    setattr(cat, 'name', 'tiger') # same as: a.name = 'tiger'

print (getattr(cat, 'name'))# same as: print a.name
# getattr 的文档
''' Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.'''
# tiger
getattr(cat, 'sayHi')() # same as: cat.sayHi()
# tiger says Hi!

'''dir([obj]): 
调用这个方法将返回包含obj大多数属性名的列表（会有一些特殊的属性不包含在内）。obj的默认值是当前的模块对象。
hasattr(obj, attr): 
这个方法用于检查obj是否有一个名为attr的值的属性，返回一个布尔值。
getattr(obj, attr): 
调用这个方法将返回obj中名为attr值的属性的值，例如如果attr为’bar’，则返回obj.bar。
setattr(obj, attr, val): 
调用这个方法将给obj的名为attr的值的属性赋值为val。例如如果attr为’bar’，则相当于obj.bar = val。'''
# class Cat(object):
#     def say(self):
#         print("i am a cat")
#
# class Dog(object):
#     def say(self):
#         print("i am a dog")
#
# class Duck(object):
#     def say(self):
#         print("i am a duck")
#
# animal_list = [Cat,Dog,Duck]
# for animal in animal_list:
#     animal().say()
#python实现多态，定义了对象就行
#i am a cat
#i am a dog
#i am a duck

'''类变量和实例变量
类变量可以用类名或者self的形式访问。当 self.类变量 被重新赋值时，它的值就发生了变化，
但类变量的值不会随之变化。方法内的局部变量会屏蔽掉类变量和实例变量。类变量是所有实例共享的，
而实例变量只属于对象自己，每个实例的实例变量可以有不同的值。
'''

# class A:
#     aa = 1
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
# a = A(2,3)
# A.aa = 11
# a.aa = 100
# print(a.x,a.y,a.aa)# 2 3 100
# print(A.aa)# 11 可以看到对象a的赋值并不会影响类A的值，类变量还是所有实例共享的

'''静态方法和常量方法'''
# class Date:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def tomorrow(self):#最常用的实例方法
#         self.day += 1
#
#     @classmethod#类方法
#     def from_string(cls,data_str):#cls时类的简称
#         year,month,day = tuple(data_str.split("-"))
#         return Date(int(year),int(month),int(day))
#
#
#     def __str__(self):#实例方法
#         return "{year}/{month}/{day}".format(year=self.year,month=self.month,day=self.day)
#
# if __name__ == "__main__":
#     # new_day = Date(2018,12,31)
#     # print(new_day)#2018/12/31
#
#     new_day = Date(2018, 12, 31)
#     new_day.tomorrow()
#     print(new_day)  # 2018/12/32
#
#     #用class类方法完成初始化
#     date_str = "2018-12-31"
#     new_day = Date.from_string(date_str)
#     print(new_day)
















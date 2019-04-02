'''
要开发一款教育类App,帮助幼儿在识数阶段做一百以内自然
数[0,99]的加减法
屏幕上会显示"1""2""3""4""5""6""7""8""9""0""+""-""="这些按钮,
用户在按了若干按钮之后,如果按了“=”,则会把按=“之前的字
符串作为一个算式,计算结果
中间结果或最后结果可以为负数
输入描述
输入为一个字符串,形如“23+86-6+37+2+-8-13°
输入字符串中保证:
不会包含
除“1”“2″“3”4”“5”“6"“7"“8”“9″“0”“+”“-”之外的字
符
长度不为0
不以“+”或“-”开始;不以“+"或“-"结束
例子：（自己编写）
输入：1+3+32-4-17
输出：15
'''

# import sys
# string = sys.stdin.readline()
# print(eval(string))
string = '1+3+32-4-17'
def isnum(c):
    if c.isdigit():
        return True
    else:
        return False
total=0
i=0
sig = '+'
n1 = -1
n2 = -1
fuhao = True
'1+3+32-4-17'
while i<len(string):
        tmp = 0
        while i<len(string) and isnum(string[i]):
            tmp = tmp*10+int(string[i])
            i+=1
        if n1 == -1:
            n1 = tmp
        else:
            n2 =tmp
        if n2 != -1:
            #res=0
            if fuhao:
                res = n1 + n2
            else:
                res = n1 - n2
            n1 =res
        if i<len(string) and string[i]=='+':
            fuhao = True
        elif i<len(string) and string[i]=='-':
            fuhao = False
        i += 1
print(n1)



















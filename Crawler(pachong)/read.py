f = open('text.txt','r')
#print(f.readline())#读一行
#print(f.readlines())#读出一个数组

#for line in f.readlines():
#    print(line.strip())#消除空格

with open('text.txt') as f:
    #print(dir(f))
    #dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
    #带参数时，返回参数的属性、方法列表。
    #如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
    for line in f.readlines():
        print(line)


import numpy as np

world_alcohol = np.genfromtxt("world_alcohol.txt",delimiter=",",dtype="str",skip_header=1)#skip_header跳过第一行
#print(type(world_alcohol))
#print(world_alcohol)
#print(help(numpy.genfromtxt))

vector = np.array([5,10,15,20])
matrix = np.array([[5,10,15],[20,25,30],[35,40,45]])
#print(vector)
#print(matrix)

vector = np.array([1,2,3,4])
print(vector.shape)#(4,)一维指的是4个元素
matrix1=np.array([[5,10,15],[20,25,30]])
print(matrix.shape)#(3，3)
print(matrix1.shape)#(2,3)

numbers=np.array([1,2,3,4.0])#这个里面要存的值是一样的如果不一样，会自动转换
print(numbers)
print(numbers.dtype)#float64,若没有4.0则是int32

print(vector[1:3])#[2,3]从1开始不包括3

matrix = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(matrix[:,1])#[10 25 40] :指所有的部分

print(matrix[:,0:2])#[[ 5 10]  [:,0:2] :代表取所有的行，列取前两列
                    # [20 25]
                    #[35 40]]
print(matrix[1:3,0:2])#取后两行，前两列

vector = np.array(["1","2","3"])
print(vector.dtype)
vector = vector.astype(float)
print(vector.dtype)

matrix = matrix = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(matrix.sum(axis=1))#按行求和
print(matrix.sum(axis=0))#按列求和

a = np.arange(15)
print(a)
b = a.reshape(3,5)#改成3行5列
print(b)

print(np.zeros((3,4)))

a = np.ones((2,3,4),dtype=np.int32)
print(a)

c = np.random.random((2,3))
print(c)

from numpy import pi
d = np.linspace(0,2*pi,100)#0到6.28的平均分布的100个数
print(d)

A = np.array([[1,1],
              [0,1]])
B = np.array([[2,0],
              [3,4]])
print('-------')
print(A*B)#求内积，对应位置相乘
print('-------')
print(A.dot(B))
print('-------')
print(np.dot(A,B))

B = np.arange(3)
print(B)
print(np.exp(B))#  e的B次方
print(np.sqrt(B))#开方

A = np.floor(10*np.random.random((3,4)))#floor向下取整
print(A)
print(A.ravel())#将A变成一维的长度

a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))
print(a)
print(b)
print(np.vstack((a,b)))#按行拼接  4*2
print(np.hstack((a,b)))#按列拼接  2*4

a = np.floor(10*np.random.random((2,12)))
print(a)
print('===')
print(np.hsplit(a,3))#列分3份
print('---')
print(np.hsplit(a,(3,4)))#在第3列和第四列分别切开
a = np.floor(10*np.random.random((12,2)))
print('----')
print(a)
print(np.vsplit(a,3))#行分3份

data = np.sin(np.arange(20)).reshape(5,4)
print(data)
ind = data.argmax(axis=0)#0是按列定义维度，argmax找最大的标签
print(ind)
data_max = data[ind,range(data.shape[1])]
print(data_max)

a = np.array([[4,3,5],[1,2,1]])
print(a)
print('------')
b = np.sort(a,axis=1)#按行排序
print(b)




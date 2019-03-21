import numpy as np
import pandas as pd
df = pd.read_csv('iris.csv')
#print(df.head())

df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']
#print(df.head())

#分离数据x和标签y,iloc：通过选取行（列）位置编号索引数据
X = df.iloc[:,0:4].values
y = df.iloc[:,4].values
print(X)
#print(y)

from matplotlib import  pyplot as plt
import math
#这个打标签和贝叶斯中的那款效果是一样的
label_dict = {1: 'Iris-Setosa',
              2: 'Iris_Versicolor',
              3: 'Iris-Virgnica'}

feature_dict = {0: 'sepal length [cm]',
                1: 'sepal width [cm]',
                2: 'petal length [cm]',
                3: 'petal width [cm]'}

plt.figure(figsize=(8,6))#figsize指定图像的长和宽
for cnt in range(4):
    plt.subplot(2,2,cnt+1)
    for lab in ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'):
        plt.hist(X[y==lab,cnt],
                    label=lab,
                     bins=10,
                     alpha=0.3,)
    plt.xlabel(feature_dict[cnt])
    plt.legend(loc='upper right',fancybox=True,fontsize=8)

plt.tight_layout()
plt.show()

from sklearn.preprocessing import StandardScaler
#
# 标准化数据，保证每个维度的特征数据方差为1，均值为0，使得预测结果不会被某些维度过大的特征值而主导
# fit_transform()先拟合数据
X_std = StandardScaler().fit_transform(X)
#print(X_std)
print(X_std.shape)#(150,4)

mean_vec = np.mean(X_std,axis=0)#axis = 0得到按列计算得到的均值
#print((mean_vec).shape)#(4,)
#print((X_std-mean_vec).shape)
#协方差矩阵公式 (150,4)维度的矩阵-(4，)这个时候就会用行来减，减150次
cov_mat = (X_std-mean_vec).T.dot((X_std-mean_vec))/(X_std.shape[0]-1)#149
#print('Covariance matrix \n%s' %cov_mat)
#print(cov_mat.shape)

#numpy也有提供的协方差矩阵的计算函数
print('Numpy covariance matrux: \n%s'%np.cov(X_std.T))

eig_vals, eig_vecs = np.linalg.eig(cov_mat)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)#特征值大小差异代表当前特征向量的重要程度

# Make a list of (eigenvalue, eigenvector) tuples  #abs这个函数是取绝对值
eig_pairs = [(np.abs(eig_vals[i]),eig_vecs[:,i])for i in range(len(eig_vals))]
print(eig_pairs)
print('-------')
# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort(key=lambda x: x[0],reverse=True)
# Visually confirm that the list is correctly sorted by decreasing eigenvalues
print('Eigenvalues in descending order:')
for i in eig_pairs:
    print(i[0])

#归一化操作，数据加起来等于1
tot = sum(eig_vals)
#eig_vals里的值挨个和tot比较
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
print (var_exp)#[72.96244541329986, 22.850761786701774, 3.6689218892828808, 0.5178709107154879]加起来可以等于100了
cum_var_exp = np.cumsum(var_exp)
cum_var_exp
#从这上面就可以看到前两个特征是最重要的

a = np.array([1,2,3,4])
print (a)
print ('-----------')
print (np.cumsum(a))#加上之前所有的值[1,3,6,10]

plt.figure(figsize=(6, 4))

plt.bar(range(4), var_exp, alpha=0.5, align='center',
            label='individual explained variance')
plt.step(range(4), cum_var_exp, where='mid',
             label='cumulative explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()

#np.hstack():在水平方向上平铺
#print('eig_pairs ',eig_pairs)
#print(eig_pairs.__sizeof__())
matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1),
                      eig_pairs[1][1].reshape(4,1)))

print('Matrix W:\n', matrix_w)#[[ 0.52106591 -0.37741762]
                               #[-0.26934744 -0.92329566]
                               #[ 0.5804131  -0.02449161]
                               #[ 0.56485654 -0.06694199]]

#降维操作(150,4)*(4,2)降成了(150,2)的维度
Y = X_std.dot(matrix_w)
print(Y)

#没降维之前，随便选两个特征
plt.figure(figsize=(6, 4))
for lab, col in zip(('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'),
                        ('blue', 'red', 'green')):
     plt.scatter(X[y==lab, 0],
                X[y==lab, 1],
                label=lab,
                c=col)
plt.xlabel('sepal_len')
plt.ylabel('sepal_wid')
plt.legend(loc='best')
plt.tight_layout()
#plt.show()

#降维后
plt.figure(figsize=(6, 4))
for lab, col in zip(('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'),
                        ('blue', 'red', 'green')):
     plt.scatter(Y[y==lab, 0],
                Y[y==lab, 1],
                label=lab,
                c=col)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(loc='lower center')
plt.tight_layout()
#plt.show()

from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

x = [[2, 0, 1], [1, 1, 2], [2, 3, 3]]
y = [0, 0, 1]  # 分类标记
clf = svm.SVC(kernel='linear')  # SVM模块，svc,线性核函数
clf.fit(x, y)
print(clf)
print(clf.support_vectors_)  # 支持向量点
print(clf.support_)  # 支持向量点的索引
print(clf.n_support_)  # 每个class有几个支持向量点

#展示图
np.random.seed(0)
x = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]  # 正态分布来产生数字,20行2列*2
y = [0] * 20 + [1] * 20  # 20个class0，20个class1

clf = svm.SVC(kernel='linear')
clf.fit(x, y)

w = clf.coef_[0]  # 获取w
a = -w[0] / w[1]  # 斜率
# 画图划线
xx = np.linspace(-5, 5)  # (-5,5)之间x的值
yy = a * xx - (clf.intercept_[0]) / w[1]  # xx带入y，截距

# 画出与点相切的线
b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

print("W:", w)
print("a:", a)

print("support_vectors_:", clf.support_vectors_)
print("clf.coef_:", clf.coef_)

plt.figure(figsize=(8, 4))
plt.plot(xx, yy)
plt.plot(xx, yy_down)
plt.plot(xx, yy_up)
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80)
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Paired)  # [:，0]列切片，第0列

plt.axis('tight')

plt.show()
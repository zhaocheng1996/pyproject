#随机森林分类预测泰坦尼尼克号幸存者

import pandas as pd
import numpy as np

# 数据预处理前期工作：
# 筛选特征值，丢掉不需要的特征数据
# 对性别进行二值化处理（转换为0和1）
# 港口转换成数值型数据
# 处理缺失值（如年龄，有很多缺失值）

def read_dataset(fname):#index_col为指定数据中哪一列作为Dataframe的行索引
#     指定第一列作为行索引
    data = pd.read_csv(fname,index_col=0)
#     丢弃无用数据
    data.drop(['Name','Ticket','Cabin'],axis=1,inplace=True)
#处理性别数据
    lables = data['Sex'].unique().tolist()
    #print(lables)#去重后这个labels中就剩下[male,female]了
    #假设有函数
    #def test(a, b, c)
    #test(*args)：* 的作用其实就是把序列 args 中的每个元素，当作位置参数传进去。比如上面这个代码，如果 args 等于 (1,2,3)
    #，那么这个代码就等价于 test(1, 2, 3) 。
    # test(**kwargs)：** 的作用则是把字典 kwargs 变成关键字参数传递。比如上面这个代码，如果 kwargs 等于 {‘a’:1,’b’:2,’c’:3} ，
    # 那这个代码就等价于 test(a=1,b=2,c=3) 。
    #index返回索引位置，male就是0，female就是1
    data['Sex'] = [*map(lambda x: lables.index(x),data['Sex'])]
#   处理登船港口数据
    lables = data['Embarked'].unique().tolist()
    #print(lables)#港口这个时候为['S', 'C', 'Q', nan]，依旧由下面的代码处理成0，1的形式
    data['Embarked'] = data['Embarked'].apply(lambda n:lables.index(n))
    #print(data.head(5))
    #处理缺失数据填充0
    data = data.fillna(0)
    return data
train = read_dataset('titanic_train.csv')
#把Survived列提取出来作为标签，然后在元数据集中将其丢弃。同时拆分数据集和交叉验证数据集

from sklearn.model_selection import train_test_split

y = train['Survived'].values
X = train.drop(['Survived'],axis=1).values#删除drop列需要加axis=1

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
#X_train_shape: (712, 7)  y_train_shape: (712,)
#X_test_shape: (179, 7)   y_test_shape: (179,)

#拟合数据集
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X_train,y_train)
print("train score:",clf.score(X_train,y_train))
print("test score:",clf.score(X_test,y_test))

# 优化模型参数
# 1、通过max_depth参数来优化模型
# 从以上输出数据可以看出，针对训练样本评分很高，但针对测试数据集评分较低。
# 很明显这是过拟合的特征。解决决策树过拟合的方法是剪枝，包括前剪枝和后剪枝。
# 但是sklearn不支持后剪枝，这里通过max_depth参数限定决策树深度，在一定程度上避免过拟合。
# 这里先创建一个函数使用不同的模型深度训练模型，并计算评分数据。

def cv_score(d):
    clf = DecisionTreeClassifier(max_depth=d)
    clf.fit(X_train, y_train)
    return(clf.score(X_train, y_train), clf.score(X_test, y_test))
   #cv_score返回的是，[train_scores,test_scores]
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
depths = np.arange(1,10)#depths为1~9
scores = [cv_score(d) for d in depths]
tr_scores = [s[0] for s in scores]
#print('tr_scores:',tr_scores)
te_scores = [s[1] for s in scores]
#print('te_scores:',te_scores)

# 找出交叉验证数据集评分最高的索引
tr_best_index = np.argmax(tr_scores)#argmax就是找最大
te_best_index = np.argmax(te_scores)

print("bestdepth:", te_best_index+1, " bestdepth_score:", te_scores[te_best_index], '\n')

# 这里由于以上train_test_split方法对数据切分是随机打散的，造成每次用不同的数据集训练模型总得到不同的最佳深度。
# 这里写个循环反复测试，最终验证这里看到最佳的分支深度为5出现的频率最高，
# 初步确定5为深度模型最佳。把模型参数和对应的评分画出来：

from matplotlib import pyplot as plt
depths = np.arange(1,10)
plt.figure(figsize=(6,4),dpi=120)
plt.grid()
plt.xlabel('max depth of decison tree');
plt.ylabel('Scores')
plt.plot(depths,te_scores,label='test_scores')
plt.plot(depths,tr_scores,label='train_scores')
plt.legend()

#plt.show()

#2通过min_impurity_decrease来优化模型
#这个参数用来指定信息墒或者基尼不纯度的阀值，当决策树分裂后，其信息增益低于这个阀值时则不再分裂。
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

def minsplit_score(val):
    clf = DecisionTreeClassifier(criterion='gini',min_impurity_decrease=val)
    clf.fit(X_train,y_train)
    return (clf.score(X_train,y_train),clf.score(X_test,y_test),)

#指定参数范围，分别训练模型并计算得分

vals = np.linspace(0, 0.2, 100)#0到0.2均分100份
scores = [minsplit_score(v) for v in vals]
tr_scores = [s[0] for s in scores]
te_scores = [s[1] for s in scores]

bestmin_index = np.argmax(te_scores)
bestscore = te_scores[bestmin_index]
print('bestmin:',vals[bestmin_index])
print('bestscore:',bestscore)

plt.figure(figsize=(6,4), dpi=120)
plt.grid()
plt.xlabel("min_impurity_decrease")
plt.ylabel("Scores")
plt.plot(vals, te_scores, label='test_scores')
plt.plot(vals, tr_scores, label='train_scores')

plt.legend()
#plt.show()

# 问题：每次使用不同随机切割的数据集得出最佳参数为0.002很接近0，该怎么解读
# 值此为我们找到了两个参数,最佳深度depth=5 和最佳min_impurity_decrease=0.002，下面我来用两个参数简历模型进行测试：

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
from sklearn import metrics

model = DecisionTreeClassifier(max_depth=5, min_impurity_decrease=0.002)
model.fit(X_train, y_train)

print("tees_score:", model.score(X_test, y_test))

y_pred = model.predict(X_test)

print("查准率:",metrics.precision_score(y_test, y_pred))
print("召回率:",metrics.recall_score(y_test, y_pred))
print("F1_score:",metrics.f1_score(y_test, y_pred))





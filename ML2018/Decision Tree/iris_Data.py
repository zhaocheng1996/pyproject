#这个数据集的标签没有改为数字，改为数字就行了

import pandas as pd

iris_data  = pd.read_csv('iris.csv')
iris_data.columns = ['sepal_length_cm','speal_width_cm','petal_length_cm','petal_width_cm','class']
classes = iris_data['class'].unique().tolist()
print(classes)
iris_data['class'] = [*map(lambda x:classes.index(x),iris_data['class'])]

print(iris_data.head())

#print(iris_data.describe())

# import matplotlib.pyplot as plt
# import seaborn as sb
# sb.pairplot(iris_data.dropna(),hue='class')
#
# plt.figure(figsize=(10,10))
# for column_index,column in enumerate(iris_data.columns):
#     if column =='class':
#         continue
#     plt.subplot(2,2,column_index+1)
#     sb.violinplot(x='class',y=column,data=iris_data)
#
# plt.show()

from sklearn.cross_validation import train_test_split
all_inputs = iris_data[['sepal_length_cm','speal_width_cm','petal_length_cm','petal_width_cm','class']].values
all_classes = iris_data['class'].values

(training_inputs,testing_inputs,training_classes,testing_classes) = train_test_split(all_inputs,all_classes,train_size=0.75,random_state=1)

from sklearn.tree import DecisionTreeClassifier #分类树

decision_tree_classifier = DecisionTreeClassifier()

decision_tree_classifier.fit(training_inputs,training_classes)
acc = decision_tree_classifier.score(testing_inputs,testing_classes)
print(acc)

# criterion
#   特征选择标准
#   ‘gini’ or ‘entropy’ (default=”gini”)，前者是基尼系数，后者是信息熵。两种算法差异不大对准确率无影响，信息墒云孙效率低一点，因为它有对数运算.一般说使用默认的基尼系数”gini”就可以了，即CART算法。除非你更喜欢类似ID3, C4.5的最优特征选择方法。
#
#
#   splitter
#   特征划分标准
#   ‘best’ or ‘random’ (default=”best”) 前者在特征的所有划分点中找出最优的划分点。后者是随机的在部分划分点中找局部最优的划分点。 默认的”best”适合样本量不大的时候，而如果样本数据量非常大，此时决策树构建推荐”random” 。
#
#
#   max_depth
#   决策树最大深度
#   int or None, optional (default=None) 一般来说，数据少或者特征少的时候可以不管这个值。如果模型样本量多，特征也多的情况下，推荐限制这个最大深度，具体的取值取决于数据的分布。常用的可以取值10-100之间。常用来解决过拟合
#
#
#   min_impurity_decrease
#   节点划分最小不纯度
#   float, optional (default=0.) 这个值限制了决策树的增长，如果某节点的不纯度(基尼系数，信息增益，均方差，绝对差)小于这个阈值，则该节点不再生成子节点。 sklearn 0.19.1版本之前叫 min_impurity_split
#
#
#   min_samples_split
#   内部节点再划分所需最小样本数
#   int, float, optional (default=2) 如果是 int，则取传入值本身作为最小样本数； 如果是 float，则去 ceil(min_samples_split * 样本数量) 的值作为最小样本数，即向上取整。
#
#
#   min_samples_leaf
#   叶子节点最少样本数
#   如果是 int，则取传入值本身作为最小样本数； 如果是 float，则去 ceil(min_samples_leaf * 样本数量) 的值作为最小样本数，即向上取整。 这个值限制了叶子节点最少的样本数，如果某叶子节点数目小于样本数，则会和兄弟节点一起被剪枝。
#
#
#   max_leaf_nodes
#   最大叶子节点数
#   int or None, optional (default=None) 通过限制最大叶子节点数，可以防止过拟合，默认是”None”，即不限制最大的叶子节点数。如果加了限制，算法会建立在最大叶子节点数内最优的决策树。如果特征不多，可以不考虑这个值，但是如果特征分成多的话，可以加以限制，具体的值可以通过交叉验证得到。
#
#
#   min_impurity_split
#   信息增益的阀值
#   决策树在创建分支时，信息增益必须大于这个阀值，否则不分裂
#
#
#   min_weight_fraction_leaf
#   叶子节点最小的样本权重和
#   float, optional (default=0.) 这个值限制了叶子节点所有样本权重和的最小值，如果小于这个值，则会和兄弟节点一起被剪枝。 默认是0，就是不考虑权重问题。一般来说，如果我们有较多样本有缺失值，或者分类树样本的分布类别偏差很大，就会引入样本权重，这时我们就要注意这个值了。
#
#
#   class_weight
#   类别权重
#   dict, list of dicts, “balanced” or None, default=None 指定样本各类别的的权重，主要是为了防止训练集某些类别的样本过多，导致训练的决策树过于偏向这些类别。这里可以自己指定各个样本的权重，或者用“balanced”，如果使用“balanced”，则算法会自己计算权重，样本量少的类别所对应的样本权重会高。当然，如果你的样本类别分布没有明显的偏倚，则可以不管这个参数，选择默认的”None” 不适用于回归树 sklearn.tree.DecisionTreeRegressor
#

import pandas as pd
import numpy as np
food_info = pd.read_csv("food_info.csv")
print(type(food_info))
print(food_info.shape)
#print(food_info.head(3))#看前三行
#print(food_info.columns)#打印列的标签名
#print(food_info.tail(3))#最后三个

#print(food_info.loc[0])#看第一行的数据

#print(ndb_col = food_info["NDB_No"])

col_names = food_info.columns.tolist()
print(col_names)
gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
gram_df = food_info[gram_columns]
#print(gram_df.head(3))

#pint(food_info["Iron_(mg)"])##  #
div_1000 = food_info["Iron_(mg)"]/1000
print(div_1000)

#food_info.sort_values("odium_(mg)",inplace=True)#inplace=True直接对原对象修改，不创建新的对象

titanic_survival = pd.read_csv("titanic_train.csv")
#print(titanic_survival.head())

#age那列不满，现在要把它填充上
age = titanic_survival["Age"]
age_is_null = pd.isnull(age)

print(age_is_null)
age_null_true = age[age_is_null]
print(age_null_true)
age_null_count = len(age_null_true)
print(age_null_count)

good_ages = titanic_survival["Age"][age_is_null == False]
correct_mean_age = sum(good_ages)/len(good_ages)
print(correct_mean_age)

#pandnas直接的mean()方法自动不算缺失值
correct_mean_age = titanic_survival["Age"].mean()
print(correct_mean_age)

#每个仓的平均价格
passenger_classes = [1,2,3]
fares_by_class = {}#字典
for this_class in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival["Pclass"]==this_class]
    pclass_fares = pclass_rows["Fare"]
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fare_for_class
print(fares_by_class)

#获救和船舱等级的关系
#pivot_table   index(标签) values()不同的Pclass对应于不同的Survived，aggefunc 按平均值进行统计
passenger_survival = titanic_survival.pivot_table(index="Pclass",values="Survived",aggfunc=np.mean)
print(passenger_survival)
#pivot.table方法默认就是算均值
passenger_age = titanic_survival.pivot_table(index="Pclass",values="Age")
print(passenger_age)

port_stats = titanic_survival.pivot_table(index="Embarked",values=["Fare","Survived"],aggfunc=np.sum)
print(port_stats)

#指定一行或者一列把缺失值直接去掉,把有缺失值的都去掉
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0,subset=["Age","Sex"])

#loc定位  看多少号的样本
row_index_83_age = titanic_survival.loc[83,"Age"]
row_index_1000_pclass =  titanic_survival.loc[766,"Pclass"]
print(row_index_83_age)
print(row_index_1000_pclass)


#排序按Age降序排序
new_titanic_survival = titanic_survival.sort_values("Age",ascending=False)
print(new_titanic_survival[0:10])
titanic_reindexed = new_titanic_survival.reset_index(drop=True)
print("------")
print(titanic_reindexed.loc[0:10])

print('------------')

fandango = pd.read_csv("fandango_score_comparison.csv")
series_film = fandango["FILM"]
print(type(series_film))
print(series_film[0:5])
series_rt = fandango['RottenTomatoes']
print(series_rt[0:5])

from pandas import Series

film_names = series_film.values
#print(type(film_names))
rt_scores = series_rt.values
#print(rt_scores)
series_custom = Series(rt_scores,index=film_names)
series_custom[['Minions (2015)','Leviathan (2014)']]
#print(series_custom)
fiveten = series_custom[5:10]
print(fiveten)
print('----------')
#重新安排排序好的标签
original_index = series_custom.index.tolist()#对电影标签做一个序列
sorted_index = sorted(original_index)#对电影标签序列按字母排序
sorted_by_index = series_custom.reindex(sorted_index)#重打标签
print(sorted_by_index)

#自带的排序方法
sc2 = series_custom.sort_index()#按索引排序
sc3 = series_custom.sort_values()#按值排序




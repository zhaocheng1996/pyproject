import pandas as pd
import os #导入os模块
encoding = 'latin1'# 格式设置成“latinl""
#用pandas.read_table讲各个表分别读到一个pandas Dataframe对像中
#pandas 有两种数据格式Dataframe表示一个表格，类似表格的数据结构；Series是一个一维的类似的数组对象，包含一个数组的数据
#和一个与数组关联的数据标签，被叫做索引，最简单的Series是由一个数组的数据构成：

#os.path模块重要用于文件的属性获取，
#os.path.expanduser(path)  #把path中包含的"~"和"~user"转换成用户目录
#os.path.expandvars(path)  #根据环境变量的值替换path中包含的”$name”和”${name}”
upath = os.path.expanduser('ml-1m/users.dat')
rpath = os.path.expanduser('ml-1m/ratings.dat')
mpath = os.path.expanduser('ml-1m/movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']#设列名称
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)
#这里是用pd.read_cav读取文件 #sep="::"表示记录用“：”隔开如果记录使用“，”就sep=","
#header=None默认无，encoding=encoding默认编码如utf-8

print(users.head())
print(ratings.head())
print(movies.head())





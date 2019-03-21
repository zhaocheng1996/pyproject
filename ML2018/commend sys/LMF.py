
# 使用Tensorflow构造隐语义模型的推荐系统¶
# 3900 个电影 6,040个用户
# 数据简介: http://files.grouplens.org/datasets/movielens/ml-1m-README.txt
# 数据下载地址：http://files.grouplens.org/datasets/movielens/ml-1m.zip

# Imports for data io operations
from collections import deque #一个双端操作的list
from six import next
import readers
import pandas as pd

# Main imports for training
import tensorflow as tf
import numpy as np

# Evaluate train times per epoch
import time

# Constant seed for replicating training results
# seed( ) 用于指定随机数生成时所用算法开始的整数值。
# 1.如果使用相同的seed( )值，则每次生成的随即数都相同；
# 2.如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。
# 3.设置的seed()值仅一次有效
np.random.seed(42)

u_num = 6040 # Number of users in the dataset
i_num = 3952 # Number of movies in the dataset

batch_size = 1000 # Number of samples per batch
dims = 5          # 数据尺寸, 15
max_epochs = 50   # 网络查看所有培训数据的次数

# Device used for all computations
place_device = "/cpu:0"

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
rnames = ['user', 'item', 'rate', 'timestamp']#item=movie_id user=user_id
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)
#这里是用pd.read_cav读取文件 #sep="::"表示记录用“：”隔开如果记录使用“，”就sep=","
#header=None默认无，encoding=encoding默认编码如utf-8

df = ratings
rows = len(df)#1000209
# Purely integer-location based indexing for selection by position
# 按位置选择的基于数据的整数位置索引的维度
df = df.iloc[np.random.permutation(rows)].reset_index(drop=True)
# Separate data into train and test, 90% for train and 10% for test
split_index = int(rows * 0.9)
# Use indices to separate the data
df_train = df[0:split_index]
df_test = df[split_index:].reset_index(drop=True)
#print(df_test)#100021*4的矩阵

# def get_data():
#     # Reads file using the demiliter :: form the ratings file
#     # Columns are user ID, item ID, rating, and timestamp
#     # Sample data - 3::1196::4::978297539
#     df = readers.read_file("./ml-1m/ratings.dat", sep="::")
#     rows = len(df)#1000209
#     # Purely integer-location based indexing for selection by position
#     # 按位置选择的基于数据的整数位置索引的维度
#     df = df.iloc[np.random.permutation(rows)].reset_index(drop=True)
#     # Separate data into train and test, 90% for train and 10% for test
#     split_index = int(rows * 0.9)
#     # Use indices to separate the data
#     df_train = df[0:split_index]
#     df_test = df[split_index:].reset_index(drop=True)
#     #print(df_test)#100021*4的矩阵
#     return df_train, df_test

def clip(x):#clip这个函数将将数组中的元素限制在a_min, a_max之间，大于a_max的就使得它等于 a_max，小于a_min,的就使得它等于a_min。
    return np.clip(x, 1.0, 5.0)


def model(user_batch, item_batch, user_num, item_num, dim=5, device=place_device):
    with tf.device(place_device):
        with tf.variable_scope('lsi', reuse=True):#文件管理器，给tensorboard用的
            # Using a global bias term使用全局偏倚项
            bias_global = tf.get_variable("bias_global", shape=[],initializer=tf.random_normal_initializer())
            # User and item bias variables
            # get_variable: Prefixes the name with the current variable scope用当前变量范围前缀名称
            # and performs reuse checks.执行重用检查
            #w_bias_user为一维的tensor，shape为(user_num,)的向量
            #tf.get_variable也就是一个初始化方法
            w_bias_user = tf.get_variable("embd_bias_user", shape=[user_num],initializer=tf.random_normal_initializer())
            w_bias_item = tf.get_variable("embd_bias_item", shape=[item_num],initializer=tf.random_normal_initializer())
            # embedding_lookup: Looks up 'ids' in a list of embedding tensors
            # Bias embeddings for user and items, given a batch
            # embedding_lookup： 返回的bias_user会是w_bias_user中，下标为user_batch的新矩阵shape为[len(user_batch),1]
            bias_user = tf.nn.embedding_lookup(w_bias_user, user_batch, name="bias_user")
            bias_item = tf.nn.embedding_lookup(w_bias_item, item_batch, name="bias_item")
            # User and item weight variables      [user_num,5]
            w_user = tf.get_variable("embd_user", shape=[user_num, dim],
                                     initializer=tf.truncated_normal_initializer(stddev=0.02))
            w_item = tf.get_variable("embd_item", shape=[item_num, dim],
                                     initializer=tf.truncated_normal_initializer(stddev=0.02))
            # 给定批处理的用户和项目的权重嵌入
            # embd_user 维度为 [len(user_batch),]
            embd_user = tf.nn.embedding_lookup(w_user, user_batch, name="embedding_user")
            embd_item = tf.nn.embedding_lookup(w_item, item_batch, name="embedding_item")

    with tf.device(device):
        # reduce_sum: Computes the sum of elements across dimensions of a tensor
        infer = tf.reduce_sum(tf.multiply(embd_user, embd_item), 1)#对行求和,infer=一个数
        infer = tf.add(infer, bias_global)
        infer = tf.add(infer, bias_user)
        infer = tf.add(infer, bias_item, name="svd_inference")
        # l2_loss: Computes half the L2 norm of a tensor without the sqrt
        regularizer = tf.add(tf.nn.l2_loss(embd_user), tf.nn.l2_loss(embd_item),
                             name="svd_regularizer")
    return infer, regularizer

def loss(infer, regularizer, rate_batch, learning_rate=0.001, reg=0.1, device=place_device):
    with tf.device(device):
        # Use L2 loss to compute penalty
        cost_l2 = tf.nn.l2_loss(tf.subtract(infer, rate_batch))#infer-rate_batch
        penalty = tf.constant(reg, dtype=tf.float32, shape=[], name="l2")#penalty=0.1
        cost = tf.add(cost_l2, tf.multiply(regularizer, penalty))
        # 'Follow the Regularized Leader' optimizer
        train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
    return cost, train_op

# Read data from ratings file to build a TF model
#df_train, df_test = get_data()

samples_per_batch = len(df_train) // batch_size
print("Number of train samples %d, test samples %d, samples per batch %d" %
      (len(df_train), len(df_test), samples_per_batch))
#Number of train samples 900188, test samples 100021, samples per batch 900

# Peeking at the top 5 user values
print(df_train["user"].head())
print(df_test["user"].head())

# Peeking at the top 5 item values
print(df_train["item"].head())
print(df_test["item"].head())

# Peeking at the top 5 rate values
print(df_train["rate"].head())
print(df_test["rate"].head())


# 使用迭代器生成随机批次，用于训练
iter_train = readers.ShuffleIterator([df_train["user"],
                                     df_train["item"],
                                     df_train["rate"]],
                                     batch_size=batch_size)

#顺序生成一个历元批次，用于测试
iter_test = readers.OneEpochIterator([df_test["user"],
                                     df_test["item"],
                                     df_test["rate"]],
                                     batch_size=-1)

user_batch = tf.placeholder(tf.int32, shape=[None], name="id_user")
item_batch = tf.placeholder(tf.int32, shape=[None], name="id_item")
rate_batch = tf.placeholder(tf.float32, shape=[None])

infer, regularizer = model(user_batch, item_batch, user_num=u_num, item_num=i_num, dim=dims, device=place_device)
_, train_op = loss(infer, regularizer, rate_batch, learning_rate=0.0010, reg=0.05, device=place_device)

saver = tf.train.Saver()
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print("%s\t%s\t%s\t%s" % ("Epoch", "Train Error", "Val Error", "Elapsed Time"))
    errors = deque(maxlen=samples_per_batch)
    start = time.time()
    for i in range(max_epochs * samples_per_batch):
        users, items, rates = next(iter_train)
        _, pred_batch = sess.run([train_op, infer], feed_dict={user_batch: users,item_batch: items,rate_batch: rates})

        pred_batch = clip(pred_batch)
        errors.append(np.power(pred_batch - rates, 2))
        if i % samples_per_batch == 0:
            train_err = np.sqrt(np.mean(errors))
            test_err2 = np.array([])
            for users, items, rates in iter_test:
                pred_batch = sess.run(infer, feed_dict={user_batch: users,
                                                        item_batch: items})
                pred_batch = clip(pred_batch)
                test_err2 = np.append(test_err2, np.power(pred_batch - rates, 2))
            end = time.time()

            print("%02d\t%.3f\t\t%.3f\t\t%.3f secs" % (
            i // samples_per_batch, train_err, np.sqrt(np.mean(test_err2)), end - start))
            start = end

    saver.save(sess, './save/')

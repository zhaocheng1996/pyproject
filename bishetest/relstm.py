#!/usr/bin/env python
# coding=utf-8
# author: Tony

import csv
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.contrib import rnn
import os
import matplotlib.pyplot as plt

# load data
x_data = []
y_data = []
with open('total_week.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        row = [float(i) for i in row]
        x_data.append(row[2:])
        y_data.append(row[1])

row = np.shape(x_data)[0]
col = np.shape(x_data)[1]

# import data
train_start = 0
train_end = int(np.floor(0.8 * row))
test_start = train_end + 1
test_end = row
#x_train = x_data[train_start:train_end]
#y_train = y_data[train_start:train_end]
x_test = x_data[test_start:test_end]
y_test = y_data[test_start:test_end]

# scaler = MinMaxScaler()#将数据处理为0到1分布
# scaler.fit(x_train)
# scaler.transform(x_train)
# scaler.transform(x_test)
#y_train=scaler.transform(y_train)
#y_test=scaler.transform(y_test)

#x_train = np.array(x_train)
#y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

# define hype param
epcho = 29000 #训练次数
#learning_rate = 0.001 #学习率
#training_iters = 10000
#batch_size = len(y_train) #批次长度
display_step = 2  #损失率展示步长

# define lstm param
#num_layers = 2#RNN的层数
n_input = 1  #输入维度
n_steps = 6  #步长
n_hidden = 80  #隐藏层单元数
n_classes = 1  #输出分类

X = tf.placeholder(tf.float32, shape=[None, n_steps, n_input], name='lstm_inputX') #占位符
Y = tf.placeholder(tf.float32, shape=[None, n_classes],name='lstm_Y')

# Define weights
weights = {
    'out': tf.Variable(tf.truncated_normal([n_hidden, n_classes]), name='lstm_weight')#w给隐藏层用的，隐藏层设定了20层
}
biases = {
    'out': tf.Variable(tf.random_normal([n_classes]), name='lstm_bais')
}

#训练模型及存储模型
ckpt_dir = "./ckpt_dir"
if not os.path.exists(ckpt_dir):
    os.makedirs(ckpt_dir)

#定义一个计数器，设置trainable=False，不需要被训练
#global_step = tf.Variable(0, name='global_step', trainable=False)

#声明完所有变量后，调用存储器
# Call this after declaring all tf.Variables.
saver = tf.train.Saver()
#saver = tf.train.import_meta_graph("./ckpt_dir/model.ckpt-5851.meta")
#位于tf.train.Saver之后的变量将不会被存储
# This variable won't be stored, since it is declared after tf.train.Saver()
#non_storable_variable = tf.Variable(777)


def RNN(x, weights, biases):
    x = tf.unstack(x, n_steps, 1)#按列拆成6个
    with tf.variable_scope('lstm'):
        lstm_cell = rnn.BasicLSTMCell(n_hidden, forget_bias=1.0,state_is_tuple = True)#第一个参数代表lstm种神经元的大小
        #static_rnn的输入不足要设置步长，x此时为6个[182,1]，而另外一种dynamic_rnn输入的x的结构则是[batch,步长,input]
        #lstm_cell = rnn.MultiRNNCell([RNN(X, weights, biases) for i in range(3)], state_is_tuple=True)
        # init_state=lstm_cell.zero_state(batch_size,dtype=tf.float32)
        #lstm_cell = rnn.DropoutWrapper(lstm_cell, input_keep_prob=1.0, output_keep_prob=0.5)
        outputs, states = rnn.static_rnn(lstm_cell, x ,dtype=tf.float32)
        # Linear activation, using rnn inner loop last output
        return tf.add(tf.matmul(outputs[-1], weights['out']), biases['out'], name='op_lstm_output')
pred = RNN(X, weights, biases)

# with tf.name_scope('cost'):
#     cost = tf.reduce_mean(tf.squared_difference(pred, Y))
#     train_op = tf.train.AdamOptimizer(learning_rate).minimize(cost)

with tf.name_scope("accuracy"):
    acc_op = tf.reduce_mean(tf.squared_difference(pred, Y))

with tf.Session() as sess:
    tf.global_variables_initializer().run()
    #tf.initialize_all_variables().run()

    ckpt = tf.train.get_checkpoint_state(ckpt_dir)
    if ckpt and ckpt.model_checkpoint_path:
        print(ckpt.model_checkpoint_path)
        saver.restore(sess, ckpt.model_checkpoint_path)  # restore all variables

    # meta_graph_or_file = "./ckpt_dir/model.ckpt-5851.meta"
    # saver = tf.train.import_meta_graph(meta_graph_or_file="./ckpt_dir/model.ckpt-5851.meta")
    # model_file = tf.train.latest_checkpoint(checkpoint_dir="ckpt_dir")
    # saver.restore(sess=sess, save_path=model_file)
    #
    # init graph
    # graph = tf.get_default_graph()
    #
    # # get placeholder from graph
    #
    # x_test = graph.get_tensor_by_name("lstm_inputX:0")
    # y_test = graph.get_tensor_by_name("lstm_Y:0")
    #
    x_test = x_test.reshape((len(y_test), n_steps, n_input))
    y_test = y_test.reshape(len(y_test), 1)

    #acc = sess.run(acc_op, feed_dict={X: x_test, Y: y_test})
    y_pred=sess.run(pred,feed_dict={X :x_test})
    #print(y_pred)

    acc_op = tf.reduce_mean(tf.squared_difference(pred, y_test))
    print("loss:",acc_op)


fig = plt.figure()
# ’b'指的是蓝色，‘r’指的是红色
plt.plot(range(len(y_pred)), y_pred, 'b', label='predict')
plt.plot(range(len(y_pred)), y_test, 'r', label='test')
plt.xlabel('week')
plt.ylabel('priceindex')
plt.legend(loc='upper right')  # 加标签右上
plt.show()

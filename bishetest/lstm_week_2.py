#!/usr/bin/env python
# coding=utf-8
# author: Tony

import csv
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.contrib import rnn
import os

# load data
x_data = []
y_data = []
with open('total_week手版.csv') as csvfile:
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
x_train = x_data[train_start:train_end]
y_train = y_data[train_start:train_end]
x_test = x_data[test_start:test_end]
y_test = y_data[test_start:test_end]

scaler = MinMaxScaler()#将数据处理为0到1分布
scaler.fit(x_train)
#x_train=scaler.transform(x_train)
#x_test=scaler.transform(x_test)

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

# define hype param
epcho = 29000 #训练次数
learning_rate = 0.001 #学习率
#training_iters = 10000
batch_size = len(y_train) #批次长度处理182个
display_step = 3  #损失率展示步长

# define lstm param
num_layers = 2#RNN的层数
n_input = 1  #输入维度
n_steps = 6  #步长
n_hidden =80  #隐藏层单元数
n_classes = 1  #输出分类

X = tf.placeholder(tf.float32, shape=[None, n_steps, n_input], name='lstm_inputX') #占位符
Y = tf.placeholder(tf.float32, shape=[None, n_classes])

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
global_step = tf.Variable(0, name='global_step', trainable=False)

#声明完所有变量后，调用存储器
# Call this after declaring all tf.Variables.

saver = tf.train.Saver()
#位于tf.train.Saver之后的变量将不会被存储
# This variable won't be stored, since it is declared after tf.train.Saver()
#non_storable_variable = tf.Variable(777)


def RNN(x, weights, biases):
    x = tf.unstack(x, n_steps, 1)#按列拆成6个二维的矩阵
    # x = tf.reshape(x,[-1,n_steps,n_hidden])
    # print('x:',x.shape)
    # with tf.variable_scope('lstm_week'):
    #     lstm_cells = rnn.BasicLSTMCell(num_units=n_hidden,forget_bias=1.0,state_is_tuple = True)
    #                  #for layer in range(num_layers)
    #     # 使用 DropoutWrapper 类来实现 dropout 功能，input_keep_prob 控制输出的 dropout 概率
    #     lstm_cells =rnn.DropoutWrapper(lstm_cells, output_keep_prob=0.5)
    #
    #     multi_cell = rnn.MultiRNNCell([lstm_cells] * num_layers,state_is_tuple=True)
    #
    #     init_state=multi_cell.zero_state(batch_size,dtype=tf.float32)
    #     outputs, states = tf.nn.dynamic_rnn(multi_cell, x ,initial_state=init_state,dtype=tf.float32)
    #     h_state=states[-1][1]
    lstm_cell = rnn.BasicLSTMCell(n_hidden, forget_bias=1.0,state_is_tuple = True)#第一个参数代表lstm种神经元的大小
    #static_rnn的输入不足要设置步长，x此时为6个[182,1]，而另外一种dynamic_rnn输入的x的结构则是[batch,步长,input]
    #lstm_cell = rnn.MultiRNNCell([lstm_cell] * num_layers, state_is_tuple=True)

        #lstm_cell = rnn.DropoutWrapper(lstm_cell, input_keep_prob=1.0, output_keep_prob=0.5)
    outputs, states = rnn.static_rnn(lstm_cell, x ,dtype=tf.float32)
    # Linear activation, using rnn inner loop last output
        #print('h_state:',h_state.shape)
    return tf.add(tf.matmul(outputs[-1], weights['out']), biases['out'], name='op_lstm_output')


pred = RNN(X, weights, biases)


tf.summary.histogram("weight_summ", weights['out'])
tf.summary.histogram("biases_summ", biases['out'])


# with tf.name_scope('average_error'):
#      deduce=abs(Y-pred)
#      #new_deduce=np.round(deduce,2)
#      error=np.round(deduce/Y,4)
#      average_error=sum(error)/len(Y)
#      #print("average_error",'%.4f%%' % (average_error*100))

with tf.name_scope('cost'):
    cost = tf.reduce_mean(tf.squared_difference(pred, Y))
    train_op = tf.train.AdamOptimizer(learning_rate).minimize(cost)
    tf.summary.scalar("cost", cost)

with tf.name_scope("accuracy"):
    acc_op = tf.reduce_mean(tf.squared_difference(pred, Y))
    tf.summary.scalar("accuracy", acc_op)

with tf.name_scope('loss_rate'):
    cost = tf.reduce_mean(tf.squared_difference(pred, Y))
    average = sum(y_test)/len(y_test)
    Loss_rate= cost/average

with tf.Session() as sess:
    writer = tf.summary.FileWriter("./logs/lstm_logs", sess.graph)  # for 0.8
    merged = tf.summary.merge_all()

    tf.global_variables_initializer().run()

    ckpt = tf.train.get_checkpoint_state(ckpt_dir)
    if ckpt and ckpt.model_checkpoint_path:
        print(ckpt.model_checkpoint_path)
        saver.restore(sess, ckpt.model_checkpoint_path)  # restore all variables

    start1 = global_step.eval()  # get last global_step
    print("Start from:", start1)
    #sess.run(tf.global_variables_initializer())

    step = 1
    epcho_i = 0
#    while epcho_i < epcho:
    for i in range(start1,epcho):
            start=0
            batch_x = x_train[start:start + batch_size]
            batch_y = y_train[start:start + batch_size]

            #print('baych_X:',batch_x.shape)

            global_step.assign(i).eval()
            saver.save(sess, ckpt_dir + "/model.ckpt", global_step=i)

            batch_x = batch_x.reshape((batch_size, n_steps, n_input))
            batch_y = batch_y.reshape(batch_size, 1)

            #训练
            #print('a')
            sess.run(train_op, feed_dict={X: batch_x, Y: batch_y})
            #print(sess.run(pred.shape,feed_dict={X: batch_x}))
            #print('b')
            if i % display_step == 0:
                x_test = x_test.reshape((len(y_test), n_steps, n_input))
                y_test = y_test.reshape(len(y_test), 1)
#                x_train=x_train.reshape(len(y_train),n_steps,n_input)
                summary, acc,loss_rate= sess.run([merged, acc_op, Loss_rate], feed_dict={X: x_test, Y: y_test})
                writer.add_summary(summary, i)  # Write summary
                print('test loss is {}, loss_rate is {}, finished {} training'.format(acc,loss_rate, i))
                #print('test average_error is {}, finished {} training'.format('%.4f%%' % (average_error*100), i))
                #print("wights:", sess.run(weights))
                #print("bias:", sess.run(biases))

         #   step += 1

        #epcho_i += 1
    print("Optimization Finished!")


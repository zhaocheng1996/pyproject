import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import os

#定义权重函数
def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))

#加载数据
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels

X = tf.placeholder("float", [None, 784])
Y = tf.placeholder("float", [None, 10])
#初始化权重参数
w_h = init_weights([784, 625])
w_h2 = init_weights([625, 625])
w_o = init_weights([625, 10])

#定义模型
def model(X, w_h, w_h2, w_o, p_keep_input, p_keep_hidden): # this network is the same as the previous one except with an extra hidden layer + dropout
    X = tf.nn.dropout(X, p_keep_input)
    h = tf.nn.relu(tf.matmul(X, w_h))

    h = tf.nn.dropout(h, p_keep_hidden)
    h2 = tf.nn.relu(tf.matmul(h, w_h2))

    h2 = tf.nn.dropout(h2, p_keep_hidden)

    return tf.matmul(h2, w_o)

#生成网络模型，得到预测值
p_keep_input = tf.placeholder("float")
p_keep_hidden = tf.placeholder("float")
py_x = model(X, w_h, w_h2, w_o, p_keep_input, p_keep_hidden)
print(py_x.shape)#(?, 10)每行有十个元素

#得到预测函数
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=py_x, labels=Y))
train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)
predict_op = tf.argmax(py_x, 1)#返回行上最大的索引

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
non_storable_variable = tf.Variable(777)



#训练模型并存储
with tf.Session() as sess:
    # you need to initialize all variables
    tf.global_variables_initializer().run()

    start = global_step.eval() # get last global_step
    print("Start from:", start)

    for i in range(start, 100):
        for start, end in zip(range(0, len(trX), 128), range(128, len(trX)+1, 128)):
            sess.run(train_op, feed_dict={X: trX[start:end], Y: trY[start:end],
                                          p_keep_input: 0.8, p_keep_hidden: 0.5})

        global_step.assign(i).eval() # set and update(eval) global_step with index, i 更新计数器
        saver.save(sess, ckpt_dir + "/model.ckpt", global_step=i)
        print(i, np.mean(np.argmax(teY, axis=1) ==
                         sess.run(predict_op, feed_dict={X: teX,
                                                         p_keep_input: 1.0,
                                                         p_keep_hidden: 1.0})))

with tf.Session() as sess:
    tf.initialize_all_variables().run()

    ckpt = tf.train.get_checkpoint_state(ckpt_dir)
    if ckpt and ckpt.model_checkpoint_path:
        print(ckpt.model_checkpoint_path)
        saver.restore(sess,ckpt.model_checkpoint_path)#加载所有参数，从这里开始就可以直接使用模型进行预测了，或接着训练


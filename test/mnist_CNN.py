import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

#构建一个CNN模型
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)
#得到训练集的图片和标记的矩阵，以及测试集的额图片和标记的矩阵
trX,trY,teX,teY = mnist.train.images,mnist.train.labels,mnist.test.images,mnist.test.labels

#处理需要输入的数据，把上述trX和trY的形状变成[-1,28,28,1],-1表示不考虑输入图片的数量，
#28X28是图片的长和宽的像素数，1是通道数量
trX = trX.reshape(-1,28,28,1)
teX = teX.reshape(-1,28,28,1)

X=tf.placeholder("float",[None,28,28,1])
Y=tf.placeholder("float",[None,10])

#初始化网络权重和定义网络结构。我们将构建一个拥有3个卷积层和3个池化层，随后接1个全连接层
#和一个输出层的卷积神经网络

#定义初始化权重
def init_weights(shape):
    return tf.Variable(tf.random_normal(shape,stddev=0.01))

#初始化权重方法，设置卷积核大小为3X3
w=init_weights([3,3,1,32])#patch 大小为3X3，输入维度为1，输出维度为32
w2=init_weights([3,3,32,64])
w3=init_weights([3,3,64,128])
w4=init_weights([128*4*4,625])#全连接层，输入维度为128*4*4，是上一层的输出数据又三维的转成一维，输出维度为625
w_o=init_weights([625,10])#输出层，输入维度为625，输出维度为10，代表10类


#神经网络模型的构建函数，传入以下参数
#X:输入数据
#W:每一层的权重
#p_keep_conv,p_keep_hidden：dropout要保留的神经元比例

def model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden):
    #第一组卷积层及池化层，最后dropout一些神经元
    l1a = tf.nn.relu(tf.nn.conv2d(X, w,                       # l1a shape=(?, 28, 28, 32)
                        strides=[1, 1, 1, 1], padding='SAME'))
    l1 = tf.nn.max_pool(l1a, ksize=[1, 2, 2, 1],              # l1 shape=(?, 14, 14, 32)
                        strides=[1, 2, 2, 1], padding='SAME')
    l1 = tf.nn.dropout(l1, p_keep_conv)
    #第二组卷积层及池化层，最后dorpout一些神经元
    l2a = tf.nn.relu(tf.nn.conv2d(l1, w2,                     # l2a shape=(?, 14, 14, 64)
                        strides=[1, 1, 1, 1], padding='SAME'))
    l2 = tf.nn.max_pool(l2a, ksize=[1, 2, 2, 1],              # l2 shape=(?, 7, 7, 64)
                        strides=[1, 2, 2, 1], padding='SAME')
    l2 = tf.nn.dropout(l2, p_keep_conv)
    #第三组
    l3a = tf.nn.relu(tf.nn.conv2d(l2, w3,                     # l3a shape=(?, 7, 7, 128)
                        strides=[1, 1, 1, 1], padding='SAME'))
    l3 = tf.nn.max_pool(l3a, ksize=[1, 2, 2, 1],              # l3 shape=(?, 4, 4, 128)
                        strides=[1, 2, 2, 1], padding='SAME')
    l3 = tf.reshape(l3, [-1, w4.get_shape().as_list()[0]])    # reshape to (?, 2048)
    l3 = tf.nn.dropout(l3, p_keep_conv)
    #全连接层
    l4 = tf.nn.relu(tf.matmul(l3, w4))
    l4 = tf.nn.dropout(l4, p_keep_hidden)
    #输出层
    pyx = tf.matmul(l4, w_o)
    return pyx

#定义dropout的占位符——keep_conv,它表示在一层中有都多少比例的神经元被保留下来。生成网络模型，得到预测值
p_keep_conv = tf.placeholder("float")
p_keep_hidden = tf.placeholder("float")
py_x = model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden)#得到预测操作

#定义损失函数，使用RMSProp算法的RMSPropOptimizer，学习率为0.01，衰减值为0.9，使损失最小；
#cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=py_x, labels=Y))
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y,logits=py_x))
train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)
#定义预测操作
predict_op = tf.argmax(py_x, 1)


#训练模型和评估模型
batch_size = 128#训练时的批次大小
test_size = 256#评估是的批次大小
#启动图
# with tf.Session() as sess:
#     #初始化全局变量
#     tf.global_variables_initializer().run()
#     for i in range(10):
#         training_batch=zip(range(0,len(trX),batch_size),
#                            range(batch_size,len(trX)+1,batch_size))
#         for start,end in training_batch:
#             sess.run(train_op,feed_dict={X:trX[start:end],Y:trY[start:end],
#                                          p_keep_conv:0.8,p_keep_hidden:0.5})
#             test_indices=np.arange(len(teX))
#             np.random.shuffle(test_indices)#shuffle打乱顺序
#             test_indices=test_indices[0:test_size]
#    #  if i % 20 == 0:
#             i+=1
#             print(i,np.mean(np.argmax(teY[test_indices],axis=1)==
#                             sess.run(predict_op,feed_dict={X:teX[test_indices],
#                                                            p_keep_conv:1.0,
#                                                            p_keep_hidden:1.0})))

with tf.Session() as sess:
    # you need to initialize all variables
    tf.global_variables_initializer().run()

    for i in range(100):
        training_batch = zip(range(0, len(trX), batch_size),
                             range(batch_size, len(trX)+1, batch_size))
        for start, end in training_batch:
            sess.run(train_op, feed_dict={X: trX[start:end], Y: trY[start:end],
                                          p_keep_conv: 0.8, p_keep_hidden: 0.5})

        test_indices = np.arange(len(teX)) # Get A Test Batch
        np.random.shuffle(test_indices)
        test_indices = test_indices[0:test_size]

        print(i, np.mean(np.argmax(teY[test_indices], axis=1) ==
                         sess.run(predict_op, feed_dict={X: teX[test_indices],
                                                         p_keep_conv: 1.0,
                                                         p_keep_hidden: 1.0})))





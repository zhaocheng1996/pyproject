
import tensorflow as tf
from tensorflow.contrib import rnn

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#设置训练超参数，设置学习率，训练次数和每轮训练的数据大小
lr=0.001#训练次数
training_iters=100000
batch_size=128

#神经网络的参数
n_inputs=28 #输入层的n
n_steps=28#mnist数据集的大小是28X28，将每一个图像样本看成一行行的序列。共有(28个元素的序列)X(28行),然后每一步的输入的序列长度是28
#输入步数是28步。
n_hidden_units=128  #隐藏层神经元个数
n_classes=10#输出的数量，十个数字

#定义数据和权重
x=tf.placeholder(tf.float32,[None,n_steps,n_inputs])
y=tf.placeholder(tf.float32,[None,n_classes])

#定义权重
weights = {
    #(28,128)
    'in':tf.Variable(tf.random_normal([n_inputs,n_hidden_units])),
   #(128,10)
    'out':tf.Variable(tf.random_normal([n_hidden_units,n_classes]))
}
biases = {
    #(128,)
    'in': tf.Variable(tf.constant(0.1,shape=[n_hidden_units, ])),
    #(10,)
    'out': tf.Variable(tf.constant(0.1,shape=[n_classes, ]))
}

#定义RNN模型
def RNN(X,weights,biases):
    #把输入的X转为X   （128 batch*28steps，28inputs）
    X=tf.reshape(X,[-1,n_inputs])

    #进入隐藏层
    #X_in = 128 batch*28steps，28inputs）
    X_in=tf.matmul(X,weights['in'])+biases['in']
    #X_in (128 batch,28steps，128 hidden)
    X_in=tf.reshape(X_in,[-1,n_steps,n_hidden_units])
    lstm_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden_units,forget_bias=1.0,state_is_tuple=True)
    #初始化为零，lstm单元由两个部分组成：(c_state,h_state)
    init_state = lstm_cell.zero_state(batch_size,dtype=tf.float32)
    #dynamic_rnn接收张量(batch,steps,inputs)
    outputs,final_state=tf.nn.dynamic_rnn(lstm_cell,X_in,initial_state=init_state,time_major=False)
    results=tf.matmul(final_state[1],weights['out'])+biases['out']
    return results

#定义损失函数和优化器
pred = RNN(x,weights,biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=pred,labels=y))
train_op=tf.train.AdamOptimizer(lr).minimize(cost)

#定义模型预测结果机准确率计算方法
correct_pred=tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
accuracy=tf.reduce_mean(tf.cast(correct_pred,tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    step=0
    while step * batch_size < training_iters:
        batch_xs,batch_ys = mnist.train.next_batch(batch_size)
        batch_xs=batch_xs.reshape([batch_size,n_steps,n_inputs])
        sess.run([train_op],feed_dict={
            x:batch_xs,
            y:batch_ys,
        })
        if step %20 ==0:
            print(step,sess.run(accuracy,feed_dict={
                x:batch_xs,
                y:batch_ys,
            }))
        step+=1








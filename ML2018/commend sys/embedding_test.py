import tensorflow as tf;
import numpy as np;

c = np.random.random([10, 1])
b = tf.nn.embedding_lookup(c, [1, 3])

a = np.random.random([10,5])
f = tf.nn.embedding_lookup(a,[2,5])
#d = tf.nn.embedding_lookup(a,[1,3])#预测shape为(2,5)选的是第一行和第三行
d = tf.nn.embedding_lookup(a,3)#shape为(5,) 输出d [0.82966517 0.89779507 0.57941362 0.5271285  0.050316  ]挑的第四行
c_= tf.nn.embedding_lookup(c,2)#挑的第三行的[0.47017075]
e = tf.reshape(d,[5,1])

e_d = tf.multiply(d,e)#[5,5]的矩阵 (5,)*(5,1) (5,)就是1行5列
penalty = tf.constant(0.1, dtype=tf.float32, shape=[], name="l2")

vocabulary_size = 10
embedding_size = 5
#train_sources = [3,5]#和(3,5)的结果一样的shape为(2,5)
#train_sources = (3,4,6)#shape就是(3,5)
train_sources = [1,2,3,4]#shape就是(4,5)拿的第1，2，3，4行
#print("train_sources:",train_sources.__sizeof__())

# 初始化embeddings矩阵,这个就是经过多步训练后最终我们需要的embedding
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))

# 将输入序列转换成embedding表示, [batch_size, embedding_size]
embed = tf.nn.embedding_lookup(embeddings, train_sources)#train_sources是batch_size维的词向量

with tf.Session() as sess:
     sess.run(tf.initialize_all_variables())
     #print(sess.run(penalty))
#     print(sess.run(f))
#     print(sess.run(b))
#     print(c)
#     print(a)
#     print("d",sess.run(d))
#     print("e",sess.run(e))
#     print("e_d",sess.run(e_d))
#     print("c_",sess.run(c_))
     print(sess.run(embeddings))
     print(sess.run(embed))
     print(embed.shape)
#
# print(c.shape)
# print(b.shape)
# print(a.shape)
# print("d",d.shape)
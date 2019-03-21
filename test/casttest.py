import tensorflow as tf
a=tf.constant([True,False,True])
b=tf.reduce_mean(tf.cast(a,tf.float32))

with tf.Session() as sess:
    c=sess.run(b)
    print(c)


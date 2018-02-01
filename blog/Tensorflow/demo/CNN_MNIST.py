#-*-coding:utf-8-*-

import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST/', one_hot=True)

sess=tf.InteractiveSession()

input=tf.placeholder(tf.float32, [None, 784])
label=tf.placeholder(tf.float32, [None, 10])
n_conv=32
n_fc=1024

input_reshape=tf.reshape(input, [-1,28,28,1])

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

W1=weight_variable([5,5,1,n_conv])
b1=bias_variable([n_conv])
conv=tf.nn.relu(conv2d(input_reshape,W1)+b1)
pool=max_pool_2x2(conv)


pool_flat=tf.reshape(pool,[-1, 14*14*n_conv])


W2=weight_variable([14*14*n_conv,n_fc])
b2=bias_variable([n_fc])
fc=tf.nn.relu(tf.matmul(pool_flat, W2)+b2)


W3=weight_variable([n_fc, 10])
b3=bias_variable([10])
output=tf.nn.softmax(tf.matmul(fc, W3)+b3)


loss=-tf.reduce_sum(label*tf.log(output))
train_step=tf.train.AdamOptimizer().minimize(loss)
correct_prediction=tf.equal(tf.argmax(output,1), tf.argmax(label,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction, tf.float32))



tf.global_variables_initializer().run()

for i in range(300):
    x, y=mnist.train.next_batch(50)
    train_step.run({input:x, label:y})
    if i%10==0:
        accuracy_eval=accuracy.eval({input:mnist.test.images, label:mnist.test.labels})
        print('step %d, accuracy %s'%(i,accuracy_eval))
accuracy_eval=accuracy.eval({input:mnist.test.images, label:mnist.test.labels})
print('step %d, accuracy %s'%(300,accuracy_eval))
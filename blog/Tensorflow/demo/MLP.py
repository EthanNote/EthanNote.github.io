#-*-coding:utf-8-*-

import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

sess=tf.InteractiveSession()
train_writer=tf.summary.FileWriter('./train')
data_size=1000

#生成数据
C1=(np.random.randn(data_size, 2)+[-4,-4])
C2=(np.random.randn(data_size, 2)+[4,4])
C3=(np.random.randn(data_size, 2)+[-4,4])
C4=(np.random.randn(data_size, 2)+[4,-4])

CA=np.vstack((C1, C2))
CB=np.vstack((C3, C4))

LA=np.hstack((np.ones([data_size*2, 1]), np.zeros([data_size*2, 1])))
LB=np.hstack((np.zeros([data_size*2, 1]), np.ones([data_size*2, 1])))

input=tf.placeholder(tf.float32, [None, 2], name="input")
n_hidden=200

W1=tf.Variable(tf.truncated_normal([2,n_hidden], stddev=0.1), name="W1")
b1=tf.Variable(tf.truncated_normal([n_hidden]),name="b1")
W2=tf.Variable(tf.truncated_normal([n_hidden,2], stddev=0.1), name="W2")
b2=tf.Variable(tf.truncated_normal([2]), name="b2")

hidden = tf.sigmoid(tf.matmul(input, W1)+b1)
output = tf.nn.softmax(tf.sigmoid(tf.matmul(hidden, W2)+b2))

label = tf.placeholder(tf.float32, [None, 2], name="label")
#loss = tf.reduce_sum((output-label)**2)

loss=-tf.reduce_sum(label * tf.log(output))

train_step = tf.train.AdamOptimizer().minimize(loss)

train_writer.add_graph(sess.graph)
tf.global_variables_initializer().run()
for i in range(10000):
    x=np.vstack((CA, CB))
    y=np.vstack((LA, LB))
    
    train_step.run({input:x, label:y})
    if i%100==0:
        print("step %s  loss %s"%(i, loss.eval({input:x, label:y})))
 
test=np.zeros([0,2])
for x in range(-100,100,2):
    for y in range(-100, 100, 2):
        result=output.eval({input:[[x/10.0,y/10.0]]})
        #print(result)
        if result[0][0]<result[0][1]:
            test=np.vstack((test, [[x/10.0,y/10.0]]))

plt.scatter(test[:,0], test[:, 1], c='green')
plt.scatter(CA[:, 0], CA[:,1])
plt.scatter(CB[:,0], CB[:,1])

plt.show()
train_writer.close()

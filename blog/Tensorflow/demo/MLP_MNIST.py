#-*-coding:utf-8-*-

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import numpy as np

mnist = input_data.read_data_sets('MNIST/', one_hot=True)

sess=tf.InteractiveSession()

input=tf.placeholder(tf.float32, [None, 784])
label=tf.placeholder(tf.float32,[None, 10])

n_hidden=50

W1=tf.Variable(tf.zeros([784, n_hidden]))
b1=tf.Variable(tf.zeros([n_hidden]))

hidden=tf.sigmoid(tf.matmul(input, W1)+b1)

W2=tf.Variable(tf.zeros([n_hidden, 10]))
b2=tf.Variable(tf.zeros([10]))

output=tf.nn.softmax(tf.matmul(hidden,W2)+b2)

loss=-tf.reduce_sum(label*tf.log(output))

train_step=tf.train.AdamOptimizer().minimize(loss)



correct_prediction=tf.equal(tf.argmax(output,1), tf.argmax(label,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
plt.title('Hidden layer size %d'%n_hidden)
plt.xlabel('Train step')
plt.ylabel('Accuracy')
for k in range(5):
    tf.global_variables_initializer().run()
    log=np.zeros([2,101])

    for i in range(10000):
        if i%100==0:
            accuracy_eval=accuracy.eval({input:mnist.test.images, label:mnist.test.labels})
            print('step %d, accuracy %s'%(i,accuracy_eval))
            log[0][i/100]=i
            log[1][i/100]=accuracy_eval
        x, y=mnist.train.next_batch(100)
        train_step.run({input:x, label:y})

    accuracy_eval=accuracy.eval({input:mnist.test.images, label:mnist.test.labels})
    print('step %d, accuracy %s'%(10000,accuracy_eval))
    log[0][100]=10000
    log[1][100]=accuracy_eval

    plt.plot(log[0], log[1])
plt.show()

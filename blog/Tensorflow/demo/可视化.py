#-*-coding:utf-8-*-
#求二元二次函数的极小值
import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

sess = tf.InteractiveSession()
train_writer=tf.summary.FileWriter('./train')

#定义一个二维向量
X=tf.Variable(tf.zeros([2]))

#定义二次函数
Y=(X[0]-1)*(X[0]-1)+(X[1]-2)*(X[1]-2)

#使用梯度下降法对函数进行优化，优化过程在调用train.run 时开始
train=tf.train.GradientDescentOptimizer(0.01).minimize(Y)
train_writer.add_graph(sess.graph)
#初始化变量
tf.global_variables_initializer().run()
for i in range(1000):
	train.run()
train_writer.close()
print(X.eval())
#-*-coding:utf-8-*-
#求二次函数的极小值
import tensorflow as tf
sess=tf.InteractiveSession()

#定义一个变量
x=tf.Variable(tf.zeros([1]))

#定义一个二次函数
y=-2*x*x+x+1

#使用梯度下降法对函数进行优化，优化过程在调用train.run 时开始
train=tf.train.GradientDescentOptimizer(0.01).minimize(y)

#初始化变量
tf.global_variables_initializer().run()
for i in range(1000):
	train.run()

print(x.eval())
#-*-coding:utf-8-*-

import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
sess=tf.InteractiveSession()

#样本点的个数，输入数据的个数
data_size=1000
input_size=100
batch_count=data_size/input_size

#生成数据
C1=(np.random.randn(data_size, 2)).transpose()
C2=(np.random.randn(data_size, 2)+[3,4]).transpose()

#定义输入节点
input_1 = tf.placeholder(tf.float32, [2, input_size])
input_2 = tf.placeholder(tf.float32, [2, input_size])

#直线方程的系数A、B，设置一个初始值
AB=tf.Variable([[-1.0,-1.0]])
A=AB[0][0]
B=AB[0][1]

#定义一个函数，用来计算点(x, y)到直线 Ax + By + 1 = 0 的距离
#距离为负值时表示点位于法向量指向相反的一侧
def distance_to_line(xy):
    return (tf.matmul(AB, xy)+1)/(A**2+B**2)**0.5

#计算输入的点到直线的距离
d1=distance_to_line(input_1)
d2=distance_to_line(input_2)

#定义一个函数，对距离值做评分，评分越高越说明点在法向量指向的一侧
def distance_score(d):
    return tf.reduce_sum(tf.sigmoid(d)**2)

#定义损失函数
loss = -distance_score(d1)-distance_score(-d2)

train_step = tf.train.AdamOptimizer(0.35).minimize(loss)
tf.global_variables_initializer().run()

for n in range(100):
    for i in range(batch_count):
        for j in range(batch_count):
            x1=C1[:,i*input_size:(i+1)*input_size]
            x2=C2[:,j*input_size:(j+1)*input_size] 
            train_step.run({input_1:x1, input_2:x2})
    
    print("step %s    value %s"%(n, [A.eval(), B.eval()]))
   

#绘制数据和直线
plt.scatter(C1[0,:], C1[1, :])
plt.scatter(C2[0,:], C2[1, :])
a=A.eval()
b=B.eval()
a2b2=a**2+b**2

plt.plot([-(a-10*b)/a2b2,-(a+10*b)/a2b2], 
[-(10*a+b)/a2b2,-(-10*a+b)/a2b2])
plt.show()
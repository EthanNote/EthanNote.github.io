import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
sess=tf.InteractiveSession()

X=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
Y_=[1.1, 1.9, 3.1, 3.9, 5.1, 5.9, 7.1, 7.9, 9.1]

k=tf.Variable(0.0)
b=tf.Variable(0.0)
Y=k*X+b

loss=tf.reduce_sum((Y-Y_)*(Y-Y_))

train_step=tf.train.AdamOptimizer(0.05).minimize(loss)

tf.global_variables_initializer().run()

for i in range(1000):  
    train_step.run()

print(k.eval())
print(b.eval())

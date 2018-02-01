# RNN 与 LSTM
## RNN 循环特点
- RNN 层的输入是一个序列，序列中的数值依次经RNN处理
- RNN 的激活函数同时接收当前输入值和上一次输入值
- 与使用全连接层处理序列输入相比，RNN 对数据先后顺序敏感，参数少，能够处理不同长度的输入序列

## LSTM 的特点
- LSTM 是对简单RNN的改进，激活函数的
- LSTM 在RNN的基础上增加了一条数据流，或称为一个状态变量，用来调整激活函数的输出。该数值体现的是遗忘，它的状态值随序列输入不断更新，更新算法被称为 LSTM 的 cell
- RNN 可以看做是 LSTM 的 cell 退化为简单的线性叠加

## Keras 中使用LSTM

```python
from keras.layers import LSTM

model = Sequential()
model.add(Embedding(max_features, 32))
model.add(LSTM(32))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop')
    loss='binary_crossentropy',
    metrics=['acc'])
history = model.fit(input_train, y_train, 
    epoch=10, batch_size=128,
    validation_split=0.2)
```

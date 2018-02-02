<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# Cross Entropy

## 定义

为了训练模型，我们需要定义一个 loss function 来描述模型对问题的分类精度，Loss 越小，代表模型的分类结果与真实值偏差越小，也就是说模型越精确。

对于多分类问题，通常使用 cross-entropy 做为 loss function。 Cross-entropy 最早出自信息论（Information Theory）中的信息熵，然后被用到很多地方。

Cross-entropy 的定义如下：

$$H_{y'}=-\sum_{i}{y'} _ {i} log(y_i)$$

其中 y 是预测的概率分布， y'是真实的概率分布。

## 实现

### API

|名称|作用|
|--- |---|
|tf.reduce_mean | 返回集合中各个元素的平均值 |
|tf.reduce_sum | 返回集合中各个元素的和 |
|tf.log| 对数函数|

#### 注意

tf.reduce_* 系列函数中的参数 reduction_indices 用来控制对哪些下标进行求和，例如 reduce_sum 中使用 reduction_indices = [1] 表示将集合中各个向量的第一个元素加起来

### 示例

```python

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y), reduction_indices = [1]))

```

# One-hot word vector 与 Word embedding

《Deep Learning With Python》 P167, P170, P173

## 单词或字符的 One-hot 编码

- 对文本中所有出现的单词构造 One-hot 编码，编码向量的维数即不同单词的个数

- 构造方法简单，遍历文本，将单词加入到字典中，字典值等于单词出现的序号。根据字典构造 One-hot 编码

- 存储开销大，当文本中的单词很多时，One-hot 编码存在大量的0

## Word embedding

- 使用既定长度的 float vector 对单词进行编码，编码值从文本中学习得到

- 比较常见的向量维数有 256维， 512维， 1024维， 相比之下 One-hot 通常需要用2000维

- 维度能够体现单词之间的关系，代表一种可比性

- Word2Vec 算法是最著名、最成功的 Word embedding 方法之一

## Keras Embedding layer

```python
from keras.layers import Embedding

embedding_layer = Embedding(1000, 64)
```
Embedding 接受两个参数，token个数和向量维数

Embedding layer可以被视为将整数映射到向量的字典
word index -> Embedding layer -> corresponding word vector

Embedding layer的输入是 2D tensor (samples, sequence_length)，即有samples行，每一行都是 sequence_length 个 token 的整数值
Embedding layer的输出是 3D tensor (samples, sequence_length, embedding_dimensionality),即每个 token 从 index 到 vector 增加了一维
Embedding layer的输出可被后续的 RNN layer 或者 1D convolution layer 处理

## 加载IMDB数据集并用 Embedding layer 处理

```python
from keras.datasets import imdb
from keras import preprocessing

max_features = 1000    # 用作特征的单词的个数。
maxlen = 20     # 每段文本保留的单词数

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = max_features)
x_train = preprocessing.sequence.pad_sequence(x_train, maxlen=maxlen)
x_test = preprocessing.sequence.pad_sequence(x_test, maxlen=maxlen）


from keras.models import Sequential
from keras.layers import Flatten, Dense

model = Sequential()

model.add(Embedding(10000, 8, input_length=maxlen))
# Embedding 之后，激活函数的输入是（samples, maxlen, 8）的张量
# 经过Flatten 之后，得到（samples, maxlen*8）的2D张量
model.add(Flatten())

# 添加分类器
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_cross'， metrics=['acc'])
model.summary()

history = model.fit(x_train, y_train, epoch=10, batch_size=32, validation_split=0.2)

```

这里要注意的是，Embedding Layer 的输入指的是训练及分类数据的输入，并非API的输入参数。API接受的两个重要参数是单词表大小和单词向量的大小。当缺省输入序列长度时，表示输入序列长度可变

API文档是这么写的：

```
  # Arguments
    input_dim: int > 0. Size of the vocabulary,
        i.e. maximum integer index + 1.
    output_dim: int >= 0. Dimension of the dense embedding.
    embeddings_initializer: Initializer for the `embeddings` matrix
        (see [initializers](../initializers.md)).
    embeddings_regularizer: Regularizer function applied to
        the `embeddings` matrix
        (see [regularizer](../regularizers.md)).
    embeddings_constraint: Constraint function applied to
        the `embeddings` matrix
        (see [constraints](../constraints.md)).
    mask_zero: Whether or not the input value 0 is a special "padding"
        value that should be masked out.
        This is useful when using [recurrent layers](recurrent.md)
        which may take variable length input.
        If this is `True` then all subsequent layers
        in the model need to support masking or an exception will be raised.
        If mask_zero is set to True, as a consequence, index 0 cannot be
        used in the vocabulary (input_dim should equal size of
        vocabulary + 1).
    input_length: Length of input sequences, when it is constant.
        This argument is required if you are going to connect
        `Flatten` then `Dense` layers upstream
        (without it, the shape of the dense outputs cannot be computed).

  # Input shape
      2D tensor with shape: `(batch_size, sequence_length)`.

  # Output shape
      3D tensor with shape: `(batch_size, sequence_length, output_dim)`.

  Methods defined here:

  __init__(self, input_dim, output_dim, embeddings_initializer='uniform', embeddings_regularizer=None, activity_regularizer=None, embeddings_constraint=None, mask_zero=False, input_length=None, **kwargs)
```

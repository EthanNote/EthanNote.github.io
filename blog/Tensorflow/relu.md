<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML'></script>
# 修正线性单元（Rectified linear unit, ReLU）

在人工神经网络中，rectifier 激活函数的定义为:

$$f(x) = max(0,x)$$

其中x为神经元输入。它的特点被认为更加符合神经元信号激励原理，一个平滑近似

$$f(x) = ln(1+e^x)$$

被称之为softplus 函数。它的导函数

$$f'(x) = \frac{e^x}{e^x +1} = \frac{1}{1+e^{-x}}$$

为logistic函数 



## 变体

### Noisy ReLUs

$$f(x)=max(0,x+Y)$$

其中 $$Y \sim N(0, \sigma(x))$$



### Leaky ReLUs

$$f(x) = \begin{cases} x & \quad \text{if }x>0\\ 0.01x & \quad \text{otherwise}\end{cases}$$

$$f(x) = \begin{cases} x & \quad \text{if }x>0\\ ax & \quad \text{otherwise}\end{cases}$$

$$f(x) = max(x, ax)$$



### ELUs

$$ f(n) =  \begin{cases}    x       & \quad\text{if 	}  x  >= 0\\    a(e^x-1)  & \quad \text{otherwise }\\  \end{cases}$$

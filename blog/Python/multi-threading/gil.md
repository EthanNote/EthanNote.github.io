# 全局解释器锁(GIL)
GIL 是 CPython 解释器内部的一个概念，最初为了使 Python 具备多线程锁功能而实现的一把超级大锁，
以这样的方式实现多线程，也就造成 Python 本质上是单线程运行的。

而在 CPython 以外的解释器实现中不存在GIL。例如 JPython 可以利用 JVM 本身的功能来实现锁机制。
所以 GIL 并不是 Python 语言的特性，在 threading 或者其它模块中没有办法访问 GIL 锁。而在 Python C API 开发中则可以操作GIL。

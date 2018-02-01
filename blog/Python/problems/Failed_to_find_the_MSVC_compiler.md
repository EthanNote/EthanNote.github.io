# Failed to find the MSVC compiler
## 关键词
- MSVC
- https://www.lfd.uci.edu/~gohlke/pythonlibs/

## 问题描述
一些 python 库下载安装时需要使用本地的编译器进行编译，在 Windows 这么一个神坑的系统上编程的话，本地的 C、C++ 编译器往往就指的是 MSVC 了。
如果系统没有安装或者没有配置好 MSVC，就无法对下载好的python库进行编译。比如使用 pip 下载安装 PySide：
```
pip install pyside
```
下载完成后，运行 setup.py 时，就报错了：
```
    Running setup.py install for PySide: finished with status 'error'
    Complete output from command ...\python.exe -u -c ...
    Removing C:\Users\...\PySide\pyside_package
    running install
    running build
    Python architecture is 64bit
    nmake not found. Trying to initialize the MSVC env...
    Searching MSVC compiler version 10.0
    error: Failed to find the MSVC compiler version 10.0 on your system.
```

如果你经常拿 Visual C++ 写程序那倒还好说，可以尝试把编译器所在路径加入到 PATH 环境变量中。

然而，我等 Python 教徒怎能就此妥协，不惜安装 Visual C++ ？

## 解决方法 1
去非官方 python 包网站，下载已编译好的轮子
https://www.lfd.uci.edu/~gohlke/pythonlibs/

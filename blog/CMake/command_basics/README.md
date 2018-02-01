# CMake 命令基础

## project 
设置整个项目的名称、版本，以及启用语言支持
```cmake
project(<PROJECT-NAME> [LANGUAGES] [<language-name>...])
project(<PROJECT-NAME>
        [VERSION <major>[.<minor>[.<patch>[.<tweak>]]]]
        [LANGUAGES <language-name>...])
```

## add_executable
为项目添加可执行文件编译目标，项目经编译后会生成名为<name>的可执行文件，该可执行文件由 source1 等源代码编译得到
```cmake
add_executable(<name> [WIN32] [MACOSX_BUNDLE]
               [EXCLUDE_FROM_ALL]
               source1 [source2 ...])
```

## cmake_minimum_required
设置 CMake 最低版本
```cmake
cmake_minimum_required(VERSION major[.minor[.patch[.tweak]]]
                       [FATAL_ERROR])
```

## 示例 1
```cmake
cmake_minimum_required (VERSION 2.6)
project (Tutorial)
add_executable(Tutorial tutorial.cxx)
```

## set
给某个变量设定一个值
```cmake
set(<variable> <value>... [PARENT_SCOPE])                    # set normal variable
set(<variable> <value>... CACHE <type> <docstring> [FORCE])  # set cache entry
set(ENV{<variable>} <value>...)                              # set environment variable
```
变量是 CMake 语言最基本的存储单元，变量的值都是字符串类型的，一些命令会根据需要将字符串解释为其它类型。set 和 unset 命令显式定义、取消定义一个变量，
一些命令也能更改变量值


## option
提供可供用户选择的选项
```cmake
option(<option_variable> "help string describing option"
       [initial value])
```
用户可以选择 ON 或者 OFF 选项，默认为 OFF


## configure_file 
将文件复制到指定位置并对内容进行修改（模板引擎）
```cmake
configure_file(<input> <output>
               [COPYONLY] [ESCAPE_QUOTES] [@ONLY]
               [NEWLINE_STYLE [UNIX|DOS|WIN32|LF|CRLF] ])
```
将文件 <input> 复制为 <output>，并替换形如 @VAR@ 或者 ${VAR} 的变量引用，每个变量引用都会被替换为对应变量的值，如果变量未定义则替换为空字符串。
此外，形如
```cmake
#cmakedefine VAR ...
```

的输入行会被替换为
```c
#define VAR ...
```

或者
```c
/* #undef VAR */
```

取决于 VAR 是否被赋予了 CMake 赋予了某个不为 if（） 命令返回的 false 常量


## 示例 2
假设源码树中有这样一个名为 foo.h.in 的文件
```c
#cmakedefine FOO_ENABLE
#cmakedefine FOO_STRING "@FOO_STRING@"
```
相邻的 CMakeList.txt 中使用 configure_file 配置头文件
```cmake
option(FOO_ENABLE "Enable Foo" ON)
if(FOO_ENABLE)
  set(FOO_STRING "foo")
endif()
configure_file(foo.h.in foo.h @ONLY)
```
CMake就会在相应的 build 目录下创建 foo.h 如果 FOO_ENABLE 选项设置为 ON， 配置后的文件就会包含：
```c
#define FOO_ENABLE
#define FOO_STRING "foo"
```
否则它会包含：
```c
/* #undef FOO_ENABLE */
/* #undef FOO_STRING */
```
之后用户可以使用 include_directories() 命令将输出目录指定为包含目录

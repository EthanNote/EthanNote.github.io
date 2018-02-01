# Golang 初学者笔记
Go Tour 划重点
## Go Tour
网页版：

https://tour.golang.org

离线版本

下载
```
go get github.com/Go-zh/tour/gotour
```
运行

```
cd $GOPATH/bin
./gotour
```

## 包
每个 Go 程序都是由包组成的，程序运行的入口是包 main。
```go
package main
```

按照惯例，包名与导入路径的最后一个目录一致。

可以编写多个导入语句，不过使用打包的导入语句是更好的形式。
```go
import (
	"fmt"
	"math/rand"
)
```


在 Go 中，首字母大写的名称是被导出的(math.Pi)。在导入包之后，你只能访问包所导出的名字，任何未导出的名字是不能被包外的代码访问的。

## 函数
函数可以没有参数或接受多个参数。注意类型在变量名之后 。
```go
func add(x int, y int) int {
	return x + y
}
```

当两个或多个连续的函数命名参数是同一类型，则除了最后一个类型之外，其他都可以省略。
```go
func add(x, y int) int {
	return x + y
}
```

函数可以返回任意数量的返回值。
```go
func swap(x, y string) (string, string) {
	return y, x
}
```

Go 的返回值可以被命名，并且就像在函数体开头声明的变量那样使用。
返回值的名称应当具有一定的意义，可以作为文档使用。
没有参数的 return 语句返回各个返回变量的当前值。这种用法被称作“裸”返回。
直接返回语句在长的函数中它们会影响代码的可读性。
```go
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}
```

## 变量
var 语句定义了一个变量的列表；跟函数的参数列表一样，类型在后面。
```go
var c, python, java bool
```
就像在这个例子中看到的一样， var 语句可以定义在包或函数级别。

变量定义可以包含初始值，每个变量对应一个。
```go
var i, j int = 1, 2
```
如果初始化是使用表达式，则可以省略类型；变量从初始值中获得类型。
```go
var c, python, java = true, false, "no!"
```
在函数中， := 简洁赋值语句在明确类型的地方，可以用于替代 var 定义。
函数外的每个语句都必须以关键字开始（ var 、 func 、等等）， := 结构不能使用在函数外。

## 类型
Go 的基本类型有Basic types

bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // uint8 的别名

rune // int32 的别名
     // 代表一个Unicode码

float32 float64

complex64 complex128

int，uint 和 uintptr 类型在32位的系统上一般是32位，而在64位系统上是64位。当你需要使用一个整数类型时，你应该首选 int，仅当有特别的理由才使用定长整数类型或者无符号整数类型。

表达式 T(v) 将值 v 转换为类型 T 。与 C 不同的是 Go 的在不同类型之间的项目赋值时需要显式转换。

在定义一个变量却并不显式指定其类型时（使用 := 语法或者 var = 表达式语法）， 变量的类型由（等号）右侧的值推导得出。

变量的定义“打包”在一个语法块中
```go
var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)
```

变量在定义时没有明确的初始化时会赋值为 零值 。

零值是：

数值类型为 0 ，
布尔类型为 false ，
字符串为 "" （空字符串）。

## 常量
常量的定义与变量类似，只不过使用 const 关键字。
```go
const Pi = 3.14
```
常量可以是字符、字符串、布尔或数字类型的值。常量不能使用 := 语法定义。

数值常量是高精度的值 。一个未指定类型的常量由上下文来决定其类型。
```go
const (
	Big   = 1 << 100
	Small = Big >> 99
)

```

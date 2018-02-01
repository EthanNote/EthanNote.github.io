# MMD 模型导入Unity

## 方法1： PmdEditor 导出 Wavefront(.obj) 模型
点击菜单 フアイル -> エケスポート [File -> Export] 导出当前模型

#### 贴图UV坐标错位问题
原因是导出的模型使用贴图坐标左下角为原点，而Unity3D等一些软件使用左上角为原点。可将贴图做一次垂直翻转来修复
#### 颜色错误
可能是导出OBJ模型时，仅导出了漫反射贴图，需要手动在Unity3D或其他软件中手动给材质增加法向量贴图。
也可能是PmdEditor的着色器与Unity3D处理方式不同导致的。

## 方法2： PMX to FBX 转换工具
https://github.com/anydream/Pmx2Fbx (膜拜一番 Orz)

#### Build 所需的工具
- Visual Studio 2013 或更高版本
- AutoDesk FBX SDK

**Build 过程**
1. Clone 源代码
2. 安装FBX SDK
3. 用VS打开源代码中的解决方案文件，如遇到询问是否升级平台工具，选择升级，除非已安装了v120平台工具集。
4. 设置 VC++ 的include 和 path
5. Build

#### #include <vld.h> 报错
注释掉就可以了


# Window Bat 脚本文件语言

## 等待按键代码

```powershell
TIMEOUT /T -1
```

## 设置参数

```powershell
set WorkDir=C:\\Software\\XXXX
```

## 使用参数

```powershell
echo "%WorkDir%\\XXXXXX.exe"
```

## 注释

```powershell
:: (内容注释)
```

## 打开 cmd 命令行 并执行后续命令

```powershell
start cmd /k "cd C:\\Software\\DownImages && echo 开始"
```

## 切换编码为UTF-8

```powershell
chcp 65001
```

## 去掉回显

```powershell
@echo off
```

## 切换路径

如果目标路径与执行文件路径不在一个磁盘中需要先切换盘符
```powershell
D:\XXX\XXX> cd /d C:\
```

```powershell
cd C:\XXX\XXX
```

## 打开执行路径的资源管理器

```powershell
start explorer %cd%
```

## 获取当前路径地址

```powershell
%cd%
```

## 链接学习

* [window bat 文件运行中文乱码](https://www.cnblogs.com/Marydon20170307/p/9321495.html)
* [bat批处理脚本中文乱码问题解决](https://blog.csdn.net/u012815136/article/details/101549751)
* [Windows下的bat文件的@echo off 作用？](https://blog.csdn.net/Fly_as_tadpole/article/details/85177379)
* [Windows的cmd中cd指令无法转换路径怎么办？](https://jingyan.baidu.com/article/656db918ec8211e381249ce8.html)
* [bat中获取当前路径](https://blog.csdn.net/hongkaihua1987/article/details/104560108)

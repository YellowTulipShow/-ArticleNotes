# Window Bat 脚本文件语言

## 等待按键代码

```bat
TIMEOUT /T -1
```

## 设置参数

```bat
set WorkDir=C:\\Software\\XXXX
```

## 使用参数

```bat
echo "%WorkDir%\\XXXXXX.exe"
```

## 注释

```bat
:: (内容注释)
```

## 打开 cmd 命令行 并执行后续命令

```bat
start cmd /k "cd C:\\Software\\DownImages && echo 开始"
```

## 链接学习

* [window bat 文件运行中文乱码](https://www.cnblogs.com/Marydon20170307/p/9321495.html)

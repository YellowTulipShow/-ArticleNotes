﻿# PowerShell

#### 问题: 因为在此系统上禁止运行脚本，解决方法

管理员身份打开 `PowerShell`:

```powershell
set-executionpolicy remotesigned
```

输入 `Y` 即可执行其他 `*.ps1` 文件脚本

#### 使用powershell打开新的powershell窗口, 并执行指定命令

```powershell
Start-Process powershell -ArgumentList "-NoExit","-Command","Write-Host 'ddd'"
```

## 学习链接

* [PowerShell教程](https://www.yiibai.com/powershell)
* [PowerShell：因为在此系统上禁止运行脚本，解决方法](https://www.jianshu.com/p/4eaad2163567)
* [PowerShell do while continue break循环脚本示例](https://blog.51cto.com/543925535/2367541)
* [Split](https://docs.microsoft.com/zh-cn/powershell/module/microsoft.powershell.core/about/about_split?view=powershell-7.2)

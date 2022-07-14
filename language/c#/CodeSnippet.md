# 代码片段

## 应用程序目录获取

```C#
// 获取程序的基目录。
System.AppDomain.CurrentDomain.BaseDirectory

// 获取和设置当前目录(该进程从中启动的目录)的完全限定目录。
System.Environment.CurrentDirectory

// 获取模块的完整路径。
System.Diagnostics.Process.GetCurrentProcess().MainModule.FileName

// 获取应用程序的当前工作目录。
System.IO.Directory.GetCurrentDirectory()

// 获取和设置包括该应用程序的目录的名称。
System.AppDomain.CurrentDomain.SetupInformation.ApplicationBase
```

# window 系统常用命令

## 快捷操作:
快速在文件夹目录中打开cmd:
    文件夹空白处按住shift键鼠标右键选择【在此处打开命令窗口】即可

## 常用应用程序命令:
```powershell
# 远程连接
> mstsc.exe

# 注册表
> regedit
> regedit.exe

# 注册表编辑器
> regedt32

# 系统配置-系统启动项
> msconfig.exe

# 服务
> services.msc

# (ServiceName服务命令)
# 启动服务
> net start
# 关闭服务
> net stop

# 资源监视器
> Resmon

# 计算机
> calc

# 画图
> mspaint

# 打印管理
> printmanagement.msc

# 电源选项 睡眠时间
> powercfg.cpl

# 问题步骤记录器
# (保存出来的 zip 文件夹 .mht 文件需要使用 ie 打开)
> psr


# 服务列表:
# 主题关闭-还原原始window样式, 省资源
# (但好像省不了多少, window10可以试试)
> Themes
```

## 目录相关参数
```powershell
@echo off
echo 当前盘符: %~d0
echo 当前盘符和路径: %~dp0
echo 当前批处理全路径: %~f0
echo 当前盘符和路径的短文件名格式: %~sdp0
echo 当前CMD默认目录: %cd%
echo 目录中有空格也可以加入“避免找不到路径
echo 当前盘符: %~d0
echo 当前盘符和路径: %~dp0
echo 当前批处理全路径: %~f0
echo 当前盘符和路径的短文件名格式: %~sdp0
echo 当前CMD默认目录: %cd%
pause
```

## 参考链接:
```shell
# Win8系统108个运行命令 你能记住多少?
http://win8.zol.com.cn/277/2772193.html
```

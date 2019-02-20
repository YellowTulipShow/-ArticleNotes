# window 系统常用命令

## DNS 修复
静态绑定 `IP` 与网址关联, 配置文件地址为:

`C:\Windows\System32\drivers\etc\host`

文件中如:

```shell
    192.30.253.113  github.com
    151.101.185.194 github.global.ssl.fastly.net
    204.79.197.200 bing.com
```

最后执行 `ipconfig /flushdns` 命令, 刷新 DNS 缓存

## DNS 修复
问题: 连上网络但是不能浏览网页,但能Ping通一些常见域名地址
解决: DHCP问题(重新启动服务), winsock(管理员权限的cmd输入命令: `netsh winsock reset` (说是LSP目录))

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
* [Win8系统108个运行命令 你能记住多少?](http://win8.zol.com.cn/277/2772193.html)

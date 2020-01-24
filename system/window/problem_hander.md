# 问题处理

## 文件夹删不掉, 提示权限不足

其实是磁盘读取错误的, 重启Window资源管理器即可

杀掉正在运行的资源管理器进程程序: `explorer.exe`

```powershell
tskill explorer
```

如果不能自动重新启动资源管理器的话, 命令行指定即可:

```powershell
explorer.exe
```

## 清理 C 盘占用大空间文件
关闭休眠功能(仅适用于台式机), 笔记本关闭会出问题, 即删除 `Hiberfil.sys` 系统保护文件

    powercfg -h off
    powercfg -h on # 开启休眠

调整休眠内容文件 `Hiberfil.sys` 同步内容的比例 `*%` 例如: 占用70%

    powercfg -h -size 70

参考链接:
* [win7系统c盘空间显示与实际占用空间不对怎么回事？解决方法](http://www.xitongcheng.com/jiaocheng/win7_article_29079.html)
* [*重点(占用超大空间) - 调整和删除Win7休眠文件Hiberfil.sys释放C盘*](https://jingyan.baidu.com/article/f3ad7d0fc0992e09c2345b51.html)


## window 10 电脑网络图标异常

命令:
```powershell
net localgroup administrators localservice /add
net localgroup administrators networkservice /add
```

### PS
    但感觉也可以解决其他的问题
    因为 net localgroup 命令是操作用户与组的

## window10 能联网, 但是出现感叹号
    桌面 -> 我的电脑 右键 -> 设备管理器 -> 选择使用的网卡设备 右键 ->
    属性 -> 高级 -> IPv4校验和分载传输(Large Send Offload IPv4) ->
    设置为: 禁用(Enabled)

设置完成后解决了问题, 但重启电脑后问题依旧, 而且配置是上面设好的值

## 解决Antimalware Service Executable CPU占用高
windows8/8.1，WIN10自带的安全软件Windows defender还不错，基本可以不用装其他杀毒软件了。

但是其进程Antimalware Service Executable 出现CPU使用率和占用大，困扰许多用户。网上的基本方法是关闭Windows defender,但是还得安装其他杀软，而且不能禁止其服务的启动（至少win10里是这样的，该服务管理中的选项都是灰色不可用的）。

初步判断是Windows defender在后台执行扫描产生的CPU和内存占用居高不下的问题，有的人说是没有进行过全盘扫描，所以它还要扫描，但是昨晚做了一次全屏扫描。早上起床发现，共扫描了140多万个文件，但是问题依旧，重启几次都不行，于是再找其他方法，终于发现解决方法，现在一切宁静了：

方法是从组策略中设置。

win键+R键打开运行对话框框，输入gpedit.msc打开本地组策略编辑器（组策略）

依次打开计算机配置-管理模板-Windows组件-Windows Defender；

如果要关闭Windows defender，则将“关闭 Windows Defender”项设置为“已启用”即可。

如果要保留Windows defender，只解决CPU占用和内存占用高的问题，则继续下列步骤；

打开“实时保护”，将里面的“不论何时启动实时保护，都会启动进程扫描”这一配置项设置为“已禁用”（此步骤最关键）；

打开“扫描”，将里面的以下几项设置为“已禁用”：

（1）指定每天进行快速扫描的时间间隔；

（2）仅当计算机处于打开但未使用状态才启动计划扫描；

（3）指定每天进行快速扫描的时间；

（4）指定每天的不同时间运行计划扫描；

将“指定每周的不同时间运行计划扫描”设置为“从不”，并设置为“已启用”。
7

总之，看情况，可能禁用第5步的选项就解决问题了。希望能帮到大家。

注意事项

看情况，可能禁用第5步的选项就解决问题了

* [解决Antimalware Service Executable CPU占用高](https://jingyan.baidu.com/article/e75057f2c1f6edebc91a89ed.html)

## Win10 1709提示“因文件共享不安全 不能连接文件共享”如何解决？
控制面板 -> 启用或关闭Windows功能 -> 勾选: SMB1.0/CIFS文件共享支持

除了以上方法，微软官方也提供了通过PowerShell来进行设置的方法，用管理员权限打开Powershell之后，可以参考下面的命令：

SMB v1

检测： Get-WindowsOptionalFeature –Online –FeatureName SMB1Protocol

禁用： Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol

启用： Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol

SMB v2/v3

检测：Get-SmbServerConfiguration | Select EnableSMB2Protocol

禁用：Set-SmbServerConfiguration –EnableSMB2Protocol $false

启用：Set-SmbServerConfiguration –EnableSMB2Protocol $true

* [Win10 1709提示“因文件共享不安全 不能连接文件共享”如何解决？](https://www.pconline.com.cn/win10/1035/10357000.html)

# 问题处理

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

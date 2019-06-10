# window 系统常用命令

## Window 系统资源
* [MSDN 资源网站](https://msdn.itellyou.cn/)

## DNS
* [点击查看详情...](./DNS.md)

## DHCP
* [点击查看详情...](./DHCP.md)

## 快捷操作:
快速在文件夹目录中打开cmd:
    文件夹空白处按住shift键鼠标右键选择【在此处打开命令窗口】即可

## 清理 C 盘占用大空间文件
关闭休眠功能(仅适用于台式机), 笔记本关闭会出问题, 即删除 `Hiberfil.sys` 系统保护文件

    powercfg -h off
    powercfg -h on # 开启休眠

调整休眠内容文件 `Hiberfil.sys` 同步内容的比例 `*%` 例如: 占用70%

    powercfg -h -size 70

参考链接:
* [win7系统c盘空间显示与实际占用空间不对怎么回事？解决方法](http://www.xitongcheng.com/jiaocheng/win7_article_29079.html)
* [*重点(占用超大空间) - 调整和删除Win7休眠文件Hiberfil.sys释放C盘*](https://jingyan.baidu.com/article/f3ad7d0fc0992e09c2345b51.html)

## 常用应用程序命令
* [点击查看详情...](./application_command.md)

## 目录相关参数
* [点击查看详情...](./directory_parameter.md)

## 参考链接:
* [Win8系统108个运行命令 你能记住多少?](http://win8.zol.com.cn/277/2772193.html)
* [Win10怎么优化？安装好Win10后必做的22项优化！](http://www.xitonghe.com/jiaocheng/Windows10-5634.html)

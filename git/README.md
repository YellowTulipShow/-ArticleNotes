# 总结学习常用 Git 命令

## Git 基础命令
* [本地学习各命令文档](./CommandNote.md)

## SSH Key
```shell
$ ssh-keygen -t rsa -C "<email account>"
```
* [本地 SSH Key 学习详情](./SSH_Config.md)

## Git 基础概念:
### 工作区:
    用户看到和直接更改的部分
### 版本库
    Git控制文件版本主要部分 体现为文件夹: .git
    - 暂存区
        $ git add <file> 命令 添加的文件暂时存储在此区域
    - 分支部分
        存储"已经固定" 内容 真正的版本存储地方
### HEAD
    表示当前 分支/位置/记录的指针


## 分支策略 几个原则进行分支管理:
> `M.D.B.R.F` 五种分支类型: (名称以 `YellowTulipShow` 自己命名,最好理解的方式)
> 这是最基本的几个, 具体根据项目实际需要有变换

### M master
    唯一的主分支, 和生产环境相同版本
    主分支只用来分布重大版本，日常开发应该在另一条分支上完成
    分支应该是非常稳定的,也就是仅用于发布新版本,平时不能再上面干活

### D dev
    开发分支,一直在此分支工作, 不需要删除
    干活都在 dev 分支上,也就是说, dev 分支是不稳定的
    到某个时候,比如1.0版本发布时,再把 dev 分支合并到 master 上, 在 master 分支发布1.0版本

### B bug
    出现Bug时创建, 用完需要删除

### R release
    发布新版本时创建, 用完需要删除

### F function
    开发新功能时创建, 用完需要删除

## 别名命令收藏
可以直接使用下面代码添加到 `~/.gitconfig` 文件
```shell
[alias]
    # 日志格式
    logs = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an %Creset' --abbrev-commit -n 10

    # 含有文件差异的文件名列表
    diffn = diff --name-status

    # 标签和标签注释
    tags = tag -ln
```
* [个性化你的 Git Log 的输出格式](https://ruby-china.org/topics/939)

## 系统别名命令
`~/.bashrc` 则每次打开新的终端时，都要被读取

`~/.bash_profile` 只在会话开始时被读取一次

* [Linux/mac下的自定义命令alias，并保存别名使其永久生效（重启不会失效)](http://blog.csdn.net/jianglei421/article/details/8510723)
* [linux下.bashrc文件 /PATH环境变量修改 /提示符修改](http://shunfengwei.blog.163.com/blog/static/17522511720122299241143/)

### 生效配置文件
```shell
# 使用 .bashrc 文件
source ~/.bashrc
```

### 文件类型
```shell
# 匹配 Web 上传更新文件类型
alias grepf='grep -E ".*\.(aspx|html|htm|css|js|xml|md|)$"'
```

### 检查目录下多个项目库的状态 - Python脚本
```shell
alias gitdc='python /D/ZRQWork/YTS.ZRQ/GitDirectoryCheck/main.py'
```

* [点击查看自定义配置和使用](https://github.com/YellowTulipShow/GitDirectoryCheck)

## Git mintty 配置
对于 `Git` 的操作基本上都是使用 `mintty` 命令行工具来实现

从 `Git` 官网上下载的工具 `Git Bash` 便是 `mintty`

* [具体的习惯性配置 点击进行查看](./mintty.md)


## 提高访问 GitHub 速度
更改 `hosts` 文件: (如果没有创建之, 并且注意需要管理员权限)

    Window: -> C:\Windows\System32\drivers\etc\hosts
    Mac: -> /etc/hosts

    192.30.253.113      github.com
    151.101.185.194     github.global.ssl.fastly.net

[浏览器访问](https://www.ipaddress.com/), 分别输入 `github.com` 和 `github.global.ssl.fastly.net` 以获取对应速度最快的ip写入到配置文件中

最后执行 `ipconfig /flushdns` 命令, 刷新 DNS 缓存

## window10 Git Bash 启动闪退

问题原因:

**C:\Windows\System32\drivers\null.sys** 文件非正版系统不兼容

解决:

获取大神的文件: [百度网盘地址](https://pan.baidu.com/s/1UtcZizm-iFcVk4OKrnFJVg) 密码: 1q4d

替换之即可, 详细查看下面文章:

* [**win10 专业版 git bash 闪退问题终极解决方案**](https://www.cnblogs.com/ricklz/p/9216395.html)
* [WIN10 GIT BASH 闪退问题终极解决方案](https://blog.csdn.net/qq_36927265/article/details/81538873)

## 日期英文:
### 周:

简写 | 英文 | 中文
--- | --- | ---
Mon | Monday    | 星期一
Tue | Tuesday   | 星期二
Wed | Wednesday | 星期三
Thu | Thursday  | 星期四
Fri | Friday    | 星期五
Sat | Saturday  | 星期六
Sun | Sunday    | 星期日

### 月:

简写 | 英文 | 中文
--- | --- | ---
Jan | January    | 一月
Feb | February   | 二月
Mar | March      | 三月
Apr | April      | 四月
May | May        | 五月
Jun | June       | 六月
Jul | July       | 七月
Aug | August     | 八月
Sep | September  | 九月
Oct | October    | 十月
Nov | November   | 十一月
Dec | December   | 十二月

## 日志格式参数:
* [点击查看详情](./log_format_arguments.md)

## 参考学习链接:
* [廖雪峰Git学习](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
* [Git-scm.com 中文版](https://git-scm.com/book/zh/v2)
* [腾讯云 Git 中文开发者手册](https://cloud.tencent.com/developer/doc/1096)
* [阮一峰 Git分支管理策略](http://www.ruanyifeng.com/blog/2012/07/git.html)
* [介绍一个成功的 Git 分支模型](http://www.oschina.net/translate/a-successful-git-branching-model)
* [Git常用命令查询](http://www.open-open.com/lib/view/open1340532874842.html)
* [Git 一次性 pull push 所有的分支](https://www.cnblogs.com/zengjfgit/p/6212073.html)
* [git clone一个github上的仓库，太慢，经常连接失败，但是github官网流畅访问，为什么？](https://www.zhihu.com/question/27159393)
* [解决GitHub下载速度太慢的问题](https://blog.csdn.net/qing666888/article/details/79123742)
* [一篇文章搞定Github API 调用 (v3）](https://segmentfault.com/a/1190000015144126?utm_source=tag-newest)
* [Git查看、删除、重命名远程分支和tag](https://blog.zengrong.net/post/1746.html)
* [改写历史，永久删除git库的物理文件](https://my.oschina.net/jfinal/blog/215624?fromerr=ZTZ6c38X)
* [仓库体积过大，如何减小？](https://gitee.com/help/articles/4232)
* [git之https或http方式设置记住用户名和密码的方法](https://www.cnblogs.com/wish123/p/3937851.html)
* [Gitee 码云APP链接地址](https://gitee.com/appclient)
* [git commit时暂时忽略已提交的文件](https://blog.csdn.net/FCXD_2014/article/details/101167158)

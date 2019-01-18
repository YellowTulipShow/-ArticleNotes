# 总结学习常用 Git 命令

## Git 基础命令
点击 **[`这里`](./CommandNote.md)** 来查看更多

## SSH Key
```shell
$ ssh-keygen -t rsa -C "<email account>"
```
点击 **[`这里`](./SSH_Config.md)** 来查看更多

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
> 参考学习链接:
>
> - [个性化你的 Git Log 的输出格式](https://ruby-china.org/topics/939)

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

## 系统别名命令
> - [Linux/mac下的自定义命令alias，并保存别名使其永久生效（重启不会失效)](http://blog.csdn.net/jianglei421/article/details/8510723)
> - [linux下.bashrc文件 /PATH环境变量修改 /提示符修改](http://shunfengwei.blog.163.com/blog/static/17522511720122299241143/)

### `~/.bashrc` 则每次打开新的终端时，都要被读取
```shell
# 匹配 Web 上传更新文件类型
alias grepf='grep -E ".*\.(aspx|html|htm|css|js|xml|md|)$"'
```

### `~/.bash_profile` 只在会话开始时被读取一次
```shell
# 使用 .bashrc 文件
source ~/.bashrc
```

## Git mintty 配置
对于 `Git` 的操作基本上都是使用 `mintty` 命令行工具来实现

从 `Git` 官网上下载的工具 `Git Bash` 便是 `mintty`

具体的习惯性配置 点击 **[这里](./mintty.md)** 进行查看


## 日期英文:
### 周:
```shell
Monday      # 星期一   Mon
Tuesday     # 星期二   Tue
Wednesday   # 星期三   Wed
Thursday    # 星期四   Thu
Friday      # 星期五   Fri
Saturday    # 星期六   Sat
Sunday      # 星期日   Sun
```

### 月:
```shell
January     # 一月     Jan
February    # 二月     Feb
March       # 三月     Mar
April       # 四月     Apr
May         # 五月     May
June        # 六月     Jun
July        # 七月     Jul
August      # 八月     Aug
September   # 九月     Sep
October     # 十月     Oct
November    # 十一月   Nov
December    # 十二月   Dec
```

## 日志格式参数:
```shell
%H: commit hash
%h: 缩短的commit hash
%T: tree hash
%t: 缩短的 tree hash
%P: parent hashes
%p: 缩短的 parent hashes
%an: 作者名字
%aN: mailmap的作者名字 (.mailmap对应，详情参照git-shortlog(1)或者git-blame(1))
%ae: 作者邮箱
%aE: 作者邮箱 (.mailmap对应，详情参照git-shortlog(1)或者git-blame(1))
%ad: 日期 (--date= 制定的格式)
%aD: 日期, RFC2822格式
%ar: 日期, 相对格式(1 day ago)
%at: 日期, UNIX timestamp
%ai: 日期, ISO 8601 格式
%cn: 提交者名字
%cN: 提交者名字 (.mailmap对应，详情参照git-shortlog(1)或者git-blame(1))
%ce: 提交者 email
%cE: 提交者 email (.mailmap对应，详情参照git-shortlog(1)或者git-blame(1))
%cd: 提交日期 (--date= 制定的格式)
%cD: 提交日期, RFC2822格式
%cr: 提交日期, 相对格式(1 day ago)
%ct: 提交日期, UNIX timestamp
%ci: 提交日期, ISO 8601 格式
%d: ref名称
%e: encoding
%s: commit信息标题
%f: sanitized subject line, suitable for a filename
%b: commit信息内容
%N: commit notes
%gD: reflog selector, e.g., refs/stash@{1}
%gd: shortened reflog selector, e.g., stash@{1}
%gs: reflog subject
%Cred: 切换到红色
%Cgreen: 切换到绿色
%Cblue: 切换到蓝色
%Creset: 重设颜色
%C(...): 制定颜色, as described in color.branch.* config option
%m: left, right or boundary mark
%n: 换行
%%: a raw %
%x00: print a byte from a hex code
%w([[,[,]]]): switch line wrapping, like the -w option of git-shortlog(1).
```

## 参考学习链接:
```shell
# 廖雪峰Git学习
https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000

# Git-scm.com 中文版
https://git-scm.com/book/zh/v2

# 阮一峰 Git分支管理策略
http://www.ruanyifeng.com/blog/2012/07/git.html

# 介绍一个成功的 Git 分支模型
http://www.oschina.net/translate/a-successful-git-branching-model

# Git常用命令查询
http://www.open-open.com/lib/view/open1340532874842.html

# Git 一次性 pull push 所有的分支
https://www.cnblogs.com/zengjfgit/p/6212073.html

# git clone一个github上的仓库，太慢，经常连接失败，但是github官网流畅访问，为什么？
https://www.zhihu.com/question/27159393

# 解决GitHub下载速度太慢的问题
https://blog.csdn.net/qing666888/article/details/79123742
```

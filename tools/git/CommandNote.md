﻿# Git 基础命令

## git 配置

```shell
$ git config
    # 针对当前 "用户(系统)" 做全局配置
    --global

    # 为 "命令" 配置 别名 (<command contnet> 不需要加 git)
    alias.<alias name> "<command contnet>"

    # 设置操作的用户 名称
    user.name "<Your Name>"

    # 设置操作的用户 电子邮箱
    user.email "<email@example.com>"

    # 使用 http / https 方式操作版本库时记住用户名密码
    credential.helper store
```

个人命令:

```shell
git config --global user.name "YellowTulipShow"
git config --global user.email "main@yellowtulipshow.site"
git config --global user.email "1426689530@qq.com"
```


## 创建初始化仓库

```shell
$ git init
```

## 查看仓库状态

```shell
# 随时掌握工作区的状态
$ git status
```

## 文件修改内容

```shell
$ git diff
    # 查看具体文件变更内容
    <file>

    # 查看当前暂存区与当前版本的 HEAD 的变更内容
    HEAD

    # 查看区别的'文件目录'
    --name-status

    # 查看区别的'文件目录'具体更改行数据
    --stat
```

## 添加到暂存区

```shell
$ git add
    # 添加 当前目录所有文件 到缓存区
    .

    # 添加 指定 文件 到缓存区
    <file>

    # 强制 添加 指定 文件 到缓存区
    -f <file>
```

## 删除文件

```shell
$ git rm
    # 用于删除一个在版本库文件 提交到 暂存区 和 git add 类似
    <file>
```

## 提交到本地仓库

```shell
$ git commit
    # 全部提交
    -a

    # 提交并附加说明消息
    -m "(not content)"

    # 可以修改最后一次 commit
    --amend
```

## 显示信息

> 官方文档里还有输出格式自定义的功能, 需要细看...

```shell
$ git show <object>
```

## 查看历史日志

```shell
$ git log
    # 查看最近的几条日志
    -n <number>

    # 单行显示记录
    --pretty=oneline

    # 查看分支合并图
    --graph

    # 查看分支 合并情况 简介版本
    --graph --pretty=oneline --abbrev-commit
```

## 查看命令历史

> 常用于回到 未来 的后悔药

```shell
$ git reflog
```

## 跳转历史

> 后悔药的最主要实现手段

```shell
$ git reset
    # 将在暂存区的修改撤销, 重新放回工作区
    HEAD <file>

    # 回退到上一个版本 一个 "^" 符号就是代表往前数一个版本
    --hard HEAD^

    # HEAD指向的版本就是当前版本, 因此, Git允许我们在版本的历史之间穿梭, 使用命令git reset --hard commit_id
    --hard <commit_id>
```

## 切换...

```shell
$ git checkout
    # 把文件在 "工作区" 的修改全部撤销
    -- <file>

    # 创建 + 切换 指定名称 "分支" 默认从当前分支获取
    -b <branch name>

    # 创建 基于<source branch name>源分支的<new branch name>新分支
    -b <new branch name> <source branch name>

    # 在本地创建和远程分支对应的分支,本地和远程分支的名称最好一致
    -b <branch name> <origin name>/<branch name>

    # 切换到 指定名称 "分支"
    <branch name>
```

## 分支操作

> 无参数时, 查看分支列表

```shell
$ git branch
    # 创建 指定名称 "分支
    <branch name>

    # 查看所有分支 包括远程分支
    -a

    # 查看所有远程分支
    -r

    # 查看分支详情
    -v

    # 删除 指定名称 "分支"
    -d <branch name>

    # 强制删除 指定名称 "分支"
    -D <branch name>

    # 为分支更改名称
    -m <原名>/(不填表示当前分支) <新名>

    # 建立本地分支和远程分支的关联
    --set-upstream <local branch name> <origin name>/<origin branch name>
```

## 合并分支

```shell
$ git merge
    # 合并某分支到当前分支
    <branch name>

    # 强制禁用 fast forward 模式进行合并 使其创建一次 commit 所以需要加 -m
    --no-ff -m <message>
```

## 隐藏工作区内容

```shell
$ git stash # 隐藏当前 工作区内容
    # 可以查看 隐藏的工作区内容都有哪些
    list

    # 恢复但 stash 内容并不删除 需要 drop
    apply

    # 手动删除 stash 内容
    drop

    # 恢复的同时把 stash 内容也删除掉了
    pop
```

## 标签

```shell
$ git tag # 可以查看所有标签
    # (已不建议使用) 用于新建一个标签, 默认是HEAD
    <tagname>

    # 新建一个标签 指定 commit id
    <tagname> <commit_id>

    # (建议默认使用) 创建 并 给标签指定说明信息
    -a <tagname> -m

    # 使用PGP签名标签 并 给标签指定说明信息
    -s <tagname> -m

    # 删除标签
    -d <tagname>
```

常用:

```shell
$ git tag <tagname> <commit_id> -a -m "<message>"
```

## 从 远程服务器 克隆

```shell
$ git clone <url address>
```

## 远程仓库处理

```shell
$ git remote
    # 查看远程库的各名称 (比 -v 差)
    show

    # 查看远程库的详细信息
    -v

    # 查看指定远程库的巨细信息 (比 -v 强)
    show <remote name>

    # 将本地仓库 关联 远程仓库 (记得需首先在远程仓库 网站设置好SSH)
    add <origin name> <url address>

    # 在本地删除 已经关联的远程库信息
    rm <origin name>

    # 更改新的地址
    set-url <origin name> <url address>
```

## 往 远程仓库 推送

```shell
$ git push
    # 第一次推送所有内容 必须添加此参数
    -u

    # 推送 <branch name> 分支内容 到 远程仓库 <origin name>
    <origin name> <branch name>

    # 推送本地版本库的所有分支到远程版本库
    <origin name> --all

    # 推送 <tagname> 标签 到 远程仓库 <origin name
    <origin name> <tagname>

    # 一次性推送全部尚未推送到远程的本地标签
    <origin name> --tags

    # 可以删除一个远程标签 不能删除本地
    <origin name> :refs/tags/<tagname>

    # 可以使用这种语法删除远程分支
    origin --delete <branchName>

    # 可以使用这种语法删除远程标签
    origin --delete tag <tagname>
```

## 从 远程仓库 抓取

```shell
$ git pull
    # 抓取指定仓库 的 指定分支内容合并到本地相同名称分支中
    <origin name> <branch name>

    # 抓取远程版本库的所有分支到本地版本库
    <origin name> --all
```


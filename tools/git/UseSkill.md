# 使用技巧

## 合并分支.冲突解决

采用当前分支的版本:
```shell
git checkout --ours <...>
```

采用合并分支的版本:
```shell
git checkout --theirs <...>
```

合并中断
```shell
git merge --abort
```

## 取消跟踪 但是不删除文件


1. `git rm --cached logs/xx.log`
2. 然后更新 `.gitignore` 忽略掉目标文件，
3. 最后 `git commit -m "xxxx"`



## 配置

### 使用 Notepad++ 取代 Git Bash 的默认Vim编辑器

```shell
git config core.editor "\"C:/Program Files (x86)/Notepad++/notepad++.exe\" -multiInst -notabbar -nosession -noPlugin"
```

注意`Notepad++`程序的路径与外面的引号


还原 `Vim` 配置

```shell
git config core.editor vim
```

## Git 清除远端已删除的分支

可以查看remote地址，远程分支，还有本地分支与之相对应关系等信息。

```shell
git remote show origin
```

可以看到那些远程仓库已经不存在的分支，根据提示使用命令:

```shell
git remote prune origin
```

这样就删除了那些远程仓库不存在的分支。

* [Git 清除远端已删除的分支](https://www.cnblogs.com/weifeng1463/p/9916469.html)

## 查看单个文件修改历史

```shell
git log -p <filename>
```

可以看到`<filename>`相关的`<commit_id>`记录

```shell
git log <filename>
```

只看某次提交中的某个文件变化，可以直接加上`<filename>`

```shell
git show <commit_id> <filename>
```

## 常用后悔药:

### Need Revoked: (需要撤销: )

```shell
# 工作区内容已更改
# 取消指定文件 在工作区内容的更改操作
$ git checkout -- <file>

# 需要撤销: 暂存区内容已更改
# 可以把暂存区的修改撤销掉（unstage），重新放回工作区
$ git reset HEAD <file>

# 需要撤销: 仓库(版本库)内容已更改
# 将版本跳转到指定的版本节点上去
$ git reset --hard <commit_id>

# 重新备注说明最近一次的提交信息:
$ git commit --amend
```

## 常用代码

## 一行命令处理/拉取/更新/提交

```shell
git pull origin master && git add . && git commit -m "修改" && git push origin master
```

### 测试与代码服务器是否连通

GitHub
```shell
ssh git@github.com
```

Gitee 码云
```shell
ssh git@gitee.com
```

### 推送本地代码到远程代码库

```shell
git remote add <origin name> <url address>
git push -u origin --all
git push origin --tags
```

### git 从远程仓库获取所有分支

```shell
git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
git fetch --all
git pull --all
```

* [引用链接](http://stackoverflow.com/questions/10312521/how-to-fetch-all-git-branches)


### 拉取指定远程仓库分支到本地 (本地分支不存在)

```shell
git checkout -b <branch> origin/<branch>
```

### 暂时屏蔽文件

当正在修改某文件A，此时需要commit，但是A没修改完暂时不能一起commit。 执行：

```shell
git update-index --assume-unchanged A的路径
```

git暂时会忽略该文件的修改， git status查看时A已经不在待commit列表中了。

让git重新监视文件A的修改：

```shell
git update-index --no-assume-unchanged A的路径
```

如果忽略的文件多了，可以使用以下命令查看忽略列表

```shell
git ls-files -v | grep '^h\ '
```

提取文件路径，方法如下

```shell
git ls-files -v | grep '^h\ ' | awk '{print $2}'
```

所有被忽略的文件，取消忽略的方法，如下

```shell
git ls-files -v | grep '^h' | awk '{print $2}' |xargs git update-index --no-assume-unchanged
```

* [Git命令git update-index --assume-unchanged，忽略不想提交的文件（忽略跟踪）](https://www.cnblogs.com/wt645631686/p/10007328.html)

## 删除 .gitignore 已经在版本库中的文件

```shell
git rm -r --cached .
git add .
git commit -m 'update .gitignore'
-- 删除 .git/ 以外的所有文件
git checkout -- .
```

## 查看当前分支所有提交者及其提交次数，按次数由高到低排序
```shell
git log | grep "^Author: " | awk '{print $2}' | sort | uniq -c | sort -k1,1nr
```
* [来源:博客地址](https://blog.csdn.net/cyf15238622067/article/details/82980782)


## 分析 Git 日志来统计代码量
```shell
git log --author="_your_name_" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }'
```
```
输出结果：added lines: 38861, removed lines: 22916, total lines: 15945
```
* [来源:博客地址](https://blog.csdn.net/cyf15238622067/article/details/82980782)

## 关于git：我怎么知道分支是否已经合并为master？

```shell
列出合并为master的分支
git branch --merged master

列出合并到HEAD的分支(即当前分支的尖端)
git branch --merged

列出尚未合并的分支
git branch --no-merged
```

* [关于git：我怎么知道分支是否已经合并为master？](https://www.codenong.com/226976/)

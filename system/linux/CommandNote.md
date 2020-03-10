# Linux 命令笔记

## 修改Bash配置文件: .bashrc

* `.bash_history` 记录之前输入的命令
* `.bash_logout` 当你退出时执行的命令
* `.bash_profile` 当你登入shell时执行
* `.bashrc` 当你登入shell时执行

请注意后两个的区别: `.bash_profile`只在会话开始时被读取一次，而`.bashrc`则每次打开新的终端时，都要被读取。

别名设置 `gits`:

```shell
alias gits='python3 /var/work/YTS.ZRQ/GitDirectoryCheck/main.py'
```

**每次修改`.bashrc`后，使用 `source ~/.bashrc`（或者 `. ~/.bashrc`）**

**就可以立刻加载修改后的设置，使之生效。**

### 系统配置

除了可以修改用户目录下的`.bashrc`文件外，还可以修改如`/etc/profile`文件、`/etc/bashrc`文件及目录`/etc /profile.d`下的文件。但是修改/etc路径下的配置文件将会应用到整个系统，属于系统级的配置，而修改用户目录下的.bashrc则只是限制在用户应用上，属于用户级设置。两者在应用范围上有所区别，建议如需修改的话，修改用户目录下的.bashrc，即无需root权限，也不会影响其他用户。

## 学习连接地址:

* [linux下.bashrc文件修改和生效](https://blog.csdn.net/eleanoryss/article/details/70207767)

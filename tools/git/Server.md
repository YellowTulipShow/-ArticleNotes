# Git 服务器搭建 Ubuntu Linux 环境

首先安装 `Git`

```shell
sudo apt-get install git
```

创建 `git` 用户用于管理所有的仓库

```shell
sudo adduser git
```

登陆 `git` 用户进行后续操作, 也是为了保证有相关的权限

```shell
su git
```

切换到 `git` 用户的主目录并创建 `ssh` 协议存储公钥文件

```shell
cd ~
mkdir .ssh/
touch authorized_keys
```

手动写入客户端的公钥文件内容一行一个

```shell
vim authorized_keys
```

配置完成!

接下来切换到 `git` 用户 `home` 目录下的某一个文件夹建立仓库位置就可以了

例如:

```shell
cd ~
mkdir librarys/
git init --bare <project>.git
```

之后就可以在客户端使用模板

```shell
git remote add <origin name> ssh://git@<ip address>:/home/git/librarys/<project>.git
```

## 参考学习链接:

* [Ubuntu下搭建Git服务器](https://blog.csdn.net/zhouxiangbai/article/details/78851276)
* [Ubuntu18.04搭建git服务器](https://blog.csdn.net/zhen_apple/article/details/88655414?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)

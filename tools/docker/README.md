# Docker 环境容器


## 常用操作

* 映射创建容器:
```shell
docker run -itd --name="<容器实例别名>" -v <本机路径Linux格式>:<容器中路径Linux格式> <Image镜像名称> /bin/bash
```

* 启动容器
```shell
docker start <容器实例别名>
```

* 进入已开启的容器中
```shell
docker exec -it <容器实例别名> /bin/bash
```

* 查看所有容器
```shell
docker ps --all
docker container ls --all
```

* 删除容器
```shell
docker container rm <容器实例别名>
```

* 把dos格式的文件(Window系统使用)转换为unix格式的文件(Linux系统使用)
```shell
dos2unix <文件名称路径>
```

## 链接

* [阮一峰的网络日志 - Docker 入门教程](https://ruanyifeng.com/blog/2018/02/docker-tutorial.html)
* [Windows 下的docker 本地文件夹 映射到docker的容器中](https://blog.csdn.net/m0_38044453/article/details/98080461)
* [执行shell脚本报错“/bin/bash^M: bad interpreter: No such file or directory”](https://blog.csdn.net/li1325169021/article/details/115361901)

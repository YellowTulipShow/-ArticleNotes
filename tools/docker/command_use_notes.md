# 命令使用笔记

### 远程镜像拉取

```shell
docker image pull <容器实例地址:版本号>
```

### 映射创建容器:
```shell
docker run -itd --name="<容器实例别名>" -v <本机路径Linux格式>:<容器中路径Linux格式> <Image镜像名称> /bin/bash

docker run -itd --name="<容器实例别名>" -v <本机路径Linux格式>:<容器中路径Linux格式> <Image镜像名称>
```

### 启动容器
```shell
docker start <容器实例别名>
```

### 关闭容器
```shell
docker kill <容器实例别名>
```

### 进入已开启的容器中
```shell
docker exec -it <容器实例别名> /bin/bash
```

### 查看所有容器
```shell
docker ps --all
docker container ls --all
```

### 删除容器
```shell
docker container rm <容器实例别名>
```

### 把dos格式的文件(Window系统使用)转换为unix格式的文件(Linux系统使用)
```shell
dos2unix <文件名称路径>
```


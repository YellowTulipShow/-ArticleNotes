# 发布网站

## 基础流程

登录 Linux 服务器
```ssh
ssh root@xxx.xxx.xxx.xxx
```

nginx 是否安装, 如未安装尽心
```ssh
sudo nginx -v
sudo apt install nginx
```

修改默认80端口发布的程序地址
```ssh
vim /etc/nginx/sites-enabled/default
```

修改文件部分
```vim
server {
    root /var/xxx(目标地址)
}
```

检查配置是否正确
```ssh
sudo nginx -t

类似以下输出正确
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

重启 nginx 服务
```ssh
nginx -s reload
```

坑:阿里云服务器发布程序需配置安全组信息
```
登陆控制台 -> 实例 -> 安全组设置 -> 安全组列表 -> 选择安全组(管理规则)
    SSH(22) git 拉取代码使用ssh 方式使用
    http(80) 普通访问
    https(443) 加密访问
```

## 链接

* [ 使用 Nginx 搭建静态网页服务 ](https://aimerneige.com/zh/post/devops/deploy-web-page-with-nginx/)
* [在阿里云云服务器上发布自己的网站（建站|详细）](https://www.jianshu.com/p/aac827db9fe0)

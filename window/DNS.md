# DNS 相关配置

静态绑定 `IP` 与网址关联, 配置文件地址为:

`C:\Windows\System32\drivers\etc\host`

文件中如:

```shell
    192.30.253.113  github.com
    151.101.185.194 github.global.ssl.fastly.net
    204.79.197.200 bing.com
```

最后执行 `ipconfig /flushdns` 命令, 刷新 DNS 缓存


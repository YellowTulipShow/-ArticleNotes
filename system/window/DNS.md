# DNS 相关配置

静态绑定 `IP` 与网址关联, 配置文件地址为:

`C:\Windows\System32\drivers\etc\hosts`

文件中如:

```shell
204.79.197.200 bing.com
```

最后执行如下命令, 刷新 DNS 缓存 (注意需要使用管理员模式启动命令行)

```powershell
ipconfig /flushdns
```

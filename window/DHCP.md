## DHCP 相关配置
    问题: 连上网络但是不能浏览网页,但能Ping通一些常见域名地址
    解决: DHCP问题(重新启动服务), winsock(管理员权限的cmd输入命令: `netsh winsock reset` (说是LSP目录))

## window10 能联网, 但是出现感叹号
    桌面 -> 我的电脑 右键 -> 设备管理器 -> 选择使用的网卡设备 右键 ->
    属性 -> 高级 -> IPv4校验和分载传输(Large Send Offload IPv4) ->
    设置为: 禁用(Enabled)

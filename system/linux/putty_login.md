# Putty 登录 Linux

首先, 需要下载 Putty 软件:

https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

安装需要下载即可, 如果 需要 `ssh` 登录的话需要再下载: `puttygen.exe`

## 配置使用
软件下载安装完成后, 就需要进行配置使用

因为个人习惯的问题, 按照 使用 `ssh` 秘钥方式登录, 密码方式详情可以参阅: https://cloud.tencent.com/document/product/213/5436

必须填写的信息:
```shell
# 会话
Session -> (右侧面板)
    # 指定要连接的目标
    Specify the destination you want to connect to ->
        # 一般填写服务器 ip 地址即可
        Host Name(or IP address)
        # 需要链接的端口
        Port
        # 链接类型 -> 选择 SSH 秘钥方式
        Connection type: -> SSH
    # 用于整体保存一个会话的配置, 方便使用
    Load, save or delete a stored session ->
        # "当前" 要保存的会话名称, 如果为空需要输入 点击 Save 按钮进行保存
        Saved Sessions
        # 加载
        Load
        # 保存
        Save
        # 删除
        Delete
```

```shell
# 软件窗口样式 -> 外貌 ->
Window -> Appearance -> (右侧面板) ->
    # 字体设置
    Font settings -> Change 按钮 -> 对话框 自行设置
        # 一般设置为:
        Consolas, 14-point
```

```shell
# 连接服务器设置, 也是重点
Connection ->
    # 数据
    Data -> (右侧面板) ->
        # 登录详细信息
        Login details ->
            # 自动登录的用户名, 根据系统类型不一样,
            Auto-login usename:
                # 实例操作系统          管理员帐号
                SUSE/CentOS/Debian     root
                Ubuntu                 ubuntu
    # 秘钥
    SSH ->
        # 验证
        Auth -> (右侧面板) ->
            # 验证参数
            Authentication parameters ->
                # 私有键值文件验证
                Private key file for authentication: ->
                    按钮 Browse
                    这里需要选择已 *.ppk 为扩展名的文件
                    正常的 SSH 的 秘钥文件为:  公有(*.pub扩展名) + 私有(没扩展名)
                    *.ppk 需要 私有秘钥文件 使用 puttygen.exe 程序进行转化
```

私有秘钥文件 转化 `*.ppt` 秘钥验证文件

打开 `puttygen.exe`
```shell
面板 ->
Actions -> Load 按钮 -> 选择一个 私有秘钥文件如 id_rsa ->
Save private key -> 选好路径, 并填写 (文件名).ppt  !!! 一定要将 *.ppt 扩展名写上 ->
创建完成, 即可使用 (文件名).ppt
```

接下来在 `putty.exe` 软件中将编辑好的 `Session` 会话保存就可以了

然后在服务器中写入 `ssh` 秘钥的公有文件内容, 即可自动登录 Linux 系统服务器了...

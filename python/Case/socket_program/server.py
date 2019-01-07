# coding: UTF-8

from socket import *
server = socket(AF_INET, SOCK_STREAM) # 创建套接字

# 第一个参数写一个空字符串, 代表绑定所有可用IP
# 局域网 192.168.1.106
# 互联网 113.147.156.138
# 本地回环地址 127.0.0.1
server.bind(('', 8888)) # 1024 - 65535

# listen 分配一个同时可以监听数目的属性
server.listen(5)
print("服务器开启, 等待连接...")
while True:
    # 第一个返回值, 访问者得IP和端口
    client, c_addr = server.accept()
    print("有朋自远方来: ", c_addr)
    while True:
        data = client.recv(1024)
        if not data:
            print("人家走了...", c_addr)
            break;
        print("{} 客人说: {}".format(c_addr, data.decode("utf-8")))
        buf = input("你想对客人说什么:")
        client.send(buf.encode("utf-8"))
    client.close()
server.close()

'''
网络:
    socket模块来实现

    TCP/IP
    UDP/IP
        协议: 翻译，让我们传输的数据有意义
        二进制信号 电流信号
        000011010101010
    明确目标地址:
        IP：网络中的一个唯一身份
        MAC地址: 硬件设备厂商
            局域网通信

    数据的传输协议
    TCP 更安全，更靠谱的传输方式，打电话
        三次握手，
            1：你好，你是小红吗？
            2：你好，我是小红
            3：好，小红，我们开始聊天把
        建立 连接

    UDP B/S架构 人们发短信
        无连接，更节约成本

    C/S架构
        客户端，服务端

    C/S client server
        PYQT 桌面版软件

    B/S架构
        网页版
        browser server
        Django

    二进制传输
    找到目标解析IP
    通过数据，分析业务邮件 视频 网页，游戏

    网络中传输数据，你得编码，不编码。怎么能变成2进制
        decode() 解码
        encode() 编码
    编码 国际组织出台的一个 伯努克力
    Unicode -> utf-8 utf-16 国际中文 万国码
    GBK中文
    ASCII 英文和字符
    a: 97 client
    A: 65

服务端的套路
#1:套接字
    # IP PORT 属性的变量
#2:监听数
    # 当前连接的最大数字
#3:等待连接
    # 阻塞状态
    # 有链接了
#4:let's talk
    # 你得明确目标的IP 和 PORT 套接字
    # 可以向目标的IP和PORT传输反馈信息 套接字
#5:说完了
    # 断开连接
'''

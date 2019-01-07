# coding: UTF-8

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1", 8888))

while True:
    buf = input("你要想服务器说什么:")
    if not buf:
        break
    if buf == "quit":
        break
    client.send(buf.encode("utf-8"))
    data = client.recv(1024)
    if not data:
        print("服务器关闭了!")
        break;
    print("服务器说: ", data.decode("utf-8"))

client.close()

# coding: UTF-8

from socket import *
server = socket(AF_INET, SOCK_STREAM)
server.bind(("", 8899))
server.listen(5)

fp = open('index.html', encoding = 'utf-8')
html = fp.read()

print("web 服务器开启, 等待访问...")

while True:
    client, c_addr = server.accept()
    print("有朋自远方来: ", c_addr)
    data = client.recv(1024)
    print("{} 客人说: {}".format(c_addr, data.decode("utf-8")))

    client.send(html.encode('utf-8'))
    client.close()
server.close()

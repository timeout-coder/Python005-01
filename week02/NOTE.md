1、OSI 参考模型与TCP/IP 模型

OSI 各层的基本作用

应用层：为应用程序提供网络服务
表示层：数据格式化、加密、解密
会话层：建立维护会话和管理链接
传输层：建立和维护端到端链接
网络层：IP地址和路由
数据链路层：控制网络层和物理层之间通信
物理层：比特流传输

2、socket 编程

socket 对象是网络通信的基础，相当于一个管道连接了发送端和接收端，并在两者之间相互传递数据。
对于 TCP，首先服务器启动，服务器和客户端都必须调用 socket() 建立一个套接字 socket，服务器调用 bind() 将套接字与本机指定端口绑定在一起，再调用 listen() 使套接字处于一种被动的准备接收状态。然后客户端建立套接字便可以通过调用 connect() 与服务器建立连接，服务器可以调用accept() 来接收客户端连接，然后继续监听指定端口，并发出阻塞，直到下一个请求出现，从而实现连接多个客户端。建立连接后，客户端和服务器之间就可以发送和接收数据。数据结束传送后，双方调用 close() 关闭套接字。
创建 TCP socket 的语法如下：
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
创建 UDP socket 的语法如下：
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
family 地址簇类型常用的两种：AF_INET (IPv4)、AF_INET6 (IPV6)
type 套接字类型： SOCK_STREAM (TCP)、SOCK_DGRAM(UDP)
bind/connect
   bind(address)
   connect(address)
listen([backlog])

启动一个服务器用于接受连接。如果指定 backlog 则它最低为 0（小于 0 会被置为 0），它指定系统允许暂未 accept 的连接数，超过后将拒绝新连接。未指定则自动设为合理的默认值。
accept()
接受一个连接。返回值是一个 (conn, address) 对，其中 conn 是一个新的套接字对象，用于在此连接上收发数据，address 是连接另一端的套接字所绑定的地址。
recv(bufsize[, flags])
从套接字接收数据。返回值是一个字节对象，表示接收到的数据。bufsize 指定一次接收的最大数据量。
send(bytes[, flags])
发送数据给套接字。本套接字必须已连接到远程套接字。
close(fd)
关闭一个套接字文件描述符。它类似于 os.close()，但专用于套接字。在某些平台上（特别是在 Windows 上），os.close() 对套接字文件描述符无效。

3、with 语句的原理
上下文管理协议（Context Management Protocol）：包含方法 __enter__()和__exit__()，支持该协议的对象要实现这两个方法。
上下文管理器（Context Manager）：支持上下文管理协议的对象，这种对象实现了__enter__()和__exit__()方法。上下文管理器定义执行with语句时要建立的运行时上下文，负责执行with语句块上下文中的进入与退出操作。通常使用with语句调用上下文管理器，也可以通过直接调用其方法来使用。

4、网页爬取
使用requests 库进行HTTP 请求：
1. 发送请求
2. 传递URL参数
3. 定制请求头
4. POST请求
5. 响应状态
6. cookie
7. 请求超时处理
8. 错误和异常处理

5、异常捕获
def a():
    return b()

def b():
    return c()

def c():
    return d()

def d():
    x = 0
    return 100/x

a()

6、lxml 模块 构建和解析html元素 。

例如。解析 html 元素

from lxml import etree
selector = etree.HTML(response.text)
film_name = selector.xpath('//div[@class="hd"]/a/span[1]/text()')
xpath 语法规则。

/从当前节点选取直接子节点
//从当前节点选取子孙节点
@选取属性
..选取当前节点的父节点
.选取当前节点
text() 选取文本内容
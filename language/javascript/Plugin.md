# 插件

## WebUploader 百度文件上传插件

* [官网地址](http://fex.baidu.com/webuploader/)

### 坑

**使用 WebAPI 类型跨域上传文件时:**

接收端需要同时指定 `OPTIONS` 和 `GET/POST` 方式接受

因为此插件会发送两个请求, 第一个请求就是 `OPTIONS` 类型, 如果不指定会出现跨域请求失败的问题

## 打印插件

* [jquery.printarea.js打印页面，有的浏览器打印一页，有的两页](https://bbs.csdn.net/topics/390671098)

* [PrintArea](https://plugins.jquery.com/PrintArea/)

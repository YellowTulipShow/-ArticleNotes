# Java 笔记

## public、private、protected 修饰符访问权限
public，protected，private是Java里用来定义成员的访问权限的，另外还有一种是“default”，也就是在成员前不加任何权限修饰符。如：
```java
public class A {
    void method() {};
}
```
method就属于default权限。

**这四个修饰符的访问权限如下表:**

名称 | 类内部 | package内 | 子类 | 其他
--- | --- | --- | --- | ---
public | ✔ | ✔ | ✔ | ✔
protected | ✔ | ✔ | ✔ | ✔
default | ✔ | ✔ | ✘ | ✘
private | ✔ | ✘ | ✘ | ✘

比如：用protected修饰的成员（变量或方法），在类内部可以调用，同一个package下的其他类也可以调用，子类里也可以调用，其他地方则不可以调用，也就是说在其他

* [Java public、private、protected区别 -访问权限](https://blog.csdn.net/applepie1/article/details/7262419)

## 代码库:
* [点击查看跳转代码库](https://github.com/YellowTulipShow/Java)

## 环境搭建
### Eclipse
* [详细查看编辑器的使用](./eclipse.md)
* [JDK开发包下载](https://www.oracle.com/technetwork/java/javase/downloads/index.html)

## 技巧:
* [点击跳转查看更多](./development_tips_notes.md)

## 开发文档API:
### 下载:
* [帮助方法](https://jingyan.baidu.com/article/6b97984de7c8411ca2b0bf1d.html)
* [java SE 8 api download zip flie](https://www.oracle.com/technetwork/java/javase/documentation/jdk8-doc-downloads-2133158.html)

### 翻译中文版:
* [谷歌版](https://blog.fondme.cn/apidoc/jdk-1.8-google/)
* [有道版](https://blog.fondme.cn/apidoc/jdk-1.8-youdao/)
* [百度版](https://blog.fondme.cn/apidoc/jdk-1.8-baidu/)

## 参考学习链接:
* [Java基础之—反射(非常重要)](https://blog.csdn.net/sinat_38259539/article/details/71799078)
* [java反射详解](http://www.cnblogs.com/rollenholt/archive/2011/09/02/2163758.html)
* [Gson——用java-JSON实现序列化和反序列化](https://www.jianshu.com/p/d78f1b378df1)
* [java获取对象属性类型、属性名称、属性值](https://blog.csdn.net/superit401/article/details/73732873)
* [(java 取系统时间)慎用 System.currentTimeMillis()](http://blog.sina.com.cn/s/blog_6b8bd9d80101fe8t.html)
* [Java中的时间精度](https://blog.csdn.net/elky1982/article/details/4677365)
* [Java enum的用法详解](http://www.cnblogs.com/happyPawpaw/archive/2013/04/09/3009553.html)
* [java枚举类Enum方法简介(valueof,value,ordinal)](https://blog.csdn.net/congqingbin/article/details/7520137)
* [Google翻译 jdk-1.8 Enum class](https://blog.fondme.cn/apidoc/jdk-1.8-google/java/lang/Enum.html)
* [Java实现队列（Queue）的方式](https://blog.csdn.net/jsc123581/article/details/81986714)

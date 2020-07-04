# JavaScript JS 脚本语言学习

自定义和搜集的 插件工具: [PluginTools.js](./PluginTools.js)

#### input 用户输入 浮点数和整数格式化
```js
function input_format() {
    this.value = parseFloat(this.value) || 0; // 格式化为浮点或整数
    this.value = this.value.toFixed(2); // 强制保留小数点后2位
}
document.getElementById('input').onkeyup = input_format; // 键位按起时触发
document.getElementById('input').onchange = input_format; // 内容更改时触发
```

## 制作的样例地址
* [是否支持H5本地存储](https://yellowtulipshow.github.io/javascript/TestIsSupportH5DataSave.html)
* [手机宽度高度显示](https://yellowtulipshow.github.io/javascript/phone_width_height.html)

## 参考学习链接
* [js 删除数组几种方法(大神解决方案)](http://www.cnblogs.com/qiantuwuliang/archive/2010/09/01/1814706.html)
* [JQuery 插件库](http://www.jq22.com/)
* [jquery JSON的解析方式](https://www.cnblogs.com/leejersey/p/3594473.html)
* [JavaScript继承详解](http://www.cnblogs.com/sanshi/archive/2009/07/08/1519036.html)
* [Html5 学习系列（六）Html5本地存储和本地数据库](https://www.cnblogs.com/fly_dragon/p/3946012.html)
* [Javascript面向对象编程一:封装](http://www.ruanyifeng.com/blog/2010/05/object-oriented_javascript_encapsulation.html)
* [Javascript面向对象编程二:构造函数的继承](http://www.ruanyifeng.com/blog/2010/05/object-oriented_javascript_inheritance.html)
* [Javascript面向对象编程三:非构造函数的继承](http://www.ruanyifeng.com/blog/2010/05/object-oriented_javascript_inheritance_continued.html)
* [ 奇怪-正则匹配的test函数](https://www.cnblogs.com/sanshi/archive/2009/07/09/1519585.html)
* [WebSocket 教程 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2017/05/websocket.html)
* [WebSocket 对象文档 - MDN Web docs](https://developer.mozilla.org/zh-CN/docs/Web/API/WebSocket)
* [Web 开发技术Web API 接口参考 - IndexedDB](https://developer.mozilla.org/zh-CN/docs/Web/API/IndexedDB_API)
* [HTML5本地存储——IndexedDB - 知乎](https://zhuanlan.zhihu.com/p/27419332)
* [HTML5 indexedDB前端本地存储数据库实例教程](https://www.zhangxinxu.com/wordpress/2017/07/html5-indexeddb-js-example/)
* [encodeURI()和encodeURIComponent() 区别](https://blog.csdn.net/qq_34629352/article/details/78959707)
* [JS逗号运算符的用法详解](https://blog.csdn.net/wl110231/article/details/8162732)
* [图表插件](https://www.chartjs.org/samples/latest/)
* [图表插件](https://chartjs.bootcss.com/)

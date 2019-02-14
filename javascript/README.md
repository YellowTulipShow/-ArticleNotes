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

## 参考学习链接
* [js 删除数组几种方法(大神解决方案)](http://www.cnblogs.com/qiantuwuliang/archive/2010/09/01/1814706.html)
* [JQuery 插件库](http://www.jq22.com/)
* [jquery JSON的解析方式](https://www.cnblogs.com/leejersey/p/3594473.html)

# Sublime Text 编辑器

## 配置安装
### 编辑器格式配置
```json
{
    // 字体样式
    "font_face": "consolas",

    // 字体大小
    "font_size": 14,

    // 忽略软件包
    "ignored_packages": [
        "Vintage"
    ],

    // tab大小
    "tab_size": 4,

    // 文本自动换行
    "word_wrap": true,
    // "word_wrap": true,

    // 高亮当前行
    "highlight_line": true,

    // 高亮有修改的标签
    "highlight_modified_tabs": true,

    // 添加行宽标尺
    "rulers": [120],

    // 显示空白字符
    "draw_white_space": "selection",

    // 使用空格代替tab内容
    "translate_tabs_to_spaces": true,

    // 保存时自动去除行末空白
    "trim_trailing_white_space_on_save": true,

    // 保存时自动增加文件末尾换行
    "ensure_newline_at_eof_on_save": true,
}
```

### Package Control
使用Package Control组件安装

也可以安装package control组件，然后直接在线安装:

1. 按 **Ctrl+\`** 调出console（注：避免热键冲突）

2. 粘贴以下代码到命令行并回车：
```shell
import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
```

3. 重启Sublime Text 3

4. 如果在Perferences->package settings中看到package control这一项，则安装成功。

### 输入法不跟随光标
解决sublime text3中的不根随光标问题

插件名称：IMESupport

GitHub页面：https://github.com/chikatoike/IMESupport

通过 `Package Control` 在线安装：安装 `Package Control` 插件（安装方法请自行搜索），通过 `Install Package` 选项列出插件列表，搜索 `IMESupport` 安装即可。

### 内置静态服务器
安装插件: SublimeServer

通过 `Install Package` 选项列出插件列表，搜索 `SublimeServer` 安装即可。

GitHub页面：https://github.com/learning/SublimeServer

使用:
```shell
Tools -> SublimeServer ->
    Strat SublimeServer         # 开启服务
    Stop SublimeServer          # 关闭服务
    Restart SublimeServer       # 重启服务
    Settings                    # 配置
```

配置 Settings:
```json
{
    "attempts": 5,
    "autorun": true,
    "defaultExtension": ".html",
    "interval": 500,
    "mimetypes":
    {
        "": "application/octet-stream",
        ".c": "text/plain",
        ".h": "text/plain",
        ".py": "text/plain"
    },

    // 开启服务的端口
    "port": 4001,
}
```

开启服务后, 打开浏览器, 输入地址: `127.0.0.1:4001` 即可访问静态服务器

Ps: 使用时, 关闭 `Sublime Text` 软件, `SublimeServer` 也会同步关闭


## 常用问题:
### 顶部菜单栏消失了
快捷键: `Ctrl` + `Shift` + `P` 打开命令框选择 -> `View:Toggle Menu` 选项即可


## 参考学习链接:
```shell
# 配置Chrome支持本地（file协议）的AJAX请求
http://www.cnblogs.com/micua/p/chrome-file-protocol-support-ajax.html

# 用sublime server 启动本地服务器（手机访问电脑页面）
http://www.cnblogs.com/lhy-93/p/5741274.html

# Sublime Text 有哪些使用技巧？
https://www.zhihu.com/question/24896283

# sublime安装服务器sublimeServer插件
https://blog.csdn.net/tengxing007/article/details/76038475
```

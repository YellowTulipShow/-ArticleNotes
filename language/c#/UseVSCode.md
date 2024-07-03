# 使用VSCode开发注意文档

## 安装 C# 扩展插件

开发时没有智能提示和调试工具时就是 `omnisharp` 和 `debugger` 没有安装好, 默认情况下是自动联网安装的, 但绝大部分情况安装不好

那么就需要手动安装:

首选需要找到C#插件的配置文件

目录是:
* `C:\Users\***\.vscode\extensions\ms-vscode.csharp-****` 或者
* `C:\Users\***\.vscode\extensions\ms-dotnettools.csharp-****`

然后找到配置文件: `project.json`, 打开找到配置项: `runtimeDependencies`

再其中选择需要的版本 `OmniSharp` 配置项

其中 `url` 就是预计下载的文件路径, 直接下载即可

其中压缩包内容解压到上述C#插件根目录 `.omnisharp` 目录下

`Debugger`也是同理, 不过是解压到 `.debugger` 目录下

完成后创建空文件: `install.LOCK` 表示安装完成, 重启 VSCode 即可正常开发

## 链接

* [C# for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)
* [VS Code离线配置omnisharp和debugger](https://www.cnblogs.com/xiaojwang/p/8662211.html)

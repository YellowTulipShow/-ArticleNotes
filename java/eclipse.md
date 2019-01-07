# Eclipse 编辑器的使用:

## 常用配置位置:
### 字体
```shell
# 字体样式与大小:
window -> Preferences -> General -> Appearance -> Colors and Fonts -> 右侧面板 -> 语言选择: Basic -> Text Font | Text Editor Block Selection Font
```

### Tab 行号
```shell
# 全局设置
window -> Preferences -> General -> Editors -> Text Editors -> 右侧面板底部
    Displayed tab width # 填写: Tab长度为4
    Insert spaces for tabs # 勾选: 使用空格来替换Tab
    Show line numbers # 勾选: 显示行号

# 设置 Java 代码格式
window -> Preferences -> Java -> Code Style -> Formatter -> 右侧面板 -> Actice profile -> Edit -> 弹出面板
    # 缩进
    Indentaion -> General settings ->
        Tab policy -> 选择 Spaces Only
        Indentation size -> 4
        Tab size -> 4
```

### 编码设置
```shell
# 修改工作空间默认编码:
window -> Preferences -> General -> Workspace -> 右侧面板底部 -> Text file Encoding | New text file line delimiter

# 修改文件的编码
Eclipse项目文件上右键 -> Properties -> Resource -> 右侧面板 -> Text file Encoding | New text file line delimiter

# 修改某文件类型的编码
window -> Preferences -> General -> Content Types -> 右侧面板 -> 找到要修改的文件的类型 -> 底部 Default encoding 填写编码(UTF-8) -> Update -> OK

# 修改单个文件的编码
任意文件上右键 -> Properties -> Resource -> 右侧面板 -> Text file Encoding
```

## 常用技巧:

### 代码格式化
```shell
# 链接: https://jingyan.baidu.com/article/4f7d5712ae407f1a201927b6.html
# 代码格式化
    快捷键: Ctrl+Shift+F
# 如果失效 输入法其他程序快捷键占用:
    文件空白处右键 -> source -> format
```

### 动态刷新工程目录文件
```shell
右键需要刷新的文件夹 -> Refresh(F5)
```

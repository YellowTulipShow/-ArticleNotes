# 使用 Android Studio 工具开发

## 文档
* [探索 Android Studio](https://developer.android.google.cn/studio/intro)

## 设置
### IDE 软件字体大小设置
    File -> Setting (对话框) ->
    Appearance & Behavior -> Appearance -> UI Options ->
    Override default font by (not recommended) 勾选 -> 选择字体和大小 -> OK

### 代码编辑区字体
    File -> Setting (对话框) ->
    Editor -> Colors & Fonts -> Font ->
    Save As (这里注意第一次设置需要 额外保存一个Scheme, 默认的Scheme 不支持修改) ->
    Editor Font -> 选择字体和大小 -> OK

### 关闭拼写检查
    File -> Setting (对话框) ->
    Editor -> Inspections ->
    Spelling 取消勾选 -> OK
* [Android Studio关闭拼写错误提示](https://jingyan.baidu.com/article/e8cdb32b45e6e837052badaa.html)

### 关闭 Insert App Indexing
    File -> Setting (对话框) ->
    Editor -> Intentions ->
    Android -> Insert App Indexing API Code 取消勾选 -> OK
不是很明白这个是什么? 但是在代码编辑区域总是弹黄色灯泡让你添加, 添加之后代码就炸了, 无法运行编译 贼烦!!!
* [怎么让android studio不indexing](https://zhidao.baidu.com/question/370604206984525924.html?qbl=relate_question_0)

## 快捷键
键位 | 功能说明
---- | ---
**Ctrl + Q** | 把光标移至方法处，按此组合键可快速查看方法的说明文档。
**Ctrl + B** | 直接跳转到类、方法、成员变量定义的地方。与Ctrl+鼠标左键效果一样
**Alt + F7** | 选中方法的, 查找所有引用项
**Shift + F6** | 把光标放在变量上, 批量更改重命名 [变量 / 文件 / 方法] 名称

* [键盘快捷键 - 官网详细说明](https://developer.android.google.cn/studio/intro/keyboard-shortcuts)

## 参考学习链接
* [AndroidStudio编译提速，快过eclipse](https://blog.csdn.net/zero_and_one/article/details/42009487)
* [Android Studio单元测试入门](https://github.com/soaringEveryday/BlogRoad/blob/master/Android%20Studio%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95%E5%85%A5%E9%97%A8.md)

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




## Eclipse空间的基本配置
### 程序的编译和运行的环境配置(一般不改)
    window -- Preferences -- Java
    编译环境：Compiler   默认选中的就是最高版本。
    运行环境：Installed JREs 默认会找你安装的那个JDK。建议配置了Java的环境变量。
    问题：
    低编译，高运行。可以。
    高编译，低运行。不可以。
        建议，编译和运行的版本一致。

### 如何去掉默认注释?
    window -- Preferences -- Java -- Code Style -- Code Templates
    选择你不想要的内容，通过右边Edit编辑。
    注意：请只删除注释部分，不是注释部分的不要删除。

### 行号的显示和隐藏
    显示：在代码区域的最左边的空白区域，右键 -- Show Line Numbers即可。
    隐藏：把上面的动作再做一次。

### 字体大小及颜色
### Java代码区域的字体大小和颜色：
            window -- Preferences -- General -- Appearance -- Colors And Fonts -- Java修改 -- Java Edit Text Font
### 控制台
            window -- Preferences -- General -- Appearance -- Colors And Fonts -- Debug -- Console font
### 其他文件
            window -- Preferences -- General -- Appearance -- Colors And Fonts -- Basic -- Text Font

### 窗体给弄乱了，怎么办?
        window -- Reset Perspective

### 控制台找不到了，怎么办?
        Window--Show View—Console

## 常用快捷键
    alt+/ 内容辅助键
        1、main+alt+/ 回车
            补齐main函数代码格式
        2、输出语句 syso+alt+/
            将控制台输出代码自动写好
        3、提示作用
            帮助你补齐一些你记不住的东西，还可以帮你名字等
    格式化  ctrl+shift+f
    导入包  ctrl+shift+o
        如果该类仅仅在一个包中有，就自己显示了
        如果该类在多个包中有，会弹出一个框框供你选择
    注释
        单行：注释 ctrl+/，取消注释再来一次。
        多行：ctrl+shift+/,ctrl+shift+\
    代码上下移动
        选中代码alt+上/下箭头
    查看源码
        选中类名(F3或者Ctrl+鼠标点击)

## 如何提高开发效率
    自动生成构造方法
    无参构造方法 在代码区域右键--source--Generate Constructors from Superclass
    带参构造方法 在代码区域右键--source--Generate Constructors using fields.. -- finish
    自动生成getXxx()/setXxx()方法
        在代码区域右键--source--Generate Getters and Setters...

    提供了对应的快捷键操作。
        alt+shift+s
        按下带有下划线的那个字母即可。

### 如何继承抽象类和实现接口。
    Override的作用
        表示该方法是重写父类的。如果方法声明和父类不匹配，就会报错。

## 通过讲解的快捷键和提高开发效率的一些内容完成如下内容
    自定义学生类:Student
        成员变量；
            姓名
            年龄
        构造方法：
            无参
            带参
        成员方法：
            getXxx()/setXxx()
            在给出一个show()方法，显示类的所有成员信息。

    然后，写一个测试类，对学生的代码进行测试。
        StudentDemo

## 删除项目和导入项目
    删除项目
        选中项目 – 右键 – 删除
            从项目区域中删除
            从硬盘上删除

    导入项目
        在项目区域右键找到import
        找到General，展开，并找到
        Existing Projects into Workspace
        点击next,然后选择你要导入的项目
        注意：这里选择的是项目名称

## 要注意的几个小问题
    如何查看项目所在路径
        选中 -- 右键 -- Properties -- Resource -- Location
    导入项目要注意的问题
        项目区域中不可能出现同名的项目(新建或者导入)
        自己随意建立的文件夹是不能作为项目导入的
    修改项目问题
        不要随意修改项目名称
        如果真要修改，不要忘记了配置文件.project中的
        <name>把这里改为你改后的名称</name>


## 接收文件的注意事项
    专门建立一个文件夹用于接收项目，不要随意放置。
    同一个项目再次接收的时候，先去存放目录把原始项目删除，然后重新存储，最后刷新项目即可。
    每天对照我写的项目，自己也创建一个练习项目
    举例：我的项目名称 day11_eclipse
          你就创建一个项目名称 day11_eclipse_test

## Eclipse中代码的高级(Debug)调试
    作用：
        调试程序
        查看程序执行流程

    如何查看程序执行流程
        要想看程序流程，就必须设置断点。

        什么是断点：
            就是一个标记，从哪里开始。

        如何设置断点：
            你想看哪里的程序，你就在那个有效程序的左边双击即可。

        在哪里设置断点：
            哪里不会点哪里。
            目前：我们就在每个方法的第一条有效语句上都加。

        如何运行设置断点后的程序：
            右键 -- Debug as -- Java Application

        看哪些地方：
            Debug：断点测试的地方
                在这个地方，记住F6，或者点击也可以。一次看一行的执行过程。
            Variables：查看程序的变量变化
            ForDemo：被查看的源文件
            Console：控制台

        如何去断点：
            再次双击即可
            找到Debug视图，Variables界面，找到Breakpoints，并点击，然后看到所有的断点，最后点击那个双叉。
## jar包
    将一个项目的编译出来的*.class文件打包成一个可携带的压缩包，方便于跨项目使用
    创建jar包：
        在eclipse中选择项目---右键---Export(导出)---java---JAR File---自己指定一个路径用于存放包---Finish
    使用jar包：
        复制jar包到项目路径下并添加至构建路径下
            选中复制过来的jar文件---右键---Build Path---Add Build Path
## 说明文档：
    在eclipse中选择项目---右键---Export(导出)---Javadoc---可以选择目录(最后一个目录是文件夹，不要加后缀名)

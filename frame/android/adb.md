# ADB

可以在 `Window` 电脑上通过 `ADB` 直接与 `Android` 手机进行关联操作 比如开发手机 `Shell`

## ADB 工具命令
工具获取地址: (已经保存到百度网盘 ====)
* [百度网盘 - 提取码: a9w7](https://pan.baidu.com/s/1fPqkweSFdqPPzKLZvlTtqg)

## 基础命令

### 查看连接的设备
    adb devices

### 进入android shell
    adb shell

### 进入Fastboot mode
    adb reboot bootloader

### 单刷recovery.img
    fastboot flash recovery recovery.img

### 使用 ### 解锁码解锁设备:
    fastboot oem unlock ###

### 安装 ###.apk APP 软件
    adb install ###.apk

## 参考学习链接:
* [什么是adb工具？怎么用？](https://jingyan.baidu.com/article/ce4366494962083773afd3d0.html)

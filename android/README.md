# Android 笔记

## 环境搭建
### Eclipse 开发工具包
链接: https://pan.baidu.com/s/1_Y7cmIMfzBWoeiaiPg9ekg 提取码: 4gxv


### 使用 adb 动态刷新安卓设备
```shell
# 切换到 adb 程序根目录执行命令:
# window: 资源管理器 (shift + 鼠标右键) -> 在此处打开命令窗口
> adb devices
```
更多 adb 学习:
* [什么是adb工具？怎么用？](https://jingyan.baidu.com/article/ce4366494962083773afd3d0.html)


## 开发文档:
### 官网英文版:
https://docs.oracle.com/javase/8/docs/api/

### 翻译中文版:
http://www.android-doc.com/reference/packages.html

## 正式签名:
### 查看地址:
#### Eclipse:
```shell
window -> Preferences -> Android -> Build -> 右侧面板 -> Custom debug keystore
```

### 创建新签名:
#### Eclipse:
```shell
右击 XXX 项目 -> Android Tools -> Export Signed Application Package -> 弹出面板 ->
Project Checks (检查项目) -> Next ->
Keystore selection ->
    Create new keystore ->
        Location (路径): 如: D:\\[name].keystore
        Password (密码):
        Confirm (确认密码): -> Next ->
Key Creation: (创建 keystore 文件所必要的信息)
    Alias (别名, 默认填写):
    Password (密码):
    Confirm (确认密码):
    Validity(years) (合法期限,年为单位): 500
    First and Last Name (名字和姓氏): YTS.ZRQ
    Organizational Unit (组织单元): Individual (个人)
    Organization (组织): Individual
    City or Locality (城市或地区): QingDao
    State or Province (州或省): ShanDong
    Country Code (XX) (国家代码): China -> Next ->
Destination and key/certificate checks (目的地和密钥/证书检查):
    Destination APK file (生成的APK文件输出地址): D:\\Download -> Finish (完成)
```

## 打包项目
https://jingyan.baidu.com/article/fedf0737b7e76835ac8977a6.html

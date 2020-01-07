# 使用 Eclipse IDE 开发 Android 程序

## 打包项目
* [百度百科 - eclipse怎么打包android项目](https://jingyan.baidu.com/article/fedf0737b7e76835ac8977a6.html)

## 测试
* [Eclipse IDE Android Test Project](http://www.cnblogs.com/GnagWang/archive/2010/12/16/1908710.html)

## 设置
* [多数在 Eclipse 中的设置请详看 Java 配置](../java/eclipse.md)

## 查看签名
    window ->
    Preferences ->
    Android ->
    Build ->
    右侧面板 ->
    Custom debug keystore

## 创建新签名
过程步骤:

    右击 XXX 项目 ->
    Android Tools ->
    Export Signed Application Package ->
    弹出面板 ->
    Project Checks (检查项目) -> Next ->
    Keystore selection ->
        Create new keystore ->
            Location (路径): 如: D:\\[name].keystore
            Password (密码):
            Confirm (确认密码):
    Next ->
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
        Country Code (XX) (国家代码): China
    Next ->
    Destination and key/certificate checks (目的地和密钥/证书检查):
        Destination APK file (生成的APK文件输出地址): D:\\Download ->
    Finish (完成)

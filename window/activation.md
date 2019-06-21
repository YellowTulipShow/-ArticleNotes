# 激活

## Window10:

* [Win10专业版永久激活方法](https://jingyan.baidu.com/article/73c3ce2812e0ede50343d9f8.html)
* [**好用: w10怎么激活**](https://zhidao.baidu.com/question/371166074023061124.html)

命令:
```powershell
// 卸载当前产品密钥
slmgr.vbs /upk

// 设置产品密钥
slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX

// 设置批量激活地区地址
slmgr /skms zh.us.to

// 开始激活
slmgr /ato

// 查看激活状态 (有时间限制到期激活结束 尝试重新使用上面方法激活)
slmgr.vbs -xpr
```

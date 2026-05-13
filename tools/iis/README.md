
## 配置

使用管理员身份运行cmd

应用程序池：

```cmd
# 导出所有应用程序池
%windir%\system32\inetsrv\appcmd list apppool /config /xml > D:\Work\YTS.ErTuiShengShi\Account_ErTuiShengShi\configs\apppools.xml

# 导入所有应用程序池
%windir%\system32\inetsrv\appcmd add apppool /in < D:\Work\YTS.ErTuiShengShi\Account_ErTuiShengShi\configs\apppools.xml
```

站点：

```cmd
# 导出所有站点
%windir%\system32\inetsrv\appcmd list site /config /xml > D:\Work\YTS.ErTuiShengShi\Account_ErTuiShengShi\configs\sites.xml

# 导入所有站点
%windir%\system32\inetsrv\appcmd add site /in < D:\Work\YTS.ErTuiShengShi\Account_ErTuiShengShi\configs\sites.xml
```

﻿@ECHO OFF


@echo
@echo 此处由 YellowTulipShow(https://github.com/YellowTulipShow/) 整理发布
@echo
del /f /s /q "C:\Windows\SoftwareDistribution\Download\*"
rd /s /q %windir%\temp & md %windir%\temp


@echo 此批处理由护卫神(http://www.huweishen.com)整理发布
@echo 　　
@echo 清理几个比较多垃圾文件的地方
DEL /F /S /Q "C:\WINDOWS\PCHealth\ERRORREP\QSIGNOFF\*.*"
DEL /F /S /Q "C:\WINDOWS\PCHealth\ERRORREP\UserDumps\*.*"
DEL /F /S /Q "C:\WINDOWS\system32\LogFiles\HTTPERR\*.*"
DEL /F /S /Q "C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\Temporary ASP.NET Files\*.*"
DEL /F /S /Q "C:\WINDOWS\Microsoft.NET\Framework\v1.1.4322\Temporary ASP.NET Files\*.*"
DEL /F /S /Q "C:\windows\temp\*.*"
DEL /F /S /Q /A:S "C:\WINDOWS\IIS Temporary Compressed Files\*.*"

@echo 删除补丁备份目录
RD %windir%\$hf_mig$ /Q /S

@echo 把补丁卸载文件夹的名字保存成2950800.txt
dir %windir%\$NtUninstall* /a:d /b >%windir%\2950800.txt

@echo 从2950800.txt中读取文件夹列表并且删除文件夹
for /f %%i in (%windir%\2950800.txt) do rd %windir%\%%i /s /q

@echo 删除2950800.txt
del %windir%\2950800.txt /f /q

@echo 删除补丁安装记录内容（下面的del /f /s /q %systemdrive%\*.log已经包含删除此类文件）
del %windir%\KB*.log /f /q

@echo 删除系统盘目录下临时文件
del /f /s /q %systemdrive%\*.tmp

@echo 删除系统盘目录下临时文件
del /f /s /q %systemdrive%\*._mp

@echo 删除系统盘目录下日志文件
del /f /s /q %systemdrive%\*.log

@echo 删除系统盘目录下GID文件(属于临时文件，具体作用不详)
del /f /s /q %systemdrive%\*.gid

@echo 删除系统目录下scandisk（磁盘扫描）留下的无用文件
del /f /s /q %systemdrive%\*.chk

@echo 删除系统目录下old文件
del /f /s /q %systemdrive%\*.old

@echo 删除回收站的无用文件
del /f /s /q %systemdrive%\recycled\*.*

@echo 删除系统目录下备份文件
del /f /s /q %windir%\*.bak

@echo 删除应用程序临时文件
del /f /s /q %windir%\prefetch\*.*

@echo 删除系统维护等操作产生的临时文件
del /f /s /q %windir%\temp\*.*

@echo 删除当前用户的COOKIE（IE）
del /f /s /q %userprofile%\cookies\*.*

@echo 删除internet临时文件
del /f /s /q "%userprofile%\local settings\temporary internet files\*.*"

@echo 删除当前用户日常操作临时文件
del /f /s /q "%userprofile%\local settings\temp\*.*"

@echo 删除访问记录（开始菜单中的文档里面的东西）
del /f /q "%userprofile%\recent\*.*"
del /f /s /q "%userprofile%\recent\*.*"

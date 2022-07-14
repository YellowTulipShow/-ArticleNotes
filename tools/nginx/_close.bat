@echo off
::切换执行环境编码为UTF-8
@chcp 65001

::获取=> 环境路径
set execute_environment_path=%cd%
::切换=> 当前脚本文件路径
cd /d %~dp0
::获取=> 当前脚本文件路径
set script_file_path=%cd%

echo 发布执行 Nginx

tasklist | find /i "nginx.exe" || exit
taskkill /im nginx.exe /f

echo 执行完毕!

::切换=> 环境路径
cd /d %execute_environment_path%
::判断=> 当前脚本文件路径==环境路径 执行用户等待命令
if %execute_environment_path%==%script_file_path% TIMEOUT /T -1

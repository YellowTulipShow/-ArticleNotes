@echo off
::切换执行环境编码为UTF-8
@chcp 65001
::获取=> 环境路径
set execute_environment_path=%cd%
::切换=> 当前脚本文件路径
cd /d %~dp0

git pull origin master
git status
git add .
git commit -m "update data"
git push origin master
git logs
echo "执行完毕!"

::切换=> 环境路径
cd /d %execute_environment_path%
TIMEOUT /T -1

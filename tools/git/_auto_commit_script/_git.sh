#!/bin/bash

# 获取=> 环境路径
execute_environment_path=`pwd`
# 切换=> 当前脚本文件路径
cd `dirname $0`

git pull origin master
git add .
git commit -m "update data"
git status
git push origin master
git logs
echo "执行完毕!"

# 切换=> 环境路径
cd $execute_environment_path

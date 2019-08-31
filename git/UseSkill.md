# 使用技巧

#### 查看当前分支所有提交者及其提交次数，按次数由高到低排序
```shell
git log | grep "^Author: " | awk '{print $2}' | sort | uniq -c | sort -k1,1nr
```
* [来源:博客地址](https://blog.csdn.net/cyf15238622067/article/details/82980782)


#### 分析 Git 日志来统计代码量
```shell
git log --author="_your_name_" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }'
```
```
输出结果：added lines: 38861, removed lines: 22916, total lines: 15945
```
* [来源:博客地址](https://blog.csdn.net/cyf15238622067/article/details/82980782)

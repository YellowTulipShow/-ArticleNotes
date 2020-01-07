# 各语言使用正则表达式

## Python
### 提取长字符串当中的单词
```python
strlist = '''
add
bundle
commit
'''
import re
re_model = re.compile(r'([a-zA-Z-]+)\s*', re.I | re.M | re.U)
result = re_model.findall(strlist)
# result = ['add', 'bundle', 'commit']
```

### 判断是否 Window 格式的路径
```python
import re
result = re.match(r"[a-zA-Z]:\\.*", r"/D/ZRQWork/") # None
result = re.match(r"[a-zA-Z]:\\.*", r"D:\\ZRQWork\\") # re.object
```

## JavaScript
### 修饰符
```shell
i   # 执行对大小写不敏感的匹配。
g   # 执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。
m   # 执行多行匹配。
```

### 判断是否匹配
```js
var isbool
isbool = /^admin$/gi.test("admin"); // true
isbool = /^admin$/gi.test("aDmIn"); // true
isbool = /^admin$/gi.test("aDmDIn"); // false
isbool = /^admin$/gi.test("1aDmIn"); // false
```

### 字符串替换 - 只要数字
```js
var result = "2524Ewq533".replace(/[^\d]/g, ""); // "2524533"
```

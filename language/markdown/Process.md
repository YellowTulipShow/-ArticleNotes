# 流程图

## 定义语法
```shell
tag=>type: content:>url
```

`tag` 就是元素名字
`type` 是这个元素的类型, 有6种类型, 分别为:
```
start         # 开始
end           # 结束
operation     # 操作
subroutine    # 子程序
condition     # 条件
inputoutput   # 输入或产出
```

`content` 就是在框框中要写的内容，注意type后的冒号与文本之间一定要有个空格。
`url` 是一个连接，与框框中的文本相绑定

## 连接元素的语法
用 `->` 符号来连接两个元素，需要注意的是 `condition` 类型，因为他有 `yes` 和 `no` 两个分支，所以要写成
```shell
c2(yes)->io->e
c2(no)->op2->e
```

## 实例:
### 实例1 (小例子)
代码:
```shell
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```

效果图:
```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```

### 实例2 (比较全)
代码:
```shell
st=>start: Start
e=>end: End
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
sub2=>subroutine: Two Subroutine
cond=>condition: Yes or No?
io=>inputoutput: catch something...

st->op1->sub2->cond
cond(yes)->io->e
cond(no)->sub1(right)->op1
```

效果图:
```flow
st=>start: Start
e=>end: End
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
sub2=>subroutine: Two Subroutine
cond=>condition: Yes or No?
io=>inputoutput: catch something...

st->op1->sub2->cond
cond(yes)->io->e
cond(no)->sub1(right)->op1
```

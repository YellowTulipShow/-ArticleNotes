# SQLite 数据库

## 显示读取数据库内容
工具下载:
* [sqlcipher.exe 百度链接 -  提取码: tqum](https://pan.baidu.com/s/137UmjTCgeuB7lhmSikfjJA)

### 读取 sqlcipher 加密数据库
比如微信的 **EnMicroMsg.db** 数据库是已经加密的, 注意!!! 巨坑如下:

直接使用 Android 程序从微信的包下把数据库复制出来...即!可!

注意: 仅仅只是复制! 仅仅只是复制! 仅仅只是复制! 重要的话说三遍!!!

不要在程序中直接打开数据库, 否则复制出来的数据无法读取, 会报错 is not a database 烦死你!!!

然后使用 sqlcipher.exe 工具正常打开, 输入密码, 就可以显示查看数据库结构了

## 查询表结构
### 查询数据库中拥有哪些表
```sql
select * from sqlite_master
```
例如:

type | name | tbl_name | rootpage | sql
---- | ---- | -------- | -------- | ---
table | rcontect | rcontect | 2 | CREATE TABLE rcontect (\`text\` TEXT, \`numberic\` NUMERIC, \`blob\` BLOB, \`integer_primary_key\` INTEGER PRIMARY KEY);

### 具体哪一个表的信息
```sql
# 注意: 仅替换 'table_name' 即可, 必须带小括号
PRAGMA table_info(table_name)
```
例如:

cid | name | type | notnull | dflt_value | pk
--- | ---- | ---- | ------- | ---------- | --
0 | text | TEXT | 0  |  | 0
1 | numberic | NUMERIC | 0 |  | 0
2 | blob | BLOB | 0 |  | 0
3 | integer_primary_key | INTEGER | 0 |  | 1

### 学习链接
* [sqlite查询库里所有表名](https://blog.csdn.net/runtime233/article/details/52439881)

## 数据格式
SQLite 数据类型是一个用来指定任何对象的数据类型的属性。SQLite 中的每一列，每个变量和表达式都有相关的数据类型。您可以在创建表的同时使用这些数据类型。SQLite 使用一个更普遍的动态类型系统。在 SQLite 中，值的数据类型与值本身是相关的，而不是与它的容器相关。

### SQLite 存储类
每个存储在 SQLite 数据库中的值都具有以下存储类之一：

存储类 | 描述
--- | ---
NULL | 值是一个 NULL 值。
INTEGER | 值是一个带符号的整数，根据值的大小存储在 1、2、3、4、6 或 8 字节中。
REAL | 值是一个浮点值，存储为 8 字节的 IEEE 浮点数字。
TEXT | 值是一个文本字符串，使用数据库编码（UTF-8、UTF-16BE 或 UTF-16LE）存储。
BLOB | 值是一个 blob 数据，完全根据它的输入存储。

SQLite 的存储类稍微比数据类型更普遍。INTEGER 存储类，例如，包含 6 种不同的不同长度的整数数据类型。

### SQLite 亲和(Affinity)类型
SQLite支持列的亲和类型概念。任何列仍然可以存储任何类型的数据，当数据插入时，该字段的数据将会优先采用亲缘类型作为该值的存储方式。SQLite目前的版本支持以下五种亲缘类型：

亲和类型 | 描述
--- | ---
TEXT | 数值型数据在被插入之前，需要先被转换为文本格式，之后再插入到目标字段中。
NUMERIC | 当文本数据被插入到亲缘性为NUMERIC的字段中时，如果转换操作不会导致数据信息丢失以及完全可逆，那么SQLite就会将该文本数据转换为INTEGER或REAL类型的数据，如果转换失败，SQLite仍会以TEXT方式存储该数据。对于NULL或BLOB类型的新数据，SQLite将不做任何转换，直接以NULL或BLOB的方式存储该数据。需要额外说明的是，对于浮点格式的常量文本，如"30000.0"，如果该值可以转换为INTEGER同时又不会丢失数值信息，那么SQLite就会将其转换为INTEGER的存储方式。
INTEGER | 对于亲缘类型为INTEGER的字段，其规则等同于NUMERIC，唯一差别是在执行CAST表达式时。
REAL | 其规则基本等同于NUMERIC，唯一的差别是不会将"30000.0"这样的文本数据转换为INTEGER存储方式。
NONE | 不做任何的转换，直接以该数据所属的数据类型进行存储。　　

### Boolean 数据类型
SQLite 没有单独的 Boolean 存储类。相反，布尔值被存储为整数 0（false）和 1（true）。

### Date 与 Time 数据类型
SQLite 没有一个单独的用于存储日期和/或时间的存储类，但 SQLite 能够把日期和时间存储为 TEXT、REAL 或 INTEGER 值。

存储类 | 日期格式
--- | ---
TEXT | 格式为 "YYYY-MM-DD HH:MM:SS.SSS" 的日期。
REAL | 从公元前 4714 年 11 月 24 日格林尼治时间的正午开始算起的天数。
INTEGER | 从 1970-01-01 00:00:00 UTC 算起的秒数。

您可以以任何上述格式来存储日期和时间，并且可以使用内置的日期和时间函数来自由转换不同格式。

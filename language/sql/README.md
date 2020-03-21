# SQL 数据库操作语句

## ALTER TABLE:
如需在表中添加列,请使用下列语法:
```sql
ALTER TABLE table_name
ADD column_name datatype
```

要删除表中的列,请使用下列语法:
```sql
ALTER TABLE table_name
DROP COLUMN column_name
-- 注释:某些数据库系统不允许这种在数据库表中删除列的方式 (DROP COLUMN column_name)
```

要改变表中列的数据类型，请使用下列语法：
```sql
ALTER TABLE table_name
ALTER COLUMN column_name datatype
```

## 删除内容:
删除数据表内容和表的三种方式:
```sql
-- 指定数据
delete from TableName where id=1

-- 删除整个表数据,完全清空,但不删除格式结构
truncate table TableName

-- 删除整个表,全部清空: 数据,格式,结构, 然后... 就没有然后了
drop table TableName
```

## 查询:
### 查询所有表行数
```sql
select b.name,a.row_count from sys.dm_db_partition_stats a,
sys.objects b
where a.object_id=b.object_id
and a.index_id<=1
and b.type='U'
order by a.row_count desc
```

## 测试创建表
```sql
--创建表
create table 表(a1 varchar(10),a2 char(2))
--为表添加描述信息
EXECUTE sp_addextendedproperty N'MS_Description', '人员信息表', N'user', N'dbo', N'table', N'表', NULL, NULL
--为字段a1添加描述信息
EXECUTE sp_addextendedproperty N'MS_Description', '姓名', N'user', N'dbo', N'table', N'表', N'column', N'a1'
--为字段a2添加描述信息，
EXECUTE sp_addextendedproperty N'MS_Description', '性别', N'user', N'dbo', N'table', N'表', N'column', N'a2'
--更新表中列a1的描述属性：
EXEC sp_updateextendedproperty 'MS_Description','字段1','user',dbo,'table','表','column',a1
--删除表中列a1的描述属性：
EXEC sp_dropextendedproperty 'MS_Description','user',dbo,'table','表','column',a1
--删除测试
drop table 表
```

## 创建数据库
```sql
Create DataBase YTSSYS on (
    Name ='YTSSYS',
    FileName='D:\Downloads\DataBase\YTSSYS.mdf',
    Size = 10MB,
    MaxSize = UNLIMITED,
    FileGrowth = 10%
) log on (
    Name= 'YTSSYS_log',
    FileName='D:\Downloads\DataBase\YTSSYS_log.ldf',
    Size = 3MB, MaxSize = 5MB, FileGrowth = 1MB
)
sp_helpdb YTSSYS
```

## 修改数据库
```sql
Alter DataBase YTSDataB
```


## 运行时间
```sql
declare @d datetime
set @d=getdate()
/*你的SQL脚本开始*/
SELECT [TestCase] FROM [TestCaseSelect]
/*你的SQL脚本结束*/
select [语句执行花费时间(毫秒)]=datediff(ms,@d,getdate())
```


## 参考学习链接:
* [SQL中char、varchar、nvarchar的区别](http://www.cnblogs.com/carekee/articles/2094676.html)
* [查看sql语句执行时间/测试sql语句性能](http://www.cnblogs.com/qanholas/archive/2011/05/06/2038543.html)
* [SQL server 树形递归查询](https://blog.csdn.net/weixin_36408281/article/details/81316334)
* [Sqlite Browser](https://sqlitebrowser.org/)

# Microsoft SQL Server 微软关系型数据库

## 使用技巧
* [SQL Server2012如何导出sql脚本并且还原数据库](https://www.cnblogs.com/seekdream/p/5723079.html)
* [SQL Server直接执行.sql文件](https://blog.csdn.net/m0_37988746/article/details/79517923)

### 操作数据库命令

```shell
osql --help
```

## SQL Server 2012 序列号(密钥)
```
SQL Server 2012 序列号(密钥)：
SQL SERVER 2012 ENTERPRISE CORE: FH666-Y346V-7XFQ3-V69JM-RHW28
SQL SERVER 2012 BUSINESS INTELLIGENCE: HRV7T-DVTM4-V6XG8-P36T4-MRYT6
SQL SERVER 2012 DEVELOPER: YQWTX-G8T4R-QW4XX-BVH62-GP68Y
SQL SERVER 2012 ENTERPRISE SERVER/CAL EDITION: 748RB-X4T6B-MRM7V-RTVFF-CHC8H
SQL SERVER 2012 STANDARD: YFC4R-BRRWB-TVP9Y-6WJQ9-MCJQ7
SQL SERVER 2012 WEB: FB3W8-YRXDP-G8F8F-C46KG-Q998F
Microsoft SQL SERVER 2012 商业智能版激活码序列号: HRV7T-DVTM4-V6XG8-P36T4-MRYT6
Microsoft SQL SERVER 2012 开发版激活码序列号: YQWTX-G8T4R-QW4XX-BVH62-GP68Y
Microsoft SQL SERVER 2012 企业服务器版/CAL版序列号: 748RB-X4T6B-MRM7V-RTVFF-CHC8H
```

## SQL Server 2017 序列号(密钥)
```
Enterprise Core 6GPYM-VHN83-PHDM2-Q9T2R-KBV83
Developer 22222-00000-00000-00000-00000
Enterprise TDKQD-PKV44-PJT4N-TCJG2-3YJ6B
Strandard PHDV4-3VJWD-N7JVP-FGPKY-XBV89
Web WV79P-7K6YG-T7QFN-M3WHF-37BXC
```

## 参考学习链接:
* [解决SQL Server CPU占用率高](https://jingyan.baidu.com/article/39810a239f92f9b636fda6a8.html)
* [sql server查询历史执行sql语句](https://blog.csdn.net/qq_35409113/article/details/109518326)

### sql server查询历史执行sql语句

```sql
SELECT st.text as sql_statement,
       qs.creation_time as plan_last_compiled,
       qs.last_execution_time as plan_last_executed,
       qs.execution_count as plan_executed_count,
       qp.query_plan
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.plan_handle) st
CROSS APPLY sys.dm_exec_query_plan(qs.plan_handle) qp
order by qs.creation_time desc
```

```sql
Select TOP 1000
       ST.text AS '执行的SQL语句',
       QS.execution_count AS '执行次数',
       QS.total_elapsed_time AS '耗时',
       QS.total_logical_reads AS '逻辑读取次数',
       QS.total_logical_writes AS '逻辑写入次数',
       QS.total_physical_reads AS '物理读取次数',
       QS.creation_time AS '执行时间' ,
       QS.*
FROM   sys.dm_exec_query_stats QS
       CROSS APPLY
sys.dm_exec_sql_text(QS.sql_handle) ST
-- Where  QS.creation_time BETWEEN '2020-07-01 00:00:00' AND '2020-09-02 11:00:00'
ORDER BY
     QS.creation_time DESC
```

### 查询表结构

* [访问链接](https://www.cnblogs.com/davidhou/p/6474002.html)

SQL Server表描述 及 字段描述的增、删、改、查询
```sql
--测试:
--创建表及描述信息
create table geovindu(duname varchar(10),isname char(2))
--为表添加描述信息
EXECUTE sp_addextendedproperty N'MS_Description', '人员信息表', N'user', N'dbo', N'table', N'geovindu', NULL, NULL
--为字段duname添加描述信息
EXECUTE sp_addextendedproperty N'MS_Description', '姓名', N'user', N'dbo', N'table', N'geovindu', N'column', N'duname'
--为字段isname添加描述信息
EXECUTE sp_addextendedproperty N'MS_Description', '性别', N'user', N'dbo', N'table', N'geovindu', N'column', N'isname'
--更新表中列duname的描述属性：
EXEC sp_updateextendedproperty 'MS_Description',N'聚文','user',dbo,'table','geovindu','column',duname
EXEC sp_updateextendedproperty N'MS_Description', '涂聚文', N'user', N'dbo', N'table', N'geovindu', N'column', N'duname'
--删除表中列duname的描述属性：
EXEC sp_dropextendedproperty 'MS_Description','user',dbo,'table','geovindu','column',duname
--至于查询出来，sql server有提供系统函数fn_listextendedproperty ()：
--获取某一个字段的描述
SELECT * FROM ::fn_listextendedproperty (NULL, 'user', 'dbo', 'table', 'geovindu', 'column', default)
--其他变数，按照你的要求你照写即可，只要表名换成你的where objname = '字段名
--删除测试
drop table geovindu
go
```

1.SQL查询表的所有字段的备注说明
```sql
---1.SQL查询表的所有字段的备注说明
SELECT Sysobjects.name AS TABLE_NAME, syscolumns.Id, syscolumns.name AS COLUMN_NAME,
systypes.name AS DATA_TYPE, syscolumns.length as CHARACTER_MAXIMUM_LENGTH,
sys.extended_properties.[value] AS COLUMN_DESCRIPTION,  syscomments.text as
COLUMN_DEFAULT,syscolumns.isnullable as IS_NULLABLE FROM syscolumns
INNER JOIN systypes
    ON syscolumns.xtype = systypes.xtype
    LEFT JOIN sysobjects ON syscolumns.id = sysobjects.id
  LEFT OUTER JOIN sys.extended_properties ON
  ( sys.extended_properties.minor_id = syscolumns.colid
    AND sys.extended_properties.major_id = syscolumns.id)
  LEFT OUTER JOIN syscomments ON syscolumns.cdefault = syscomments.id
  WHERE syscolumns.id IN
    (SELECT id FROM SYSOBJECTS WHERE xtype = 'U') AND (systypes.name <> 'sysname')
    ORDER BY table_name,syscolumns.colid
```

2.SQL查询表的所有字段的备注说明
```sql
--2.SQL查询表的所有字段的备注说明
SELECT
(case when a.colorder=1 then d.name else '' end) N'表名',
a.colorder N'字段序号',
a.name N'字段名',
(case when COLUMNPROPERTY( a.id,a.name,'IsIdentity')=1 then '√'else ''
end) N'标识',
(case when (SELECT count(*)
FROM sysobjects
WHERE (name in
           (SELECT name
          FROM sysindexes
          WHERE (id = a.id) AND (indid in
                    (SELECT indid
                   FROM sysindexkeys
                   WHERE (id = a.id) AND (colid in
                             (SELECT colid
                            FROM syscolumns
                            WHERE (id = a.id) AND (name = a.name))))))) AND
        (xtype = 'PK'))>0 then '√' else '' end) N'主键',
b.name N'类型',
a.length N'占用字节数',
COLUMNPROPERTY(a.id,a.name,'PRECISION') as N'长度',
isnull(COLUMNPROPERTY(a.id,a.name,'Scale'),0) as N'小数位数',
(case when a.isnullable=1 then '√'else '' end) N'允许空',
isnull(e.text,'') N'默认值',
isnull(g.[value],'') AS N'字段说明'
FROM syscolumns a
left join systypes b
on a.xtype=b.xusertype
inner join sysobjects d
on a.id=d.id and d.xtype='U' and d.name<>'dtproperties'
left join syscomments e
on a.cdefault=e.id
left join sys.extended_properties g
on a.id=g.major_id AND a.colid = g.minor_id
order by object_name(a.id),a.colorder
```

3.SQL查询表的所有字段的备注说明
```sql
--3. SQL查询表的所有字段的备注说明
SELECT
    TableName=CASE WHEN C.column_id=1 THEN O.name ELSE N'' END,
    TableDesc=ISNULL(CASE WHEN C.column_id=1 THEN PTB.[value] END,N''),
    Column_id=C.column_id,
    ColumnName=C.name,
    PrimaryKey=ISNULL(IDX.PrimaryKey,N''),
    [IDENTITY]=CASE WHEN C.is_identity=1 THEN N'√'ELSE N'' END,
    Computed=CASE WHEN C.is_computed=1 THEN N'√'ELSE N'' END,
    Type=T.name,
    Length=C.max_length,
    Precision=C.precision,
    Scale=C.scale,
    NullAble=CASE WHEN C.is_nullable=1 THEN N'√'ELSE N'' END,
    [Default]=ISNULL(D.definition,N''),
    ColumnDesc=ISNULL(PFD.[value],N''),
    IndexName=ISNULL(IDX.IndexName,N''),
    IndexSort=ISNULL(IDX.Sort,N''),
    Create_Date=O.Create_Date,
    Modify_Date=O.Modify_date
FROM sys.columns C
INNER JOIN sys.objects O ON C.[object_id]=O.[object_id]
    AND O.type='U' AND O.is_ms_shipped=0
INNER JOIN sys.types T ON C.user_type_id=T.user_type_id
LEFT JOIN sys.default_constraints D ON C.[object_id]=D.parent_object_id
    AND C.column_id=D.parent_column_id AND C.default_object_id=D.[object_id]
LEFT JOIN sys.extended_properties PFD ON PFD.class=1
    AND C.[object_id]=PFD.major_id AND C.column_id=PFD.minor_id
-- AND PFD.name='Caption' -- 字段说明对应的描述名称(一个字段可以添加多个不同name的描述)
LEFT JOIN sys.extended_properties PTB ON PTB.class=1
    AND PTB.minor_id=0 AND C.[object_id]=PTB.major_id
-- AND PFD.name='Caption' -- 表说明对应的描述名称(一个表可以添加多个不同name的描述)
LEFT JOIN -- 索引及主键信息
    (
    SELECT
        IDXC.[object_id],
        IDXC.column_id,
        Sort=CASE INDEXKEY_PROPERTY(IDXC.[object_id],IDXC.index_id,IDXC.index_column_id,'IsDescending')
        WHEN 1 THEN 'DESC' WHEN 0 THEN 'ASC' ELSE '' END,
        PrimaryKey=CASE WHEN IDX.is_primary_key=1 THEN N'√'ELSE N'' END,
        IndexName=IDX.Name
    FROM sys.indexes IDX
    INNER JOIN sys.index_columns IDXC ON IDX.[object_id]=IDXC.[object_id]
        AND IDX.index_id=IDXC.index_id
    LEFT JOIN sys.key_constraints KC ON IDX.[object_id]=KC.[parent_object_id]
        AND IDX.index_id=KC.unique_index_id
    INNER JOIN -- 对于一个列包含多个索引的情况,只显示第1个索引信息
        (
            SELECT [object_id], Column_id, index_id=MIN(index_id)
            FROM sys.index_columns
            GROUP BY [object_id], Column_id
        ) IDXCUQ ON IDXC.[object_id]=IDXCUQ.[object_id]
            AND IDXC.Column_id=IDXCUQ.Column_id    AND IDXC.index_id=IDXCUQ.index_id
    ) IDX ON C.[object_id]=IDX.[object_id]
    AND C.column_id=IDX.column_id
    --WHERE O.name=N'tablename' -- 如果只查询指定表,加上此条件
ORDER BY O.name,C.column_id
```

### 查询SQL Server数据库中的所有级联约束并导出为SQL脚本

方法一：使用系统视图查询
```sql
-- 查询所有外键约束及其级联操作设置
SELECT
    obj.name AS '约束名称',
    sch1.name + '.' + tab1.name AS '主表',
    col1.name AS '主表列',
    sch2.name + '.' + tab2.name AS '引用表',
    col2.name AS '引用表列',
    CASE WHEN fk.delete_referential_action = 1 THEN 'ON DELETE CASCADE'
         WHEN fk.delete_referential_action = 2 THEN 'ON DELETE SET NULL'
         WHEN fk.delete_referential_action = 3 THEN 'ON DELETE SET DEFAULT'
         ELSE '' END AS '删除操作',
    CASE WHEN fk.update_referential_action = 1 THEN 'ON UPDATE CASCADE'
         WHEN fk.update_referential_action = 2 THEN 'ON UPDATE SET NULL'
         WHEN fk.update_referential_action = 3 THEN 'ON UPDATE SET DEFAULT'
         ELSE '' END AS '更新操作'
FROM
    sys.foreign_keys AS fk
INNER JOIN
    sys.objects AS obj ON obj.object_id = fk.object_id
INNER JOIN
    sys.tables AS tab1 ON tab1.object_id = fk.referenced_object_id
INNER JOIN
    sys.schemas AS sch1 ON tab1.schema_id = sch1.schema_id
INNER JOIN
    sys.tables AS tab2 ON tab2.object_id = fk.parent_object_id
INNER JOIN
    sys.schemas AS sch2 ON tab2.schema_id = sch2.schema_id
INNER JOIN
    sys.foreign_key_columns AS fkc ON fk.object_id = fkc.constraint_object_id
INNER JOIN
    sys.columns AS col1 ON col1.object_id = fkc.referenced_object_id AND col1.column_id = fkc.referenced_column_id
INNER JOIN
    sys.columns AS col2 ON col2.object_id = fkc.parent_object_id AND col2.column_id = fkc.parent_column_id
WHERE
    fk.delete_referential_action <> 0 OR fk.update_referential_action <> 0
ORDER BY
    '主表', '引用表';
```


方法二：生成可重用的SQL脚本
```sql
-- 生成所有外键约束的创建脚本（包含级联设置）
SELECT
    'ALTER TABLE ' + QUOTENAME(SCHEMA_NAME(fk.schema_id)) + '.' + QUOTENAME(OBJECT_NAME(fk.parent_object_id)) +
    ' ADD CONSTRAINT ' + QUOTENAME(fk.name) +
    ' FOREIGN KEY (' +
    STUFF((
        SELECT ', ' + QUOTENAME(c.name)
        FROM sys.foreign_key_columns AS fkc
        INNER JOIN sys.columns AS c ON fkc.parent_object_id = c.object_id AND fkc.parent_column_id = c.column_id
        WHERE fkc.constraint_object_id = fk.object_id
        FOR XML PATH('')), 1, 2, '') +
    ') REFERENCES ' + QUOTENAME(SCHEMA_NAME(ro.schema_id)) + '.' + QUOTENAME(ro.name) +
    ' (' +
    STUFF((
        SELECT ', ' + QUOTENAME(c.name)
        FROM sys.foreign_key_columns AS fkc
        INNER JOIN sys.columns AS c ON fkc.referenced_object_id = c.object_id AND fkc.referenced_column_id = c.column_id
        WHERE fkc.constraint_object_id = fk.object_id
        FOR XML PATH('')), 1, 2, '') + ')' +
    CASE WHEN fk.delete_referential_action = 1 THEN ' ON DELETE CASCADE'
         WHEN fk.delete_referential_action = 2 THEN ' ON DELETE SET NULL'
         WHEN fk.delete_referential_action = 3 THEN ' ON DELETE SET DEFAULT'
         ELSE '' END +
    CASE WHEN fk.update_referential_action = 1 THEN ' ON UPDATE CASCADE'
         WHEN fk.update_referential_action = 2 THEN ' ON UPDATE SET NULL'
         WHEN fk.update_referential_action = 3 THEN ' ON UPDATE SET DEFAULT'
         ELSE '' END + ';' AS '创建外键SQL'
FROM
    sys.foreign_keys AS fk
INNER JOIN
    sys.objects AS ro ON ro.object_id = fk.referenced_object_id
WHERE
    fk.delete_referential_action <> 0 OR fk.update_referential_action <> 0;
```

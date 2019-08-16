# Microsoft SQL Server 微软关系型数据库

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

## 参考学习链接:
* [解决SQL Server CPU占用率高](https://jingyan.baidu.com/article/39810a239f92f9b636fda6a8.html)


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

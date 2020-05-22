/*
如下解决了五个问题
1. 清空数据
2. 有外键也可以, 因为是逆向删除, 从最后一张表删除. 且使用的是delete, 因为truncate不能对有外键的表
3. 种子问题, 如果表存在种子重设为0, 如不存在就不操作
4. 加了事务, 中间报错, 有后悔机会
5. 截断日志功能, 因为使用delete, 删除后日志文件会增大, 可以不使用

https://blog.csdn.net/nuptsv_ice/article/details/17996151?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase

原文出处：http://topic.csdn.net/u/20090816/17/EE0FA21E-8616-4236-A9CB-8C5A3D45C9D9.html 中 45楼
*/

if( object_id('pr_DataClear') is not null )
        drop procedure pr_DataClear
    go
create procedure pr_DataClear
as
begin transaction
declare @cTblName varchar(128)
declare cur_Clear cursor for select rtrim(name)
from sysobjects
where type = 'U'
order by crdate desc
open cur_Clear
declare @cSQL varchar(255)
fetch next from cur_Clear into @cTblName
while( @@fetch_status = 0)
        begin
    set @cSQL = 'delete from ' + @cTblName
    print @cSQL
    exec( @cSQL )
    if( ident_seed(@cTblName) is not null )
            begin
        dbcc checkident( @cTblName, reseed, 0 )
        print '有种子且成功重置为1'
    end
    fetch next from cur_Clear into @cTblName
end
close cur_Clear
deallocate cur_Clear
commit
    go
-- 清空所有表数据
exec pr_DataClear




-- 截断日志
backup log LZ的数据库 with no_log
dbcc shrinkdatabase( LZ的数据库 )
dbcc updateusage( LZ的数据库 )
-- 查看表空间(概数)
select object_name(id) as 表名, (rtrim(8*reserved/1024) + 'MB') as 总量, (rtrim(8*dpages/1024) + 'MB') as 已使用,
    (rtrim(8*(reserved-dpages)/1024) + 'MB') as 未使用, (rtrim(8*dpages/1024-rows/1024*minlen/1024) + 'MB' ) as 空隙
from sysindexes
where indid=1
order by reserved desc

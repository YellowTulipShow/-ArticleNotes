# 常用命令

## dotnet -h

输出各命令详情文档

## 发布项目

```powershell
dotnet publish ./<项目目录>/<项目目标文件>.csproj -o ./_release/<项目发布目标目录> --runtime <发布目标运行时系统类型> --self-contained
```

```powershell
例如:
dotnet publish ./IOFileServer.WebApi/IOFileServer.WebApi.csproj -o ./_release/IOFileServer.WebApi --runtime win-x64 --self-contained
```

```powershell
Write-Host "<输出命令内容>"
```

**发布目标运行时系统类型**:
* win-x64
* linux-x64


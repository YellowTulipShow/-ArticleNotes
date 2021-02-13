# NuGet

## 发布包到NuGet

### 打包

```shell
dotnet pack // 打包
```

### 推送包到 NuGet.org

```
dotnet nuget push <PackagesPath> --api-key <ApiKey> --source https://api.nuget.org/v3/index.json
```

## 学习参考链接

* [NuGet 官网](https://www.nuget.org/)
* [快速入门：创建和发布包 (dotnet CLI)](https://docs.microsoft.com/zh-cn/nuget/quickstart/create-and-publish-a-package-using-the-dotnet-cli)

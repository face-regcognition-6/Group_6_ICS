# Group_6_ICS
## 信息与计算科学 代码 第一版

***这是一套脾气很大的代码……

## 项目大致内容

后端基于Django框架，前端为简单的HTML文件。

根据小学期老师的要求制作的一个***电商平台***的包含前后端的网站。

~~海南这边似乎对课题要求的解读不是很到位（）~~

## 环境要求

**1. Python软件包**

**【参考内容】

[Django升级3.27连接SqlServer数据库的方法 - 知乎](https://zhuanlan.zhihu.com/p/416452804)

Django建议为Django3.2或同代版本。

```cmd
pip install django==3.2
```

另外可能需要的软件包：

```cmd
pip install django-sqlserver django-pytds pyodbc django-pyodbc
pip install django-mssql-backend
```

**2. 驱动程序**

除此之外，还需要安装微软的用于SQL Server的ODBC驱动程序：

[Microsoft ODBC Driver for SQL Server - ODBC Driver for SQL Server | Microsoft Learn](https://learn.microsoft.com/zh-cn/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver16)

下载链接：

[下载 ODBC Driver for SQL Server - ODBC Driver for SQL Server | Microsoft Learn](https://learn.microsoft.com/zh-cn/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16#version-17)

***请注意***，请下载` Microsoft ODBC Driver 17 for SQL Server `的版本，而非版本18，否则会出现兼容性问题。

~~（要不是因为旧的数据库试用到期了才不会有这么多事呢……）~~

**3. 关于数据库**

这套代码的数据库基于阿里云的云数据库RDS，访问会受到IP地址的限制，如果访问报错或受到权限限制，请联系群中史钰瑄同学，将你的IP地址加入白名单。

## 开发人员

（有什么问题欢迎来问）

前端：史钰瑄
后端：刘玉宁

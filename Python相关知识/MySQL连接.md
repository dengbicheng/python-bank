# MySQL 的基础操作

## MySQL 的安装

在使用 PyMySQL 之前，我们需要确保 PyMySQL 已安装。

PyMySQL 下载地址：https://github.com/PyMySQL/PyMySQL。

如果还未安装，我们可以使用以下命令安装最新版的 PyMySQL：

    pip install PyMySQL

如果你的系统不支持 pip 命令，可以使用以下方式安装：

1、使用 git 命令下载安装包安装(你也可以手动下载)：

    git clone https://github.com/PyMySQL/PyMySQL
    cd PyMySQL/
    python3 setup.py install
2、如果需要制定版本号，可以使用 curl 命令来安装：

    # X.X 为 PyMySQL 的版本号
    curl -L https://github.com/PyMySQL/PyMySQL/tarball/pymysql-X.X  
    | tar xz
    cd PyMySQL*
    python3 setup.py install
    # 现在你可以删除 PyMySQL* 目录

## 连接 数据库

### 方法一： 

``` python
data = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'dengbicheng0810',
    'db':'用户信息',
    'charset':'utf8'
}
#连接数据库
db = pymysql.connect(**data)
print("连接成功")
```

### 方法二：

```python
host = 'localhost'  # 数据库地址
port = 3306  # 数据库端口
user = 'root'   # 数据库用户名
password = 'dengbicheng0810'    # 数据库密码
db = '用户信息'  # 数据库名称
charset = 'utf8'    # 编码方式
pymysql.connect(host=host,port=port,user=user,password=password,db=db,charset=charset) # 连接数据库
print("连接成功")
```

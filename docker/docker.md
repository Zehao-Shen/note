# docker

下载，看官网

```tex
docker官网：http://www.docker.com
Docker Hub官网: https://hub.docker.com/
```

镜像下载速度慢解决方案，

1. 可以使用阿里源，清华源

```py
https://cr.console.aliyun.com/cn-beijing/instances/mirrors?accounttraceid=243699c1936e48a5966a5c72d2847c75qvon
```

不要用别人的，用自己的。按照官网执行就行。

# docker组成

## 镜像(image)

Docker 镜像（Image）就是一个只读的模板。镜像可以用来创建 Docker 容器，一个镜像可以创建很多容器。
它也相当于是一个root文件系统。比如官方镜像 centos:7 就包含了完整的一套 centos:7 最小系统的 root 文件系统。
相当于容器的“源代码”，

在docker中，**image的意思是“镜像”，是一个文件系统**；image可以将几层目录挂载到一起，形成一个与linux目录结构一样的虚拟文件系统，docker通过这些文件再加上宿主机的内核提供了一个linux的虚拟环境。

docker镜像文件类似于python的类，而docker容器实例类似于pyhton中类的实例化。

## 容器(container)

1 从面向对象角度
Docker 利用容器（Container）独立运行的一个或一组应用，应用程序或服务运行在容器里面，容器就类似于一个虚拟化的运行环境，容器是用镜像创建的运行实例。就像是Java中的类和实例对象一样，镜像是静态的定义，容器是镜像运行时的实体。容器为镜像提供了一个标准的和隔离的运行环境，它可以被启动、开始、停止、删除。每个容器都是相互隔离的、保证安全的平台

2 从镜像容器角度
可以把容器看做是一个简易版的 Linux 环境（包括root用户权限、进程空间、用户空间和网络空间等）和运行在其中的应用程序。

docker镜像文件类似于python的类，而docker容器实例类似于pyhton中类的实例化。

## 仓库(repository)

仓库（Repository）是集中存放镜像文件的场所。

类似于
Maven仓库，存放各种jar包的地方；
github仓库，存放各种git项目的地方；
Docker公司提供的官方registry被称为Docker Hub，存放各种镜像模板的地方。

仓库分为公开仓库（Public）和私有仓库（Private）两种形式。
最大的公开仓库是 Docker Hub(https://hub.docker.com/)，
存放了数量庞大的镜像供用户下载。国内的公开仓库包括阿里云 、网易云等

# 常用命令

## 帮助命令

```bash
启动docker： systemctl start docker
停止docker： systemctl stop docker
重启docker： systemctl restart docker
查看docker状态： systemctl status docker
开机启动： systemctl enable docker
查看docker概要信息： docker info
查看docker总体帮助文档： docker --help
查看docker命令帮助文档： docker 具体命令 --help
```

## 镜像命令

#### 1.查看镜像的信息

1.查看所有的镜像和镜像信息

`docker images `

```
docker images -a :列出本地所有的镜像（含历史映像层）
docker images -q :只显示镜像ID。
docker images -qa  ：同时使用
```

镜像的信息

```
各个选项说明:
REPOSITORY：表示镜像的仓库源
TAG：镜像的标签版本号
IMAGE ID：镜像ID
CREATED：镜像创建时间
SIZE：镜像大小
同一仓库源可以有多个 TAG版本，代表这个仓库源的不同个版本，我们使用 REPOSITORY:TAG 来定义不同的镜像。
如果你不指定一个镜像的版本标签，例如你只使用 ubuntu，docker 将默认使用 ubuntu:latest 镜像
```

![image-20240125212030109](D:\笔记\docker\assets\image-20240125212030109.png)

#### 2.寻找镜像

`docker search`

去仓库https://hub.docker.com寻找我们需要的镜像

```ba
docker search [OPTIONS] 镜像名字
--limit : 只列出N个镜像，默认25个
docker search --limit 5 redis
```

#### 3.下载镜像

`docker pull` 

```ba
docker pull 镜像名字:版本
不写版本就是latest最新版
```

例子：

```
docker pull ubuntu
```

#### 4.查看所占的空间

docker system df 查看镜像/容器/数据卷所占的空间

![image-20240125212113841](D:\笔记\docker\assets\image-20240125212113841.png)

#### 5.删除镜像

`docker rmi`

删除单个

```
docker rmi -f 镜像ID
```

删除多个

```ba
docker rmi -f 镜像名1:TAG 镜像名2:TAG
```

删除全部

```ba
docker rmi -f $(docker images -qa)
```

## 容器命令

#### 1.启动命令

pull过的镜像，就优先启动，没有pull会下载镜像后在启动。

启动分两种

- 前台交互式启动     -it
- 后台守护式启动      -d

`docker run`

```
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

OPTIONS说明（常用）：有些是一个减号，有些是两个减号

--name="容器新名字" 为容器指定一个名称；
-d: 后台运行容器并返回容器ID，也即启动守护式容器(后台运行)；

-i：以交互模式运行容器，通常与 -t 同时使用；
-t：为容器重新分配一个伪输入终端，通常与 -i 同时使用；
也即启动交互式容器(前台有伪终端，等待交互)；

-P: 随机端口映射，大写P...
-p: 指定一个端口：小p
```

一般是和`-it`是连用的。

例子1：连用`-it`进入镜像命令行

```
sudo docker run -it 容器ID或者名字:版本 bash
sudo docker run -it redis:6.0.8 bash
# 启动redis，并进去到bash命令行，在命令行输入redis-cli -p 6379。就进入redis中了
或者
sudo docker run -it redis:6.0.8 
# 直接进入redis中
```

例子2：`-d`后台启动

```
sudo docker run -d 容器ID或者名字:版本
```

例子3：`-d加-p`后台启动nginx(小p)

```
sudo docker run -d -p 自定义端口:软件端口 容器ID
```

```
sudo docker run -d -p 8000:80 容器ID
```

访问127.0.0.1:8000，访问成功

相当于8000端口映射80端口，

`-d加-p`后台启动redis(小p)

```
sudo docker run -d -p 8000:6379 容器ID
```

##### 1.1后台启动后如何进入交互模式

**建议使用第一种方式**

两种方式

```py
第一种方式
sudo docker exec -it 容器ID /bin/bash
第二种方式
sudo docker attach 容器ID 
```

区别

```py
第一种方式
exec 是在容器中打开新的终端，并且可以启动新的进程
用exit退出，不会导致容器的停止。

第二种方式
attach 直接进入容器启动命令的终端，不会启动新的进程
用exit退出，会导致容器的停止。
```

#### 2.列出运行的容器

`docker ps`

列出当前所有正在运行的容器

```
docker ps [OPTIONS]

OPTIONS说明（常用）：

-a :列出当前所有正在运行的容器+历史上运行过的
-l :显示最近创建的容器。
-n：显示最近n个创建的容器。
-q :静默模式，只显示容器编号。
```

#### 3.退出容器

两种退出方式

- exit >>>>>>> >>>>run进去容器，exit退出，容器停止
- ctrl+p+q>>>>>>>>run进去容器，ctrl+p+q退出，容器不停止

#### 4.启动已停止运行的容器

`docker start`

```
docker start 容器ID或者容器名
```

#### 5.重启容器

`docker restart`

```
docker restart 容器ID或者容器名
```

#### 6.停止容器

`docker stop`

```
docker stop 容器ID或者容器名
```

#### 7.强制停止容器

`docker kill`

```
docker kill 容器ID或容器名
```

#### 8.删除已停止的容器

`docker rm`

```
docker rm 容器ID
```

一次性删除多个容器实例(两种方式)

```py
sudo docker rm -f $(docker ps -a -q)
sudo docker ps -a -q | xargs docker rm
```

#### 9.查看容器日志

```
docker logs 容器ID
```

#### 10.查看容器内运行的进程

```
docker top 容器ID
```

#### 11.查看容器内部细节

```
docker inspect 容器ID
```

#### 12.从容器内拷贝文件到主机上

容器→主机

```
docker cp 容器ID:容器内路径 目的主机路径
```

例子：

启动一个ubuntu系统，在这个ubuntu中的/opt文件下创建一个a.txt文件，将这个文件拷贝到宿主机中的/tmp文件夹中

```
sudo docker cp 容器ID:/opt/a.txt /tmp
```

执行成功返回

```py
Successfully copied 1.54kB to /tmp
```

#### 13.导入和导出容器

##### 导出

```
export 导出容器的内容留作为一个tar归档文件[对应import命令]
```

例子：将一个ubuntu系统导出到宿主机

```
docker export 容器ID > 文件名.tar
sudo docker export 容器ID > abcd.tar
```

我用户的ubuntu系统，直接拷贝到主文件夹。

##### 导入

import 从tar包中的内容创建一个新的文件系统再导入为镜像[对应export]

```
cat 文件名.tar | docker import - 镜像用户/镜像名:镜像版本号
```

例子：将导出的Ubuntu系统在次导入

```
sudo cat abcd.tar|sudo docker import - shen/ubutu1:22.04
镜像用户/镜像名:镜像版本号 这三个式随便写的，
```

#### 14.给镜像下载软件，并生成新的镜像

`docker commit`提交容器副本使之成为一个新的镜像

给ubuntu下载vim

- 进入镜像

```
sudo docker run -it 镜像ID  bash
```

- 执行命令

```
apt-get update
apt-get -y install vim
```

- 退出镜像，执行commit 命令

```bash
# docker commit -m="add vim cmd  ok " -a="shenzehao" 容器ID 要创建的目标镜像名:[版本号]
sudo docker commit -m="add vim cmd  ok " -a="shenzehao " 0ef6f2c1ccdc ubuntu2.0/ubuntu:2.0
```

- 运行`sudo docker images`查看，SIZE变高

![截图 2024-01-26 16-36-40](D:\笔记\docker\assets\截图 2024-01-26 16-36-40.png)

# 镜像上传阿里云仓库

仓库方分为共有仓库和私有仓库

上传共有仓库，我们选择阿里云

- 第一步：

首先先要在阿里云创建https://cr.console.aliyun.com/cn-beijing/instances，建立个人版实例

![屏幕截图 2024-01-27 205505](D:\笔记\docker\assets\屏幕截图 2024-01-27 205505.png)

- 第二步：创建命名空间

![屏幕截图 2024-01-27 205749](D:\笔记\docker\assets\屏幕截图 2024-01-27 205749.png)

- 第三步：按步骤来

![屏幕截图 2024-01-27 210019](D:\笔记\docker\assets\屏幕截图 2024-01-27 210019-17063606178474.png)

执行成功就将镜像上传到阿里云

![屏幕截图 2024-01-27 211218](D:\笔记\docker\assets\屏幕截图 2024-01-27 211218.png)

# 从阿里云pull镜像

按照阿里云中的代码就可以。

![屏幕截图 2024-01-27 211649](D:\笔记\docker\assets\屏幕截图 2024-01-27 211649.png)

# 数据卷

在执行容器券代码一定加上`--privileged=true`，要不然有些会报错的。

```
 Docker挂载主机目录访问如果出现cannot open directory .: Permission denied
解决办法：在挂载目录后多加一个--privileged=true参数即可
```

如果是CentOS7安全模块会比之前系统版本加强，不安全的会先禁止，所以目录挂载的情况被默认为不安全的行为，
在SELinux里面挂载目录被禁止掉了额，如果要开启，我们一般使用--privileged=true命令，扩大容器的权限解决挂载目录没有权限的问题，也即使用该参数，container内的root拥有真正的root权限，否则，container内的root只是外部的一个普通用户权限。

## 数据券是干什么的

将docker容器内的数据保存进宿主机的磁盘中

防止有人将容器删掉，导致容器内的数据全部被删除。(删库)

特点：
1：数据卷可在容器之间共享或重用数据
2：卷中的更改可以直接实时生效，爽
3：数据卷中的更改不会包含在镜像的更新中
4：数据卷的生命周期一直持续到没有容器使用它为止

## 命令

- docker修改，宿主机同步获得
-  宿主机修改，docker同步获得
-  docker容器stop，宿主机修改，docker容器重启看数据是否同步。

```
docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录 镜像名  镜像ID
```

宿主机绝对路径目录和容器内目录没有这目录会自动创建目录。

### 可读可写

默认就是rw(可读可写)，宿主机可以向容器内读写，容器内也可以向宿主机读写

例子：

```bash
sudo docker run -it --privileged=true -v /tmp/dockerdata:/tmp/data --name ub1 ba6acccedd29 bash
# 镜像名 --name 可以不写，会自动分配一个名字
# 版本号ba6acccedd29
# bash shell
```

![屏幕截图 2024-01-27 213100](D:\笔记\docker\assets\屏幕截图 2024-01-27 213100.png)

ubuntu系统写入docker需要sudo命令

### 只读

加一个ro就是read only

宿主机可读可写，容器只能读不能写

```bash
docker run -it --privileged=true -v /宿主机绝对路径目录:/容器内目录:ro 镜像名
```

例子：

```bash
sudo docker run -it --privileged=true -v /tmp/dockerdata:/tmp/data:ro --name ub1 ba6acccedd29 bash
# 镜像名 --name 可以不写，会自动分配一个名字
# 版本号ba6acccedd29
# bash shell
```

## 查看是否挂载成功

```
docker inspect 容器ID
```

## 继承

容器2继承容器1的卷规则

```
docker run -it --privileged=true --volumes-from 父类 --name u2 ubuntu
```

# Docker常规安装简介

### 总体步骤

- 搜索镜像
- 拉取镜像
- 查看镜像
- 启动镜像 ——服务端口映射
- 停止容器
- 移除容器

### 安装mysql

- 实战安装
    示例安装，就安装tmp下，如果要一直使用不要安装到tmp目录下，系统关机后，会将tmp清除。
- 


```bash
sudo docker run -d -p 8080:3306 --privileged=true -v /tmp/mysql/log:/var/log/mysql -v /tmp/mysql/data:/var/lib/mysql -v /tmp/mysql/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=123456  --name mysql mysql:5.7或者容器ID
```

命令解析

``` bash
docker run -d -p 8080:3306 --privileged=true 
-v /tmp/mysql/log:/var/log/mysql 
-v /tmp/mysql/data:/var/lib/mysql 
-v /tmp/mysql/conf:/etc/mysql/conf.d 
-e MYSQL_ROOT_PASSWORD=123456  
--name mysql mysql:5.7
# 端口映射 8080:3306
# -v数据券  将容器中mysql的配置，日志和库表，全部都和宿主机绑定，防止删除镜像后数据也被删除
# -e ,给MySQL设置密码
# --name 给镜像起名字
```

- 宿主机的`/tmp/mysql/conf`文件夹下创建文件`my.cnf`

`my.cnf`

```
[client]
default_character_set=utf8
[mysqld]
collation_server = utf8_general_ci
character_set_server = utf8
```

- 重启mysql

```bash
sudo docker restart 镜像ID
```

重启后进入mysql输入`SHOW VARIABLES LIKE 'character%';`查看编码

- 进入进入mysql中

```bash
sudo docker exec -it 镜像ID bash
```

```
mysql -u root -p123456
```

或者打开一个新的终端

输入

```
mysql -h 127.0.0.1 -P 8080 -u root -p 
```



- 建库，

```
create database 库名 charset utf8;
```

```
use 库名
```

- 建表，

````
create table t1(id int,name char(20));
````

- 插入数据。

```
insert  into t1(id,name) values(1,'沈泽昊1')
```

可以使用pycharm或者dbeaver都可以连接成功

- 容器实例删除，重新来一次，只要数据券中的内容还在那么数据就不会删除。

# Dockerfile

**Dockerfile中的D必须是大写。**

Dockerfile就是一个文本文件。里面写特定的docker语法。

Dockerfile是用来构建Docker镜像的文本文件，是由一条条构建镜像所需的指令和参数构成的脚本。

官网：https://docs.docker.com/engine/reference/builder/

#### 构建三步骤

- 编写Dockerfile文件
- docker build命令构建镜像
- docker run依镜像运行容器实例

#### Dockerfile内容基础知识

- 每条保留字指令都必须为大写字母且后面要跟随至少一个参数
- 指令按照从上到下，顺序执行
- #表示注释
- 每条指令都会创建一个新的镜像层并对镜像进行提交

```
docker build -t build后的镜像名字 Dockerfile文件所在的目录.（这个点一定要有）
```

例子：

![屏幕截图 2024-01-28 210943](D:\笔记\docker\assets\屏幕截图 2024-01-28 210943.png)

#### DockerFile常用保留字指令

常用的有FROM，CMD，COPY，RUN，WORKDIR

##### FROM

只有FROM这个Dockerfile也是可以运行的

这个镜像必须是我们pull好的镜像

```
基础镜像，当前新镜像是基于哪个镜像的，指定一个已经存在的镜像作为模板，第一条必须是from
```

##### MAINTAINER

```
镜像维护者的姓名和邮箱地址
```

##### RUN

容器构建时需要运行的命令

两种格式

```
shell格式和exec格式
我一般使用shell格式eg：yum -y install vim
```

##### EXPOSE

```
EXPOSE 80
类似命令 docker -p 8080:3306
```

##### WORKDIR

指定在创建容器后，终端默认登陆的进来工作目录，

没有这个目录也会自动创建目录

```
ENV MYPATH /usr/local
WORKDIR $MYPATH

上面两行代码，我们通过bash，进入，直接就到看/usr/local目录下
```

##### USER

一般不用

```
指定该镜像以什么样的用户去执行，如果都不指定，默认是root
```

##### ENV

就是定义变量。后面的代码可以使用需要加$

```
ENV MY_PATH /usr/mytest
ENV MYPATH=/usr/local   
# 这两个一样。
这个环境变量可以在后续的任何RUN指令中使用，这就如同在命令前面指定了环境变量前缀一样；
也可以在其它指令中直接使用这些环境变量，

ENV MY_PATH /usr/mytest
比如：WORKDIR $MY_PATH
```

##### ARG

和上面的ENV类似都是定义变量的作用。不过ENV定义完不能在修改了，ARG可以通过docker build命令来进行修改

`Dcokerfile`

```
FROM ubuntu
MAINTAINER shen<<31453154@126.com>
 
ENV MYPATH=/usr/local
WORKDIR $MYPATH
ARG B=12 
ENV c $B
RUN apt-get update
RUN apt-get -y install vim
#安装ifconfig命令查看网络IP
RUN apt-get -y install net-tools

EXPOSE 80

CMD echo $c
```

```bash
sudo docker  build -t ubuntu1.9 --build-arg B=123 .
# 给B传值
sudo docker run -it ubuntu1.9
# 输出 123
```

##### VOLUME

```
容器数据卷，用于数据保存和持久化工作
```

##### CMD

指定容器启动后的要干的事情

```
Dockerfile 中可以有多个 CMD 指令，但只有最后一个生效，CMD 会被 docker run 之后的参数替换
```

它和前面RUN命令的区别

```
CMD是在 docker run 时运行。
RUN是在 docker build时运行。
```

##### ENTRYPOINT

也是用来指定一个容器启动时要运行的命令

```
类似于 CMD 指令，但是ENTRYPOINT不会被docker run后面的命令覆盖，
而且这些命令行参数会被当作参数送给 ENTRYPOINT 指令指定的程序
```

优点

```
在执行docker run的时候可以指定 ENTRYPOINT 运行所需的参数。
```

注意

```
如果 Dockerfile 中如果存在多个 ENTRYPOINT 指令，仅最后一个生效。
```

ENTRYPOINT非json则以ENTRYPOINT为准，如果ENTRYPOINT和CMD都是JSON则ENTRYPOINT和CMD拼到shell。

##### ADD

```
将宿主机目录下的文件拷贝进镜像且会自动处理URL和自动解压tar压缩包
```

##### COPY

```
类似ADD，拷贝文件和目录到镜像中。
将从构建上下文目录中 <源路径> 的文件/目录复制到新的一层的镜像内的 <目标路径> 位置
```

```
COPY src dest
COPY ["src", "dest"]
上面这两种写法都可以。可以写shell或者json字符串。
<src源路径>：源文件或者源目录
<dest目标路径>：容器内的指定路径，该路径不用事先建好，路径不存在的话，会自动创建。
```

##### LABEL

标识作用，没有作用

##### ONBUILD

自己的build和run都不会运行，只有别人，以我们为父亲时才会输出。

# docker网络

## 网络命令

##### 查看网络

```bash
sudo docker network ls
```

输出：

![5e371627a257a0c1d0bfe649e07c5e3](D:\笔记\docker\assets\5e371627a257a0c1d0bfe649e07c5e3.png)

- bridge

桥接

##### 创建网络

```bash
# sudo docker network create -d briage  网络名字
sudo docker network create -d briage  briage1.2
```



##### 查看网络源数据

```
sudo docker network inspect XXX网络名字或者id
```

##### 删除网络

```
sudo docker network rm XXX网络名字或者id
```

## 网络案例

## bridge

docker默认有三种网络模式bridge，host，null

- 没有下载docker前的网络，终端输入ifconfig

输出结果

![47feb9301e7dfdc36f00005c34c3791](D:\笔记\docker\assets\47feb9301e7dfdc36f00005c34c3791.png)

lo测试接口，ens33以太网接口，IP地址(ens33可能名字不一样)

- 下载docker后，在命令行输入。

多个docker0

![e1e255a4c205fad4d5b56f4b5284b7e](D:\笔记\docker\assets\e1e255a4c205fad4d5b56f4b5284b7e.png)

多了一个docker0，这个其实相当于网关。用于容器的镜像和容器外的设备进行传输。这个docker是一个私有地址，外部网络不能直接访问这个地址。

运行命令

```
sudo docker network inspect bridge
```

输出

```
[
   {
       "Name": "bridge",
        "Id": "cf11d33ddadf077064795ce4f5d7be3fe76ad292dec06b3087595b57f34227a4",
        "Created": "2024-01-30T21:46:44.606909795+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
```

看上面的输出Containers是空

- 运行一个镜像

![image-20240130222728358](D:\笔记\docker\assets\image-20240130222728358.png)

运行ubuntu镜像

```bash
sudo docker run -it  ba6acccedd29 bash
sudo docker ps
```

![image-20240130223853230](D:\笔记\docker\assets\image-20240130223853230.png)

查看宿主的网络ifconfig

![image-20240130223028643](D:\笔记\docker\assets\image-20240130223028643.png)

多了一个网络，

运行命令

```bash
sudo docker network inspect bridge
```

输出：

```
[
   {    "Name": "bridge",
        "Id": "cf11d33ddadf077064795ce4f5d7be3fe76ad292dec06b3087595b57f34227a4",
        "Created": "2024-01-30T21:46:44.606909795+08:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "807d813c1df2fe0eb6896baa742768c2930a99e0a4e3125a79924d8bfec4daad": {
                "Name": "pedantic_lederberg",
                "EndpointID": "646f7681b2585b5db8b7a5556263b147bdf9252ef4a59150a5164ef9c2199159",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
```

Containers多了内容。并且Name就是运行ubuntu镜像的名字pedantic_lederberg

进入ubuntu镜像中输入ifconfig，

发现也有一个网络

![image-20240130225244253](D:\笔记\docker\assets\image-20240130225244253.png)

其实是下面这个图

容器内可以通过docker0向容器外发送网络请求。

![无标题-2024-01-29-0936](D:\笔记\docker\assets\无标题-2024-01-29-0936.png)



![屏幕截图 2024-01-30 215726](D:\笔记\docker\assets\屏幕截图 2024-01-30 215726.png)



端口：命令中的  -p

## 自定义网络

使用命令

```bash
sudo docker network create -d briage  briage1.2
```

输入ifconfig

![屏幕截图 2024-01-31 090727](D:\笔记\docker\assets\屏幕截图 2024-01-31 090727.png)

多出了一个网络，这个就是我们新建的网络，这个新网络的桥，

自定义的briage网络可以自动NDS，默认bridge访问其他容器ping 镜像ID，但是自定义ping 名字就可以，

## host网络

运行一个镜像



```bash
sudo docker run -d -p 8080:80 --name nginx2.1 --network host 605c77e624dd

#因为指定了端口，所有这个会报错，但是不影响镜像启动。
WARNING: Published ports are discarded when using host network mode
```

docker 会使用nginx本身的端口。我们不需要指定映射端口。

## null网络

就是没有网，运行起来的镜像没有网

```bash
sudo docker run -d  --name nginx2.1 --network none 605c77e624dd
# 命令是none  这个网络的名字是null，但是我们的命令是none。
```

## 网络对比

![无标题-2024-01-31-0915](D:\笔记\docker\assets\无标题-2024-01-31-0915.png)

# docker-compose

dokcerfile是一个下载容器的脚步，docker-compose是启动容器的脚步

- docker-compose 是一个容器编排工具（自动化部署、管理）;
- 它用来在单台 Linux 服务器上运行多个 Docker 容器;
- docker-compose 使用YAML文件来配置所有需要运行的 Docker 容器，该 YAML 文件的默认名称为 docker-compose.yml

## 下载

去看官网

## 命令

```bash
Compose常用命令
docker-compose -h # 查看帮助
docker-compose up # 启动所有docker-compose服务
docker-compose up -d # 启动所有docker-compose服务并后台运行
docker-compose down # 停止并删除容器、网络、卷、镜像。
docker-compose exec yml里面的服务id # 进入容器实例内部 docker-compose exec docker-compose.yml文件中写的服务id /bin/bash
docker-compose ps # 展示当前docker-compose编排过的运行的所有容器
docker-compose top # 展示当前docker-compose编排过的容器进程
```

## 使用 docker-compose 启动一个容器

```bash
version: '2.1'
services:
  nginx:
    image: nginx:latest
    container_name: nginx_test
    ports:
      - 8080:80
    volumes:
      - /opt/nginx:/opt/nginx/html
```

上面内容的解析

```
参数：

compose 文件格式的版本，恒定为 2.1

services 标签下可以定义多个类似 nginx 这样的服务

container_name 服务定义， nginx_test 是容器的名称

image nginx容器所使用的镜像

ports 定义端口映射，本例将容器内的 80 端口映射到宿主机的 8080 端口

volumes 定义目录映射，本例将容器内的 /opt/nginx/html 目录映射到宿主机的 /opt/nginx 目录
```

不写网络默认是bridge，容器新建一个bridge网络。

使用命令`sudo docker network ls`是4个网络

## docker-compose 创建多个容器

```
version: '2.1'
services:

  nginx:
    image: nginx:latest
    container_name: nginx_host1
    ports:
      - 8081:80
    volumes:
      - /opt/nginx:/opt/nginx/html
    networks:
      - host1-network

  redis:
    image: redis:latest
    container_name: redis_host1
    ports:
      - 63790:6379
    networks:
      - host1-network

networks:
  host1-network:
    driver: bridge
```

上面内容的解析

```
参数：

networks 定义容器网络，host1-network 为定义的网络名称，

config 网络配置，subnet 代表网段，gateway 代表网关。
```






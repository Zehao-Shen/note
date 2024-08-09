# Linux

# 如何远程连接

![image-20220303093545859](D:\笔记\Linux\assets\image-20220303093545859.png)

### windows连接方法

```
 ssh root@192.168.0.241    
 @ ssh命令 root 用户名，@ ip，端口是22就不用写，不是就空格写端口
 
eg：
	[D:\~]$ ssh root@192.168.96.130


    Connecting to 192.168.96.130:22...
    Connection established.
    To escape to local shell, press 'Ctrl+Alt+]'.


    Last login: Fri Aug 11 09:47:30 2023 from 192.168.96.1
    [root@bogon ~]#   
```

### Linux连接方法

```
ssh   -p 22 root@192.168.0.132
# ssh命令，-小p 端口  用户名 ip
```

会问你yes/no，输入yes

输入用户名密码

用户名改变，那就是成功了

![image-20230811100221199](D:\笔记\Linux\assets\image-20230811100221199.png)

### 修改主机名字

```
set-hostname 主机名字
```

```
# root用户修改主机名称
[root@server ~]#hostnamectl set-hostname shenzehao
# 主机名修改完成，重新登陆系统使其生效
[root@server ~]#logout
Connection to 10.0.0.4 closed.
[autox@r9000x wangr]$ssh root@10.0.0.4
root@10.0.0.4's password:
# 重新登录，主机名修改成功
Last login: Thu Mar 3 20:55:02 2022
[root@shenzehao ~]#hostname
shenzehao
```

# linux区别

## 1.严格区分大小写

输入的时候 不必须区分大小写

## 2.linux的命令返回结果理解

有的命令会返回，有的不返回，

## 3.关于后缀名（linux不关心文件后缀）

虽然linux不关心后缀名，但是还是要写，因为写多了后，自己都看不懂。

```
通过命令   ls -l
```

### 3.1需要记忆的后缀

为了区分出文件类型，我们还是会给linux文件，添加上阅读性更好的文件扩展名字。

常见的有

- 压缩文件（打包，压缩）
    - Linux 下常见的压缩文件名有 *.gz、*.bz2、*.zip、*.tar.gz、*.tar.bz2、*.tgz 等。
    - 为什么压缩包一定要写扩展名呢？很简单，如果不写清楚扩展名，那么管理员不容易判断压缩包的格式，虽然有命令可以帮助判断，但是直观一点更加方便。
    - 就算没写扩展名，在 Linux 中一样可以解压缩，不影响使用。
- 软件安装包
    - 如windows下的exe文件一样作用，linux也需要安装软件，也有软件包的格式。后面学习软件管理时重点讲解。
    - 如redhat系列的RPM包，所有的RPM包都是.rpm后缀格式。

## 4.linux一切皆文件

你在linux系统上，所有的 操作，都会以文件形式可以找到

网络的配置		

软件的配置				

程序的脚本	

进程的信息

都可以用命令，找到和它有关的文件

## 5.绝对路径和相对路径

![image-20220303113522665](D:\笔记\Linux\assets\image-20220303113522665.png)

windows和linux和斜杠不同

- linux命令+ 以根开始的路径，叫做绝对路径
- linux 命令 +  非根目录开始的路径，叫做相对路径

```
关于相对路径，需要添加 

.   当前路径
..  上一级路径
```



## 6.环境变量PATH

添加到环境变量中，我们输入的命令都会去环境变量中。

可通命令`echo ${PATH}`

```
eg:

[root@bogon /]#  echo ${PATH}
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
```

`which 命令`,可以查看命令在哪里储存。 

```shell
eg:
    [root@bogon /]# which ls
    alias ls='ls --color=auto'
        /usr/bin/ls
得到这个路径后，可通过路径写命令
eg：
	[root@bogon /]# /usr/bin/ls /opt
    好饿.tet  好饿.txt
    [root@bogon /]# ls /opt
    好饿.tet  好饿.txt
# 这两个是一样的。输入ls后，ls会在path中以冒号为分隔符，一个一个的查询。如果将/usr/bin/删除，ls就不能用了。
```

**修改环境变量**





## 7linux的重要文件

![1691806341397](D:\笔记\Linux\assets\1691806341397.png)

![1691806371140](D:\笔记\Linux\assets\1691806371140.jpg)

![1691806394675](D:\笔记\Linux\assets\1691806394675.png)

**/usr/local/ 该目录,安装各种软件，往这里装就行了！**

装好软件后，软件的可执行命令会在

```
/usr/local/xxxxxx软件名称/sbin/xxxxx
```

## 隐藏文件

Linux下的隐藏文件都是以 . 开头，Linux系统默认不显示隐藏文件，需要使用`ls -a `参数查看隐藏文件。

```shell
[root@server ~]#ls -la
total 32
dr-xr-x---. 4 root root 179 Mar 4 17:14 .
dr-xr-xr-x. 19 root root 247 Mar 4 15:20 ..
-rw-------. 1 root root 517 Mar 4 17:49 .bash_history
-rw-r--r--. 1 root root 18 Dec 29 2013 .bash_logout
-rw-r--r--. 1 root root 176 Dec 29 2013 .bash_profile
-rw-r--r--. 1 root root 176 Dec 29 2013 .bashrc
-rw-r--r--. 1 root root 100 Dec 29 2013 .cshrc
drwxr-----. 3 root root 19 Mar 4 14:02 .pki
```

## linux的单引号、双引号区别是

```
Linux的单引号之中的 特殊符号 * ? \ & $ 没有任何含义;
而双引号之中的 特殊符号 * ? \ & $ 可以还原其特殊含义。
```

# 下载

有两种办法

1. 现在下载到windows中，使用传输工具，传给linux。
2. 直接下载到linux

第一种方法：

```
 xftp工具

和xshell是一个系列的软件

xshell是专门用于ssh登录服务器的终端软件

xftp 专门用于win和linux之间传输大量文件的，且支持短点续传。使用文件传输工具，将该文件，发给linux
方法1，你的linux安装lrzsz工具，即可实现windows和xshell，直接拖拽文件

[root@shenzehao ~]#  yum install lrzsz -y 

安装该工具后，会自动生成
rz  （接收）
sz   (send 发送)
两个命令 


3.获取win下载的那个文件

linux 接收，来自于win的文件

输入rz命令，会出现一个Windows框，就可以了

扩充，也可以直接win，拖拽到xshell里，即可传输


xftp工具

和xshell是一个系列的软件

xshell是专门用于ssh登录服务器的终端软件

xftp 专门用于win和linux之间传输大量文件的，且支持短点续传。
短点续传 就是可以暂停。
```

2.直接在linux中下载

```
1.获取该软件的，下载链接即可
https://tengine.taobao.org/download/tengine-2.3.3.tar.gz

2.到linux中，使用命令下载wget即可获取一个链接的资源。
还得安装该命令
yum install wget -y

直接使用wget + 资源url(资源链接地址)即可。

直接下载到tengine-2.3.3.tar.gz文件到当前目录
wget https://tengine.taobao.org/download/tengine-2.3.3.tar.gz

加-o，可以指定下载到哪里
wget -o 指定下载到哪里  资源的下载链接
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo

```



# shell命令语法

# 查询命令

**man**

查看这个命令如何使用，

```bash
shenzehao@shenzehao:~$ man find
# 输出的就是这个命令如何使用。
# 通过 / 查询主要内容
# q 退出
```



- 1、命令：要执行的操作（必选）
- 2、选项：如何具体执行操作，通常以 -, --, +开头（可选）
- 3、参数：具体操作的对象（可选）

# 简单命令

通配符只是用来找文件的

```
* 通配符
注释符
/ 根目录
~ 家目录
. 当前目录
- 上一次工作目录
>和>> 重定向
| 管道符
```

**pwd**

查看所在的目录

**ls**

查看以在；路径下的所有文件，也可以写成  `ls  -l`   ,`ls  -lh`，`ls -a` ，这两个是显示文件的详细内容的。

```shell
[root@bogon /]# ls /home -l
总用量 0
drwx------. 2 shen shen 83 8月  11 05:24 shen
[root@bogon /]# ls -lh /opt
总用量 4.0K
-rw-r--r--. 1 root root  0 8月  11 16:51 好饿.tet
-rw-r--r--. 1 root root 20 8月  11 17:00 好饿.txt

#  d开头大部分是文件夹,r开头大都是文件。
```

选项

```
-l # 列出当前目录可见文件详细信息
-h # 以可读大小显示文件大小
-a # 列出所有文件（包括隐藏）的详细信息
-d # 将目录名像其它文件一样列出，而不是列出它们的内容
-i # 输出文件前先输出文件系列号（即 i 节点号: i-node number）
-r # 逆序排列
-t # 按时间信息排序(最近修改的文件显示在最上面)
-m # 水平列出文件，每行尽可能多，相互用逗号和一个空格分隔
-n # 打印文件的UID和GID
-F # 按照特殊字符对文件进行分类
-R # 递归列出全部目录的内容
```

**cd**

```shell
	cd 切换工作目录
	cd  文件路径
eg:
	cd  /xxxx
	cd ./xxxx
	cd ..   #返回上一级
	cd ../../opt  # 回到上一级的上一级，在进入opt文问价夹。
	[root@bogon home]# cd ../../opt
	[root@bogon opt]# 

```

选项

```
$ cd # 进入用户家目录
$ cd / # 进入根目录
$ cd ~ # 进入 用户家目录
$ cd .. # 返回上级目录（若当前
```



**touch**

```shell
	1.作用
		touch  文件名   ，创建普通文件，touch 我是叙利亚的运维.txt
	2.作用2
		如果当前目录，存在该文件，则表示修改该文件的访问时间属性
		
eg：
	[root@bogon home]# touch /opt/好饿.tet 
```

**mkdir**

```
当前目录，判断是否存在同名问价夹，没有就创建，重复就报错，
可以创建多个文件夹，
也可以，递归的创建多个文件夹。mkdir -p

eg :
    [root@bogon ~]# mkdir ./0224/学生/沈 -p   # 不加——p会报错。
    [root@bogon ~]# cd ./0224/学生
    [root@bogon 学生]# ls
    沈
```

**cat**

查看文件的内容

```
eg:
    [root@bogon opt]# cat 好饿.txt

    我就好评了，

```

**echo**

```
-n 不输出尾部换行符
-e 启用反斜杠转义的解释
```



向文件中写数据将原数据覆盖，或者追加数据

```
写数据
eg:
    [root@bogon opt]# echo "整的吗?"  >好饿.txt
    [root@bogon opt]# cat 好饿.txt
    整的吗?
    
    
追加数据
eg： 
	[root@bogon opt]# echo "整的吗?阿"  >> 好饿.txt
	[root@bogon opt]# cat 好饿.txt
	整的吗?
	整的吗?阿 
	
# 显示数据
$ echo “$PATH”
```

**whoami**

```
# 拿到当前的用户名
[root@bogon ~]# whoami
root
```

**id**

```
# 查看系统中的用户信息，和验证该用户是否存在 
[root@bogon ~]# id
uid=0(root) gid=0(root) 组=0(root) 环境=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
```

**history**

```
查看历史敲过的命令
清空历史数据   history -c
显示最后的5条数据   history 5
```

**stat**

```
查看文件的详细信息
stat  文件名

eg： 	
	[root@bogon home]# stat shen
  文件："shen"
  大小：83        	块：0          IO 块：4096   目录
    设备：fd00h/64768d	Inode：4194688     硬链接：2
    权限：(0700/drwx------)  Uid：( 1000/    shen)   Gid：( 1000/    shen)
    环境：unconfined_u:object_r:user_home_dir_t:s0
    最近访问：2023-08-11 05:34:01.827013410 +0800
    最近更改：2023-08-11 05:24:32.381000623 +0800
    最近改动：2023-08-11 05:24:32.381000623 +0800
    创建时间：-
```

**uname**

```
显示系统信息
[root@bogon home]# uname
Linux
[root@bogon home]# uname -a
Linux bogon 3.10.0-1160.el7.x86_64 #1 SMP Mon Oct 19 16:18:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

**查看主机名**

```
hostname
eg :
	[root@shenzehao ~]# hostname
	shenzehao
```

**su**

切换用户

```shell
# 第一种方式
[root@server ~]#su jack
[jack@server root]$
# 第二种方式（包括环境变量）
[root@server ~]#su - jack
Last login: Fri Mar 4 18:07:50 CST 2022 on pts/0
[jack@server ~]$
```

两个用户来回切换

```
#  root切换到yuchao01
[root@server ~]#su - yuchao01
[yuchao01@server ~]$
# yuchao01切换到root
[yuchao01@server ~]$su - root
Password:
Last login: Fri Mar 4 18:08:40 CST 2022 on pts/0
[root@server ~]#
```

**who**

```
判断当前登录了几个用户
[root@shenzehao ~]# who
root     tty1         2023-08-12 05:43
root     pts/1        2023-08-12 07:25 (192.168.96.1)
root     pts/2        2023-08-12 09:32 (192.168.96.1)
```

**hostnamectl**

查看主机配置

```shell
[root@shenzehao ~]# hostnamectl
   Static hostname: shenzehao
         Icon name: computer-vm
           Chassis: vm
        Machine ID: 1ff2c357e25940df9073c0a8aba69e77
           Boot ID: c36fede4274b4cb39a00384b6445c04a
    Virtualization: vmware
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-1160.el7.x86_64
      Architecture: x86-64

```

**tree**

用命令安装apt-get install yum 

```
4.使用tree查看目录结构，且显示中文，且显示该文件的类型
tree -NF      # -N 是显示中文 -F 显示文件类型
tree -L  n     #  n是我们输入一个数字，看第一个层级。    
```

**wc**

```
作用：单词的统计,一般统计步数，单词数，字节数

-l 表示lines      行数（以回车行，换行数，为标准）

-w 表示words      单词数按照空格来判断单词的数量

-c 表示bytes      字节数（空格，回车，换行）
```

**rename**

```shell
#修改文件的后缀比较好用 
rename  源字符串  新字符串   文件对象
```

**atat**

查看文件属性的信息

```shell
 stat  /文件或文件夹
[root@shenzehao home]# stat /时间
  文件："/时间"
  大小：6         	块：0          IO 块：4096   目录
设备：fd00h/64768d	Inode：4195072     硬链接：2
权限：(0755/drwxr-xr-x)  Uid：(    0/    root)   Gid：(    0/    root)
环境：unconfined_u:object_r:default_t:s0
最近访问：2023-08-14 22:38:52.277014775 +0800
最近更改：2023-08-12 16:05:23.218046801 +0800
最近改动：2023-08-12 16:05:23.218046801 +0800     
创建时间：-
```

文件属性变化`最近改动`的时间就会修改

文件内容被人读`最近访问`的时间就会修改。

文件内容被人修改`最近更改和最近改动`的时间就会修改。

# 通配符

```
1.通配符的作用是查找和匹配文件名称而不是文件里的内容！
2.通配符是shell的内置功能
3.Linux大部分命令都支持通配符
```

## 常⻅通配符

|   符号   |                             作⽤                             |
| :------: | :----------------------------------------------------------: |
|    *     |                匹配任意，0或多个字符，字符串                 |
|    ?     |              匹配任意1个字符，有且只有⼀个字符               |
| 符号集合 |                      匹配⼀堆字符或⽂本                      |
|  [abcd]  |     匹配abcd中任意⼀个字符，abcd也可以是不连续任意 字符      |
|  [a-z]   | 匹配a到z之间任意⼀个字符，要求连续字符，也可以 连续数字，匹配[1-9] |
| [!abcd]  |    不匹配括号中任意⼀个字符，也可以书写[!a-d]，同于 写法     |
| [^abcd]  |                      同上，！可以换成 ^                      |

## 特殊通配符



```
&lt;		标准输入
&gt;       标准正确重定向
&gt;&gt;      标准正确追加重定向
2&gt;      标准错误重定向
2&gt;&gt;     标准错误追加重定
```

```
&&     前面执行成功后面才执行
||     前面执行失败后面才执行
;      不管前面是否执行成功，都执行后面的命令
\      转义特殊字符，还原字符本来的含义
$()    优先执行小括号里的命令，并且结果可以被其他命令使用  
``     同$()效果一样，但是容易和单双引号搞混
$?     上一条命令执行的结果
|      管道
{}     生成序列
```

|    符号     |       作⽤       |
| :---------: | :--------------: |
| [[:upper:]] |   所有⼤写字⺟   |
| [[:lower:]] |   所有⼩写字⺟   |
| [[:alpha:]] |     所有字⺟     |
| [[:digit:]] |     所有数字     |
| [[:alnum:]] | 所有的字⺟和数字 |
| [[:space:]] |  所有的空⽩字符  |
| [[:punct:]] |   所有标点符号   |

[[:upper:]] 和[a-z] 效果是一样的。

## 特殊引号

在linux系统中，单引号、双引号可以⽤于表示字符串

|    名 称    |                             解释                             |
| :---------: | :----------------------------------------------------------: |
| 单 引 号 '' |          所⻅即所得，强引⽤，单引号中内容会原样输出          |
| 双 引 号 "" | 弱引⽤，能够识别各种特殊符号、变量、转义符等，解析后 再输出结果 |
| 没 有 引 号 | ⼀般连续字符串、数字、路径可以省略双引号，遇⻅特殊字 符，空格、变量等，必须加上双引号 |
| 反 引 号 `` |               常⽤于引⽤命令结果，同于$(命令)                |

## 输出重定向特殊符号

⽽每打开⼀个⽂件，就有⼀个代表该打开⽂件的⽂件描述符。 程序启动时默认打开三个I/O设备⽂件：

-  标准输⼊⽂件stdin，⽂件描述符0 
- 标准输出⽂件stdout，⽂件描述符1 
- 标准错误输出⽂件stderr，⽂件描述符2

|          符号           |       特殊符号       |                 简介                  |
| :---------------------: | :------------------: | :-----------------------------------: |
|      标准输⼊stdin      | 代码为0，配 合< 或<< |            数据流从右向左             |
|     标准输出stdout      |  代码1，配合> 或>>   |             数据从左向右              |
|     标准错误stderr      |  代码2，配合> 或>>   |             数据从左向右              |
|       重定向符号        |                      |           数据流是箭头⽅向            |
|     标准输⼊重定向      |       0< 或 <        |      数据⼀般从⽂件流向处理命 令      |
|     追加输⼊重定向      |       0<<或<<        |      数据⼀般从⽂件流向处理命 令      |
|     标准输出重定向      |        1>或>         |    正常输出重定向给⽂件，默 认覆盖    |
|   标准输出追加重 定向   |       1>>或>>        |    内容追加重定向到⽂件底 部，追加    |
|   标准错误输出重 定向   |          2>          | 讲标准错误内容重定向到⽂ 件，默认覆盖 |
| 标准错误输出追 加重定向 |         2>>          |      标准错误内容追加到⽂件底 部      |

eg:

```shell
[root@shenzehao home]# ls yy 2 >coun.txt
# 没有yy这个文件夹，会报错，2的意思将错误输出写入到coun.txt中。
# 1 就是将正确的输出写入文件中。
```

其他特殊符号

| 符号 |                            解释                            |
| :--: | :--------------------------------------------------------: |
|  ;   |                 分号，命令分隔符或是结束符                 |
|  \#  |            1.⽂件中注释的内容 2.root身份提示符             |
|  \|  |              管道符，传递命令结果给下⼀个命令              |
|  $   |         1.$变量，取出变量的值 2.普通⽤户身份提示符         |
|  \   |           转义符，将特殊含义的字符还原成普通字符           |
|  {}  |       1.⽣成序列 2.引⽤变量作为变量与普通字符的分割        |
|  &   |                         后台进程符                         |
|  &&  | 逻辑与符号，命令1 && 命令2 ，当命令1执⾏成 功继续执⾏命令2 |

### $符

Linux系统命令⾏中，字符串前加$符，代表字符串变量的值

```
[root@shenzehao home]# echo PATH
PATH
[root@shenzehao home]# echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
```



## 特殊重定向，合并重定向

- 2>&1 把标准错误，重定向到标准输出

把命令的执⾏结果写⼊⽂件，标准错误当做标准输出处理，也写⼊⽂件

```shell
[root@shenzehao home]# ls > ./coun.txt  2>&1
#在home文件下，执行ls命令，把正确的输入或者错误的输入都写入coun.txt
```



# 文件管理

## 文件的名字

文件夹和文件除了/外，都可以用，但是尽量不要使用特殊字符，如果一个文件夹中的包含了特殊字符，那么在访问这和个问价夹时就需要用引号将文件名括起来。

Linux严格区分大小写，所以，尽量都用小写。

如果必须对文件名进行分割，建议使用"_"。

文件的扩展名，文件的后缀不代表任何特殊含义。

文件名最长255个字符

## 文件时间

首次创建时间     touch和mkidr创建文件时系统给的时间。

访问时间            这个文件通过，cat ，vim，vi等命令访问过

修改时间    		这个文件通过vim，vi，echo等命令修改过

## 文件管理命令

#### file

```bash
查看文件类型
eg：file 文件名
```



#### 新建

```
touch 创建文件
mkdir 创建文件夹
vi ,vim 也可以创建文件

# echo本身是打印的，需要>才可以创建文件，并将数据写到文件中。
echo 结合 重定向符号(>)  才能创建文件      
 # 	echo "男儿当自强"  > /opt/man.txt 
```

##### mkdir

```
1.用法一：mkdir 不加参数，路径（需要包含目录名称）
eg：
	[root@shenzehao home]# mkdir nihao
    [root@shenzehao home]# ls
    nihao  
2.用法二：递归创建写法
eg：
	# 在这个目录下/opt/0224/linux/，创建shenzehao文件夹，因为linux这个文件夹没有，所有需要加-p
	mkdir -p /opt/0224/linux/shenzehao
	
3.同时创建多个文件夹，且注意绝对，相对路径,下面命令中top路径没有，所以需要加-p
[root@fjh001 ~]# mkdir  -p  ./王者  /opt/lol/top/瑞雯    /dnf  ../cs 
```

什么时候用 `-p`

```
在写路径中有一段没有，就加-p
```

##### touch

```
1. 当文件不存在，执行touch 是创建该文本文件

touch  hello.txt


2. 当文件，文件夹（名字）已经存在后，touch命令是修改它的时间戳

touch /opt/


3.touch一次性创建多个文件，注意，要保证，路径中的文件夹是存在的，否则报错

4.在某个目录，创建多个 同级的文件
	学习shell的花括号用法 ，一次性在同级目录，创建多个文件
	[root@shenzehao ~]# touch /opt/王者/坦克/{老夫子,廉颇,吕布,妲己}
	# 在opt目录下，创建100个log文件
	[root@shenzehao ~]# touch /opt/{1..100}/.log
```

![image-20220307105304799](D:\笔记\Linux\assets\image-20220307105304799.png)

#### 删除

##### rmdir

`删除空目录`

```
rmdir  文件夹的路径
	eg:
	[root@shenzehao ~]# rmdir /home/王者
	[root@shenzehao ~]# cd /home
	# 文件夹必须是空的
```

##### rm

remove   删除的简写rm

权限最大化

root + rm（参数）

```
rm 命令和其他一样

rm (remove移除)

语法是
rm   可选参数  可选对象



-r ：递归删除，主要用于删除目录，可删除指定目录及包含的所有内容，包括所有子目录和文件

-f ：强制删除，不提示任何信息。操作前一定要慎重！！！不小心你就删库跑路（放心，跑不掉的）

-i  ：删除前需要确认


eg:
	1.rm命令不带参数，只删除1个文件
    [root@shenzehao ~]# rm /opt/2.log
    rm：是否删除普通空文件 "/opt/2.log"？y     # 输入y就可以删掉

eg：
	2. rm命令删除多个文件
    [root@shenzehao ~]# rm /opt/1.log  /opt/3.log
    rm：是否删除普通空文件 "/opt/1.log"？y
    rm：是否删除普通空文件 "/opt/3.log"？y

eg：3.强制删除   -f
	[root@shenzehao ~]# rm -f /opt/4.log
eg：4.删除文件夹，文件夹里还有文件夹，将父文件夹直接删除，需要-r参数使用，递归删除
	[root@shenzehao ~]# rm  -r /opt/时间
    rm：是否进入目录"/opt/时间"? y
    rm：是否进入目录"/opt/时间/ok"? y
    rm：是否删除目录 "/opt/时间/ok/pp"？y
    rm：是否删除目录 "/opt/时间/ok"？y
    rm：是否删除目录 "/opt/时间"？y
eg:递归就加强行删除
	rm -rf /文件  
	这个命令很危险。
	危险命令，注意rm命令后面，到底跟着的路径是什么，错一个字符，就删错了，没有回头路
	确保虚拟机快照备份完毕
```

#### 自定义命令的名字

**alias**

直接敲alias，可以看到我们所有的自定义命令。

```
[root@shenzehao opt]# alias
alias cp='cp -i'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l.='ls -d .* --color=auto'
alias ll='ls -l --color=auto'
alias ls='ls --color=auto'
alias mv='mv -i'
alias rm='rm -i'
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde'
```

修改命令

```
敲rm命令是默认是rm -i，我们可以不让它提示
eg：
	[root@shenzehao ~]# alias rm="rm"
    [root@shenzehao ~]# cd /opt
    [root@shenzehao opt]# ls 
    10.log  5.log  6.log  7.log  8.log  9.log  a.txt  b.txt  c.txt  好的  好饿.tet  好饿.txt  时时间  王者荣焉  		王者荣耀
    [root@shenzehao opt]# rm 10.log
    [root@shenzehao opt]# alias rm="rm -i"
    [root@shenzehao opt]# rm 5.log
    rm：是否删除普通空文件 "5.log"？y
```

自定义命令

```shell
[root@shenzehao opt]# alias ll="ls /opt"     # 自定义命令。
[root@shenzehao opt]# ll
6.log  7.log  8.log  9.log  a.txt  b.txt  c.txt  好的  好饿.tet  好饿.txt  时时间  王者荣焉  王者荣耀
```

#### 更改

```
修改文件内容的命令很多

vim 
```

#### 查看

```
cat 读取文件内容
```

#### 复制

```
copy 拷贝，缩写的命令，就是 cp

cp   -选项   复制文件   目标文件
```

```shell
eg：1复制文件并且改名。
	[root@shenzehao ~]# cp /opt/好饿.txt  /home/不饿了.txt     
    [root@shenzehao ~]# ls /home
    nihao  shen  不饿了.txt  王者容颜
    # 这样就不改名。
    # [root@shenzehao ~]# cp /opt/好饿.txt  /home/
eg：2复制一个文件夹，并且将文件夹中的所有数据都复制    加 -r 
	[root@shenzehao ~]# ls /home/王者容颜/坦克
    项羽  张飞
    [root@shenzehao ~]# cp /home/王者容颜   /opt
    cp: 略过目录"/home/王者容颜"
    [root@shenzehao ~]# cp -r  /home/王者容颜   /opt
    [root@shenzehao ~]# ls /opt
    6.log  7.log  8.log  9.log  a.txt  b.txt  c.txt  好的  好饿.tet  好饿.txt  时时间  王者容颜  王者荣焉  王者荣耀
    [root@shenzehao ~]# ls /opt/王者容颜/坦克
    项羽  张飞

```

#### 移动，剪切，重命名

move 缩写

出现同名文件夹后，会移动到同名文件夹的里面。

```shell
移动
    [root@shenzehao ~]# mv /opt/7.log  /home
    [root@shenzehao ~]# ls /home
    7.log  a.txt  nihao  shen  不饿了.txt  王者容颜

	
剪切
	[root@shenzehao ~]# ls /opt
    a.txt  b.txt  c.txt  哈哈.log  好的  好饿.tet  好饿.txt  时时间  王者荣誉
    [root@shenzehao ~]#  mv /opt/a.txt /home 
    mv：是否覆盖"/home/a.txt"？ y
    [root@shenzehao ~]# ls /opt
    b.txt  c.txt  哈哈.log  好的  好饿.tet  好饿.txt  时时间  王者荣誉
    [root@shenzehao ~]# ls /home
    7.log  a.txt  nihao  shen  不饿了.txt  哈哈.log  王者容颜


重命名     
	# 1.就是在当前目录下，不变，但是改名
	[root@shenzehao ~]# mv /opt/8.log  /opt/哈哈.log
    [root@shenzehao ~]# ls /home
    7.log  a.txt  nihao  shen  不饿了.txt  哈哈.log  王者容颜
	# 2.移动文件目录，且重命名
	[root@shenzehao ]# mv  /努力学习怎么放大招的亚索.txt  /opt/垃圾压缩.txt
# 修改后缀名  rename
[root@linux0224 ~]#rename mp4 html /网易云音乐/华语/女歌
手/王菲/*.mp4
```

#### 打包压缩，解压缩

##### tar

作用：将多个文件打包到一个文件,也可以拆包，，压缩，解压缩

```
-c，create 创建的意思 ，打包

-v，显示打包文件过程

-f，指定打包的文件名，此参数是必须加的，且必须在最后一位

-u，update缩写，更新原打包文件中的文件（了解）

-t，查看打包的文件内容（了解）  （不解压，看看里面有什么）

-x  解包，解压缩  （将一个单个的压缩文件，解压其中内容）

-z  压缩操作，是tar命令，去调用gzip压缩命令的过程，压缩的参数

提示：

tar命令打包的文件，通常称为tar包，如 yuchao-all.tar文件
```

##### 压缩文件名的规范

```
*.tar   仅仅是打包了

*.tar.gz  打包+压缩

*.tgz    打包+压缩
```

```shell
eg:
	# 1.打包多个文件 ，打包就是将多个文件放到一个文件夹下
    #tar -cvf all_robts.tar  y1  y2  y3  y4
    #tar  参数   打包后的文件名  要打包的内容 
    
	[root@shenzehao 王者荣耀]# ls
    y1  y2  y3  y4                        # 三个文件
    [root@shenzehao 王者荣耀]# tar -cvf all_robts.tar  y1  y2  y3  y4
    y1/
    y2/
    y3/
    y4/
    [root@shenzehao 王者荣耀]# ls
    all_robts.tar  y1  y2  y3  y4
    # 2.查看打包文件
    [root@shenzehao 王者荣耀]# tar -tf all_ll.tar 
    y1
    y2
    y3
    y4
    # 3.追加进去，往压缩包中再放一个文件。
    [root@shenzehao 王者荣誉]# tar -uf all_ff.tar y5
    [root@shenzehao 王者荣誉]# ls
    all_ff.tar  all_ll.tar  y1  y2  y3  y4  y5
    [root@shenzehao 王者荣誉]# tar -uf all_ll.tar y5
    [root@shenzehao 王者荣誉]# ls
    all_ff.tar  all_ll.tar  y1  y2  y3  y4  y5
    [root@shenzehao 王者荣誉]# tar -tf all_ll.tar 
    y1
    y2
    y3
    y4
    y5
```

##### tar压缩

```bash
tar czvf  xxxxxx.tar.gz  xxxxx
tar czvf 压缩包的名字  需要压缩的名字
```



```shell
eg:
# tar -czvf all_ll.tar.gz  ./*
# tar 选项   压缩后的文件夹名   需要压缩的文件
# 1 压缩文件
[root@shenzehao 王者荣誉]# tar -zcvf all_ll.tar.gz  ./*
    ./all_ff.tar
    ./all_ll.tar
    ./y1
    ./y2
    ./y3
    ./y4
    ./y5
    
eg:
# 2 查看压缩包里有什么文件
[root@shenzehao 王者荣誉]# tar -tvf all_ll.tar.gz  
    -rw-r--r-- root/root     81920 2023-08-13 09:42 ./all_ff.tar
    -rw-r--r-- root/root    768000 2023-08-13 09:42 ./all_ll.tar
    -rw-r--r-- root/root     81920 2023-08-13 09:52 ./all_ll.tar.gz
    -rw-r--r-- root/root    168894 2023-08-13 09:36 ./y1
    -rw-r--r-- root/root    168894 2023-08-13 09:36 ./y2
    -rw-r--r-- root/root    168894 2023-08-13 09:36 ./y3
    -rw-r--r-- root/root    168894 2023-08-13 09:36 ./y4
    -rw-r--r-- root/root     78904 2023-08-13 09:41 ./y5
    
3.除了-z的压缩参数，还有哪些   windows下的 .zip  .rar  .7z 
 
 # 遇到什么文件，用什么选项。
-z，压缩为.gz格式 ，记住用这个就好了，主流的80%人都用这个
	你拿到一个 all_files.tar.gz ，这个如何解压？
	tar  -zxvf  all_files.tar.gz

-j，压缩为.bz2格式   
	all_files.tar.bz2   ，如何解压？
    tar -xjvf all_files.tar.bz2 
	
	

-J，压缩为.xz格式
	

-c，create 创建的意思

-x，解压缩

-v，显示打包文件过程

-f，file指定打包的文件名，此参数是必须加的。

-u，update缩写，更新原打包文件中的文件（了解）

-t，查看打包的文件内容（了解）
```

##### tar解压

```bash
tar xzvf  xxxx.tar.gz  xxxxxx
tar xzvf 压缩包名字   解压后的名字
```

**很危险：加压后可能会覆盖我们的文件**

总结：

```

  1）解压缩的时候文件如果已存在会覆盖并且没有任何提示
  2）解压缩的时候，如果目录已经存在，会合并并没有任何提示
  3）这样会有风险，因为可能会把别人机器上的文件覆盖到自己的机器
  4）如果压缩的文件是绝对路径比如/etc，不用担心，tar会自动帮我们去掉/，但是会有报错提示
  5）如果不想要报错提示，那么进入到要压缩的文件回目录上级，然后使用相对路径打包压缩
    cd / && tar zcvf /opt/etc.tar.gz etc
  6）只查看压缩包内容不解压用tf
  7）打包压缩软链接时如果想保留软链接指向的真实目录，使用zcvhf，但是如果想保留目录原来的结构不需要h
  ``8）指定要解压到哪个目录使用-C
```



##### zip压缩

这个最多的就是解压windows传过来的文件。

需要下载`yum install zip -y`

 zip压缩会自动给压缩包加.zip后缀

zip压缩目录，需要添加-r参数

```shell
eg: 
	# 1 压缩 	
	[root@shenzehao 王者荣誉]# zip all y1 y2 y3 y4
      adding: y1 (deflated 85%)
      adding: y2 (deflated 85%)
      adding: y3 (deflated 85%)
      adding: y4 (deflated 85%)
    [root@shenzehao 王者荣誉]# ls
    all.zip  y1  y2  y3  y4  y5	

# -r 处理指定目录和指定目录下的使用子目录
    [root@shenzehao opt]# zip -r all  王者荣誉/y1
      adding: 王者荣誉/y1 (deflated 85%)
```

##### unzip解压缩

需要下载`yum install zip -y`

```py
unzip xxx.zip
unzip xxx.zip -d 目标目录
unzip 解压文件
```



```shell
eg:
	# 1解压文件到那个文件夹下
    [root@shenzehao opt]# unzip ./all.zip -d /home
    Archive:  ./all.zip
    inflating: /home/王者荣誉/y1   
```

### vim

1.所有你可见到的linux机器，都会默认有vi编辑器，但是它不好用，就好比windows的记事本。

2.你可以选择更强大的编辑器 ，叫vim，需要额外安装

```
yum install vim -y
```

vim的使用流程

![image-20220307153213889](D:\笔记\Linux\assets\image-20220307153213889.png)

打开文件时出现了

![image-20230814101217943](D:\笔记\Linux\assets\image-20230814101217943.png)

原因是1.多人编辑同一个文件。2.编辑好后，没有正常保存退出

解决办法：

​				不要这个文件了，直接删除
​				还要的话，

### vim的使用流程

基本上 vim 共分为三种模式，分别是：

- 命令模式（Command mode）
    - 最长用的，按下字母,a,i,o（a 在光标前开始编辑，i是在光标处，开始编辑，o是在光标下一行开始编辑）
    - 当你使用vim 标记某个文件时，第一步就进入了命令模式。
    - *你此时可以按下键盘的几个快捷键，进入不同的指令模式。*
    - 可以移动光标位置，输入快捷键指令，对文件进行编辑，如插入字符，复制，粘贴，删除等操作
- 输入模式（Insert mode）
    - 可以对文件内容进行编辑。
    - 退出编辑模式（按下esc键，回到了命令模式）
- 末行模式（Last line mode）底线模式
    - 从命令模式下 ，输入冒号，即进入了底线命令模式。
    - 进行一些特殊操作，如文本信息的查找，替换，保存，退出等；

还有一种特殊的`可视化模式`（多行操作模式），用于批量的列选操作。



![image-20220308102922965](D:\笔记\Linux\assets\image-20220308102922965.png)

### vim的使用

#### 命令模式

**复制粘贴**

```
复制粘贴

指令：yy

作用：复制光标所在行

指令：p或大P

作用：小p是在光标的后面粘贴，大p相反
```

**撤销**

```
撤销

指令   u，

作用：按下即可撤销上一步作用
```

**恢复**

```
恢复

指令    ctul + r       恢复vim撤销的内容
```

**剪切**

```
剪切

指令   dd

数字+dd    剪切几行。

粘贴p或大p
```

删除

```shell
x   和windows的删除有写差异。但是都是删除。
```

多行删除

```
删除当前光标的所有位置，以及文档末尾的，所有内容
dG
```

#### 底线模式

:  冒号进入底线模式

写入数据

```
指令   ：w     保存写入
      :w  路径      保存到哪里文件
```

退出quit

```
指令  ： q  退出，不保存内容
	  ：!q  强制退出
	  ::wq  保存写入
	  : !x   强制写入，且退出
	  :!wq  强制写入，且退出
```

搜索，查找

```
输入/+你想要的搜索的数据
:/沈    找到后会出现高亮
取消高亮   : noh
```

语法提示

```
:syntax  on       开语法提示
:syntax  off      关闭语法提示
```

替换

单行替换

```
指令  :s/原内容/新内容/
```

多行替换

```
:s%/原内容/新内容/
只将第一个替换掉，将全文中的都加高亮。
```

全局替换

```
:s%/原内容/新内容/g
所有的替换掉，
```

显示行号

 ```
 :set nu
 ```

paste粘贴模式

例子：将一个py文件，而一个py文件是有缩进的，我们直接粘贴会乱，这时就需要进入粘贴模式

```shell
第一部:进入粘贴模式:set paste
第二部:粘贴你的代码
第三步:保存退出
```

### cat

```shell
1.cat 适合读取小文件，不能读取大文件，一次性将文件内容全部读取到内存中，且输出到屏幕上

查看nginx软件的配置文件（前提是你安装了该软件，linux默认安装的软件，配置文件会自动写到/etc目录下）
[root@shenzehao ~]# cat /etc/nginx/nginx.conf
# 2 显示行数
[root@shenzehao ~]# cat -n  /etc/passwd

# 3. cat不适合读取大文件，显示也不友好

# 4. 还可以连续读取多个文件，并且显示三文件一共有多少行
[root@shenzehao home]# cat vim vim_aa _aa
# 5.结合重定向符号使用
>   重定向覆盖输出符  ，数据从左边，覆盖写入到右边 
<   重定向覆盖输入符，数据从右边，覆盖写入到左边
>>  重定向追加输出符， ，数据从左边，追加写入到右边 
<<  重定向覆盖输入符，数据从右边，追加写入到左边
# 将多个文件写入到一个文件
[root@shenzehao home]# cat  vim vim_aa > _aa
[root@shenzehao home]# cat _aa

# cat和重定向结合使用
[root@shenzehao home]# cat  >> a.txt  << EOF
[root@shenzehao home]# cat  > a.txt  << EOF
# 命令会进入一个交互模式 写完后写EOF
# 8. cat证明文件存在空行的办法
-b  只会对有内容的行，显示其行号，空行不显示,空行不输出
-E  在linux文件中，每一行的结束，默认会添加一个你看不到的，特殊符号 '$'  ，表示是该行的结尾
```

### tac

将文件从后，向前，倒着查看，倒叙的输出出来

```shell
cat   xxxx
输出：1
	 2
     3
tac   xxxx
输出：  3
 	   2
 	   1
```

### more和less

more和cat都是一次性读取所有内容到内存，不适合读取大文件，占资源

less命令是显示多少文本，消耗多少内存，省资源。

```
空格，翻篇

回车 下一行
```

### head和tail命令

```shell
head 脑袋   显示前10行
查看文件的默认前10行
[root@shenzehao home]# head vim_aa

# head -5  文件   # 查看文件的前5行
[root@shenzehao home]# head  -5  vim_aa

tail 命令    显示后10行
查看文件的后默认10行
[root@shenzehao home]# tail vim_aa

显示后5行
[root@shenzehao home]# tail -5 vim_aa
```

**tail  -f有一个重点命令，叫做实时刷新文件内容**

```
-f  跟踪文件内容变化，但是需要文件正常退出后，可见，最常用的也就是小写的f，检测程序的日志变化（程序代码，追加新内容到文件中的）
当一个文件用了-f后，这个文件会被监控，当有人写入数据时，这个文件会更新，实时刷新文件内容
```

```
eg:
	1.用tail 检测nginx的访问日志
    [root@localhost opt]# tail -f  /var/log/nginx/access.log 

    2.用浏览器，访问nginx的页面即可，不断刷新，不断出现新的日志
```

**tail -F** 

```shell
文件不存在也可以检测,能够对文件进行刷新读取，，也可以检测

[root@shenzehao home]# tail -F  user.txt
    tail: 无法打开"user.txt" 读取数据: 没有那个文件或目录   # 没有文件也可以。会等待
    tail: "user.txt" 已被建立，正在跟随新文件的末尾
		用户沈泽昊访问
```

### wc

统计文件的行，下面这三个都可以

- vim（set nu）
- cat -n
- wc -l 

```shell
# 1.统计文件有多少行
	[root@shenzehao home]# wc -l user.txt
	4 user.txt
# 2. wc -w 统计文件内的单词数
	[root@shenzehao home]# wc -w user.txt
	4 user.txt
	因为-w是通过空格的数判断的
	[root@shenzehao home]# cat user.txt
    用户沈泽昊访问
    用户沈泽昊访问
    用户沈泽昊访问
    用户沈泽昊访问
# 有四个空格，所以是四
```

### du

统计文件大小的命令

- ls -lh

```shell
du命令
作用：查看文件或目录(会递归显示子目录)占用磁盘空间大小

语法：du [参数选项] 文件名或目录名

常见参数：

-s ：summaries，只显示汇总的大小，统计文件夹的大小
-h：表示以高可读性的形式进行显示，如果不写-h，默认以KB的形式显示文件大小

linux的文件系统，对文件最小管理单位是4kb算起。

    [root@shenzehao home]# du -sh user.txt
    4.0K	user.txt

# 显示文件夹的大小
[root@shenzehao ~]# du -h /home
0	/home/华语/乐队组合
0	/home/华语/女歌手
0	/home/华语/男歌手/陈奕迅
0	/home/华语/男歌手
0	/home/华语
0	/home/Eason
0	/home/vim_ll
2.9M	/home

```

### find

找文件

windows有Everything，在Linux中的find。

```
find  路径   -name   文件名
```

```
eg：
	[root@shenzehao ~]# find / -name aa.txt
	/home/aa.txt
	[root@shenzehao ~]# find /var -name 'log'
	/var/log
```

模糊搜索

```
eg:
	
	[root@shenzehao ~]# find /var -name '*log'
	....很多
	 
```

-type  f   找到文本类型的数据 

-type  d    找到文件夹类型的数据

-name   按名称查找
-type   按类型查找 f 文件  d 目录
-size   按文件大小+- k M G
-mtime  按时间查找 -N N +N

```
#可能存在文件和文件夹是同一个名字的。
find /    -type f     -name   'doupo.txt' 
```

-ok

这个也是删除，但是这个有提示

```shell
find -name '*.txt' -ok rm {} \;# 花括号代表的是find -name '*.txt'找到的文件，这个命令结尾必须加;

eg：
    [root@shenzehao home]# find / -name '*.txt' -ok rm {} \;
    < rm ... /etc/pki/nssdb/pkcs11.txt > ? y
    < rm ... /var/tmp/yum-shen-x8lJoJ/x86_64/7/base/mirrorlist.txt > ? y
    < rm ... /var/tmp/yum-shen-x8lJoJ/x86_64/7/timedhosts.txt > ? y
    < rm ... /var/tmp/yum-shen-x8lJoJ/x86_64/7/extras/mirrorlist.txt > ? ^C

```

-exec

删除

这个删除不友好。

```shell
find -name '*.txt' -exec rm {};  # 花括号代表的是find -name '*.txt'找到的文件，这个命令结尾必须加;
```

find可以以通过时间找。

find还可以找文件中的内容。

```bash
# 查询当前目录下的文件中的内容。
find  . -name c.txt | xargs grep "需要找的内容"
```

### xargs

xargs 一般是和管道一起使用

是一个强有力的命令，它能够捕获一个命令的输出，然后传递给另外一个命令。

```bash
find  . -name c.txt | xargs grep "需要找的内容"
```

将|前的命令结果，传递给后面的命令，

find  . -name c.txt 这个的结果是个字符串，我们要将字符串转换成文件名，传给后面的命令。

### grep

功能

```tex
1.grep命令是Linux系统中最重要的命令之一，其功能是从文本或管道数据流中筛选匹配的行及数据。
2.如果配合正则表达式技术一起使用，则功能会更加强大。
3.grep过滤就相当于一个筛子，有可能筛子里面的东西是要保留的，也有可能筛出来的需要保留。
```

在文件中搜索关键字，无法查文件夹

```shell
创建一个文本
[root@shenzehao home]# vim vim_txt
[root@shenzehao home]# cat -n vim_txt
     1	 teach linux.
     2	
     3	I like python.
     4	
     5	My qq is 877348180.
     6	
     7	My name is chaoge.
     8	
     9	Our school website is http://yuchaoit.cn。
    10	
    11	Where is my girl friend.
    12	
    13	Who is your boy friend.
    14	My phone number is 15233334444.
```

查文件中的M

```
[root@shenzehao home]# grep M vim_txt
My qq is 877348180.
My name is chaoge.
My phone number is 15233334444.
```

主要的几个参数

```py
-v 选中不匹配的行
-n 输出的同时打印行号
-i 对于模式和数据，忽略大小写
-E <模式> 是扩展正则表达式
-w 	仅匹配整个单词
-A n 找到这个语句后，在找前n句。
-B n 找到这个语句后，在找后n句。
-c n 找到这个语句后，在找这个语句的前后n句。
```

`-n`- 参数，显示存在该关键字的行号

```
[root@shenzehao home]# grep -n M vim_txt
5:My qq is 877348180.
7:My name is chaoge.
14:My phone number is 15233334444.
```

linux是区分大小的，`-i`可以忽略大小写

```shell
#  既忽略大小写，也显示行数
[root@shenzehao home]# grep -in M vim_txt
5:My qq is 877348180.
7:My name is chaoge.
11:Where is my girl friend.
14:My phone number is 15233334444
```

可以多个文件查找

```shell
[root@shenzehao home]# grep -in  my vim_txt vim_txt1 vim_txt2
vim_txt:5:My qq is 877348180.
vim_txt:7:My name is chaoge.
vim_txt:11:Where is my girl friend.
vim_txt:14:My phone number is 15233334444.
vim_txt1:5:     5	My qq is 877348180.
vim_txt1:7:     7	My name is chaoge.
vim_txt1:11:    11	Where is my girl friend.
vim_txt1:14:    14	My phone number is 15233334444.
vim_txt2:5:     5	My qq is 877348180.
vim_txt2:7:     7	My name is chaoge.
vim_txt2:11:    11	Where is my girl friend.
vim_txt2:14:    14	My phone number is 15233334444.
```





### 管道符

管道符，和grep结合的是最多的

管道是一种通信机制，通常用于进程间的通信。

它表现出来的形式将==前面每一个进程的输出（stdout）直接作为下一个进程的输入（stdin）==。

```shell
命令1  | 命令2 
# 如何判断是否有shen用户
命令1，拿到用户文件信息   |  交给grep再去过滤
[root@shenzehao home]#  cat /etc/passwd |  grep 'shen'    # car命令，拿到/etc/passwd的文本后，交给shen去查找。
shen:x:1000:1000:shen:/home/shen:/bin/bash
```

### xargs

作用是，简单的说 就是把其他命令的给它的数据，传递给它后面的命令作为参数

通过find找到一些文件，在找这些文件中的是否有我们要的关键字apple。

```
find -name 'txt' |  grep 'apple'
# 这样是不行的，grep是去文件中的内容中，而管道符中是一堆的文件，不是文件中的内容，需要用到；类似python中的for循环一样。
# cat 找到的文件|grep ‘apple’  
# 所以需要用到xargs
```

 ```shell
 找到文件或文件夹 |xargs -i {}   # 花括号代表管道符前的文件或文件夹
 xargs -i 是必须写的，后面可以写其他命令
 eg：
 	找到文件或文件夹 |xargs -i rename log txt {}  # 修改找到文件的后缀	
 ```

eg：找到所有的txt文件，并找到这些文件是否有apple，这个关键字

```shell
find / -name  '*txt' | xargs -i grep 'apple' {}  # 花括号代表的find / -name  '*txt' 的结果，之后grep去所有文件的内容找apple。
```

# 用户管理

不同的用户可以同时登录一个linux服务器，每一个用户的权限不同，可访问，可操作的的计算机资源不同。

权限是通过

- 登陆的用户
- 文件和用户之间的关系。

linux是一个多任务，多用户的服务器。

在单位里运维作为服务器的管理员，root权限是有的

而开发，测试，他们是不可能有root权限的

即使需要使用root权限，运维会给他配置（临时使用管理员身份运行）----sudo

root对普通账号的管理

- 修改他的密码
- 禁止他登录
- 禁止他一个月登录

## 用户的分类

- root
- 普通用户
- 计算机创建的普通用户

如何判断，根据用户的ID，和UID来确定的。

分组，将不同的权限的人分一组。可以一人一组。方便管理

## 关于root

- root为什么是root呢？为什么权限最大呢，因为他的UID是0，系统根据用户的id号，决定它的作用
- linux中的每一个用户，都有一个自己的组

## linux的用户组

- 为了方便管理属于同一组的用户，Linux 系统中还引入了用户组的概念。
    - 通过使用用 户组号码(GID，Group IDentification)，我们可以把多个用户加入到同一个组中，从而方 便为组中的用户统一规划权限或指定任务。
- 对于linux而言，比如公司的开发部门，需要访问服务器上一个文件夹的资料，并且允许读取、允许修改写入，开发部门有30个人，你要给每一个人都添加读写权限吗？
- 那必然是给开发部门设置的权限就是，允许读写该文件夹，然后属于该部门的人员，就自然有了组内的权限，后续开发部门招新人，只要加入组内，权限也有了。
- Linux管理员在创建用户时，将自动创建一个与其同名的用户组，这个用户组只有该用户一个人，
    - `useradd yuchao01`

## root的权利

- Linux系统的特性就是可以满足多个用户，同时工作，因此Linux系统必须具备很好的安全性。
- 在安装RHEL7时设置的root管理员密码，这个root管理员就是所有UNIX系统中的超级用户，它拥有最高的系统所有权，能够管理系统的各项功能，如添加/删除用户，启动/关闭进程，开启/禁用硬件设备等等。
- 因此“能力越大，责任越大”，root权限必须很好的掌握，否则一个错误的命令可能会摧毁整个系统。

## root为什么权利这么大？

root只是个名字而已，权利很大的原因，在于他的UID是0。

- UID，user Identify，好比身份证号
- GID，group Identify，好比户口本的家庭编号
- 在Linux系统中，用户也有自己的UID身份账号且唯一
- 在Linux中UID为0，就是超级用户，如要设置管理员用户，可以改UID为0（不推荐该操作）
    - 建议普通用户用sudo提权。
- 系统用户UID为1~999 Linux安装的服务程序都会`创建独有的用户`负责运行。
- 普通用户UID从1000开始：由管理员创建（centos7），最大值1000~60000范围
- centos6创建普通用户的UID是从500开始

查看所有的用户

```shell
[root@shenzehao home]# cat /etc/passwd -n
     1	root:x:0:0:root:/root:/bin/bash
     2	bin:x:1:1:bin:/bin:/sbin/nologin
     3	daemon:x:2:2:daemon:/sbin:/sbin/nologin
     4	adm:x:3:4:adm:/var/adm:/sbin/nologin
     5	lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
     6	sync:x:5:0:sync:/sbin:/bin/sync
     7	shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
     8	halt:x:7:0:halt:/sbin:/sbin/halt
     9	mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
    10	operator:x:11:0:operator:/root:/sbin/nologin
    11	games:x:12:100:games:/usr/games:/sbin/nologin
    12	ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
    13	nobody:x:99:99:Nobody:/:/sbin/nologin
    14	systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
    15	dbus:x:81:81:System message bus:/:/sbin/nologin
    16	polkitd:x:999:998:User for polkitd:/:/sbin/nologin
    17	sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
    18	postfix:x:89:89::/var/spool/postfix:/sbin/nologin
    19	shen:x:1000:1000:shen:/home/shen:/bin/bash
    20	nginx:x:998:996:Nginx web server:/var/lib/nginx:/sbin/nologin
#         root:x:0:0:root:/root:/bin/bash
# 分别是   用户名 密码 UID GID 用户注释   用户家目录   用户使用的解释器  
```

## 和用户创建相关的配置文件

useradd命令

```
/etc/passwd 用户信息
/etc/shadow  用户密码信息
/etc/group 用户组信息
/etc/gshadow 用户组密码信息  ，在大公司，用户和组数量很大的情况下，需要制定复杂的权限管理，那时会用到组密码

当你执行useradd的时候，系统自动创建 /home/chengzhiwei01 这个家目录下会一些用户默认模板文件
是从下面这个文件夹，拷贝过去的


/etc/skel
skel是skeleton的缩写，意为骨骼、框架。故此目录的作用是在建立新用户时，用于初始化用户根目录。系统会将此目录下的所有文件、目录都复制到新建用户的根目录，并且将用户属主与用户组调整为与此根目录相同。
```

命令列表

|   命令   |          作用          |
| :------: | :--------------------: |
| useradd  |        创建用户        |
| usermod  |      修改用户信息      |
| userdel  |    删除用户配置文件    |
|  passwd  |      更改用户密码      |
| chpasswd |    批量更新用户密码    |
|  chage   |    修改用户密码属性    |
|    id    | 查看用户UID、GID组信息 |
|    su    |        切换用户        |
|   sudo   |   用root身份执行命令   |
|  visudo  |  编辑sudoers配置文件   |

## 命令

### groupadd

添加组

```shell
[root@shenzehao ~]# groupadd -g 1000 xionfid
groupadd：GID “1000”已经存在
[root@shenzehao ~]# groupadd -g 1010 xionfid
[root@shenzehao ~]# cat /etc/group
可以查看
# 

-g  可以设置组id
# 默认从1000开始创建
```

### groupdel

删除组

```shell
# groupdel 组名 
[root@shenzehao ~]# groupdel xionfid
[root@shenzehao ~]#
```

### groupmod

改组

```shell
# groupmod  -n 修改后叫的名字   UID号   现在的名字
[root@shenzehao ~]# groupmod -n xd -g 2000 ll  
-g 修改组id
-n 修改组名
```

### useradd

添加用户

```shell
useradd xxx

id 选项  xxx
-u  查看用户的UID
-g  设置主组     
-G  设置附加组
-c  设置用户注释
-s  设置用户登录的shell解释器

# 创建用户后会创建一个主组和一个用户，还可以将这个用户放到别的组，那么这个别的组就是附加组。
```

### passwd

```
给创建的用户设置密码
passwd   用户
```

### id

查看用户

```
id xxx
```

### usermod

修改用户信息，只能修改未登录的用户信息。就是以前的开发组的，现在成运维组的了

修改用户各种属性

```shell
usermod  选项  用户名
# 修改用户的UID
eg：
    [root@shenzehao ~]# usermod  -u 2320 shen
    [root@shenzehao ~]# id shen
    uid=2320(shen) gid=1000(shen) 组=1000(shen)

-L   上锁，给用户上锁。
```

所有的用户密码都在 /etc/shadow中，只有root用户可以看。

### userdel

建议注释文件的用户信息行。

```shell
userdel   用户名    # 仅删除用户，保留期间目录。
```

### whoami

```
打印当前的用户名
```

### who

```
显示登录的用户

tty          是虚拟终端的代码
pts/序号      ssh远程终端的代码
```

### w

```
显示系统登陆的用户信息，以及负载信息
```

### last

```
显示近期登录的终端有哪些

eg：
	last -5    # 显示最新的5天登录记录
```

### lastlog

```
显示关于用户的登录记录
```

### Linux用户身份却换

#### su

切换用户

```
su   用户名
```

#### sudo

用户身份提取，

1. root密码不能给人，
2. 普通用户想要拿到root权限，就要使用sudo，给用户特权，提升root的身份，再去执行命令
3. 编辑sudo的配置文件，添加你的用户信息 ，

#### visudo

需要编辑sudo配置文件，     `/etc/sudoers` ，可以直接用vim去编辑这个文件

linux提供visudo命令，    默认用vi去打开该文件，且提供语法检测功能。

修改 `/etc/sudoers`文件的92行。

```shell
# root    ALL=(ALL)       ALL
照个它的这个写
shen     ALL=(ALL)       ALL
```

#### chgrp

```shell
chgrp devopt /tmp/cao01    			# 修改组，将cao01修改到devopt组下。
```

## 权限

每一个用户的权限不同，可访问，可操作的的计算机资源不同。

不同的用户，以及不同的组，对于linux的文件操作，权限高地，权限不同。

读取 cat，more，tail

写入  echo 追加 ，vim编辑，cat重定向

修改，修改文件属性，mv改名字，修改文件权限

执行， 文件中写的是可执行的语句，如bash语句，python的脚本文件

​		执行一般指的是，文件中写的是编程语言的语句的一个特殊文件

​		可以运行该文件，称之为脚本

## 权限分类

|                   | 权限针对文件，file                                   | 限针对目录，directory                                        |
| ----------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| 读r，read         | 表示可以查看文件内容                                 | 表示可以(ls)查看目录中存在的文件名称                         |
| 写w，             | 表示可以更改文件的内容；vim 修改，保存退出           | 表示是否可以删除目录中的子文件或者新建子目录(rm/touch/mkdir) |
| 执行x，executable | 表示是否可以执行文件，一般指二进制文件、或者脚本文件 | 表示是否可以进入目录中(cd)                                   |

## linux的文件是属于谁

Linux的每一个文件，都有自己的主任，并且有权限限制，限制主人的读，写，执行权限，

linux的文件，有三个角色             root是个特例，即使文件查看的权限是空，root依然是，可以做任何事。权限控制，只是针对普通用户

- user        属主
- group     属组
- other      其他人     

## user属主

表示文件的创建者 ，拥有者，也可以理解成某个用户，对这个文件拥有的权限。

一个文件只有一个主人，

## group属组

文件属于的用户组，拥有组，可以理解成>>>>>某一组的用户，对这个文件的权限。

## othor其他用户

除了root的其他用户，root可以访问所有文件，最高权限。

除了root和文件的创建者，和属组，都是其他人

```
[root@shenzehao home]# ls -l
总用量 2820
-rw-r--r--. 1 root      root      1395 8月  14 17:18 _aa.txt
-rw-r--r--. 1 root      root         0 8月  14 17:44 aa.txt.txt
drwx------. 2 ahei      ahei        62 8月  16 09:32 ahei



# 解释上面是什么意思
开头  - 表示文件    d表文件夹
看的时候除了开头第一个后，三个一组，三个一组。
```

解读为什么创建的用户，没有权限在opt中创建我文件

![a3afba852a13d5f26ca260c916f7aad](D:\笔记\Linux\assets\a3afba852a13d5f26ca260c916f7aad.png)

```
d   rwx   r-x   r-x     3  root            root
                          主人：root      属主：root
    第二个rwx是root可以做的
    第二个rwx是组的权限
    第三个rwx是other的权限，可以r和x，但是不能w，不能写，所有在/opt下创建文件会没有权限。 
```



```
关于用户xxxx，对文件file.txt是否有读，写，执行的权限，需要关注
1.该文件file.txt的user，group，other的权限是多少，是否有r，w，x的权限
2.该文件的file.txt所处的目录，对于bob01是否也同样有相关的r，w，x权限
```

## all角色

每次都需要单独对u，g，o，三个角色，添加，删除，权限，很麻烦。
	只需要对a角色操作，就可以同时给u，g，o三个角色，添加，修改权限
	具体对应到的是linux命令
在后续使用linux命令，修改文件权限时，除了会用到 u、g、o三个角色，还会使用all（缩写a），表示一次性对三个角色，设置权限。

		chmod a+r  file.txt 
	chmod u-r file.txt  # 给file.txt的属主，减去读取的权限

## 查看权限

```shell
ll - d /xxxx    

stat  /xxxxx

# 这两个都可以查看
```

## 文件权限显示

![image-20230818143330108](D:\笔记\Linux\assets\image-20230818143330108.png)

## 软链接

类似Windows的快捷方式。

对单个链接添加快捷方式。（最好使用决定路径）

```
ln  -s   命令原路径   快捷方式的路径
```

通过file查看快捷方法

```bash
file 快捷方式的路径
# a.txt2: symbolic link to a.txt
```

之后在操作原路径还是快捷方式的路径都是一样的，两个都会发生变化

软连接可以移动，但是源文件不能移动，否则会报错。

软连接创捷后不能修改，只能删除了，在创捷一个新的。

在终端敲的时候，直接就敲快捷方式的路径就可以打开原命令。

## 文件权限的数字表示法

文件权限（字母，数字表示）

| 权限 | **对应数字** | 意义   |
| ---- | ------------ | ------ |
| r    | 4            | 可读   |
| w    | 2            | 可写   |
| x    | 1            | 可执行 |

## chmod

 语法

```
chmod  选项    u/g/o-w/r/x       文件/文件夹
chmod  选项    u/g/o+w/r/x       文件/文件夹
修改文件的属组，只能root才可以。
```

不能使用root，要创建一个新的用户。

```shell
# 演示 user
[cao@shenzehao /]$ cd /home   
[cao@shenzehao home]$ cd ./cao
[cao@shenzehao ~]$ pwd
/home/cao
[cao@shenzehao ~]$ touch cao01
[cao@shenzehao ~]$ ll
总用量 0
-rw-rw-r--. 1 cao cao 0 8月  19 10:31 cao01
[cao@shenzehao ~]$ chmod u-r cao01        # 将r权限删除
[cao@shenzehao ~]$ chmod u-w cao01        # 将w权限删除
[cao@shenzehao ~]$ cat cao01
cat: cao01: 权限不够
[cao@shenzehao ~]$ echo "你好，我的名字是" >cao01
bash: cao01: 权限不够
[cao@shenzehao ~]$ ll
总用量 0
----rw-r--. 1 cao cao 0 8月  19 10:31 cao01    # r和w都没有了
# 在重新加上
[cao@shenzehao ~]$ chmod u+w cao01
[cao@shenzehao ~]$ chmod u+r cao01
[cao@shenzehao ~]$ chmod u+x cao01
[cao@shenzehao ~]$ ll
总用量 0
-rwxrw-r--. 1 cao cao 0 8月  19 10:31 cao01

```

group的r，w，x

```shell
# 在root下修改组。
[root@shenzehao ~]# usermod -G devopt shen2
[root@shenzehao ~]# useradd shen2              # 创建一个用户shen2
[root@shenzehao ~]# usermod -G devopt shen2    # 将用户转移到devopt组下
[root@shenzehao ~]# grep 'devopt' /etc/group\
devopt:x:2322:shen2
# 修改组的权限
[root@shenzehao tmp]$ chmod g-r cao01
[root@shenzehao tmp]$ chmod g-w cao01


# 切换用户 shen2
[shen2@shenzehao tmp]$ ll
-rwx---r--. 1 cao  devopt   0 8月  19 10:31 cao01
[shen2@shenzehao tmp]$ cat cao01
cat: cao01: 权限不够
[shen2@shenzehao tmp]$ echo "1231" >cao01
bash: cao01: 权限不够

```

othor的演示

```shell
# 新建一个用户hao
[root@shenzehao ~]# useradd hao
[root@shenzehao ~]# su hao
[hao@shenzehao root]$ cd /tmp
[hao@shenzehao tmp]$ ll
总用量 4
-rwx---r--. 1 cao  devopt   0 8月  19 10:31 cao01

[hao@shenzehao root]$ cd /tmp
[hao@shenzehao tmp]$ cat cao01
[hao@shenzehao tmp]$ echo "123" >cao01
bash: cao01: 权限不够
# 修改权限信息
[root@shenzehao ~]# chmod o-r cao01
[root@shenzehao ~]# chmod o-r /tmp/cao01
# 切换用户
[root@shenzehao ~]# su hao
[hao@shenzehao root]$ cat /tmp/cao01
cat: /tmp/cao01: 权限不够
[hao@shenzehao root]$ 
```

## chgrp

修改文件的属组

````shell
chgrp  devopt xxxx.txt # 将xxxx.txt 的文件组改成devopt
````

## chown

修改文件夹的属主

```shell
chown   shen   xxxx.txt  # 修改文件的属主为shen
```

## 修复文件原理

```shell
# bash-4.2$ 就说明文件
[root@shenzehao ~]# su shen
bash-4.2$ 
bash-4.2$ exit
exit
[root@shenzehao ~]# su - cao
上一次登录：一 8月 21 09:43:13 CST 2023pts/0 上
[cao@shenzehao ~]$ 



1.表示系统读不到用户的个人配置文件，用户在useradd创建时候，系统会去 、/etc/skel 目录下，拷贝所有的用户个人环境变量配置文件，到用户生成的家目录下 /home/xxxx

2. 用户在登录时，自动加载 /home/xxxx 下所有的文件内容


3.修复手段，手动的拷贝 前2步操作即可修复
cp -r /etc/skel/  /home/xxxx
```

##  env

linux中可以查询用户相关的，环境变量，命令是 env

## set

linux中还有一个查询，全系统的环境变量，命令是set

# linux的基础服务管理

```
win键 + r快捷键，打开运行窗口，输入如下指令

services.msc
这条命令可以查看windows的服务
```

## linux默认提供的服务

## ssh服务

```shell
. 我可以自由启动，关闭，重启该服务，查看效果

systemctl  start/stop/restart/status   服务名称

systemctl stop sshd

systemctl status sshd

systemctl start sshd 启动
```

## network服务

管理linux的网络功能，名字叫network

```shell
# 对network服务管理，启停，查看

systemctl stop network 停止

systemctl status network 查看状态

systemctl start network   启动

systemctl restart   重启 
```

## systemctl服务管理命令

在centos6时代，是service管理服务的运行状态

```shell
service命令用于对系统服务进行管理，比如启动（start）、停止（stop）、重启（restart）、重新加载配置（reload）、查看状态（status）等。

# service mysqld  指令      #打印指定服务mysqld的命令行使用帮助。

# service mysqld start    #启动mysqld

# service mysqld stop    #停止mysqld

# service mysqld restart    #重启mysqld （先停止，再运行 ，进程会断开，id会变化）

# service mysqld reload    # 当你修改了mysqld程序的配置文件，需要重新加载该配置文件，而不重启
```

## chkconfig

指定服务是否开机启动

```shell
sshd 远程连接服务
network 提供网络的服务

设置开机自启



提供了一个维护/etc/rc[0~6] d 文件夹的命令行工具，它减轻了系统直接管理这些文件夹中的符号连接的负担。chkconfig主要包括5个原始功能：为系统管理增加新的服务、为系统管理移除服务、列出单签服务的启动信息、改变服务的启动信息和检查特殊服务的启动状态。当单独运行chkconfig命令而不加任何参数时，他将显示服务的使用信息。

[root@localhost www]# chkconfig --list    #查看系统程序列表

[root@localhost www]# chkconfig httpd on  #将httpd加入开机启动

[root@localhost www]# chkconfig httpd off  #关闭httpd开机启动
```

备注

   		在centos7中，service启停服务的命令和 chkconfig命令，都被统一整合为了systemctl

​			并且你依然可以使用旧的命令，系统会自动的转变为systemctl去执行。

​			做了向下兼容的操作，新命令，兼容旧命令。

## systemctl语法

```
systemctl（英文全拼：system control）用于控制 systemd 系统和管理服务。

语法

systemctl [OPTIONS...] COMMAND [UNIT...]

command 选项字如下：  

unit（单元，服务，指的是如sshd，network，nginx，这样的服务名（unit））

这几个指令，就替代了旧版的service 服务名 start/stop/等等
start：启动指定的 unit。
stop：关闭指定的 unit。
restart：重启指定 unit。
reload：重载指定 unit。
status：查看指定 unit 当前运行状态。
is-enabled ：查看是否设置了开机自启  



替代了旧版的chkconfig 服务名 on/off

enable：系统开机时自动启动指定 unit，前提是配置文件中有相关配置。  设置开机自启
disable：开机时不自动运行指定 unit。  禁用开机自


参数：unit 是要配置的服务名称。
```

具体用法，比如sshd服务，你也可以更换为其他的内置服务名，即可管理.

- 启动sshd，systemctl start sshd
- 关闭，systemctl stop sshd
- 重启，systemctl restart sshd
- 重新加载 systemctl reload sshd
- 开机自启  ，systemctl enable sshd
- 禁止开机自启，systemctl disbale sshd
- 查看，sshd服务，是否开机自启，systemctl is-enabled sshd.service

列出系统中，所有的内置服务，名字，和状态

## 修改网络模式，修改静态ip，动态ip获取方式

### 动态ip

1.确保你的机器，是连接的网络的，是插上了网线的。（模拟了物理服务器的软件是什么？看你的虚拟的机器（vmware））

2.进入系统，查看软件的网络配置了

```
[root@shenzehao ~]# cd /etc/sysconfig/network-scripts/
[root@shenzehao network-scripts]# ll
总用量 232
-rw-r--r--. 1 root root   310 8月  11 05:23 ifcfg-ens33
-rw-r--r--. 1 root root   254 5月  22 2020 ifcfg-lo
lrwxrwxrwx. 1 root root    24 8月  11 05:21 ifdown -> ../../../usr/sbin/ifdown
-rwxr-xr-x. 1 root root   654 5月  22 2020 ifdown-bnep
-rwxr-xr-x. 1 root root  6532 5月  22 2020 ifdown-eth
-rwxr-xr-x. 1 root root   781 5月  22 2020 ifdown-ippp
-rwxr-xr-x. 1 root root  4540 5月  22 2020 ifdown-ipv6
lrwxrwxrwx. 1 root root    11 8月  11 05:21 ifdown-isdn -> ifdown-ippp
-rwxr-xr-x. 1 root root  2130 5月  22 2020 ifdown-post
-rwxr-xr-x. 1 root root  1068 5月  22 2020 ifdown-ppp
-rwxr-xr-x. 1 root root   870 5月  22 2020 ifdown-routes
-rwxr-xr-x. 1 root root  1456 5月  22 2020 ifdown-sit
-rwxr-xr-x. 1 root root  1621 12月  9 2018 ifdown-Team
-rwxr-xr-x. 1 root root  1556 12月  9 2018 ifdown-TeamPort
-rwxr-xr-x. 1 root root  1462 5月  22 2020 ifdown-tunnel
lrwxrwxrwx. 1 root root    22 8月  11 05:21 ifup -> ../../../usr/sbin/ifup
-rwxr-xr-x. 1 root root 12415 5月  22 2020 ifup-aliases
-rwxr-xr-x. 1 root root   910 5月  22 2020 ifup-bnep
-rwxr-xr-x. 1 root root 13758 5月  22 2020 ifup-eth
-rwxr-xr-x. 1 root root 12075 5月  22 2020 ifup-ippp
-rwxr-xr-x. 1 root root 11893 5月  22 2020 ifup-ipv6
lrwxrwxrwx. 1 root root     9 8月  11 05:21 ifup-isdn -> ifup-ippp
-rwxr-xr-x. 1 root root   650 5月  22 2020 ifup-plip
-rwxr-xr-x. 1 root root  1064 5月  22 2020 ifup-plusb
-rwxr-xr-x. 1 root root  4997 5月  22 2020 ifup-post
-rwxr-xr-x. 1 root root  4154 5月  22 2020 ifup-ppp
-rwxr-xr-x. 1 root root  2001 5月  22 2020 ifup-routes
-rwxr-xr-x. 1 root root  3303 5月  22 2020 ifup-sit
-rwxr-xr-x. 1 root root  1755 12月  9 2018 ifup-Team
-rwxr-xr-x. 1 root root  1876 12月  9 2018 ifup-TeamPort
-rwxr-xr-x. 1 root root  2780 5月  22 2020 ifup-tunnel
-rwxr-xr-x. 1 root root  1836 5月  22 2020 ifup-wireless
-rwxr-xr-x. 1 root root  5419 5月  22 2020 init.ipv6-global
-rw-r--r--. 1 root root 20678 5月  22 2020 network-functions
-rw-r--r--. 1 root root 30988 5月  22 2020 network-functions-ipv6
```

敲ip addr

```
[root@shenzehao network-scripts]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:27:26:f3 brd ff:ff:ff:ff:ff:ff
    inet 192.168.96.137/24 brd 192.168.96.255 scope global noprefixroute dynamic ens33
       valid_lft 1159sec preferred_lft 1159sec
    inet6 fe80::342c:d6a7:25f4:104e/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
# 2是网络
```

打开ifcfg-ens33

```
vim ifcfg-ens33

TYPE="Ethernet"
PROXY_METHOD="none"
BROWSER_ONLY="no"
BOOTPROTO="dhcp"
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME="ens33"
UUID="f8498459-925e-4042-b4a1-6c713e79e7d8"
DEVICE="ens33"
ONBOOT="yes"
~           
```

![image-20220318114126618-16475748873202](D:\笔记\Linux\assets\image-20220318114126618-16475748873202-16926059000321.png)



4.需要关闭，禁用centos7在图形化下，设置的网络服务，同时管理wifi和有线

```
服务名  NetworkManager

systemctl stop NetworkManager # 关闭
systemctl is-enabled NetworkManager  # 查看是否开机自启

# 禁止开机运行
systemctl disbale NetworkManager
```

5.启动管理网络的服务

```
systemctl start network

systemctl  status network # 查看网络服务状态
```

6.通过ip命令，查看ip地址信息

```
ifconfig
```

**默认的dhcp动态获取ip**

dhcp的ip是有租约的，所以ip地址会变。

### 静态ip

给虚拟机配置静态ip，需要根据如上配置来，找到哪些信息

1. 确认你所在的网段环境 （10.96.0.xx）
2. 确认网关
3. 填写dns服务器地址
4. 修改网卡为 static模式

# 软件包管理

必须解决依赖关系，软件才能正常⼯作

## rpm

用的不多，应该rpm没有解决依赖关系

```
rpm  选项   安装包.rpm
-i  表示安装
-v  表示详细过程
-h  表示进度条显示
rpm -ivh 安装rpm软件
rpm -qa 查看软件是否安装
rpm -ql 查看软件详细信息s
rpm -qf 查看命令属于的安装包
rpm -e 卸载软件
```

```
安装软件的命令格式 rpm -ivh filename.rpm 
升级软件的命令格式 rpm -Uvh filename.rpm
卸载软件的命令格式 rpm -e filename.rpm
查询软件描述信息的命令格式 rpm -qpi filename.rpm
列出软件⽂件信息的命令格式 rpm -qpl filename.rpm
查询⽂件属于哪个 RPM 的命令格式 rpm -qf filename
```

## yum

配置阿里云yum，只有配置好了才可以用阿里云镜像。阿里云镜像网站有配置说明。

配置Epel 镜像，阿里云镜像网站有配置说明。

`https://developer.aliyun.com/mirror/`

## 配置网络yum源（阿里云yum源）

```
1.选择主流的开源镜像站

2.用人家提供的命令，生成yum仓库文件即可
首先必须在 /etc/yum.repos.d 只能在这个目录下，且是第一级
/etc/yum.repos.d/aliyun.repo

为什么要用网络源，因为内容更多，更全
因为如阿里云的工程师，会吧市面主流的软件，全部同步到这个阿里云仓库中，比较齐全，但是也有限制


比如，本地光盘是没有nginx这个工具的


3. 快速配置阿里云仓库，以及移除本地光盘源
https://developer.aliyun.com/mirror/


使用wget命令下载阿里云的repo文件
#wget -O 对该文件进行存放到指定目录，且改名
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo


# 上述命令等于如下
cd /etc/yum.repos.d/

wget  https://mirrors.aliyun.com/repo/Centos-7.repo

ls /etc/yum.repos.d/Centos-7.repo

4.配置阿里云仓库
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo



5. 你会发现，上面这个默认的源，软件数量也不算多，比如nginx就找不到，它的作用类似于 你挂载光盘源，用于安装很多基础，简单的工具
而第三方的工具是没有，如nginx

还得配置一个叫做epel仓库
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo


6.配置好2个仓库后，基本完事，可以安装市面绝大多数的软件了
生成缓存，便于后续加速下载
yum clean all
rm -rf /var/cache/yum
yum makecache

7.此时可以验证用yum源去安装软了
比如先看看软件列表有多少东西
yum list|wc -l

yum list|grep mysql
yum list|grep nginx

```



yum是rpm的工具

自动解决依赖关系的工具

```
[root@shenzehao ~]# cd /etc/yum.repos.d/
[root@shenzehao yum.repos.d]# rpm -qi yum
Name        : yum
Version     : 3.4.3
Release     : 168.el7.centos
Architecture: noarch
Install Date: 2023年08月11日 星期五 05时21分27秒
Group       : System Environment/Base
Size        : 5829237
License     : GPLv2+
Signature   : RSA/SHA256, 2020年10月15日 星期四 03时21分12秒, Key ID 24c6a8a7f4a80eb5
Source RPM  : yum-3.4.3-168.el7.centos.src.rpm
Build Date  : 2020年10月02日 星期五 01时03分49秒
Build Host  : x86-02.bsys.centos.org
Relocations : (not relocatable)
Packager    : CentOS BuildSystem <http://bugs.centos.org>
Vendor      : CentOS
URL         : http://yum.baseurl.org/
Summary     : RPM package installer/updater/manager
Description :
```

yum的配置文件

```shell
[root@shenzehao yum.repos.d]# cat /etc/yum.conf
[main]
cachedir=/var/cache/yum/$basearch/$releasever
keepcache=0                         #本地缓存是否保留， 0不保留，1保留
debuglevel=2                        #调试⽇志级别 
logfile=/var/log/yum.log            #⽇志路径
exactarch=1                         #精确系统平台版本匹
obsoletes=1
gpgcheck=1                          #检查软件包的合法性
plugins=1  
installonly_limit=5                 #同时安装⼏个⼯具包
bugtracker_url=http://bugs.centos.org/set_project.php?project_id=23&ref=http://bugs.centos.org/bug_report_page.php?category=yum
distroverpkg=centos-release
```

请放置你的仓库在这⾥，并且命名为.repo类型

```shell
[root@shenzehao ~]# cd /etc/yum.repos.d/
[root@shenzehao yum.repos.d]# ls
CentOS-CR.repo         CentOS-fasttrack.repo  CentOS-Sources.repo  CentOS-x86_64-kernel.repo
CentOS-Base.repo  CentOS-Debuginfo.repo  CentOS-Media.repo      CentOS-Vault.repo    epel.repo
```

打开这个 CentOS-Base.repo文件

```shell
[root@shenzehao yum.repos.d]# vim CentOS-Base.repo

name=CentOS-$releasever - Base - mirrors.aliyun.com    # 仓库说明
failovermethod=priority                                # 存在多个url，随机挑选。
baseurl=http://mirrors.aliyun.com/centos/$releasever/os/$basearch/          # 下载的网站
        http://mirrors.aliyuncs.com/centos/$releasever/os/$basearch/
        http://mirrors.cloud.aliyuncs.com/centos/$releasever/os/$basearch/
gpgcheck=1                                             #是否检测密钥
gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7      # 公钥文件存在路劲
```

eg：安装nginx

```shell
yum install nginx
# 输入这个命令后，机器会去 /etc/yum.conf/目录下的.repo文件中找到下面的仓库，然后去下载，并且解决依赖关系。
```

删除软件

```shell
[root@shenzehao yum.repos.d]# yum remove nginx redis    # 删除两个，以也可以删除一个。
```

查看所有的仓库

```shell
[root@shenzehao yum.repos.d]# yum repolist all
# 有很多，有些是禁用的。
[root@shenzehao yum.repos.d]# yum list mysql
# 查看mysql的软件包， yum list all 查看所有的软件包

```

一些相关的命令

````
yum命令的⽤法：
 yum [options] [command] [package ...]
 command is one of:
 * install package1 [package2] [...]
 * update [package1] [package2] [...]
 * update-to [package1] [package2] [...]
 * check-update
 * upgrade [package1] [package2] [...]
 * upgrade-to [package1] [package2] [...]
 * distribution-synchronization [package1] [package2] [...]
 * remove | erase package1 [package2] [...]
 * list [...]
 * info [...]
 * provides | whatprovides feature1 [feature2] [...]
 * clean [ packages | metadata | expire-cache | rpmdb | plugi
 * makecache
 * groupinstall group1 [group2] [...]
 * groupupdate group1 [group2] [...]
 * grouplist [hidden] [groupwildcard] [...]
 * groupremove group1 [group2] [...]
 * groupinfo group1 [...]
 * search string1 [string2] [...]
 * shell [filename]
 * resolvedep dep1 [dep2] [...]
 * localinstall rpmfile1 [rpmfile2] [...]
 (maintained for legacy reasons only - use install)
 * localupdate rpmfile1 [rpmfile2] [...]
 (maintained for legacy reasons only - use update)
 * reinstall package1 [package2] [...]
 * downgrade package1 [package2] [...]
 * deplist package1 [package2] [...]
 * repolist [all|enabled|disabled]
 * version [ all | installed | available | group-* | nogroups
 * history [info|list|packages-list|packages-info|summary|add
 * check
 * help [command]
显示仓库列表：
 repolist [all|enabled|disabled]
显示程序包：
 list
 # yum list [all | glob_exp1] [glob_exp2] [...]
 # yum list {available|installed|updates} [glob_exp1] [..
安装程序包：
 install package1 [package2] [...]
reinstall package1 [package2] [...] (重新安装)
升级程序包：
 update [package1] [package2] [...]
 downgrade package1 [package2] [...] (降级)
检查可⽤升级：
 check-update
卸载程序包：
 remove | erase package1 [package2] [...]
查看程序包information：
 info [...]
查看指定的特性(可以是某⽂件)是由哪个程序包所提供：
 provides | whatprovides feature1 [feature2] [...]
清理本地缓存：
clean [headers|packages|metadata|dbcache|plugins|expire-cache|al
构建缓存：
 makecache
搜索：
 search string1 [string2] [...]
 以指定的关键字搜索程序包名及summary信息；
查看指定包所依赖的capabilities：
 deplist package1 [package2] [...]
查看yum事务历史：
 history [info|list|packages-list|packages-info|summary|addon
安装及升级本地程序包：
 * localinstall rpmfile1 [rpmfile2] [...]
 (maintained for legacy reasons only - use install)
 * localupdate rpmfile1 [rpmfile2] [...]
 (maintained for legacy reasons only - use update)
包组管理的相关命令：
 * groupinstall group1 [group2] [...]
 * groupupdate group1 [group2] [...]
 * grouplist [hidden] [groupwildcard] [...]
 * groupremove group1 [group2] [...]
````

yum的优缺点

-  yum是⾃动去yum源中寻找rpm包下载且安装，⾃动解决依赖，⾃动 指定安装路径，⽆须⼈为⼲预 
- 适合初学者，不⽤考虑依赖关系即可安装使⽤⼤部分软件
-  功能由rpm包控制，这个rpm包也是别⼈编译好的，版本可能较低， 功能受限，存在漏洞
-  yum⾃动安装的软件不能定义软件的路径，与功能，机器数量较多， 与后期维护成本较⼤

## 源代码编译安装

rpm命令和yum命令，都是安装⼆进制格式的程序包，别⼈编译 好的，，别⼈给的rpm包，可能版本较低，不合适我们现有的需 求

编译安装优缺点

- 可以⼿动下载最新源代码，按照指定需求，设置参数，指定安装路 径，扩展第三⽅功能，更加灵活 
- ⽆法⾃动解决依赖关系，对新⼿不友好

**建议⽅式**

yum和编译安装结合使⽤，能够最⼤程度解决问题

安装软件的过程

![屏幕截图 2023-08-22 114127](D:\笔记\Linux\assets\屏幕截图 2023-08-22 114127.png)

先安装开发组件

```
开发⼯具：gcc make等
开发组件：
安装下面的组件
yum groupinstall "Development Tools"
yum groupinstall "Server Platform Development"
```

1.下载安装包的压缩文件，并解压(可自己选择目录)

2.进入到解压好的文件夹中。

3.输入指令

```shell
输入指令
./configure --prefix=软件安装路径

针对C、C++代码，进⾏编译安装，需要指定配置⽂件`Makefile`，需要通过`co
通过选项传递参数，指定启⽤特性、安装路径等<执⾏时会⽣成makefile
检查依赖到的外部环境
```

4.执⾏make命令

```shell
# 直接输入就可以。
make
```

5.开始安装 make install

```
开始安装软件到./configure指定的安装路径
```

eg：下载nginx为例

1.打开官网，找到download，找到linux下载，右击复制链接地址

2.进入shell，输入指令

```
[root@shenzehao ~]# wget http://nginx.org/download/nginx-1.25.2.tar.gz
```

3.解压

```
[root@shenzehao nginx-1.25.2]# tar -xzvf nginx-1.25.2.tar.gz
```

4.进入解压目录中

```
[root@shenzehao ~]# cd nginx-1.25.2
[root@shenzehao nginx-1.25.2]# pwd
/root/nginx-1.25.2
[root@shenzehao nginx-1.25.2]# ls
auto  CHANGES  CHANGES.ru  conf  configure  contrib  html  LICENSE  man  README  src
```

5.configure

```
./configure --prefix=软件安装路径
```

6.make

7.make install

## 定时任务

周期性任务执⾏

清空/tmp⽬录下的内容

mysql数据库备份 

redis数据备份

## crond

```shell
[root@shenzehao ~]# rpm -qa cron*
cronie-anacron-1.4.11-23.el7.x86_64
cronie-1.4.11-23.el7.x86_64
crontabs-1.11-6.20121102git.el7.noarch
# 就说明crond安装了
```

![屏幕截图 2023-08-22 163128](D:\笔记\Linux\assets\屏幕截图 2023-08-22 163128.png)

Cron是Linux系统中以后台进程模式周期性执⾏命令或指定程序任务的服 务软件名



Linux系统启动后，cron软件便会启动，对应的进程名字叫做crond，默认 是定期（每分钟检查⼀次）检查系统中是否有需要执⾏的任务计划，如果 有，则按计划进⾏，好⽐我们平时⽤的闹钟。 

- crond定时任务默认最快的频率是每分钟执⾏ 

- 若是需要以秒为单位的计划任务，则编写shell脚本更格式，crond不 适⽤了

## at

at 定时任务⼯具，依赖于 atd 服务，适⽤于执⾏⼀次就结束的调 度任务

没有学完

# 进程管理

## ps

```
参数
-a 显示所有终端机下执⾏的进程，除了阶段作业领导者之外。
 a 显示现⾏终端机下的所有进程，包括其他⽤户的进程。
-A 显示所有进程。
-c 显示CLS和PRI栏位。
 c 列出进程时，显示每个进程真正的指令名称，⽽不包含路径，参数或常
-C<指令名称> 指定执⾏指令的名称，并列出该指令的进程的状况。
-d 显示所有进程，但不包括阶段作业领导者的进程。
-e 此参数的效果和指定"A"参数相同。
 e 列出进程时，显示每个进程所使⽤的环境变量。
-f 显示UID,PPIP,C与STIME栏位。
 f ⽤ASCII字符显示树状结构，表达进程间的相互关系。
-g<群组名称> 此参数的效果和指定"-G"参数相同，当亦能使⽤阶段作业领
 g 显示现⾏终端机下的所有进程，包括群组领导者的进程。
-G<群组识别码> 列出属于该群组的进程的状况，也可使⽤群组名称来指定
 h 不显示标题列。
-H 显示树状结构，表示进程间的相互关系。
-j或j 采⽤⼯作控制的格式显示进程状况。
-l或l 采⽤详细的格式来显示进程状况。
 L 列出栏位的相关信息。
-m或m 显示所有的执⾏绪。
 n 以数字来表示USER和WCHAN栏位。
-N 显示所有的进程，除了执⾏ps指令终端机下的进程之外。
-p<进程识别码> 指定进程识别码，并列出该进程的状况。
 p<进程识别码> 此参数的效果和指定"-p"参数相同，只在列表格式⽅⾯稍
 r 只列出现⾏终端机正在执⾏中的进程。
-s<阶段作业> 指定阶段作业的进程识别码，并列出⾪属该阶段作业的进程
 s 采⽤进程信号的格式显示进程状况。
 S 列出进程时，包括已中断的⼦进程资料。
-t<终端机编号> 指定终端机编号，并列出属于该终端机的进程的状况。
 t<终端机编号> 此参数的效果和指定"-t"参数相同，只在列表格式⽅⾯稍
-T 显示现⾏终端机下的所有进程。
-u<⽤户识别码> 此参数的效果和指定"-U"参数相同。
 u 以⽤户为主的格式来显示进程状况。
-U<⽤户识别码> 列出属于该⽤户的进程的状况，也可使⽤⽤户名称来指定
 U<⽤户名称> 列出属于该⽤户的进程的状况。
 v 采⽤虚拟内存的格式显示进程状况。
-V或V 显示版本信息。
-w或w 采⽤宽阔的格式来显示进程状况。
 x 显示所有进程，不以终端机来区分。
 X 采⽤旧式的Linux i386登陆格式显示进程状况。
 -y 配合参数"-l"使⽤时，不显示F(flag)栏位，并以RSS栏位取代ADDR栏位
-<进程识别码> 此参数的效果和指定"p"参数相同。
--cols<每列字符数> 设置每列的最⼤字符数。
--columns<每列字符数> 此参数的效果和指定"--cols"参数相同。
--cumulative 此参数的效果和指定"S"参数相同。
--deselect 此参数的效果和指定"-N"参数相同。
--forest 此参数的效果和指定"f"参数相同
参数
-a 显示所有终端机下执⾏的进程，除了阶段作业领导者之外。
 a 显示现⾏终端机下的所有进程，包括其他⽤户的进程。
-A 显示所有进程。
-c 显示CLS和PRI栏位。
 c 列出进程时，显示每个进程真正的指令名称，⽽不包含路径，参数或常
-C<指令名称> 指定执⾏指令的名称，并列出该指令的进程的状况。
-d 显示所有进程，但不包括阶段作业领导者的进程。
-e 此参数的效果和指定"A"参数相同。
 e 列出进程时，显示每个进程所使⽤的环境变量。
-f 显示UID,PPIP,C与STIME栏位。
 f ⽤ASCII字符显示树状结构，表达进程间的相互关系。
-g<群组名称> 此参数的效果和指定"-G"参数相同，当亦能使⽤阶段作业领
 g 显示现⾏终端机下的所有进程，包括群组领导者的进程。
-G<群组识别码> 列出属于该群组的进程的状况，也可使⽤群组名称来指定
 h 不显示标题列。
-H 显示树状结构，表示进程间的相互关系。
-j或j 采⽤⼯作控制的格式显示进程状况。
-l或l 采⽤详细的格式来显示进程状况。
 L 列出栏位的相关信息。
-m或m 显示所有的执⾏绪。
 n 以数字来表示USER和WCHAN栏位。
-N 显示所有的进程，除了执⾏ps指令终端机下的进程之外。
-p<进程识别码> 指定进程识别码，并列出该进程的状况。
 p<进程识别码> 此参数的效果和指定"-p"参数相同，只在列表格式⽅⾯稍
 r 只列出现⾏终端机正在执⾏中的进程。
-s<阶段作业> 指定阶段作业的进程识别码，并列出⾪属该阶段作业的进程
 s 采⽤进程信号的格式显示进程状况。
 S 列出进程时，包括已中断的⼦进程资料。
-t<终端机编号> 指定终端机编号，并列出属于该终端机的进程的状况。
 t<终端机编号> 此参数的效果和指定"-t"参数相同，只在列表格式⽅⾯稍
-T 显示现⾏终端机下的所有进程。
-u<⽤户识别码> 此参数的效果和指定"-U"参数相同。
 u 以⽤户为主的格式来显示进程状况。
-U<⽤户识别码> 列出属于该⽤户的进程的状况，也可使⽤⽤户名称来指定
 U<⽤户名称> 列出属于该⽤户的进程的状况。
 v 采⽤虚拟内存的格式显示进程状况。
-V或V 显示版本信息。
-w或w 采⽤宽阔的格式来显示进程状况。
 x 显示所有进程，不以终端机来区分。
 X 采⽤旧式的Linux i386登陆格式显示进程状况。
 -y 配合参数"-l"使⽤时，不显示F(flag)栏位，并以RSS栏位取代ADDR栏位
-<进程识别码> 此参数的效果和指定"p"参数相同。
--cols<每列字符数> 设置每列的最⼤字符数。
--columns<每列字符数> 此参数的效果和指定"--cols"参数相同。
--cumulative 此参数的效果和指定"S"参数相同。
--deselect 此参数的效果和指定"-N"参数相同。
--forest 此参数的效果和指定"f"参数相同
```

### ps不加参数

输出的是当前⽤户所在终端的进程

```
[root@shenzehao ~]# ps
   PID TTY          TIME CMD
  1647 pts/0    00:00:00 bash
  1671 pts/0    00:00:00 ps
```

### ps -ef

显示linux机器上详细的进程信息

```shell
[root@shenzehao ~]# ps -ef
UID         PID   PPID  C STIME TTY          TIME CMD
root          1      0  0 09:21 ?        00:00:01 /usr/lib/systemd/systemd --switched-root --system --deserialize 22
root          2      0  0 09:21 ?        00:00:00 [kthreadd]
root          4      2  0 09:21 ?        00:00:00 [kworker/0:0H]
root          6      2  0 09:21 ?        00:00:00 [ksoftirqd/0]
root          7      2  0 09:21 ?        00:00:00 [migration/0]
root          8      2  0 09:21 ?        00:00:00 [rcu_bh]
root          9      2  0 09:21 ?        00:00:00 [rcu_sched]
root         10      2  0 09:21 ?        00:00:00 [lru-add-drain]
root         11      2  0 09:21 ?        00:00:00 [watchdog/0]

# 输出解释
UID ：由该⽤户执⾏的进程
PID：进程的标识号
PPID：进程的⽗进程标识号
C：CPU使⽤的资源百分⽐
STIME：进程开始的时间
TTY：该进程是哪个终端上运⾏的，若⽆终端，显示?。tty1-tty6是本
机的登录进程，pts/0等表示远程连接
TIME：进程使⽤的CPU的时⻓
CMD：正在执⾏的命令⾏
```

### 查找特定进程

```shell
[root@shenzehao ~]# ps -ef|grep ssh
root       1125      1  0 09:22 ?        00:00:00 /usr/sbin/sshd -D
root       1638   1125  0 09:22 ?        00:00:00 sshd: root@pts/0
root       1675   1647  0 09:31 pts/0    00:00:00 grep --color=auto ssh
```

### ps aux

```shell
[root@shenzehao ~]# ps aux
USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          1  0.1  0.3 194108  7228 ?        Ss   09:21   0:01 /usr/lib/systemd/systemd --switched-root --system --deserialize 2
root          2  0.0  0.0      0     0 ?        S    09:21   0:00 [kthreadd]
root          4  0.0  0.0      0     0 ?        S<   09:21   0:00 [kworker/0:0H]
root          6  0.0  0.0      0     0 ?        S    09:21   0:00 [ksoftirqd/0]
root          7  0.0  0.0      0     0 ?        S    09:21   0:00 [migration/0]
root          8  0.0  0.0      0     0 ?        S    09:21   0:00 [rcu_bh]
root          9  0.0  0.0      0     0 ?        S    09:21   0:00 [rcu_sched]
root         10  0.0  0.0      0     0 ?        S<   09:21   0:00 [lru-add-drain]
root         11  0.0  0.0      0     0 ?        S    09:21   0:00 [watchdog/0]
......
# 解释
解释
USER：该进程属于的⽤户
PID：该进程号码
%CPU：进程占⽤CPU的资源⽐率
%MEM：该进程占⽤物理内存百分⽐
VSZ：进程使⽤的虚拟内存，单位Kbytes
RSS：该进程占⽤固定的内存量，单位Kbytes
TTY：该进程运⾏的终端位置
STAT：进程⽬前状态
        R：运⾏中
        S：终端睡眠中，可以被唤醒
        D：不可中断睡眠
        T：正在检测或是停⽌了
        Z：已停⽌，⽆法由⽗进程正常终⽌，变成了zombie僵⼫进程
        +：前台进程
        I：多线程进程
        N：低优先级进程
        <：⾼优先级进程
        s：进程领导者（含有⼦进程）
        L：锁定到内存中
START：进程启动时间
TIME：CPU运⾏时间
COMMAND：进程命令
```

### 显示指定⽤户的进程

```
[root@shenzehao ~]# ps -u root
   PID TTY          TIME CMD
     1 ?        00:00:01 systemd
     2 ?        00:00:00 kthreadd
     4 ?        00:00:00 kworker/0:0H
     6 ?        00:00:00 ksoftirqd/0
     7 ?        00:00:00 migration/0
     8 ?        00:00:00 rcu_bh
     9 ?        00:00:00 rcu_sched
    10 ?        00:00:00 lru-add-drain
	......
	
```

### ⾃定义格式

想让终端显示那些信息

```shell
[root@shenzehao ~]# ps -eo pid,psr
   PID PSR
     1   4
     2   7
     4   0
     6   0
     7   0
     8   0
     9   0
    10   0
    11   0
    12   1
    13   1
    14   1
    16   1
.......
```

### pstree命令

```
[root@shenzehao ~]# yum install  pstree -y
```

选项

```
-a 显示每个程序的完整指令，包含路径，参数或是常驻服务的标示。
-c 不使⽤精简标示法。
-G 使⽤VT100终端机的列绘图字符。
-h 列出树状图时，特别标明执⾏的程序。
-H<程序识别码> 此参数的效果和指定"-h"参数类似，但特别标明指定的程序。
-l 采⽤⻓列格式显示树状图。
-n ⽤程序识别码排序。预设是以程序名称来排序。
-p 显示程序识别码。
-u 显示⽤户名称。
-U 使⽤UTF-8列绘图字符。
-V 显示版本信息。
```

### 显示进程树

```shell
[root@shenzehao ~]#  pstree 
systemd─┬─NetworkManager─┬─dhclient
        │                └─2*[{NetworkManager}]
        ├─VGAuthService
        ├─anacron
        ├─auditd───{auditd}
        ├─crond
        ├─dbus-daemon───{dbus-daemon}
        ├─firewalld───{firewalld}
        ├─irqbalance
        ├─login───bash
        ├─lvmetad
        ├─master─┬─pickup
        │        └─qmgr
        ├─polkitd───6*[{polkitd}]
        ├─rsyslogd───2*[{rsyslogd}]
        ├─sshd───sshd───bash───pstree
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-udevd
        ├─tuned───4*[{tuned}]
        └─vmtoolsd───2*[{vmtoolsd}]
```

### 显示Linux线程数量

```
root@shenzehao ~]#  pstree -p
systemd(1)─┬─NetworkManager(818)─┬─dhclient(943)
           │                     ├─{NetworkManager}(825)
           │                     └─{NetworkManager}(829)
           ├─VGAuthService(749)
           ├─anacron(1758)
           ├─auditd(726)───{auditd}(727)
           ├─crond(770)
           ├─dbus-daemon(753)───{dbus-daemon}(759)
           ├─firewalld(780)───{firewalld}(940)
           ├─irqbalance(764)
           ├─login(776)───bash(1613)
           ├─lvmetad(573)
           ├─master(1329)─┬─pickup(1332)
           │              └─qmgr(1334)
           ├─polkitd(752)─┬─{polkitd}(760)
           │              ├─{polkitd}(763)
           │              ├─{polkitd}(765)
           │              ├─{polkitd}(767)
           │              ├─{polkitd}(775)
           │              └─{polkitd}(778)
           ├─rsyslogd(1126)─┬─{rsyslogd}(1634)
           │                └─{rsyslogd}(1635)
           ├─sshd(1125)───sshd(1638)───bash(1647)───pstree(1795)
           ├─systemd-journal(547)
           ├─systemd-logind(762)
           ├─systemd-udevd(588)
           ├─tuned(1123)─┬─{tuned}(1527)
           │             ├─{tuned}(1528)
           │             ├─{tuned}(1530)
           │             └─{tuned}(1531)
           └─vmtoolsd(750)─┬─{vmtoolsd}(781)
                           └─{vmtoolsd}(785)
```

### pgrep命令

pgrep 是通过程序的名字来查询进程的⼯具，⼀般是⽤来判断程序是否正 在运⾏。

1.显示指定⽤户，所有相关的进程号

```
-u 显示指定⽤户的所有进程号
[root@shenzehao ~]# pgrep -u root
1
2
4
6
7
8
.....
```

2.可以看做ps和grep的结合，找出ssh有关的进程号

```
[root@shenzehao ~]# pgrep ssh
1125
1638
```

3.过滤进程，以及其id

```
[root@shenzehao ~]# pgrep -l ssh
1125 sshd
1638 sshd
```

## kill

参数

```
参数：
-l <信号编号>，若不加信号的编号参数，则使⽤“-l”参数会列出全部的信号名
-a 当处理当前进程时，不限制命令名和进程号的对应关系
-p 指定kill 命令只打印相关进程的进程号，⽽不发送任何信号
-s 指定发送信号
-u 指定⽤户
```

### 常⽤信号解释

```
信号 解释
1 挂起，终端掉线或是⽤户退出
2 中断，通常是ctrl+c发出此信号
3 退出，通常是ctrl + \ 发出信号
9 ⽴即结束的信号
15 终⽌，通常是系统关机时候发送
20 暂停进程，通常是ctrl + z 发出信号
```

### 终⽌进程

kill默认发送的信号是15，⽤于终⽌进程

```shell
[root@shenzehao ~]# kill 1838
# 直接杀死。
[root@shenzehao ~]# kill -9 1863
```

### 特殊信号0

kill的信号中，存在⼀个特殊信号0，使⽤kill -0 $pid，代表不发给任何信号 给pid，但是会对pid是否存在对应的进程做检查，0就是正常，1就是没有杀死。

用于判断进程是否为零。

```shell
[root@shenzehao ~]# kill 0- 1870
-bash: kill: 0-: 参数必须是进程或任务 ID
[root@shenzehao ~]# echo $?   # $?就是输出上一次的结果
0
```

### killall命令

和pkill一样，但是可能杀不死，需要执行多次命令killall

### pkill命令

pkill命令可以通过进程名终⽌指定的进程，对⽐killall杀死进程可能要执⾏ 多次，pkill可以杀死进程以及⼦进程

```
-f 显示完整程序
-l 显示源代码
-n 显示新程序
-o 显示旧程序
-v 与条件不符合的程序
-x 与条件符合的程序
-p<进程号> 列出⽗进程为⽤户指定进程的进程信息
-t<终端> 指定终端下的所有程序
-u<⽤户> 指定⽤户的程序
```

1.通过进程名杀死

```
[root@shenzehao ~]#  pkill nginx
```

2.通过终端名杀死进程

```
[root@shenzehao ~]# tty
/dev/pts/0    # 查看终端，终端为0
[root@shenzehao ~]# pkill -t pts/1
```

3.通过⽤户杀死进程

````
[root@chaogelinux ~]# pkill -u chaoge
````

## top

top命令⽤于实时的监控系统处理器状态，以及各种进程的资源占⽤情 况。 还可以按照CPU的使⽤量、内存使⽤量进⾏排序显示，以及交互式的命令 操作



直接输入top，出现一个页面

```shell
top - 11:13:31 up  1:51,  2 users,  load average: 0.00, 0.01, 0.05
Tasks: 148 total,   2 running, 146 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  1863028 total,  1276940 free,   245276 used,   340812 buff/cache
KiB Swap:  1048572 total,  1048572 free,        0 used.  1460364 avail Mem 

   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                      
    77 root      20   0       0      0      0 S   3.1  0.0   0:00.12 kworker/u256:1                                               
     1 root      20   0  194108   7228   4164 S   0.0  0.4   0:01.56 systemd                                                      
     2 root      20   0       0      0      0 S   0.0  0.0   0:00.01 kthreadd                                                     
.......有很多
    
    
# 系统资源解释
前五⾏是系统整体的统计信息。第⼀⾏是任务队列信息，同 uptime 命令的执⾏
11:13:31 当前时间
up  1:51 系统运⾏时间，格式为时:分
2 user 当前登录⽤户数
load average: 0.06, 0.60, 0.48 系统负载，即任务队列的平均⻓度。
三个数值分别为 1分钟、5分钟、15分钟前到现在的平均值。
第⼆、三⾏为进程和CPU的信息。当有多个CPU时，这些内容可能会超过两⾏。内
Tasks:148 total 进程总数
 2 running 正在运⾏的进程数
146 sleeping 睡眠的进程数
0 stopped 停⽌的进程数
0 zombie 僵⼫进程数
Cpu(s): 0.3% us ⽤户空间占⽤CPU百分⽐
0.0% sy 内核空间占⽤CPU百分⽐
0.0% ni ⽤户进程空间内改变过优先级的进程占⽤CPU百分⽐
100% id 空闲CPU百分⽐
0.0% wa 等待输⼊输出的CPU时间百分⽐
0.0% hi 
0.0% si 
最后两⾏为内存信息。内容如下：
Mem: 191272k total 物理内存总量
173656k used 使⽤的物理内存总量
17616k free 空闲内存总量
22052k buffers ⽤作内核缓存的内存量
Swap: 192772k total 交换区总量
0k used 使⽤的交换区总量
192772k free 空闲交换区总量
123988k cached 缓冲的交换区总量。
内存中的内容被换出到交换区，⽽后⼜被换⼊到内存，但使⽤过的交换区尚未被覆
该数值即为这些内容已存在于内存中的交换区的⼤⼩。
相应的内存再次被换出时可不必再对交换区写⼊

# 动态名称管理
PID 进程id
PPID ⽗进程id
RUSER Real
UID 进程所有者的⽤户id
USER 进程所有者的⽤户名
GROUP 进程所有者的组名
TTY 启动进程的终端名。不是从终端启动的进程则显示为
PR 优先级
NI nice值。负值表示⾼优先级，正值表示低优先级
P 最后使⽤的CPU，仅在多CPU环境下有意义
%CPU 上次更新到现在的CPU时间占⽤百分⽐
TIME 进程使⽤的CPU时间总计，单位秒
TIME+ 进程使⽤的CPU时间总计，单位1/100秒
%MEM 进程使⽤的物理内存百分⽐
VIRT 进程使⽤的虚拟内存总量，单位kb。VIRT=SWAP+RES
SWAP 进程使⽤的虚拟内存中，被换出的⼤⼩，单位kb。
RES 进程使⽤的、未被换出的物理内存⼤⼩，单位kb。RES=COD
CODE 可执⾏代码占⽤的物理内存⼤⼩，单位kb
DATA 可执⾏代码以外的部分(数据段+栈)占⽤的物理内存⼤⼩，
SHR 共享内存⼤⼩，单位kb
nFLT ⻚⾯错误次数
nDRT 最后⼀次写⼊到现在，被修改过的⻚⾯数。
S 进程状态。
- D=不可中断的睡眠状态
- R=运⾏
- S=睡眠
- T=跟踪/停⽌
- Z=僵⼫进程
COMMAND 命令名/命令⾏
WCHAN 若该进程在睡眠，则显示睡眠中的系统函数名
Flags 任务标志，参考
```

参数

```
参数
-b 批处理
-c 显示完整的治命令
-I 忽略失效过程
-s 保密模式
-S 累积模式
-d<时间> 设置间隔时间
-u<⽤户名> 指定⽤户名
-p<进程号> 指定进程
-n<次数> 循环显示的次数
```

交互式命令

在top执⾏过程中，输⼊⼀些指令，可以查看不同的结果

```
z：打开，关闭颜⾊
Z: 全局显示颜⾊修改
h：显示帮助画⾯，给出⼀些简短的命令总结说明；
k：终⽌⼀个进程；
i：忽略闲置和僵死进程，这是⼀个开关式命令；
q：退出程序；
r：重新安排⼀个进程的优先级别；
S：切换到累计模式；
s：改变两次刷新之间的延迟时间（单位为s），如果有⼩数，就换算成ms。输⼊
f或者F：从当前显示中添加或者删除项⽬；
o或者O：改变显示项⽬的顺序；
l：切换显示平均负载和启动时间信息；
m：切换显示内存信息；
t：切换显示进程和CPU状态信息；
c：切换显示命令名称和完整命令⾏；
M：根据驻留内存⼤⼩进⾏排序；
P：根据CPU使⽤百分⽐⼤⼩进⾏排序；
T：根据时间/累计时间进⾏排序；
w：将当前设置写⼊~/.toprc⽂件中。
B：全局字体加粗
数字1：⽤于多核监控CPU，监控每个逻辑CPU的情况
b：打开，关闭加粗
x，⾼亮的形式排序对应的列
< > ：移动选择排序的列
```

显示进程完整路径

```
显示进程完整路径
```

设置刷新的时间

设置top的检测信息，⼏秒钟更新⼀次

````
[root@shenzehao ~]# top -d 2
````

显示指定的进程信息

检测某⼀个进程的实时资源使⽤量

```
[root@shenzehao ~]# ps -ef |grep nginx
root       9604   9580  0 11:26 pts/0    00:00:00 grep --color=auto nginx

[root@shenzehao ~]# top -p 9604
```

## nohup

将程序放到后台运行

1.nohup直接加上命令

```
[root@shenzehao ~]# nohup ping www.baidu.com
nohup: 忽略输入并把输出追加到"nohup.out"

运行的结果会写在nohup.out，
但是不可以在输入其他的命令了，
关闭窗口也不会关闭，只能kill进程
ctrl + c 结束运行后，nohup.out也结束。
```

2..⼀般不会去关闭当前窗⼝，⽽是nohup配合&符 号，直接把程序放⼊后台

```shell
[root@shenzehao ~]# nohup ping www.baidu.com &
[1] 9856
[root@shenzehao ~]# nohup: 忽略输入并把输出追加到"nohup.out"
# 输出的内容，放到了nohup.out，但是还是可与输入其他命令
```

3.不显示命令执⾏结果，直接重定向

```
```

## htop

```
yum install htop -y
```

修改

```
1. 进⼊htop
2. 按下setup，进⼊设置
3. 上下左右，移动，状态栏会发⽣变化（空格键，更改⻛格）
4. 按下回⻋键，可以选择添加表(meters)
5. F10保存
6. htop能够记忆⽤户的设置
```

搜索进程

```
按下F3
输⼊nginx 查找nginx的进程
```

杀死进程

```
定位到想要杀死进程的哪⼀⾏，按下F9
选择发送给进程的信号，⼀般是15，正常中断进程
回⻋，进程就挂了
```

显示进程树

```
按下F5
```

快捷键

```
 M：按照内存使⽤百分⽐排序，对应MEM%列；
 P：按照CPU使⽤百分⽐排序，对应CPU%列；
 T：按照进程运⾏的时间排序，对应TIME+列；
 K：隐藏内核线程；
 H：隐藏⽤户线程；
 #：快速定位光标到PID所指定的进程上。 
 /：搜索进程名

```

## glances

系统检测工具，有top，htop，glances

Glances 是⼀个由 Python 编写，使⽤ psutil 库来从系统抓取信息的基于 curses 开发的跨平台命令⾏系统监视⼯具。

glances可以干什么？

```
CPU 使⽤率
内存使⽤情况
内核统计信息和运⾏队列信息
磁盘 I/O 速度、传输和读/写⽐率
⽂件系统中的可⽤空间
磁盘适配器
⽹络 I/O 速度、传输和读/写⽐率
⻚⾯空间和⻚⾯速度
消耗资源最多的进程
计算机信息和系统资源
```

### 安装glances

⽅式1

```
通过python的包管理⼯具pip直接安装，类似于yum的作⽤# 需要在linu中下载yum install python python-pip python-devel gcc -y
[root@shenzehao ~]# pip3 install glances
```

⽅式2

```
通过linux的yum⼯具安装，需要配置epel源
yum install glances -y
```

![屏幕截图 2023-08-23 152509](D:\笔记\Linux\assets\屏幕截图 2023-08-23 152509.png)



名词解释

```
glances 是⼀个命令⾏⼯具包括如下命令选项：
-b：显示⽹络连接速度 Byte/ 秒
-B @IP|host ：绑定服务器端 IP 地址或者主机名称
-c @IP|host：连接 glances 服务器端
-C file：设置配置⽂件默认是 /etc/glances/glances.conf 
-d：关闭磁盘 I/O 模块
-e：显示传感器温度
-f file：设置输出⽂件（格式是 HTML 或者 CSV）
-m：关闭挂载的磁盘模块
-n：关闭⽹络模块
-p PORT：设置运⾏端⼝默认是 61209 
-P password：设置客户端 / 服务器密码
-s：设置 glances 运⾏模式为服务器
-t sec：设置屏幕刷新的时间间隔，单位为秒，默认值为 2 秒，数值许可范围：
-h : 显示帮助信息
-v : 显示版本信息
```

```
VIRT: 虚拟内存⼤⼩
RES: 进程占⽤的物理内存值
%CPU：该进程占⽤的 CPU 使⽤率
%MEM：该进程占⽤的物理内存和总内存的百分⽐
PID: 进程 ID 号
USER: 进程所有者的⽤户名
TIME+: 该进程启动后占⽤的总的 CPU 时间
IO_R 和 IO_W: 进程的读写 I/O 速率
NAME: 进程名称
NI: 进程优先级
S: 进程状态，其中 S 表示休眠，R 表示正在运⾏，Z 表示僵死状态。
IOR/s 磁盘读取
IOW/s 磁盘写⼊
```

glances交互式命令

```
h ： 显示帮助信息
q ： 离开程序退出
c ：按照 CPU 实时负载对系统进程进⾏排序
m ：按照内存使⽤状况对系统进程排序
i：按照 I/O 使⽤状况对系统进程排序
p： 按照进程名称排序
d ： 显示磁盘读写状况
w ： 删除⽇志⽂件
l ：显示⽇志
s： 显示传感器信息
f ： 显示系统信息
1 ：轮流显示每个 CPU 内核的使⽤情况（次选项仅仅使⽤在多核 CPU 系统）
```

### glances运⾏web服务

可以在网站上看glances

```shell
1.安装python的包管理⼯具pip
yum install python python-pip python-devel gcc -y
2.安装web模块，bottle
pip install bottle
3.启动服务
[root@chaogelinux ~]# glances -w
Glances web server started on http://0.0.0.0:61208/

# 直接访问http://0.0.0.0:61208/是不行的。
# 需要ifconfig，找到ip后，自己的ip+61208，就可以了，(需要关闭防火墙)
关闭 glances -w这个命令，页面就没有了，需要
[root@shenzehao ~]# nohup glances -w & > /dev/null 2>&1
```

### glances还支持c/s模式

# 三剑客

⽂本处理⼯具，均⽀持正则表达式引擎

```
grep：⽂本过滤⼯具，（模式：pattern）⼯具
sed：stream editor，流编辑器；⽂本编辑⼯具
awk：Linux的⽂本报告⽣成器（格式化⽂本），Linux上是gawk
```

## 基本正则表达式BRE集合

|   符号    |                             作⽤                             |
| :-------: | :----------------------------------------------------------: |
|     ^     | 尖⻆号，⽤于模式的最左侧，如 "^oldboy"，匹配以 oldboy单词开头的⾏ |
|     $     | 美元符，⽤于模式的最右侧，如"oldboy$"，表示以 oldboy单词结尾的⾏ |
|    ^$     |                       组合符，表示空⾏                       |
|     .     |           匹配任意⼀个且只有⼀个字符，不能匹配空⾏           |
|     \     | 转义字符，让特殊含义的字符，现出原形，还原本 意，例如 \. 代表⼩数点 |
|     *     | 匹配前⼀个字符（连续出现）0次或1次以上 ，重复 0次代表空，即匹配所有内容 |
|    .*     |                组合符，匹配任意⻓度的任意字符                |
|    ^.*    |              组合符，匹配任意多个字符开头的内容              |
|    .*$    |             组合符，匹配以任意多个字符结尾的内容             |
|   [abc]   |       匹配[]集合内的任意⼀个字符，a或b或c，可以写[ac]        |
|  [^abc]   |    匹配除了\^后⾯的任意字符，a或b或c，^表示对[abc] 的取反    |
| <pattern> |                        匹配完整的内容                        |
|   <或>    | 定位单词的左侧，和右侧，如  可以找 出"The chao ge"，缺找不出"yuchao" |

## 扩展正则表达式ERE集合

**扩展正则必须⽤ grep -E 才能⽣效**

|  字符  |                     作⽤                     |
| :----: | :------------------------------------------: |
|   +    | 匹配前⼀个字符1次或多次，前⾯字符⾄少出现1次 |
| [:/]+  |     匹配括号内的":"或者"/"字符1次或多次      |
|   ?    |   匹配前⼀个字符0次或1次，前⾯字符可有可⽆   |
|  竖线  |         表示或者，同时过滤多个字符串         |
|   ()   |     分组过滤，被括起来的内容表示⼀个整体     |
| a{n,m} |        匹配前⼀个字符最少n次，最多m次        |
| a{n,}  |            匹配前⼀个字符最少n次             |
|  a{n}  |            匹配前⼀个字符正好n次             |
| a{,m}  |            匹配前⼀个字符最多m次             |

Tip:

```
grep命令需要使⽤参数 -E即可⽀持正则表达式
egrep不推荐使⽤，使⽤grep -E替代
grep不加参数，得在特殊字符前⾯加"\"反斜杠，识别为正则
```

## grep

grep命令需要使⽤参数 -E即可⽀持正则表达式 egrep不推荐使⽤，使⽤grep -E替代 grep不加参数，得在特殊字符前⾯加"\"反斜杠，识别为正则

语法：

```
 grep 选项 file
 
 -i：ignorecase，忽略字符的⼤⼩写；
 -o：仅显示匹配到的字符串本身；
 -v, --invert-match：显示不能被模式匹配到的⾏；
 -E：⽀持使⽤扩展的正则表达式元字符；
 -q, --quiet, --silent：静默模式，即不输出任何信息；
 -n  显示匹配⾏与⾏号
 -w   只匹配过滤的单词
 --color=auto    为grep过滤结果添加颜⾊
 -c  只统计匹配的⾏数
```

## sed

sed是Stream Editor（字符流编辑器）的缩写，简称流编辑器。

 sed是操作、过滤和转换⽂本内容的强⼤⼯具。

擅长修改文本内容，99%用于替换文本

sed会扫描文本中的所有内容。







## awk















# linux的目录

#### 环境变量

```
├── bin -> usr/bin						#常用二进制命令所在的目录，如ls,cp,mkdir,rm等，目前已经变成/usr/bin的软链接
├── boot											#Linux的内核及系统引导程序所需的文件目录
├── dev												#设备文件的目录，如磁盘，光驱等
├── etc												#Linux系统的很多配置文件和yum或rpm安装的软件的配置文件大部分都在这个目录下，非常重要
├── home											#普通用户的家目录
├── lib -> usr/lib						#启动系统和运行命令所需的共享库文件和内核模块存放目录，分为/lib和/lib64两种
├── lib64 -> usr/lib64				#同/lib目录功能一样，只不过放的是64位程序所需要的文件
├── media											#可移除的媒体的挂载点，例如：CD-ROM,U盘等介质，使用频率较低
├── mnt												#文件系统的临时挂载点，也可以作为U盘或CD-ROM等介质的挂载点
├── opt												#没有特殊要求的目录，一般可以把自己二进制安装的软件包放在这个目录下
├── proc											#操作系统运行时，进程信息及内核信息(比如CPU，硬盘分区，内存信息等)
															#proc目录是虚拟文件系统的挂载点，proc并不是真正的文件系统
├── root											#Linux超级用户root的家目录，类似于windows的administrator
├── run												#临时文件系统，存储系统或程序启动以来的信息，当程序或系统重启时该目录下的文件会应该重新生成
├── srv												#service的所以，可用于存放为用户提供服务的数据所在的目录，例如:www,ftp数据
├── sys												#与sys类似，也是虚拟的文件系统，用于存放内核等信息的目录，包含内核，总线，设备，模块组等
├── tmp												#临时文件目录，有时用户运行程序的时候，会产生临时文件，可以当作Linux的系统回收站
├── usr												#存放系统和其他程序的目录，比如命令，帮助文件等。
└── var												#系统日志和大部分程序的日志都放在这个目录下，非常重要。
```


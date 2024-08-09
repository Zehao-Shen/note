# Redis

密码 123456

redis和mysql一样，需要在终端打开redis

```tex
redis-server     		打开终端，输入redis的命令，但是cmd窗口不可以关闭，如果关闭相当于redis关闭。

redis-cli       在打开cmd不关闭的的情况下，重新打开一个cmd，输入命令，可以关闭redis，如果打开的cmd关闭了，会显示下面的话。
												Could not connect to Redis at 127.0.0.1:6379: 由于目标计算机积极拒绝，无法连接。	
                                                
redis-cli shutdown 关闭redis
```

```
如果打开redis报错
[780] 21 Sep 19:46:44.844 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
[780] 21 Sep 19:46:44.844 # Redis version=5.0.14.1, bits=64, commit=ec77f72d, modified=0, pid=780, just started
[780] 21 Sep 19:46:44.845 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
[780] 21 Sep 19:46:44.849 # Could not create server TCP listening socket *:6379: bind: 在一个非套接字上尝试了一个操作。


原因是6379端口已绑定。应该是因为上次服务没有关闭
依次输入下面指令：

redis-cli.exe（启动redis客户端，连接本机6379端口（127.0.0.1）并启动redis服务）
shutdown
exit
```

**在终端下操作redis**

```
启动redis后，在新打开一个终端，输入下面的命令。
redis-cli
```

# redis介绍

Redis（Remote Dictionary Server ，远程字典服务） 是一个使用ANSI C编写的开源、支持网络、基于内存、可选持久性的键值对存储数据库，是NoSQL数据库。

**redis的特性**

- 速度快
- 持久化
- 多种数据结构
- 支持多种编程语言
- 功能丰富
- 简单：代码短小精悍
- 主从复制
- 高可用、分布式

# redis可以用来做什么

Redis 的应用场景包括：缓存系统（“热点”数据：高频读、低频写）、计数器、消息队列系统、排行榜、社交网络和实时系统。

# 切换数据库

select切换数据库

```python
redis的配置文件中，默认有0~15之间的16个数据库，默认操作的就是0号数据库
select <数据库ID>

eg:
    127.0.0.1:6379> select 1
    OK
    # 这是在1号库
    127.0.0.1:6379[1]> select 0
    OK
    127.0.0.1:6379>
```



# redis数据类型

## string(字符串)

### 1. 设置键值

set 设置的数据没有额外操作时，是不会过期的。

```bash
set key value

eg:
set name shen
set name shenzehao 	# 一个变量可以设置多次,类似python的动态设置。
```

<img src="D:\笔记\Redis\assets\5d0dbbc0eaae8a7d24efdd82b90a077.png" alt="5d0dbbc0eaae8a7d24efdd82b90a077" style="zoom:150%;" />



注意：redis中的所有数据操作，如果设置的键不存在则为添加，如果设置的键已经存在则修改。

设置一个键，当键不存在时才能设置成功，用于一个变量只能被设置一次的情况。

```
setnx  key  value
```

一般用于给数据加锁(分布式锁)  给key设置上值后就不会在改变了。

```bash
127.0.0.1:6379> setnx goods_1 101
(integer) 1  # 表示设置成功
127.0.0.1:6379> setnx goods_1 102
(integer) 0  # 表示设置不成功

127.0.0.1:6379> del goods_1
(integer) 1
127.0.0.1:6379> setnx goods_1 102
(integer) 1
```

### 2. 设置键值的过期时间

redis中可以对一切的数据进行设置有效期。以秒为单位

```
setex key seconds value
```

```
setex name sehnze 10    # 10秒后数据删除
```

<img src="D:\笔记\Redis\assets\d058d8e3634f31e5563df996c17eba6.png" alt="d058d8e3634f31e5563df996c17eba6" style="zoom:150%;" />



### 3. 设置多个键值

```
mset key1 value1 key2 value2 ...
```

例3：设置键为`a1`值为`goland`、键为`a2`值为`java`、键为`a3`值为`c`

```
mset a1 goland a2 java a3 c
```

### 4. 字符串拼接值

```
append key value
```

```
# 这两个都可以，在双引号中的可以加空格
append name "  golang" 
append name python  
```



<img src="D:\笔记\Redis\assets\9322621809e766798ce038ad1318762.png" alt="9322621809e766798ce038ad1318762" style="zoom:150%;" />



### 5. 根据键获取值

根据键获取值，如果不存在此键则返回`nil`

```
get key
```

根据多个键获取多个值

```
mget key1 key2 ...
```

getset：设置key的新值，返回旧值

```bash
getset key value      # 返回旧值 mongodb
# 返回key的值，并且将可以设置成一个新值
```

```
getset name caolux      
```

<img src="D:\笔记\Redis\assets\1691477379129.png" alt="1691477379129" style="zoom:150%;" />

### 6. 自增自减

web开发中的电商抢购、秒杀。游戏里面的投票、攻击计数。系统中计算当前在线人数、

自增：

```bash
set id 1
incr id   # 相当于id+1
get id    # 2
incr id   # 相当于id+1
get id    # 3
```

<img src="D:\笔记\Redis\assets\image-20230808145331386.png" alt="image-20230808145331386" style="zoom:150%;" />

自减：

```bash
decr key  # 对一个值自减
```



![image-20230808145529725](D:\笔记\Redis\assets\image-20230808145529725.png)



设置自增多少和自减多少

![image-20230808145721579](D:\笔记\Redis\assets\image-20230808145721579.png)

### 7.获取字符串的长度

```bash
set name shenzehao
strlen name  # 8 
```

## key操作

查看所有键

```
keys *

输出
127.0.0.1:6379> keys *
 1) "z"
 2) "x"
 3) "gender"
 4) "y"
 5) "count"
 6) "age"
 7) "name"
 8) "id"
 9) "title"
10) "a"
```

筛选

```python
# 查看名称中包含`a`的键
keys *a*
# 查看以a开头的键
keys a*
# 查看以a结尾的键
keys *a
```

### 1.判断键是否存在

如果存在返回`1`，不存在返回`0`

```
exists key1
```

判断键`name`是否存在

```python
127.0.0.1:6379> exists name
(integer) 1
```

判断多个值是否存在

```python
127.0.0.1:6379> exists name count
(integer) 2
```

### 2.查看键的的值的数据类型

判断这个键对应的值是什么类型的。

```
type key

# string    字符串
# hash      哈希类型
# list      列表类型
# set       无序集合
# zset      有序集合
```

```python
127.0.0.1:6379> type name
string
```

### 3.删除键以及键对应的值

```
del key1 key2 ...
# 可以删除一个也可以是多个
```

### 4.查看键的有效期

```
ttl key

# 结果结果是秒作为单位的整数(输出结果是整数，结果为含有多长时间失效)
# -1 表示永不过期
# -2 表示当前数据已经过期，查看一个不存在的数据的有效期就是-2
```

### 5.设置key的有效期

给**已有**的数据重新设置有效期，redis中所有的数据都可以通过expire来设置它的有效期。有效期到了，数据就被删除。

```
expire key seconds    

eg:
127.0.0.1:6379> set name shenzehaqo
OK
127.0.0.1:6379> get name
"shenzehaqo"
127.0.0.1:6379> expire name 10
(integer) 1
```

### 6. 清空所有key

慎用，一旦执行，则redis所有数据库0~15的全部key都会被清除

```
flushall
```

### 7. key重命名

```python
rename  oldkey newkey

eg:
    127.0.0.1:6379> set name shen
    OK
    127.0.0.1:6379> rename name new
    OK
    127.0.0.1:6379> get name
    (nil)
    127.0.0.1:6379> get new
    "shen"   
```

## list（数组）

类似python中的列表，**列表的子成员类型为string**

### 1.添加数据

```python
# 在左侧(前)添加一条或多条数据
lpush key value1 value2 ...

# 在右侧(后)添加一条或多条数据
rpush key value1 value2 ...

# 在指定元素的左边(前)/右边（后）插入一个或多个数据
linsert key before 指定元素 value1 value2 ....
linsert key after 指定元素 value1 value2 ....
```

从键为`names`的列表左侧添加一个或多个数据`shen` `ze` `hao`

```py
lpush names shen
# [shen]
lpush names  shen ze hao 
# [hao,ze,shen,shen]
```

从键为`names`的列表右侧添加一个或多个数据`shen` `ze` `hao`

```python
rpush names shen
# [shen]
rpush names  shen ze hao 
# [shen,shen,ze,hao]
```

在`names`数组中的`ze`键的前或后，添加一个,不能添加多个值。

```python
linsert names after "hao" cao  # 在数组names中的hao键的前面添加数据
linsert names before "hao" cao # 在数组names中的hao键的后面面添加数据
###########################################
127.0.0.1:6379> linsert names after "hao" cao
(integer) 5
127.0.0.1:6379>  lrange names 0 -1
1) "shen"
2) "hao"
3) "cao"
4) "ze"
5) "shen"
127.0.0.1:6379>
```

### 2. 获取列表成员

根据指定的索引(下标)获取成员的值，负数下标从右边-1开始，逐个递减

```
lindex key index  # 类似pyhton的索引
```

```p
eg :
	lrange names 0 -1     # 找到names数据的低0个到最后一个
	127.0.0.1:6379>  lrange names 0 -1
    1) "shen"
    2) "cao"
    3) "cao"
    4) "cao"
    5) "hao"
    6) "cao"
    7) "ze"
    8) "shen"
```

移除并获取列表的第一个成员或最后一个成员

```
lpop key  # 第一个成员出列
rpop key  # 最后一个成员出列
# 开发中往往使用rpush和lpop实现队列的数据结构->实现入列和出列
```

```
eg:
	127.0.0.1:6379> lpop names
	"shen"
```

获得数组的切片

```
lrange key start stop
```

```
# 那数组names的值
eg :
    127.0.0.1:6379> lrange names 2 3
    1) "cao"
    2) "hao"
```

### 3. 获取列表的长度

```
llen key
```

```
eg:
	127.0.0.1:6379> llen names
	(integer) 7
```

### 4. 按索引设置值

```
lset key index value
# 注意：
# redis的列表也有索引，从左往右，从0开始，逐一递增，第1个元素下标为0
# 索引可以是负数，表示尾部开始计数，如`-1`表示最后1个元素
```

```
eg:
	127.0.0.1:6379> lset names 0 zhangsan
    OK
    127.0.0.1:6379> lrange names 0 -1
    1) "zhangsan"
    2) "cao"
    3) "cao"
    4) "hao"
    5) "cao"
    6) "ze"
    7) "shen"
```

### 5. 删除指定成员

```
lrem key count value

# 注意：
# count表示删除的数量，value表示要删除的成员。该命令默认表示将列表从左侧前count个value的元素移除
# count==0，表示删除列表所有值为value的成员
# count >0，表示删除列表左侧开始的前count个value成员
# count <0，表示删除列表右侧开始的前count个value成员
```

```
eg:    第0个元素是shen
	127.0.0.1:6379> lrem names 0 shen
    (integer) 1
    127.0.0.1:6379> lrange names 0 -1
    1) "zhangsan"
    2) "cao"
    3) "cao"
    4) "hao"
    5) "cao"
    6) "ze"
```

##  hash（哈希）

就和python中的字典一样{}，哈希是字典套字典

```
结构
键key:{
    域field: 值value,
    域field: 值value,
    域field: 值value,
}
```

### 1. 设置指定键的属性/域

```
hset key field value

eg:	
	127.0.0.1:6379> hset info name shen
    (integer) 1               # 添加成功
    127.0.0.1:6379> hget info name
    "shen"
	
	# 得到的hash就是这样的。info:{name:"shen"}
```

设置键 `user_1`的属性`name`为`xiaoming`

```python
127.0.0.1:6379> hset user_1 name xiaoming   # user_1没有会自动创建
(integer) 1
127.0.0.1:6379> hset user_1 name xiaohei    # user_1中重复的属性会被修改
(integer) 0
127.0.0.1:6379> hset user_1 age 16          # user_1中不存在的属性会被新增
(integer) 1
127.0.0.1:6379> hset user:1 name xiaohui    # user:1会在redis界面操作中以:作为目录分隔符
(integer) 1
127.0.0.1:6379> hset user:1 age 15
(integer) 1
127.0.0.1:6379> hset user:2 name xiaohong age 16  # 一次性添加或修改多个属性
```

### 2.获取指定键所有的域/属性

```python
hkeys key
```

```
eg:      # 得到所有的info中的所有的键。
    127.0.0.1:6379> hkeys info
    1) "name"
    2) "age"
    3) "class"
```

### 3. 获取指定键的单个域/属性的值

```python
hget key field
```



```python
eg:        # 得到info中name的值
    127.0.0.1:6379> hget info name    
    "shen"
    127.0.0.1:6379> hget info age
    "21"
```

### 4. 获取指定键的多个域/属性的值

```
hmget key field1 field2 ...
```

```python
eg:
	127.0.0.1:6379> hmget info name age class
    1) "shen"
    2) "21"
    3) "200"
```

### 5. 获取指定键的所有值

```
hvals key
```

```
eg:    
    127.0.0.1:6379> hvals info
    1) "shen"
    2) "21"
    3) "200"
```

### 6. 删除指定键的域/属性

```
hdel key field1 field2 ...
```



```python
eg:
	# 删除键info的属性class/age/name，当键中的hash数据没有任何属性，则当前键会被redis删除
    127.0.0.1:6379> hdel info name age  
    (integer) 2           # 删除成功
    127.0.0.1:6379> hvals info         #查看数据
    1) "200"                    # 只有一个name:200
```

### 7. 判断指定属性/域是否存在于当前键对应的hash中

```
hexists   key  field
```

```python
# 判断info中是否存在name属性
    127.0.0.1:6379> hexists info name 
    (integer) 0   # 没有数据
    127.0.0.1:6379> hexists info class
    (integer) 1   # 有数据
```

### 8. 属性值自增自减

```
hincrby key field number
```

```python
# 给info的age属性在原值基础上+-10.
    127.0.0.1:6379> hincrby info ager 10
    (integer) 10
    127.0.0.1:6379> hincrby info ager 10
    (integer) 20
    127.0.0.1:6379> hincrby info ager 10
    (integer) 30
# 在age现有值的基础上-10
    127.0.0.1:6379> hincrby info ager -10
    (integer) 20
    127.0.0.1:6379> hincrby info ager -10
    (integer) 10
    127.0.0.1:6379> hincrby info ager -10
    (integer) 0
```

##  set（集合）

无序集合，重点就是**去重**和**无序**。   重点集合中没有重复的，数据也没有顺序。 

### （1）添加元素

```
sadd key member1 member2 ...
```

向键`name_set`的集合中添加元素`shen1`、`shen2`、`shen3`

```
eg:
    127.0.0.1:6379> sadd name_set shen1 shen2 shen3
    (integer) 3
```

### （2）获取集合的所有的成员

```
smembers key
```

获取键`name_set`的集合中所有元素

```
eg:    
    127.0.0.1:6379> smembers name_set
    1) "shen3"
    2) "shen1"
    3) "shen2"
```

### （3）获取集合的长度

```
scard keys 
```

获取`name_set`集合的长度

```
eg:
	127.0.0.1:6379> scard name_set
	(integer) 3
```

### （4）随机删除一个或多个元素

抽取出来的成员被删除掉 

```bash
spop key [count=1]

# 注意：
# count为可选参数，不填则默认一个。被提取成员会从集合中被删除掉
```

随机获取`name_set`集合的成员,斌且删掉

```
eg:    
    127.0.0.1:6379> spop name_set    # 随机删除一个数据，并将数据返回
    "shen3"                  
    127.0.0.1:6379> smembers name_set   # 查看集合name_set中的数据
    1) "shen1"
    2) "shen2"
```

### （5）删除指定元素

```
srem key value
```

删除键`name_set`的集合中元素`shen1`

```
eg:
    127.0.0.1:6379> srem name_set shen1
    (integer) 1
    127.0.0.1:6379> smembers name_set
    1) "shen2"
```

### (6）交集、差集和并集

推荐、（协同过滤，基于用户、基于物品）

```python
sinter  key1 key2 key3 ....    # 交集、比较多个集合中共同存在的成员
sdiff   key1 key2 key3 ....    # 差集、比较多个集合中不同的成员
sunion  key1 key2 key3 ....    # 并集、合并所有集合的成员，并去重
```

```
eg :
   # 创建四个集合
	127.0.0.1:6379> sadd user1 1 2 3 4
    (integer) 4
    127.0.0.1:6379> sadd user2 2 3 4 5
    (integer) 4
    127.0.0.1:6379> sadd user3 3 4 5 6
    (integer) 4
    127.0.0.1:6379> sadd user4 4 5 6 7
    (integer) 4
    


# 交集    
    127.0.0.1:6379> sinter user1 user2     # 集合user1和user2中共有的数据
    1) "2"
    2) "3"
    3) "4"
# 差集 
	127.0.0.1:6379> sdiff user2 user3      #  比较集合user2和user3不同的数据
	1) "2"                                 #  显示的只有user2的数据，user3中的6没有显示。
# 并集
	127.0.0.1:6379> sunion user3 user4     #  合并集合user3 和 user4 中的数据，并去重。
    1) "3"
    2) "4"
    3) "5"
    4) "6"
    5) "7"
```

## zset（有序集合）

有序集合，**去重**并且根据score权重值来进行排序的。score从小到大排列。

#### （1）添加成员

```
zadd key score1 member1 score2 member2 score3 member3 ....

# score1必须是数字，是有序集合的权重。
```

```
eg:
	127.0.0.1:6379> zadd chengji 90 zhangsan 88 lisi 78 wangwu 66 zhaoliu   # 添加数据
    (integer) 4
    127.0.0.1:6379> zadd chengji  33 wnagba     # 可以在添加
    (integer) 1
```

#### （2）获取score在指定区间的所有成员

```python
zrangebyscore key min max     # 按score进行从低往高排序获取指定score区间
zrevrangebyscore key max min  # 按score进行从高往低排序获取指定score区间
zrange key start stop         # 按scoer进行从低往高排序获取指定索引区间
zrevrange key start stop      # 按scoer进行从高往低排序获取指定索引区间
```

```
eg :

#zrangebyscore key min max
	127.0.0.1:6379> zrangebyscore chengji 0 100     # 将chengji集合按权重从小到大排序
    1) "wnagba"
    2) "zhaoliu"
    3) "wangwu"
    4) "lisi"
    5) "zhangsan"
    
# zrevrangebyscore key max min
    127.0.0.1:6379> zrevrangebyscore chengji 100 0
    1) "zhangsan"
    2) "lisi"
    3) "wangwu"
    4) "zhaoliu"
    5) "wnagba"
    
# zrange key start stop      	# 按照建集合时的权重排序。先要几个数据，就拿几个，类似切片
    127.0.0.1:6379> zrange chengji 0 -1
    1) "wnagba"
    2) "zhaoliu"
    3) "wangwu"
    4) "lisi"
    5) "zhangsan"
 
# zrevrange key start stop
	127.0.0.1:6379> zrevrange chengji 0 -1
    1) "zhangsan"
    2) "lisi"
    3) "wangwu"
    4) "zhaoliu"
    5) "wnagba"
```

#### （3）获取集合长度

```
zcard key
```

```
eg: 	
	127.0.0.1:6379> zcard chengji   # 得到chengji的长度
	(integer) 5
```

#### （4）获取指定成员的权重值

```
zscore key member
```

```
eg: 
	127.0.0.1:6379> zscore chengji lisi    # 获取chengji集合中的lisi的数据
	"88"
```

#### （5）获取指定成员在集合中的排名

排名从0开始计算

```
zrank key member      # score从小到大的排名
zrevrank key member   # score从大到小的排名
```

```
eg:
	127.0.0.1:6379> zrank chengji lisi      # 获得chengji中lisi的排名，从小到大的排名
	(integer) 3
	127.0.0.1:6379> zrevrank chengji zhangsan  # 获得chengji中张三的排名，从大到小的排名
	(integer) 0     # 这个时第一名，不是没有值
```

#### （6）获取score在指定区间的所有成员数量

```
zcount key min max
```

获取chengji从60~80分之间的人数[闭区间]

```
eg:
	127.0.0.1:6379> zcount chengji 60 80     
	(integer) 2					# 有两个人
```

#### （7）给指定成员增加增加权重值

```
zincrby key score member
```

给chnegji中wangwu增加10分

```
eg:
 	127.0.0.1:6379> zincrby chengji 10 wangwu 
	"88"            # 增加了10分变成了88
```

#### （8）删除成员

```
zrem key member1 member2 member3 ....   # 也可以删多个
```

从chnegji中删除zhangsan的数据

```
eg: 
	127.0.0.1:6379> zrem chengji zhangsan
    (integer) 1
```

#### （9）删除指定数量的成员

```
# 删除指定数量的成员，从最低score开始删除
zpopmin key [count]
# 删除指定数量的成员，从最高score开始删除
zpopmax key [count]
```

```
eg: 
	127.0.0.1:6379> zpopmin chengji 2      # 从最低score开始删除,删除两个
    1) "wnagba"
    2) "33"
    3) "zhaoliu"
    4) "66"
    
    127.0.0.1:6379> zpopmax chengji 2       #  从最高score开始删除，删除两个
    1) "wangwu"
    2) "88"
    3) "lisi"
    4) "88"
```

# 全部删除

删除库中所有的值，谨慎使用

```
FLUSHDB
```



# python操作redis

```python
# 方式1
import redis

r = redis.Redis(host='127.0.0.1', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))


# 方式2   用的多，用到了连接池
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('bar', 'Foo')
print(r.get('bar'))

"""
通常情况下, 当我们需要做redis操作时, 会创建一个连接, 并基于这个连接进行redis操作, 操作完成后, 释放连接,一般情况下, 这是没问题的, 但当并发量比较高的时候, 频繁的连接创建和释放对性能会有较高的影响。于是, 连接池就发挥作用了。连接池的原理是, 通过预先创建多个连接, 当进行redis操作时, 直接获取已经创建的连接进行操作, 而且操作完成后, 不会释放, 用于后续的其他redis操作。这样就达到了避免频繁的redis连接创建和释放的目的, 从而提高性能。
"""
```

（2）数据类型操作

```python
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# （1）字符串操作：不允许对已经存在的键设置值
ret = r.setnx("name", "yuan")
print(ret)  # False
# （2）字符串操作：设置键有效期
r.setex("good_1001", 10, "2")
# （3）字符串操作：自增自减
r.set("age", 20)
r.incrby("age", 2)
print(r.get("age"))  # b'22'

# （4）hash操作：设置hash
r.hset("info", "name", "rain")
print(r.hget("info", "name"))  # b'rain'
r.hmset("info", {"gedner": "male", "age": 22})
print(r.hgetall("info"))  # {b'name': b'rain', b'gender': b'male', b'age': b'22'}

# （5）list操作：设置list
r.rpush("scores", "100", "90", "80")
r.rpush("scores", "70")
r.lpush("scores", "120")
print(r.lrange("scores", 0, -1))  # ['120', '100', '90', '80', '70']
r.linsert("scores", "AFTER", "100", 95)
print(r.lrange("scores", 0, -1))  # ['120', '100', '95', '90', '80', '70']
print(r.lpop("scores"))  # 120
print(r.rpop("scores"))  # 70
print(r.lindex("scores", 1)) # '95'

# （6）集合操作
# key对应的集合中添加元素
r.sadd("name_set", "zhangsan", "lisi", "wangwu")
# 获取key对应的集合的所有成员
print(r.smembers("name_set"))  # {'lisi', 'zhangsan', 'wangwu'}
# 从key对应的集合中随机获取 numbers 个元素
print(r.srandmember("name_set", 2))
r.srem("name_set", "lisi")
print(r.smembers("name_set"))  # {'wangwu', 'zhangsan'}

# （7）有序集合操作
# 在key对应的有序集合中添加元素
r.zadd("jifenbang", {"yuan": 78, "rain": 20, "alvin": 89, "eric": 45})
# 按照索引范围获取key对应的有序集合的元素
# zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)
print(r.zrange("jifenbang", 0, -1))  # ['rain', 'eric', 'yuan', 'alvin']
print(r.zrange("jifenbang", 0, -1, withscores=True))  # ['rain', 'eric', 'yuan', 'alvin']
print(r.zrevrange("jifenbang", 0, -1, withscores=True))  # ['rain', 'eric', 'yuan', 'alvin']

print(r.zrangebyscore("jifenbang", 0, 100))
print(r.zrangebyscore("jifenbang", 0, 100, start=0, num=1))

# 删除key对应的有序集合中值是values的成员
print(r.zrem("jifenbang", "yuan"))  # 删除成功返回1
print(r.zrange("jifenbang", 0, -1))  # ['rain', 'eric', 'alvin']

# （8）键操作
r.delete("scores")
print(r.exists("scores"))
print(r.keys("*"))
r.expire("name",10)
```









# 订阅

订阅就是抖音我们关注了一个人，他发布一个作品，可以给关注的他的人都通知。

订阅同时向多个客户端发送数据！

```
subscribe channel # 订阅
publish channel mes # 发布消息
```

eg:

```python
import threading

import redis

r = redis.Redis(host='127.0.0.1')


def recv_msg():
    pub = r.pubsub()            # 设置订阅，pubsub的返回是一个类，我们实例化这个类。

    pub.subscribe("room__101")   # 监听room__101这个键。
    msg=pub.parse_response()         # 订阅响应，有人给room__101，发消息，pub.parse_response()就可以收到。不过开始监听是它会先返回个数据。所以要先拿到，在循环下面的。
    print("msg",msg)

    while 1:
        msg = pub.parse_response()
        print(">>>>>",msg)


def send_msg():
    msg = input(">>>")
    r.publish("room__101", msg)     # 向room__101键发数据
	r.publish("room__101", msg.encode())  # 数据是bytes类型就这样。


t = threading.Thread(target=send_msg)
t.start()

recv_msg()
```

# 遇到的问题

```
redis.exceptions.AuthenticationError: Client sent AUTH, but no password is set
```

错误原因：在python连接redis时设置了密码，但是redis默认是没有密码的，所以需要设置一下密码。

打开redis

输入命令

```redis
CONFIG SET requirepass “123456”
```

# auth认证

```py
在redis中，如果配置了requirepass登录密码，则进入redis-cli的操作数据之前，必须要进行登录认证。
注意：在redis6.0以后，redis新增了用户名和密码登录，可以选择使用，也可以选择不适用，默认关闭的。
      在redis6.0以前，redis只可以在配置文件中，可以选择开启密码认证，也可以关闭密码认证，默认关闭的。
      
redis-cli
127.0.0.1:6379> auth <密码>
OK  # 认证通过
```


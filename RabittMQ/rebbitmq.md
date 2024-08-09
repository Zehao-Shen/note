# rebbitMQ

# 一.消息队列介绍

MQ全称为Message Queue 消息队列（MQ）是一种应用程序对应用程序的通信方法。MQ是消费-生产者模型的一个典型的代表，一端往消息队列中不断写入消息，而另一端则可以读取队列中的消息。这样发布者和使用者都不用知道对方的存在。

```tex
数据结构：队列
		先进先出
```

# 二、为什么需要MQ

消息队列中间件是分布式系统中重要的组件，主要解决应用**解耦，异步消息，流量削锋**等问题，实现高性能，高可用，可伸缩和最终一致性架构。目前使用较多的消息队列有ActiveMQ，RabbitMQ，ZeroMQ，Kafka，MetaMQ，RocketMQ

# RabbitMQ介绍

下载：https://www.rabbitmq.com/download.html

下载rabbitmq前需要下载Erlang这个编程语言，RabbitMQ和Erlang**必须看清楚版本！！！**，版本不对应rabbitmq运行不起来。

RabbitMQ 是一个由 Erlang 语言开发的 AMQP 的开源实现。

rabbitMQ是一款基于AMQP协议的消息中间件，它能够在应用之间提供可靠的消息传输。在易用性，扩展性，高可用性上表现优秀。使用消息中间件利于应用之间的解耦，生产者（客户端）无需知道消费者（服务端）的存在。而且两端可以使用不同的语言编写，大大提供了灵活性。

# 下载RabbitMQ

ubuntu22.04

### 更新一次apt-get源

```py
apt-get update
```

### 下载erlang

```py
apt-get install erlang-nox
```

### 查看erlang版本

```
终端输入
erl

Erlang/OTP 24 [erts-12.2.1] [source] [64-bit] [smp:6:6] [ds:6:6:10] [async-threads:1] [jit]

Eshell V12.2.1  (abort with ^G)
1> 
```

### 添加公钥

```py
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
```

### 再更新一次apt-get源

```py
apt-get update
```

### 执行RabbitMQ安装命令

```py
apt-get install rabbitmq-server
```

### 查看 RabbitMq状态

```py
systemctl status rabbitmq-server
```

### RabbitMQ常用操作命令

```py
service rabbitmq-server start    # 启动
service rabbitmq-server stop     # 停止
service rabbitmq-server restart  # 重启 
```



# 如何启动RabbitMQ

类似mysql，python操作mysql需要pymysql库，操作RabbitMQ需要pika库     pip  install  pika

在使用RabbitMQ时需要开启RabbitMQ（和mysql一样，需要cmd，打开RabbitMQ）

将RabbitMQ文件下sbin文件的添加到环境变量中。

打开cmd

```
rabbitmq-server     打开rabbitmq  执行完rabbitmq-server命令后，不要关闭终端。否则消费者会挂的

rabbitmqctl stop    关闭rabbitmq
```

**如果队列的名字已经用在了一个模式下。那么使用其他模式时，不能再用同一个名字。需要修改。**

# 简单模式

不一定生产者先先运行，所有生产者和消费者都可以创建队列，另一方发现创建了，就不用创建了

"""
如果没有数据了，程序不会结束运行，当生产者在运行一次，也就是生产者在将数据传入队列中，消费者程序会自动执行，输出队列中的数据。

生产者需要传bytes类型的，需要将数据encode()，才可以传入队列中，那么消费者接受的也是bytes类型，也需要

"""

```py
需要下载 pika包
```



生产者

```python
import pika


# 1.连接RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# 2.创建队列
# 2.1 创建队列的名称为hello，可以修改
channel.queue_declare(queue='hello')
# 向指定的队列，数据。简单模式exchange不需要值，交换机需要写
a="hello，我的名字是沈泽昊"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=a.encode())   #  body只等接受bytes类型的
connection.close()
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# 确定回调函数。
def callback(ch, method, properties, body):
    body=body.decode()   # 生产者传来了的bytes类型，需要转换成str类型的。
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello',    # 从那个队列中拿数据
                      auto_ack=True,    # 默认应答
                      on_message_callback=callback)   # 将回调函数的名字放到on_message_callback


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()    # 开始正式监听数据，如果有数据，执行on_message_callback赋值的那个函数。
```

# 应答参数模式

当生产者将数据传到队列中，而当消费者的代码中有语法错误时，消费者的代码就会报错，我们修改好后，生产者传来的数据，已经被上一次取走了，

我们并没有拿到数据，就会发生数据丢失。所以需要修改代码，

生产者

和上面的生产者一样

```python
import pika


# 1.连接RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# 2.创建队列
# 2.1 创建队列的名称为hello，可以修改
channel.queue_declare(queue='hello')
# 向指定的队列，数据。简单模式exchange不需要值，交换机需要写
a="hello，我的名字是沈泽昊"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=a.encode())   #  body只等接受bytes类型的
connection.close()
```

消费者

需要在回调函数中写上,并且将auto_ack改成False

```python
ch.basic_ack(delivery_tag=method.delivery_tag)
```



```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# 确定回调函数。
def callback(ch, method, properties, body):
    body=body.decode()   # 生产者传来了的bytes类型，需要转换成str类型的。
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='hello',    # 从那个队列中拿数据
                      auto_ack=False,    # 手动模式 设置成False后，消费者挂了后，生产者传入队列的数据在消费者重启后，会自动收到！
                      on_message_callback=callback)   # 将回调函数的名字放到on_message_callback


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()    # 开始正式监听数据，如果有数据，执行on_message_callback赋值的那个函数。
```

# 上面的总结

简单模式和应答参数模式

需要数据的安全时用应答参数模式，需要速度时用简单模式

# 持久化参数

如果rabbitmq这个服务器挂了，那么生产者和消费者就都没有了，需要解决这样的问题。

生产者

```python
import pika

# 1.连接RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 2.创建队列
# 2.1 创建队列的名称为hello，可以修改
# durable=True加上这个参数就是持久化队列
channel.queue_declare(queue='hello11', durable=True)   
# 向指定的队列，数据。简单模式exchange不需要值，交换机需要写
a = "hello，我的名字是沈泽昊"
channel.basic_publish(exchange='',
                      routing_key='hello11',
                      body=a.encode(),
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent  #将数据存放到零时文件中，存到硬盘中。
                      ))  # body只等接受bytes类型的
connection.close()
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello11',durable=True)


# 确定回调函数。
def callback(ch, method, properties, body):
    body = body.decode()  # 生产者传来了的bytes类型，需要转换成str类型的。
    print(f" 生产者传来数据{body}" .format(body=body))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='hello11',  # 从那个队列中拿数据
                      auto_ack=False,  # 默认应答
                      on_message_callback=callback)  # 将回调函数的名字放到on_message_callback

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # 开始正式监听数据，如果有数据，执行on_message_callback赋值的那个函数。
```

# 分发参数

如果有多个消费者时，会出现不同的消费者运行速度不同的情况，运行速度快的，接受的数据多，所以需要分发

```python
channel.basic_qos(prefetch_count=1)   # 公平分发的参数
```

生产者

```python
import pika


# 1.连接RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# 2.创建队列
# 2.1 创建队列的名称为hello，可以修改
channel.queue_declare(queue='hello12')
# 向指定的队列，数据。简单模式exchange不需要值，交换机需要写
a="hello，我的名字是沈泽昊"
channel.basic_publish(exchange='',
                      routing_key='hello12',
                      body=a.encode())   #  body只等接受bytes类型的
connection.close()
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello12')

# 确定回调函数。
def callback(ch, method, properties, body):
    body=body.decode()   # 生产者传来了的bytes类型，需要转换成str类型的。
    print(" [x] Received %r" % body)

# 公平分发
channel.basic_qos(prefetch_count=1) # 公平分发的参数 

channel.basic_consume(queue='hello12',    # 从那个队列中拿数据
                      auto_ack=False,    # 默认应答
                      on_message_callback=callback)   # 将回调函数的名字放到on_message_callback


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()    # 开始正式监听数据，如果有数据，执行on_message_callback赋值的那个函数。
```

# 交换机模式



交换机有三种模式<img src="D:\笔记\RabittMQ\assets\image-20210415101519408.png" alt="image-20210415101519408" style="zoom: 150%;" />

P是生产者，X是交换机。红色的是不同的队列

- 发布订阅模式>>>>>>>前面时创建队列，而交换机模式是，生产者向交换机发数据，多个消费者有多个队列，不同的队列可以绑定同一个交换机，只要生产者向交换机发数据，那么所有的消费者都会接收到相同的数据。（生产者创建交换机，消费者创建队列）



- 关键字模式>>>>>>>> 前面时创建队列，而交换机模式是，生产者向交换机发数据，多个消费者有多个队列，不同的队列可以绑定同一个交换机，只要生产者向交换机发数据，那么所有的消费者都会接收到相同的数据，并对接受的数据进行筛选。（生产者创建交换机，消费者创建队列）



- 通配符模式>>>>>>>>前面时创建队列，而交换机模式是，生产者向交换机发数据，多个消费者有多个队列，不同的队列可以绑定同一个交换机，只要生产者向交换机发数据，那么所有的消费者都会接收到相同的数据。（生产者创建交换机，消费者创建队列）

## 发布订阅模式

生产者

```python
import pika

# 1.连接RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明一个交换机
channel.exchange_declare(exchange="logs",
                         exchange_type="fanout")  # exchange是交换机的名字，随意起名字，exchange_type="fanout"是交换机模式下的订阅模式，

# 向指定的交换机传数据。简单模式exchange不需要值，交换机需要写
a = "hello，我的名字是沈泽昊"
channel.basic_publish(exchange='logs',  # 向交换机发数据
                      routing_key='',
                      body=a.encode())  # body只等接受bytes类型的
connection.close()
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 如果生产者没有创建交换机，那就又消费者创建。生产者创建了，那么不执行这个代码。
channel.exchange_declare(exchange="logs",exchange_type="fanout")

# 创建队列
result=channel.queue_declare("",exclusive=True)  # 让rabbitmq随机创建一个名字
queue_name=result.method.queue
print(queue_name)
# 将指定的队列绑定到交换机上
channel.queue_bind(exchange="logs",queue=queue_name)


# 确定回调函数。
def callback(ch, method, properties, body):
    body=body.decode()   # 生产者传来了的bytes类型，需要转换成str类型的。
    print(" [x] Received %r" % body)


channel.basic_consume(queue=queue_name,  # 从那个队列中拿数据
                      auto_ack=True,  # 默认应答
                      on_message_callback=callback)  # 将回调函数的名字放到on_message_callback

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # 开始正式监听数据，如果有数据，执行on_message_callback赋值的那个函数。
```

## 关键字模式

<img src="D:\笔记\RabittMQ\assets\image-20210415101537362.png" alt="image-20210415101537362" style="zoom:150%;" />

![image-20210415101723069](D:\笔记\RabittMQ\assets\image-20210415101723069.png)

生产者，给指定关键字后给交换机传数据，消费者指定关键字在队列中接受数据。

生产者

```python
import pika

# 1.连接RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明一个交换机
channel.exchange_declare(exchange="logs2",
                         exchange_type="direct")  # exchange是交换机的名字，随意起名字，exchange_type="fanout"是交换机模式下的订阅模式，

# 向指定的交换机传数据。简单模式exchange不需要值，交换机需要写
a = "hello，我的名字是沈泽昊"
channel.basic_publish(exchange='logs2',  # 向交换机发数据
                      routing_key='error',   # 关键字
                      body=a.encode())  # body只等接受bytes类型的

connection.close()
```

消费者

```py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 如果生产者没有创建交换机，那就又消费者创建。生产者创建了，那么不执行这个代码。
channel.exchange_declare(exchange="logs2",exchange_type="direct")

# 创建队列
result=channel.queue_declare("",exclusive=True)
queue_name=result.method.queue
print(queue_name)
# 将指定的队列绑定到交换机上 
for i in ["error"]:
    channel.queue_bind(exchange="logs2", queue=queue_name, routing_key=i)  
    # routing_key 可以绑定多个关键字，这里不能写列表，写多个queue_bind，routing_key接受指定的关键字数据，for循环指定多个，也可以指定一个。


# 确定回调函数。
def callback(ch, method, properties, body):
    body=body.decode()   # 生产者传来了的bytes类型，需要转换成str类型的。
    print(" [x] Received %r" % body)


channel.basic_consume(queue=queue_name,  # 从那个队列中拿数据
                      auto_ack=True,  # 默认应答
                      on_message_callback=callback)  # 将回调函数的名字放到on_message_callback

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # 开始正式监听数据，如果有数据，执行on_message_callback赋值的那个函数。
```

## 通配符模式

<img src="D:\笔记\RabittMQ\assets\image-20210415101608465.png" alt="image-20210415101608465" style="zoom:150%;" />

类似正则，模糊匹配，

*和#只有两个符号， # 可以匹配一个或者多个单词，\*只能匹配一个单词

生产者

```python
import pika

# 1.连接RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明一个交换机
channel.exchange_declare(exchange="logs3",
                         exchange_type="topic")  # exchange是交换机的名字，随意起名字，exchange_type="fanout"是交换机模式下的订阅模式，

# 向指定的交换机传数据。简单模式exchange不需要值，交换机需要写
a = "hello，我的名字是沈泽昊"
channel.basic_publish(exchange='logs3',  # 向交换机发数据
                      routing_key='teach.beiji',   # 关键字
                      body=a.encode())  # body只等接受bytes类型的

connection.close()
```

消费者

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 如果生产者没有创建交换机，那就又消费者创建。生产者创建了，那么不执行这个代码。
channel.exchange_declare(exchange="logs3",exchange_type="topic")

# 创建队列
result=channel.queue_declare("",exclusive=True)
queue_name=result.method.queue
print(queue_name)
# 将指定的队列绑定到交换机上
for i in ["error" ,"use","teach"]:
    print(i+".#")
    channel.queue_bind(exchange="logs3", queue=queue_name, routing_key=i+".#")  
    # routing_key 可以绑定多个关键字，这里不能写列表，写多个queue_bind或者for循环。


# 确定回调函数。
def callback(ch, method, properties, body):
    body=body.decode()   # 生产者传来了的bytes类型，需要转换成str类型的。
    print(" [x] Received %r" % body)


channel.basic_consume(queue=queue_name,  # 从那个队列中拿数据
                      auto_ack=True,  # 默认应答
                      on_message_callback=callback)  # 将回调函数的名字放到on_message_callback

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # 开始正式监听数据，如果有数据，执行on_message_callback赋值的那个函数。
```




























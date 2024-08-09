# 日志logging

官网https://docs.python.org/zh-cn/3.9/library/logging.html#module-logging

django中的日志官网https://docs.djangoproject.com/zh-hans/3.2/topics/logging/

django中的日志也用的是python中logging。

复制下面的代码，django可以直接用

```python
# 日志
LOGGING = {
    'version': 1, # 使用的日志模块的版本，目前官方提供的只有版本1，但是官方有可能会升级，为了避免升级出现的版本问题，所以这里固定为1
    'disable_existing_loggers': False, # 是否禁用其他的已经存在的日志功能？肯定不能，有可能有些第三方模块在调用，所以禁用了以后，第三方模块无法捕获自身出现的异常了。
    'formatters': { # 日志格式设置，verbose或者simple都是自定义的
        'verbose': { # 详细格式，适合用于开发人员不在场的情况下的日志记录。
            # 格式定义：https://docs.python.org/3/library/logging.html#logrecord-attributes
            # levelname 日志等级
            # asctime   发生时间
            # module    文件名
            # process   进程ID
            # thread    线程ID
            # message   异常信息
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{', # 变量格式分隔符
        },
        'simple': { # 简单格式，适合用于开发人员在场的情况下的终端输出
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {  # 过滤器
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': { # 日志处理流程，console或者mail_admins都是自定义的。
        'console': {
            'level': 'DEBUG', # 设置当前日志处理流程中的日志最低等级
            'filters': ['require_debug_true'], # 当前日志处理流程的日志过滤
            'class': 'logging.StreamHandler',  # 当前日志处理流程的核心类，StreamHandler可以帮我们把日志信息输出到终端下
            'formatter': 'simple'              # 当前日志处理流程的日志格式
        },
        # 'mail_admins': {
        #     'level': 'ERROR',                  # 设置当前日志处理流程中的日志最低等级
        #     'class': 'django.utils.log.AdminEmailHandler',  # AdminEmailHandler可以帮我们把日志信息输出到管理员邮箱中。
        #     'filters': ['special']             # 当前日志处理流程的日志过滤
        # }
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名，日志保存目录logs必须手动创建
            'filename': BASE_DIR.parent / "logs/luffycity.log",
            # 单个日志文件的最大值，这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 备份日志文件的数量，设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志处理的命名空间
        'django': {
            'handlers': ['console','file'], # 当基于django命名空间写入日志时，调用那几个日志处理流程
            'propagate': True,   # 是否在django命名空间对应的日志处理流程结束以后，冒泡通知其他的日志功能。True表示允许
        },
    }
}
```

# logging模块的使用

可以直接用

```py
# 1、定义三种日志输出格式，日志中可能用到的格式化串如下
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息
# 2、强调：其中的%(name)s为getlogger时指定的名字
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

test_format = '%(asctime)s] %(message)s'

# 3、日志配置字典
LOGGING_DIC = {
    'version': 1,                         # 日志的版本,使用1就行
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {                       # standard这个key是能改变的
            'format': standard_format       # format这个key是不能改变的
        },
        'simple': {                         # simple这个key是能改变的
            'format': simple_format         # format这个key是不能改变的
        },
        'test': {                           # test这个key是能改变的
            'format': test_format           # format这个key是不能改变的
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {                                # console这个key不是固定的,可以自己修改.
            'level': 'DEBUG',                       # 日志级别
            'class': 'logging.StreamHandler',       # class,就是指输出的哪里,logging.StreamHandler就是打印到屏幕
            'formatter': 'simple'                   # 输出的格式,上面formatters中的配置,选一个
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG'    ,
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard',                          # formatter日志格式
            # 可以定制日志文件路径
            # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
            # LOG_PATH = os.path.join(BASE_DIR,'a1.log')
            'filename': 'a1.log',  # 保存的路径,日志文件
            'maxBytes': 5,  # 日志大小 5M  超过5M就重命名.
            'backupCount': 100000,         # 备份制定多少份,最多就5个重命名后的文件,这个设置的大一点,会好
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'other': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',         # 保存到文件
            'formatter': 'test',                    # 保存的路径
            'filename': 'a2.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {     # 这个key是可以不写的是可以修改的,这个key可以下使用中在命名.但是下面3个key的名字都是固定的.
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',                    # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,                  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '专门的采集': {    # 这个key的名字很重要,写一个有标识性的名字
            'handlers': ['other','console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

"""
日志的配置formatters,handlers,loggers这三个重要
formatters是日志格式,以后想用那个方式就用哪一个方式.
handlers是日志的接受者,不同的handlers会将日志输出到不同位置(eg:文件,终端,不同的文件)
handlers中的class是指定输出到哪里.
loggers是日志的产生者,产生的日志会传递给handler然后控制输出.
"""


"""
日志名字,日志的名字非常重要loggers中可以设置一个空key,我们使用的时候可以传任何值.

日志轮转,记录着程序运行过程中的关键信息.日志不能轻易的删除.
一个文件太大了,好多个G,日志轮转就是文件到一定的大小,给文件重命名,然后产生一个新的日志文件.
					也可以通过时间来产生一个新的日志。
"""
```

上面代码的使用

```py
import settings
import logging
# !!!强调!!!
# 1、logging是一个包，需要使用其下的config、getLogger，可以如下导入
from logging import config
from logging import getLogger

# 2、也可以使用如下导入
# import logging.config # 这样连同logging.getLogger都一起导入了,然后使用前缀logging.config.

# 3、加载配置
logging.config.dictConfig(settings.LOGGING_DIC)

# 4、输出日志
logger1=logging.getLogger('交易')
logger1.info('这个交易失败了')

# logger2=logging.getLogger("专门的采集")
# logger2.warning("你错误了")
```

# 第二种使用

flask中设置logging

![image-20231205155701220](D:\笔记\python日志\assets\image-20231205155701220.png)

日志设置`settings.dev`

```py
"""日志配置"""
LOG_FILE: str = "logs/yingwuapp.log"   # 日志文件地址
LOG_LEVEL: str = "DEBUG"               # 日志级别
LOG_BACKPU_COUNT: int = 31			   # 日志备份计数
LOG_FORMAT: str = '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'                         # 日志格式
```

提前将上面的配置添加到flask的配置中。

```
app.config.from_object("settings.dev")
```

添加成功后下面的代码才可以找到配置

```py
import logging
from logging.handlers import RotatingFileHandler       # 按文件大小分割日志文件
from logging.handlers import TimedRotatingFileHandler    # 按时间片分割日志文件
from flask import Flask

class Logger(object):
    """日志配置类"""
    def __init__(self, app: Flask = None):
        """
        日志实例化
        :param app: 当前flask应用实例对象
        """
        if app:
            self.init_app(app)

    def init_app(self, app: Flask = None)-> None:
        """
        读取项目的日志配置项
        :param app: 当前flask应用实例对象
        :return: None
        """
        self.app = app
        # 几记得二修改日志地址。
        # self.log_file = self.app.BASE_DIR / self.app.config.get("LOG_FILE", 'logs/app.log')
                self.log_file = self.app.config.get("LOG_FILE", 'logs/app.log')
        self.log_level = self.app.config.get("LOG_LEVEL", 'INFO')
        self.log_backpu_count = self.app.config.get("LOG_BACKPU_COUNT", 31)
        self.log_format = self.app.config.get("LOG_FORMAT", '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
        self.log_rotating_time = self.app.config.get("LOG_ROTATING_TIME", "midnight")
        self.log_charseter = self.app.config.get("LOG_charseter", 'UTF-8')
        self.log_file_size = self.app.config.get("LOG_FILE_SIZE", 300*1024*1024)
        self.setup()

    def setup(self)-> None:
        """
        把日志功能安装到flask项目中
        :return:
        """
        # from logging.handlers import TimedRotatingFileHandler 按时间片分割日志
        handler: TimedRotatingFileHandler = TimedRotatingFileHandler(
            filename=self.log_file,  # 日志存储的文件路径
            when=self.log_rotating_time,  # 每天备份日志的时间，午夜
            backupCount=self.log_backpu_count,  # 备份数量
            encoding=self.log_charseter # 日志文件编码
        )

        # from logging.handlers import RotatingFileHandler      按文件大小分割日志
        # handler: RotatingFileHandler = RotatingFileHandler(
        #     filename=self.log_file,
        #     maxBytes=self.log_file_size,
        #     backupCount=self.log_backpu_count,
        #     encoding=self.log_charseter # 日志文件编码
        # )

        # 设置日志信息的等级
        handler.setLevel(self.log_level)

        # 日志信息的格式
        logging_format: logging.Formatter = logging.Formatter(self.log_format)
        # 设置此处理程序的格式化程序。
        handler.setFormatter(logging_format)
        # 将指定的处理程序添加到此记录器。
        self.app.logger.addHandler(handler)
```

上面代码的使用

```py
from flask import Flask
from utils.loger import Logger
logger=Logger()

app=Flask(__name__)
app.config.from_object("settings")

"""日志加载配置初始化"""
logger.init_app(app)

@app.route("/")
def index():
    app.logger.debug("hello, critical")
    app.logger.warning('Watch out!')
    return "欢迎使用Flask,大力欢迎"
```


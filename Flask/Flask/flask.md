# flask

Flask是一个基于Python开发并且依赖jinja2模板和Werkzeug WSGI服务的一个微型框架，对于Werkzeug本质是Socket服务端，其用于接收http请求并对请求进行预处理，然后触发Flask框架，开发人员基于Flask框架提供的功能对请求进行相应的处理，并返回给用户，如果要返回给用户复杂的内容时，需要借助jinja2模板来实现对模板的处理，即：将模板和数据进行渲染，将渲染后的字符串返回给用户浏览器。

“微”(micro) 并不表示你需要把整个 Web 应用塞进单个 Python 文件（虽然确实可以 ），也不意味着 Flask 在功能上有所欠缺。微框架中的“微”意味着 Flask 旨在保持核心简单而易于扩展。Flask 不会替你做出太多决策——比如使用何种数据库。而那些 Flask 所选择的——比如使用何种模板引擎——则很容易替换。除此之外的一切都由可由你掌握。如此，Flask 可以与您珠联璧合。

默认情况下，Flask 不包含数据库抽象层、表单验证，或是其它任何已有多种库可以胜任的功能。然而，Flask 支持用扩展来给应用添加这些功能，如同是 Flask 本身实现的一样。众多的扩展提供了数据库集成、表单验证、上传处理、各种各样的开放认证技术等功能。Flask 也许是“微小”的，但它已准备好在需求繁杂的生产环境中投入使用。

```python
from flask import Flask

app = Flask(__name__)


@app.route('/index')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
```

# 配置文件

```python
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
```



```python
flask中的配置文件是一个flask.config.Config对象（继承字典）,默认配置为：
    {
        'DEBUG':                                get_debug_flag(default=False),  是否开启Debug模式
        'TESTING':                              False,                          是否开启测试模式
        'PROPAGATE_EXCEPTIONS':                 None,                          
        'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
        'SECRET_KEY':                           None,
        'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
        'USE_X_SENDFILE':                       False,
        'LOGGER_NAME':                          None,
        'LOGGER_HANDLER_POLICY':               'always',
        'SERVER_NAME':                          None,
        'APPLICATION_ROOT':                     None,
        'SESSION_COOKIE_NAME':                  'session',
        'SESSION_COOKIE_DOMAIN':                None,
        'SESSION_COOKIE_PATH':                  None,
        'SESSION_COOKIE_HTTPONLY':              True,
        'SESSION_COOKIE_SECURE':                False,
        'SESSION_REFRESH_EACH_REQUEST':         True,
        'MAX_CONTENT_LENGTH':                   None,
        'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
        'TRAP_BAD_REQUEST_ERRORS':              False,
        'TRAP_HTTP_EXCEPTIONS':                 False,
        'EXPLAIN_TEMPLATE_LOADING':             False,
        'PREFERRED_URL_SCHEME':                 'http',
        'JSON_AS_ASCII':                        True,
        'JSON_SORT_KEYS':                       True,
        'JSONIFY_PRETTYPRINT_REGULAR':          True,
        'JSONIFY_MIMETYPE':                     'application/json',
        'TEMPLATES_AUTO_RELOAD':                None,
    }
```

```python
# 导入
app.config.from_object("python类或类的路径")
app.config.from_object(``'pro_flask.settings.TestingConfig')
```

# 路由

路由的配置有两种写法

```python
@app.route("/index",methods=["GET","POST"])
def index():
    return "hello word"
#方式二
def login():
    return "nihaoasasdasd"
app.add_url_rule('/login',view_func=login)
```

## 反向生成url

```python
from flask import Flask,render_template,url_for

app=Flask(__name__)
app.config.from_object("settings.DevelopmentConfig")
@app.route("/index/<string:nid>",methods=["GET","POST"],endpoint="n1")
def index(nid):
    print(url_for("n2"))   #/login   
    print(nid)
    return "hello word"
@app.route('/login',endpoint="n2")
def login():
    return "nihao"
```

## 自定义路由转换器

- @app.route('/user/<username>')
- @app.route('/post/<int:post_id>')
- @app.route('/post/<float:post_id>')
- @app.route('/post/<path:path>')
- @app.route('/login', methods=['GET', 'POST'])

常用路由系统有以上五种，所有的路由系统都是基于一下对应关系来处理：

```python
DEFAULT_CONVERTERS ``=` `{
  ``'default'``:     UnicodeConverter,
  ``'string'``:      UnicodeConverter,
  ``'any'``:       AnyConverter,
  ``'path'``:       PathConverter,
  ``'int'``:       IntegerConverter,
  ``'float'``:      FloatConverter,
  ``'uuid'``:       UUIDConverter,
}
```

自定义路由转换

```python
from flask import Flask, views, url_for
from werkzeug.routing import BaseConverter

app = Flask(import_name=__name__)


class RegexConverter(BaseConverter):
    """
    自定义URL匹配正则表达式
    """

    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        """
        路由匹配时，匹配成功后传递给视图函数中参数的值
        :param value: 
        :return: 
        """
        return int(value)

    def to_url(self, value):
        """
        使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value: 
        :return: 
        """
        val = super(RegexConverter, self).to_url(value)
        return val


# 添加到flask中(Flask不知道我们定义了一个转换器，需要告诉它)
app.url_map.converters['regex'] = RegexConverter



@app.route('/index/<regex("\d+"):nid>')  # regex要和上面的一样。
def index(nid):
    # 反向生成url时，会允许to_url函数，将to_url的返回值秀修改，反向生成的url也会改变。
    print(url_for('index', nid=nid))     # /index/nid的值
    return 'Index'


if __name__ == '__main__':
    app.run()
```

## 	

使用app.route进行重定向

```python
@app.route("/index/<string:nid>",methods=["GET","POST"],endpoint="n1",redirect_to='/new')
# 在路由中重定向！！   redirect_to=‘/’  
```

# 请求和响应

## 请求

```python
  # 请求相关信息
        # request.method
        # request.args
        # request.form
        # request.values
        # request.cookies
        # request.headers
        # request.path
        # request.full_path
        # request.script_root
        # request.url
        # request.base_url
        # request.url_root
        # request.host_url
        # request.host
        # request.files
        # obj = request.files['the_file_name']
        # obj.save('/var/www/uploads/' + secure_filename(f.filename))
```

## 响应

```python
 # 响应相关信息
        # return "字符串"
        # return render_template('html模板路径',**{})
        # return redirect('/index.html')

        # response = make_response(render_template('index.html'))
        # response是flask.wrappers.Response类型
        # response.delete_cookie('key')
        # response.set_cookie('key', 'value')
        # response.headers['X-Something'] = 'A value'
        # return response


        return "内容"
```

# 模板

Flask使用的是Jinja2模板，所以其语法和Django无差别

后端数据传输到后端

`s1`

```python

from flask import Flask,render_template,Markup

app = Flask(__name__)
# 在模板函数中做一个input标签，Markup必须又Markup传入，否则传入的字符串。不是input框。
def gen_input(value):
    return Markup("<input value='%s'>"%value)

@app.route("/x1",methods=["GET","POST"])
def index():
    context = {
        "k1":123,
        "k2":[11,22,33],
        "k3" :{"name":"shenzehao","age":21},
        "k5":gen_input    # 当前模板才能调用的函数
    }
    return render_template("index.html",**context)


if __name__ == '__main__':
    app.run()
```

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{{k1}}
<p>{{k2.0}} {{k2.1}}</p>
<p>{{k3.get("name")}}</p>
<p>{{k5("222")}}</p>
</body>
</html>
```

## 全局定义函数

在函数上面写@app.template_global()，那么这个函数就是被所有的模板调用

```python
@app.template_global()
def sbbbbbbb(a1, a2):
    """
    每个模板中可以调用的函数
    :param a1:
    :param a2:
    :return:
    """
    return a1 + a2
```

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{{k1}}
<p>{{k2.0}} {{k2.1}}</p>
<p>{{k3.get("name")}}</p>
<p>{{k5("222")}}</p>
<h1>{{sbbbbbbb(1,2)}}</h1>
</body>
</html>
```

## 继承

Flask和Django一样都支持模板继承

写一个母模板

```html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Title</title>
</head>
<body>
    <div >头部</div>
    <div>
        {% block content %} {% endblock %}
    </div>
    <div >底部</div>
</body>
</html>
```

子模板 

子模板继承母模板的页面，子模板可以重写页面

```python
{% extends 'layout.html'%}

{% block content %}
    <h1>{{k1}}</h1>
    <h1>{{k2.0}}  {{k2[0]}} </h1>
    <h1>{{k3.name}}  {{k3['name']}}  {{k3.get('name',888)}}</h1>
    <h1>{{k4(66)}}</h1>
    <h1>{{k5(99)}}</h1>
    <h1>{{sbbbbbbb(1,2)}}</h1>
{% endblock%}
```

# 静态文件

```python
from flask import Flask,render_template
  #  template_folder和static_folder不写都是默认的。
app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
```

模板内容

```python
    <img src="/xxx/111.png" alt="">
# 建议用下面的。
<img src="{{ url_for('static',filename='111.png')}}" />
```

# seeion

```python
from flask import Flask,session

app=Flask(__name__)
app.secret_key="12312312312312"   # 这个必须加，不加会报错。
@app.route("/x1",methods=["GET", "POST"])
def index():
    session["k1"]=123
    return "欢迎使用Flask"
```

拿seeion

```python
from flask import Flask,session

app=Flask(__name__)
app.secret_key="12312312312312"   # 这个必须加，不加会报错。
@app.route("/x1",methods=["GET", "POST"])
def index():
    if session.get("k1"):
    	return "欢迎使用Flask"
    return "去登录"
```

## 修改session

```python
#这样时修改不了的
session["user_info"]={"k1":1,"k2":2}
user_info = session.get("user_info")
print("原来的值", user_info)
session["user_info"]["k1"] = 77777
user_info = session.get("use_info")
print("修改的值", user_info)
```

需要使用下面的代码

```python
# 在源码中需要这两个都是Tur才可以。
session["modified"] = True
session.permanent = True
```

`account`

```python
@account.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    if user == "shen" and pwd == "123":
        uid = str(uuid4())
        session.permanent = True
        session["user_info"] = {"id": uid, "name": user}
        return redirect("/index")
    else:
        return redirect("/test")
```

`home`

```python
@home.route("/index")
def index():
    # user_info=session.get("user_info")
    # print(user_info)
    session["user_info"]={"k1":1,"k2":2}
    user_info = session.get("user_info")
    print("原来的值", user_info)
    session["user_info"]["k1"] = 77777
    user_info = session.get("use_info")
    print("修改的值", user_info)
    #   
    session["modified"] = True
    return "index"
```

# 特殊的装饰器

```python
# 在请求时先运行下面的函数
@app.before_request
def xxxxxx1():
    print("执行1")


# 在返回给客户端最后运行下面的函数
@app.after_request
def xxx1(response):
    print("hou")
    return response
# 在404页面时，太丑，自己可以修改404页面
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


# 有多人请求，但是只有第一个人，会运行这个函数！
@app.before_first_request
def before_first_request2():
    print('before_first_request2')
    
    
# 在函数上面写@app.template_global()，那么这个函数就是被所有的模板调用
@app.template_global()
def sb(a1, a2):
    return a1 + a2
```

# 闪现(flash)

闪现是基于session做的，用于存放临时数据。
访问一次x1,order函数的data，就会有一个<我要上楼>,访问3次x1，在访问x2，那么data中有三个<我要上楼>

```python
from flask import Flask,session,flash,get_flashed_messages

app=Flask(__name__)
app.debug=True
app.secret_key="12312312312312"


@app.route("/x1",methods=["GET", "POST"])
def index():
    flash("我要上楼")
    return "视图函数x1"

@app.route("/x2",methods=["GET","POST"])
def order():
    data=get_flashed_messages()
    print(data)
    return "视图函数x2"
```

下面的代码也可以是实现（基于session做）

```python
from flask import Flask,session

app=Flask(__name__)
app.debug=True
app.secret_key="12312312312312"


@app.route("/x1",methods=["GET", "POST"])
def index():
    session["mi"]="123123123"
    return "视图函数x1"

@app.route("/x2",methods=["GET","POST"])
def order():
    msg=session.pop('mi')
    print(msg)
    return "视图函数x2"
```

#  中间件

用的不多 

1.执行app.\__call__

# 蓝图

蓝图就是对flask的目录结构划分。

flask的创建中有一个py文件。不足以完成整个项目，所有需要蓝图

新建一个项目后，建立一个manage.py的文件为flask的入口，将一个和项目同名的python软件包，在软件包的下面创建static目录放静态文件，创建templates目录放模板文件，创建views目录为视图。

![屏幕截图 2022-08-20 223659](https://s2.loli.net/2022/08/20/Swbu6LHdWfG1ygD.png)



在views中创建多个py文件，为视图，

`views.accout`

```python
from flask import Blueprint

ac=Blueprint("ac",__name__)
@ac.route("/x3")
def login():
    return "login"


@ac.route("/x4")
def logout():
    return "logout"
```

`views.admin`

```python
from flask import Blueprint

bc=Blueprint("bc",__name__)
@bc.route("/x1")
def login():
    return "欢迎使用x1"


@bc.route("/x2")
def logout():
    return "logout"
```

`views.admin`

```python
from flask import Blueprint,render_template

cc = Blueprint("cc", __name__,url_prefix="/admin")


@cc.route("/login")
def login():
    return render_template("login.html")


@cc.route("/logout")
def logout():
    return "logout"
```

url_prefix="/admin"就和Django的路由分发一样。在admin文件下的路由，在访问时都必须时/admin/路由。

`__init__`

```python
from  flask import Flask

app=Flask(__name__)

from .views import account
from .views import admin
from .views import user


app.register_blueprint(account.ac)
app.register_blueprint(admin.bc)
app.register_blueprint(user.cc)


“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”“”
from flask import Flask


def create_app():    
    # 用函数写的化，将视图函数的导入放到函数内
    from .views import account
	from .views import admin
	from .views import user
    app = Flask(__name__)
    app.config.from_object("settings.DevelopmentConfig")
    return app
```



`manage`

```python
from pythonProject1 import app


if __name__ == '__main__':
    app.run()
```

# 上下文管理

在源码中分析上下文管理

> 第一阶段        将ctx(request,session)放到Local对象上
>
> 第二阶段        视图函数导入：request/session
>
> 第三阶段        请求处理完毕
>
> ​										--  获取session并保存带cookie
>
> ​										--  将ctx删除



请求上下文：request/session  保存请求相关的信息

程序(app)上下文：current_/g为了更好的分离程序的状态，应用起来更加灵活，方便调测等

# flask-sission

作用：将默认保存的签名cookie中的值 保存到 redis/memcached/file/Mongodb/SQLAlchemy (就是session存到其他的地方，存在redis中的使用的最多，)

```python
# 这样写session就存在rides中了
# 建议第一种
# 第一种方法
from flask_session import RedisSessionInterface
app.session_interface = RedisSessionInterface(
    redis=Redis(host="127.0.0.7", post="6379"),
    key_prefix="flaskxx",
)
# 第二种方法
from flask.ext.session import Session
from redis import Redis
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='192.168.0.94',port='6379')
Session(app)
```

## 例子

参考flask2，使用了蓝图

`settings`
将session存在redis中

```python
from datetime import timedelta
from redis import Redis


class Config(object):
    DEBUG = True
    SECRET_KEY = "11111111"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)    # 设置session的时间为20分钟。
    SESSION_REFRESH_EACH_REQUEST= True
    # 设置
    SESSION_TYPE = "redis"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    # 设置
    SESSION_REDIS = Redis(host='127.0.0.1', port='6379')


class TestingConfig(Config):
    pass
```

`__init__`

```python
from flask import Flask, session
from .views import account
from .views import home
from flask_session import Session


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')
    app.register_blueprint(account.account)
    app.register_blueprint(home.home)


    #将session替换成redis session,不用session可以不写。
    Session(app)
    return app
```

查看redis中的session

```python
from redis import Redis

conn=Redis(host="127.0.0.1")
v=conn.keys()
print(v)
```

# 数据库

Flask没有orm，所有需要自己写SQL语句，

例子：

不能再每一个视图中都连接数据库，所以需要在写一个专门的sql文件

创建一个utils文件夹，在这个文件夹中创建一个sql.py文件,

`sql`

```python
import pymysql
# from .pool import POOL


class SQLHelper():
    @staticmethod
    def open():
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='qq',
            charset='utf8',
        )
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        return conn,cursor
    @staticmethod
    def close(conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def fetch_one(cls, sql, args):
        # 建立连接
        cunn,cursor=cls.open()
        cursor.execute(sql, args)
        obj = cursor.fetchone()

        cls.close(cunn,cursor)
        return obj

    @classmethod
    def fetch_all(cls, sql, args):
        # 建立连接
        cunn, cursor = cls.open()

        cursor.execute(sql, args)
        obj = cursor.fetchall()

        cls.close(cunn,cursor)
        return obj
```

`视图`

```python
from flask import Blueprint, request, render_template, session, redirect, Flask
from ..utils.sql import SQLHelper
from uuid import uuid4

account = Blueprint("account", __name__)


@account.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    obj=SQLHelper.fetch_one("select id,name from t1 where id=%s and name=%s",[user,pwd])
    print(obj)
    if obj:
        return "登录成功"
    else:
        render_template("login.html")
```

这样写将sql放到了一个文件，但是每次都需要连接数据库，所以不好，我们用DBUtils写一个连接池，
就是将链接创建好，等待这去链接。

# 数据库连接池

使用DBUtils

DBUtils是Python的一个用于实现数据库连接池的模块。

每个线程创建一个连接，关闭连接(其实没有关闭，是放回连接池了)，线程关闭后，连接才关闭

只要写原生SQL就要，就要写数据库连接池。

`poll`

```python
import time
import pymysql
import threading
from DBUtils.PooledDB import PooledDB, SharedDBConnection

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,      # (写不写都一样)链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,  # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='qq',
    charset='utf8'
)


def func():
    # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
    # 否则
    # 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
    # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
    # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
    # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。
    conn = POOL.connection()
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

    # print(th, '链接被拿走了', conn1._con)
    # print(th, '池子里目前有', pool._idle_cache, '\r\n')
    cursor.execute('select * from t1')  # 
    result = cursor.fetchall()
    cursor.close()
    conn.close()  # 这个close并没有关掉，是放回连接池了。
    return result


func()
```

`sql`

```python
import pymysql
from .pool import POOL
# 导入POOL


class SQLHelper():
    @staticmethod
    def open():
        # conn = pymysql.connect(
        #     host='localhost',
        #     port=3306,
        #     user='root',
        #     password='123456',
        #     db='qq',
        #     charset='utf8',
        # )
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn=POOL.connection()  # 使用POOL 的一个方法， 只修改这里就可以。
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn,cursor
    @staticmethod
    def close(conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def fetch_one(cls, sql, args):
        # 建立连接
        cunn,cursor=cls.open()
        cursor.execute(sql, args)
        obj = cursor.fetchone()
        print("sql",obj)

        cls.close(cunn,cursor)
        return obj

    @classmethod
    def fetch_all(cls, sql, args):
        # 建立连接
        cunn, cursor = cls.open()

        cursor.execute(sql, args)
        obj = cursor.fetchall()

        cls.close(cunn,cursor)
        return obj
```

# wtforms

作用：WTForms是一个支持多个web框架的form组件，主要用于对用户请求数据进行验证。

**写一个类，继承类，写字段，字段中有正则，有插件**    记住前面的加粗，加黑就可以，不用记代码。

```python
from flask import Flask, render_template, request, redirect
from wtforms import Form
from wtforms.fields import core
# 由于版本的wentihtml5会出现问题
from wtforms.fields import html5
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets

app = Flask(__name__, template_folder='templates')
app.debug = True



class RegisterForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='shen'
    )

    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    pwd_confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码输入不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    gender = core.RadioField(
        label='性别',
        choices=(
            (1, '男'),
            (2, '女'),
        ),
        coerce=int
    )
    city = core.SelectField(
        label='城市',
        choices=(
            ('bj', '北京'),
            ('sh', '上海'),
        )
    )

    hobby = core.SelectMultipleField(
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )

    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))

    def validate_pwd_confirm(self, field):
        """
        自定义pwd_confirm字段规则，例：与pwd字段是否一致
        :param field: 
        :return: 
        """
        # 最开始初始化时，self.data中已经有所有的值

        if field.data != self.data['pwd']:
            # raise validators.ValidationError("密码不一致") # 继续后续验证
            raise validators.StopValidation("密码不一致")  # 不再继续后续验证


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm(data={'gender': 1})
        return render_template('register.html', form=form)
    else:
        form = RegisterForm(formdata=request.form)
        if form.validate():
            print('用户提交数据通过格式验证，提交的值为：', form.data)
        else:
            print(form.errors)
        return render_template('register.html', form=form)



if __name__ == '__main__':
    app.run()
```

在有视图函数时，前后端不分离的项目

```python
from flask import Blueprint, request, render_template, session, redirect, Flask
from ..utils.sql import SQLHelper
from uuid import uuid4
from wtforms import Form

from wtforms.fields import core
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets

account = Blueprint("account", __name__)

class LoginForm(Form):
    user = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}

    )
    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                              message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')

        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )



@account.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form=LoginForm()
        return render_template("login.html",form=form)
    # user = request.form.get("user")
    # pwd = request.form.get("pwd")
    # 拿到页面传来的数据。
    form = LoginForm(formdata=request.form)
    print(form)
    # 在数据库中进行校验。
    obj=SQLHelper.fetch_one("select id,name from t1 where id=%(user)s and name=%(owd)s",form.data)
    print(obj)
    if obj:
        return "登录成功"
    else:
        render_template("login.html")
```

# SQLAlchemy

<img src="https://s2.loli.net/2022/08/25/25roLkhzvGZxMKW.png" alt="425762-20160723192854919-886727948.png" style="zoom:80%;" />

- Engine，框架的引擎
- Connection Pooling ，数据库连接池
- Dialect，选择连接数据库的DB API种类
- Schema/Types，架构和类型
- SQL Exprression Language，SQL表达式语言



SQLAlchemy是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。

SQLAlchemy本身无法操作数据库，其必须以来pymsql等第三方插件，Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作

```python
MySQL-Python
  ``mysql+mysqldb://<``user``>:<``password``>@<host>[:<port>]/<dbname>
 
pymysql
  ``mysql+pymysql://<username>:<``password``>@<host>/<dbname>[?<options>]
 
MySQL-Connector
  ``mysql+mysqlconnector://<``user``>:<``password``>@<host>[:<port>]/<dbname>
 
cx_Oracle
  ``oracle+cx_oracle://``user``:pass@host:port/dbname[?``key``=value&``key``=value...]
 
更多详见：http://docs.sqlalchemy.org/en/latest/dialects/``index``.html
```

## 基于SQLAlchemy写原始sql

SQLAlchemy的内部提供了连接池

```python
import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

# 数据库连接池
engine = create_engine(
    "mysql+pymysql://root:123@127.0.0.1:3306/t1?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

# 执行原生sql
def task(arg):
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute(
        "select * from t1"
    )
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    
for i in range(20):
    t = threading.Thread(target=task, args=(i,))
    t.start()
```

## 用SQLAlchemy的操作

```python
from sqlalchemy.ext.declarative import declarative_base
# 想要什么就来这里导入
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index，DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/flasklianxi", max_overflow=5)

Base = declarative_base()


# 创建单表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))  # String就是varchar
    extra = Column(String(16))

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

# 一对多
class Favor(Base):
    __tablename__ = 'favor'
    nid = Column(Integer, primary_key=True)
    caption = Column(String(50), default='red', unique=True)


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    favor_id = Column(Integer, ForeignKey("favor.nid"))   # 这里不是类名，是表名


# 多对多
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)


class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)


class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))


def init_db():
    Base.metadata.create_all(engine)   # 创建一个表


def drop_db():
    Base.metadata.drop_all(engine)     # 删除一个表
```

## 增删改查

### 增

```python
# 创建数据库的文件和增代码在一个文件下
import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/flasklianxi", max_overflow=5)
xxxx=sessionmaker(bind=engine)
session= xxxx()

obj = models.Users(name="alex0", extra='sb')
session.add(obj)
session.add_all([
    models.Users(name="alex1", extra='sb'),
    models.Users(name="alex2", extra='sb'),
])
session.commit()
```

### 查

```python
# 简单的查询，
result=session.query(models.Users).all()   # result就是一个列表
for i in result:
    print(i.id,i.name)
# 条件查询
#　条件
ret = session.query(models.Users).filter_by(name='alex').all()
ret = session.query(models.Users).filter(models.Users.id > 1, models.Users.name == 'eric').all()
ret = session.query(models.Users).filter(models.Users.id.between(1, 3), models.Users.name == 'eric').all()
ret = session.query(models.Users).filter(models.Users.id.in_([1,3,4])).all()
ret = session.query(models.Users).filter(~models.Users.id.in_([1,3,4])).all()
ret = session.query(models.Users).filter(models.Users.id.in_(session.query(models.Users.id).filter_by(name='eric'))).all()
from sqlalchemy import and_, or_
ret = session.query(models.Users).filter(and_(models.Users.id > 3, models.Users.name == 'eric')).all()
ret = session.query(models.Users).filter(or_(models.Users.id < 2, models.Users.name == 'eric')).all()
ret = session.query(models.Users).filter(
    or_(
        models.Users.id < 2,
        and_(models.Users.name == 'eric', models.Users.id > 3),
        models.Users.extra != ""
    )).all()


# 通配符
ret = session.query(models.Users).filter(models.Users.name.like('e%')).all()
ret = session.query(models.Users).filter(~models.Users.name.like('e%')).all()

# 限制
ret = session.query(models.Users)[1:2]

# 排序
ret = session.query(models.Users).order_by(models.Users.name.desc()).all()
ret = session.query(models.Users).order_by(models.Users.name.desc(), models.Users.id.asc()).all()

# 分组
from sqlalchemy.sql import func

ret = session.query(models.Users).group_by(models.Users.extra).all()
ret = session.query(
    func.max(models.Users.id),
    func.sum(models.Users.id),
    func.min(models.Users.id)).group_by(models.Users.name).all()

ret = session.query(
    func.max(models.Users.id),
    func.sum(models.Users.id),
    func.min(models.Users.id)).group_by(models.Users.name).having(func.min(models.Users.id) >2).all()

# 连表
from models import Favor,Person

ret = session.query(models.Users, Favor).filter(models.Users.id == Favor.nid).all()

ret = session.query(Person).join(Favor).all()

ret = session.query(Person).join(Favor, isouter=True).all()


# 组合
q1 = session.query(models.Users.name).filter(models.Users.id > 2)
q2 = session.query(Favor.caption).filter(Favor.nid < 2)
ret = q1.union(q2).all()

q1 = session.query(models.Users.name).filter(models.Users.id > 2)
q2 = session.query(Favor.caption).filter(Favor.nid < 2)
ret = q1.union_all(q2).all()
```

### 删

```python
# 简单的删除  
result=session.query(models.Users).filter(models.Users.id>2).delete()
session.commit()
```

### 改

```python
# 更改
session.query(models.Users).filter(models.Users.id == 2).update({"name" : "099"})
session.query(models.Users).filter(models.Users.id > 2).update({models.Users.name: models.Users.name + "099"}, synchronize_session=False)  #  synchronize_session=False   字符串的相加
session.query(models.Users).filter(models.Users.id > 2).update({models.Users.name: models.Users.name + 1}, synchronize_session="evaluate")   # synchronize_session="evaluate" 数值上相加

session.commit()
```

# flask-script

```
pip  install flask-script
```

我的版本过高，这个并没有成功

在"Flask==1.1.4"前可以和django一样，在终端用命令启动项目，

可以自定义命令。

```python
from flask3 import create_app
from flask_script import Manager

app = create_app()
manager=Manager(app)



if __name__ == '__main__':
    manager.run()
```

在终端运行` python manage.py runserver `可以启动项目

# flask-sqlalchemy

操作数据库时只有orm和元素sql，flask-sqlalchemy是orm

```python
pip install flask-sqlalchemy
```

作用：将sqlalchemy相关的所有功能封到db=flask_sqlalchemy.SQLAlchemy()

`--init--`

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 包含SQLAlchemy相关的所有操作
# 第一SQLAlchemy是一个类，实例化这个类。
db = SQLAlchemy()


def create_app():
    from .views import account
    app = Flask(__name__)
    app.config.from_object("settings.DevelopmentConfig")
    app.register_blueprint(account.ac)
    # 第二执行这个方法！
    db.init_app(app)

    return app
```

`settings`

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/flasklianxi?charset=utf8"
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_POOL_RECYCLE = -1
SQLALCHEMY_TRACK_MODIFICATIONS=True
```

`flask3.models`

创建表

```python
from sqlalchemy import Column, Integer, UniqueConstraint, Index, DateTime, ForeignKey,String
from flask3 import db


class Users(db.Model):
    __tablename="users"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(32),nullable=False,unique=True)
```

在视图中操作表

```python
from flask3 import db
from flask3 import models

data=db.session.query(models.Users).all
print(data)

# 可以加上 db.session.remove()
```

可以编写离线脚本

```python
from flask3 import db
from flask3 import create_app

app=create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
    # 也可以查询。
    db.query
```

# flask-migrate

作用：帮助数据库迁移，依赖flask-script和flask-sqlalchemy

```undefined
pip install Flask-Migrate
```

django在写完orm后，需要用命令迁移数据，并在用命令创建数据库。flask-migrate就是flask也可以通过命令来创建数据库。



# 自定义组件

创建一个文件夹`exts`,在这个文件夹下写自定义的组件

`exts.auth`

```python
from flask import request,session,redirect

class Auth(object):

    def __init__(self,app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self,app):
        app.auth_manager = self

        self.app = app
        app.before_request(self.check_login)
        app.context_processor(self.context_processor)

    def check_login(self):
        """
        检查用户是否已经登录
        :return:
        """
        if request.path == '/login':
            return

        user = session.get('user')
        if not user:
            return redirect('/login')

    def context_processor(self):
        user = session.get('user')
        return dict(current_user=user)

    def login(self,data):
        """
        将用户登录信息，放入session
        :param data:
        :return:
        """
        session['user'] = data

    def logout(self):
        """
        将用户登录信息，放入session
        :param data:
        :return:
        """
        del session['user']
```

`__init__`

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 导入Auth
from flask3.exts.auth import Auth

# 包含SQLAlchemy相关的所有操作
db = SQLAlchemy()


def create_app():
    from .views import account
    from .views import home
    app = Flask(__name__)
    app.config.from_object("settings.DevelopmentConfig")
    app.register_blueprint(account.ac)
    app.register_blueprint(home.hm)
    db.init_app(app)
    # auth=auth.Auth()
    # 将app写入Auth中。
    Auth(app)
    return app
```

视图函数

```python
# current_app 在__init__中写入后，通过current_app来使用auth中的函数。
from flask import blueprints,render_template,request,session,redirect,current_app
from flask3 import models
from flask3 import db
ac = blueprints.Blueprint('ac',__name__)

@ac.route('/login',methods=['GET','POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')

        obj = db.session.query(models.Users).filter(models.Users.name==user,models.Users.pwd==pwd).first()
        db.session.remove()
        if not obj:
            return render_template('login.html',msg='用户名或密码错误')
		# 使用自定义组件
        current_app.auth_manager.login(user)
        return redirect('/index')


@ac.route('/logout')
def logout():
    print(current_app)
    current_app.auth_manager.logout()
    return redirect('/login')
```

# 多app应用

```python
#由于版本问题DispatcherMiddleware的导入有问题
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask

app01 = Flask('app01')
app02 = Flask('app02')

@app01.route('/index')
def index():
    return "app01"


@app02.route('/index')
def index2():
    return "app02"


app = DispatcherMiddleware(app01, {
    '/app01': app01,
    '/app02': app02,
})
#默认使用app01的路由，也就是访问 http://127.0.0.1:5000/index 返回app01
#当以app01开头时候使用app01的路由，也就是http://127.0.0.1:5000/app01/index 返回app01
#当以app02开头时候使用app02的路由，也就是http://127.0.0.1:5000/app02/index 返回app02

if __name__ == "__main__":
    run_simple('127.0.0.1', 5000, app)
```





# blinker

想看源码https://www.cnblogs.com/wupeiqi/p/8249576.html

信号

```
pip3 install blinker
```

```python
request_started = _signals.signal('request-started')                # 请求到来前执行
request_finished = _signals.signal('request-finished')              # 请求结束后执行
 
before_render_template = _signals.signal('before-render-template')  # 模板渲染前执行
template_rendered = _signals.signal('template-rendered')            # 模板渲染后执行
 
got_request_exception = _signals.signal('got-request-exception')    # 请求执行出现异常时执行
 
request_tearing_down = _signals.signal('request-tearing-down')      # 请求执行完毕后自动执行（无论成功与否）
appcontext_tearing_down = _signals.signal('appcontext-tearing-down')# 应用上下文执行完毕后自动执行（无论成功与否）
 
appcontext_pushed = _signals.signal('appcontext-pushed')            # 应用上下文push时执行
appcontext_popped = _signals.signal('appcontext-popped')            # 应用上下文pop时执行
message_flashed = _signals.signal('message-flashed')                # 调用flask在其中添加数据时，自动触发
```

## 自定义信号

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, current_app, flash, render_template
from flask.signals import _signals
 
app = Flask(import_name=__name__)
 
 
# 自定义信号
xxxxx = _signals.signal('xxxxx')
 
 
def func(sender, *args, **kwargs):
    print(sender)
 
# 自定义信号中注册函数
xxxxx.connect(func)
 
 
@app.route("/x")
def index():
    # 触发信号
    xxxxx.send('123123', k1='v1')
    return 'Index'
 
 
if __name__ == '__main__':
    app.run()
```

## 信号和before_request的区别

before_request可以控制请求是否可以继续往后执行

信号，在原来的基础上增加额外的操作和值

# 总结

手写flask的hello word

Flask和其他框架的区别

Flask内置组件:

- 配置
- 路由
- 视图
- 模板
- session
- 闪现
- 蓝图
- 中间件
- 特殊装饰器

Flask组件

- flask-session
    默认session放到签名的cookie中
    使用组件放到redis中
- flask-sqlalchemy
- flask-migrate
- flask-script
- blinker

公共组件(不止flask可以用，其他也可以用)

- wtforms

- dbutil
- SQLAlchemy

自定义组件

​	auth，参考的是flask-login

上下文管理

- 请求上下文

- app应用上下文

​	



为什么使用LocalStack对Local对象进行操作：

目的是想要将local中的值维护成一个栈，例如：在多app应用中编写离线脚本时，可以使用上， 
































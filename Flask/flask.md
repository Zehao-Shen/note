# flask

Flask是一个基于Python开发并且依赖jinja2模板和Werkzeug WSGI服务的一个微型框架，对于Werkzeug本质是Socket服务端，其用于接收http请求并对请求进行预处理，然后触发Flask框架，开发人员基于Flask框架提供的功能对请求进行相应的处理，并返回给用户，如果要返回给用户复杂的内容时，需要借助jinja2模板来实现对模板的处理，即：将模板和数据进行渲染，将渲染后的字符串返回给用户浏览器。

“微”(micro) 并不表示你需要把整个 Web 应用塞进单个 Python 文件（虽然确实可以 ），也不意味着 Flask 在功能上有所欠缺。微框架中的“微”意味着 Flask 旨在保持核心简单而易于扩展。Flask 不会替你做出太多决策——比如使用何种数据库。而那些 Flask 所选择的——比如使用何种模板引擎——则很容易替换。除此之外的一切都由可由你掌握。如此，Flask 可以与您珠联璧合。

默认情况下，Flask 不包含数据库抽象层、表单验证，或是其它任何已有多种库可以胜任的功能。然而，Flask 支持用扩展来给应用添加这些功能，如同是 Flask 本身实现的一样。众多的扩展提供了数据库集成、表单验证、上传处理、各种各样的开放认证技术等功能。Flask 也许是“微小”的，但它已准备好在需求繁杂的生产环境中投入使用。

官网: https://flask.palletsprojects.com/en/2.0.x/

官方文档: https://dormousehole.readthedocs.io/en/latest/index.html

# 下载

```
pip install falsk
```

**Flask常用第三方扩展包：**

- Flask-SQLAlchemy：操作数据库,ORM；
- Flask-script：终端脚本工具，脚手架； ( 淘汰，官方内置脚手架：Click)
- Flask-migrate：管理迁移数据库；
- Flask-Session：Session存储方式指定；
- Flask-Mail：邮件；
- Flask-Login：认证用户状态；（django内置Auth模块，用于实现用户登录退出，）
- Flask-OpenID：认证, OAuth；（三方授权，）
- Flask-RESTful：开发REST API的工具；
- Flask JSON-RPC:  开发json-rpc远程服务[过程]调用
- Flask-Bable：提供国际化和本地化支持，翻译；
- Flask-Moment：本地化日期和时间
- Flask-Admin：简单而可扩展的管理接口的框架
- Flask-Bootstrap：集成前端Twitter Bootstrap框架（前后端分离，除了admin站点，基本不用这玩意）
- Flask-WTF：表单生成模块；（前后端分离，除了admin站点，基本不用这玩意）
- Flask-Marshmallow：序列化（类似djangorestframework的序列化器）

可以通过  https://pypi.org/search/?c=Framework+%3A%3A+Flask 查看更多flask官方推荐的扩展

# 开始

```python
from flask import Flask

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
```

# 终端运行Flask项目

```py
#  如果要基于开发环境在终端启动项目，设置环境变量如下：
export FLASK_DEBUG=True
# 如果要基于生产环境在终端启动项目，设置环境变量如下：
# export FLASK_DEBUG=Flase

# 找到创建flask应用的模块路径，例如：manage.py
# 则ubuntu等Linux下的终端：
export FLASK_APP=manage.py  # 这是临时设置，如果有永久设置，可以通过/etc/profile保存
# 2. 在当前虚拟环境中，如果安装了flask模块，则可以使用全局命令flask run，即可运行flask项目
flask run # 采用默认的127.0.0.1 和 5000端口运行项目 
flask run --host=0.0.0.0 --port=8088 # 可以改绑定域名IP和端口
```

或者

```py
flask --app flask文件名字 run 
# 打开debug模式
flask --app flask文件名字 run --debug
```



# flask加载项目配置的三种方式

```py
# 1. 导入flask核心类
from flask import Flask

# 2. 初始化web应用程序的实例对象
app = Flask(__name__)

"""第一种：flask项目加载站点配置的方式"""
# app.config["配置项"] = 配置项值
# app.config["DEBUG"] = False

"""第二种：flask项目加载站点配置的方式"""
# app.config是整个flask项目默认的配置属性，里面包含了所有的可用配置项，配置项的属性名都是大写字母或大小字母+下划线组成
config = {
    "DEBUG": True
}
app.config.update(config)

# 4. 可以通过实例对象app提供的route路由装饰器，绑定视图与uri地址的关系
@app.route("/")
def index():
    return "<h1>hello flask</h1>"


if __name__ == '__main__':
    # 3. 运行flask提供的测试web服务器程序
    app.run(host="0.0.0.0", port=5000)
```

## 第三种

### 配置文件

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

```py
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

```py
# 导入
app.config.from_object("python类或类的路径")
app.config.from_object('pro_flask.settings.TestingConfig')
```

# 路由

```py
# 参数1：rule设置当前视图的路由地址，可以直接写路由地址
# 参数2：methods，设置当前视图的HTTP请求方法，允许一个或多个方法，不区分大小写
# 方式一
@app.route(rule="/index",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])  # 这个一样。
def index():
    return "hello word"
#方式二
def login():
    return "nihaoasasdasd"
app.add_url_rule('/login',view_func=login)
```

## 反向生成url

```py
from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route("/index/<string:nid>",methods=["GET","POST"],endpoint="n1")
def index(nid):
    print(url_for("n2"))   #/login   
    print(nid)
    return "hello word"
@app.route('/login',endpoint="n2")
def login():
    return "nihao"
```

## 接收任意路由参数

```py
@app.route("/goods/<cid>/<gid>")
def goods(gid, cid):
    print(gid, type(gid))  # 默认都是str
    print(cid, type(cid))
    return f"显示cid={cid},gid={gid}的商品信息"
```

## 接收限定类型参数

限定路由参数的类型，flask系统自带转换器编写在werkzeug/routing/converters.py文件中。底部可以看到以下字典：

```python
# converters用于对路由中的参数进行格式转换与类型限定的
DEFAULT_CONVERTERS: t.Mapping[str, t.Type[BaseConverter]] = {
    "default": UnicodeConverter, # 默认类型，也就是string
    "string": UnicodeConverter, # 字符串，不包含 /
    "any": AnyConverter,    # 任意类型
    "path": PathConverter,  # 也是字符串，但是包含了 /
    "int": IntegerConverter,
    "float": FloatConverter,
    "uuid": UUIDConverter,
}
```

系统自带的转换器具体使用方式在每种转换器的注释代码中有写，请留意每种转换器初始化的参数。

代码：

```py
@app.route("/goods/<float:cid>/<int:gid>")
def goods(gid, cid):
    print(gid, type(gid))  # 指定类型
    print(cid, type(cid))
    return f"显示cid={cid},gid={gid}的商品信息"
```

## 自定义路由参数转换器

**自定义正则**

具体实现步骤为：

- 导入转换器基类BaseConverter：在 Flask 中，所有的路由的匹配规则都是使用转换器对象进行记录
- 自定义转换器：自定义类继承于转换器基类BaseConverter
- 添加转换器到默认的转换器字典DEFAULT_CONVERTERS中
- 使用自定义转换器实现自定义匹配规则

代码实现

- 导入转换器基类

```python
from werkzeug.routing.converters import BaseConverter
```

- 自定义转换器

```py
class RegexConverter(BaseConverter):
    def __init__(self, map, *args, **kwargs):
        super().__init__(map, *args, **kwargs)
        self.regex = args[0]
```

- 添加转换器到默认的转换器字典中，并指定转换器使用时名字为: re

```python
"""
自定义路由转换[在实际项目开发中，我们会单独准备一个python文件来保存转换器的定义代码]
"""
from werkzeug.routing.converters import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self, map, *args, **kwargs):
        super().__init__(map, *args, **kwargs)
        self.regex = args[0]

app.url_map.converters["re"] = RegexConverter

@app.route("/sms/<re('1[3-9]\d{9}'):mobile>")
def sms(mobile):
    return f"发送短信给手机号：{mobile}的用户"

@app.route("/goods/<re('\d+'):id>")
def goods(id):
    return f"显示商品id={id}的信息"
```

代码：

```python
# 1. 导入flask核心类
from flask import Flask

# 2. 初始化web应用程序的实例对象
app = Flask(__name__)

# 开启debug模式
app.config["DEBUG"] = True

"""
自定义路由转换[在实际项目开发中，我们会单独准备一个python文件来保存转换器的定义代码]
"""
from werkzeug.routing.converters import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self, map, *args, **kwargs):
        super().__init__(map, *args, **kwargs)
        self.regex = args[0]

app.url_map.converters["re"] = RegexConverter

@app.route("/sms/<re('1[3-9]\d{9}'):mobile>")
def sms(mobile):
    return f"发送短信给手机号：{mobile}的用户"

@app.route("/goods/<re('\d+'):id>")
def goods(id):
    return f"显示商品id={id}的信息"

if __name__ == '__main__':
    # 3. 运行flask提供的测试web服务器程序
    app.run(host="0.0.0.0", port=5000)
```



# http的请求与响应

## flask的生命周期

客户端--->wsgi应用程序->全局钩子--> 路由 --> 视图 --> 路由---> 全局钩子 ---> wsgi应用程序---> 客户端



## 请求

文档: https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request

- **request**：flask中代表当前请求的 `request 对象`
- **作用**：在视图函数中取出本次客户端的请求数据
- **导入**：``from flask import request``
- **代码位置**：
- ​      代理类  from flask.app import request  ---> from flask.globals.request
- ​      源码类：from flask.wrappers.Request
- ​      基类：from werkzeug.wrappers import Request as RequestBase

request，常用的属性如下：



| 属性    | 说明                                                         | 类型               |
| ------- | ------------------------------------------------------------ | ------------------ |
| data    | 记录请求体的数据，并转换为字符串<br>只要是通过其他属性无法识别转换的请求体数据<br>最终都是保留到data属性中<br>例如：有些公司开发微信小程序，原生IOS或者安卓，这一类客户端有时候发送过来的数据就不一样是普通的表单，查询字符串或ajax | bytes类型          |
| form    | 记录请求中的html表单数据                                     | ImmutableMultiDict |
| args    | 记录请求中的查询字符串,也可以是query_string                  | ImmutableMultiDict |
| cookies | 记录请求中的cookie信息                                       | Dict               |
| headers | 记录请求中的请求头                                           | ImmutableMultiDict |
| method  | 记录请求使用的HTTP方法                                       | GET/POST           |
| url     | 记录请求的URL地址                                            | string             |
| files   | 记录请求上传的文件列表                                       | ImmutableMultiDict |
| json    | 记录ajax请求的json数据                                       | Dict               |

### request的常用用法

```py
from flask import Flask,request
from urllib.parse import urlparse,parse_qs

app = Flask(__name__)
# app.config["DEBUG"] = True
config={
    "DEBUG": True,
}

app.config.update(config)


 # 获取get请求url后面的参数，
@app.route("/sms")
def sms():
    # 获取get请求url后面的参数，
    # eg：http://127.0.0.1:5000/sms/1?user=shenzhao&age=22
    print(parse_qs(request.query_string.decode("utf-8")))
    # b'user=shenzhao,age=22'    
    # args会好用一点，query_string需要使用parse_qs转换成字典才可以拿到数据。
    print(request.args.get('age'))
    # ImmutableMultiDict([('user', 'shenzhao'), ('age', '22')])


    # 如果请求出现多个相同的名字http://127.0.0.1:5000/sms/1?user=shenzhao&age=22&age=23&age=88
    print(request.args.getlist('age'))
    # 输出 [22, 23, 88]
    return "数据接受从成功"

 # 拿到表单的数据
@app.route("/json",methods=["GET", "POST"])
def json_data():
     # 拿到表单的数据
    print(request.form.get("name"))      # 拿单个数据
    print(request.form.getlist("fav"))   # 拿多条数据
    print(request.form)
    # ImmutableMultiDict([('name', 'shenzhao'), ('age', '22'), ('fav', '123'), ('fav', '456'), ('fav', '6789')])
    return "数据接受从成功"
@app.route("/json2",methods=["GET", "POST"])

# 拿到ajax的数据
def json_data2():
    # 拿到ajax的数据
    print(request.is_json)   # is_json是用来判断是否是json
    print(request.json.get("name")) 
    # request.data 获取客户端请求体的的原始数据！
    import json
    print(json.loads(request.data.decode("utf-8")).get("age"),type(request.data.decode("utf-8"))) 
    return "数据接受从成功"


@app.route("/method_url", methods=["GET", "POST"])
def method_url():
    print(request.method)   
    print(request.url)
    print(request.path)
    # POST
    # http://127.0.0.1:5000/method_url
    # /method_url
     # 获取客户端的请求头中的相关数据
    print(request.user_agent)   # 用户访问服务器时使用的网络代理，一般就是浏览器标记信息，PostmanRuntime/7.26.10
    print(request.remote_addr)  # 客户端远程地址
    print(request.server)       # 服务端的端点，格式：(IP, 端口)
    return "请求成功" 

if __name__ == "__main__":

    app.run()


```

```py
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

flask默认支持2种响应方式:

数据响应: 默认响应html文本,也可以返回 JSON格式,或其他格式

页面响应: 重定向

​                  url_for  视图之间的跳转

响应的时候,flask也支持自定义http响应状态码

### 返回JSON数据

在 Flask 中可以直接使用 **jsonify** 生成一个 JSON 的响应

flask中返回json 数据,都是flask的jsonify方法返回就可以了，直接return只能返回字典格式的json数据。

```py
from flask import Flask, jsonify

app = Flask(__name__)

app.config.update({
    "DEBUG": True,
    "JSONIFY_PRETTYPRINT_REGULAR": False,
})


@app.route("/")
def index():
    # """返回json格式数据，返回json字典"""
    # data = {"name":"xiaoming","age":16}
    # return data

    # """返回json格式数据，返回各种json数据，包括列表"""
    data = [
        {"id": 1, "username": "liulaoshi", "age": 18},
        {"id": 2, "username": "liulaoshi", "age": 17},
        {"id": 3, "username": "liulaoshi", "age": 16},
        {"id": 4, "username": "小明", "age": 15},
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run()
```

### 返回html文本

```py
from flask import Flask,Response,make_response



app = Flask(__name__)
config={
    "DEBUG": True,
}

app.config.update(config)


@app.route('/')
def index():

    # return "<h1>hello</h1>", 200, {"company": "python"}
    return make_response("<h1>hello</h1>", 400, {"company": "python"})
    return Response("默认首页", 400, {"company": "python"})
    # 上面三个是一样的。 用第一个就行， 
    # 响应内容，状态码，向响应头中添加数据。


if __name__ == "__main__":

    app.run()
```

### 重定向

- 重定向跳转到自己写的页面和站外页面。

```py
from flask import Flask,redirect,url_for,request



app = Flask(__name__)
config={
    "DEBUG": True,
}

app.config.update(config)


@app.route('/login')
def loginasd():
    print("Welcome")
    return "跳转成功OK", 202

# 下面这三个都可的。
@app.route('/res')
def res():
	# 重定向，页面跳转到路由login
    return redirect("/login") 

@app.route('/index')
def index():
    url=url_for("loginasd")    # 是更具函数名字来确定的跳转。
    print(url)
    return redirect(url)
# 跳转到站外的页面
@app.route('/res')
def res():
    return redirect("https:www.baidu.com")
if __name__ == "__main__":

    app.run()
```

url_for可以传参数

```py
from flask import Flask,redirect,url_for,request



app = Flask(__name__)
config={
    "DEBUG": True,
}

app.config.update(config)

@app.route('/login/<int:mob>')
def loginasd(mob):
    print("Welcome")
    return "跳转成功OK", 202


@app.route('/index')
def index():
    url=url_for("loginasd",mob="123")    # 是更具函数名字来确定的跳转。
    print(url)    # /login/123
    return redirect(url)
if __name__ == "__main__":

    app.run()
```

### 自定义响应头

```py
from flask import Flask, redirect, url_for, make_response, Response

# 应用实例对象
app = Flask(__name__)

@app.route("/rep")
def rep():
    """常用以下写法"""
    return "ok", 201, {"Company":"python-35"}

    # """原理"""
    # response = make_response("ok", 201, {"Company": "python-35"})
    # return response
    #
    # """原理"""
    # response = Response("ok")
    # response.headers["Company"] = "oldboy" # 自定义响应头
    # response.status_code = 201             # 自定义响应状态码
    # return response

if __name__ == '__main__':
    # 启动项目的web应用程序
    app.run(host="0.0.0.0", port=5000, debug=True)
```

# http的会话控制

## cookie

Cookie是由服务器端生成，发送给客户端浏览器，浏览器会将Cookie的key/value保存，下次请求同一网站时就随着请求头自动发送该Cookie给服务器（前提是浏览器设置为启用cookie）。Cookie的key/value可以由服务器端自己定义。

使用场景: 登录状态, 浏览历史, 网站足迹,购物车 [不登录也可以使用购物车]



Cookie是存储在浏览器中的一段**纯文本信息**，建议不要存储敏感信息如密码，因为电脑上的浏览器可能被其它人使用

Cookie基于域名安全，不同域名的Cookie是不能互相访问的

如访问fuguang.com时向浏览器中写了Cookie信息，使用同一浏览器访问baidu.com时，无法访问到fuguang.com写的Cookie信息，只能获取到baidu.com的Cookie信息。

浏览器的同源策略针对cookie也有限制作用.

当浏览器请求某网站时，浏览器会自动将本网站下所有Cookie信息随着http请求头提交给服务器，所以在request中可以读取Cookie信息



![image-20211227102558619](D:\笔记\Flask\assets\image-20211227102558619.png)



![image-20211025185200357](D:\笔记\Flask\assets\image-20211025185200357-16996176836913.png)



#### 设置cookie

设置cookie需要通过flask的Response响应对象来进行设置,由响应对象会提供了方法set_cookie给我们可以快速设置cookie信息。

```python
@app.route("/set_cookie")
def set_cookie():
    """设置cookie，通过response传递到客户端进行保存"""
    response = make_response('默认首页')
    response.set_cookie('username', 'xiaoming')            # session会话期有效，关闭浏览器后当前cookie就会被删除
    response.set_cookie('user', 'xiaoming', max_age=30 )   # 指定有效时间，过期以后浏览器删除cookie，max_age=150秒
    return response
```



#### 获取cookie

```python
@app.route("/get_cookie")
def get_cookie():
    """获取来自客户端的cookie"""
    print(request.cookies)  # ImmutableMultiDict([])
    username = request.cookies.get('username')  # 没有值则返回None
    user = request.cookies.get('user')          # 没有值则返回None
    print(f"username={username},user={user}")   # username=xiaoming,user=xiaoming
    return "get cookie"
```



#### 删除cookie

```python
@app.route("/del_cookie")
def del_cookie():
    """删除cookie，重新设置cookie的时间，让浏览器自己根据有效期来删除"""
    response = make_response('del cookie')
    # 删除操作肯定是在浏览器完成的，所以我们重置下cookie名称的对饮有效时间为0，此时cookie的值已经不重要了。
    response.set_cookie('user', '', max_age=0)
    response.set_cookie('username', '', max_age=0)
    return response
```

## Session

对于敏感、重要的信息，建议要存储在服务器端，不能存储在浏览器中，如手机号、验证码等信息

在服务器端进行状态保持的方案就是`Session`

**Session依赖于Cookie**,session的ID一般默认通过cookie来保存到客户端。名字一般叫：sessionid

flask中的session需要加密,所以使用session之前必须配置SECRET_KEY选项,否则报错.

如果将来希望session的生命周期延长，可以通过修改cookie中的sessionID的有效期来完成配置。

![image-20211227105605185](D:\笔记\Flask\assets\image-20211227105605185.png)

注意：一般框架都是把session数据保存到服务端，但是，flask里面的session是基于token方式存储在客户端的，并没有安装传统的方式保存在服务端的文件中。

![image-20211227110308570](D:\笔记\Flask\assets\image-20211227110308570.png)

session的ID存在有效期的，默认是**会话期**，会话结束了，session_id就废弃了。

**必须设置SECRET_KEY否则会抱错**

```
RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
```

#### 设置session

```python
@app.route("/set_session")
def set_session():
    """设置session"""
    session['username'] = 'xiaoming'
    session['info'] = {
        "name": "xiaohong",
        "age": 16,
    }
    return "set_session"
```

可以通过客户端浏览器中的sessionid观察，其实默认情况下，flask中的session数据会被加密保存到cookie中的。当然，将来，我们可以采用flask-session第三方模块把数据转存到其他的存储设备，例如：redis或者mysql中。

#### 获取session

```python
@app.route("/get_session")
def get_session():
    """获取session"""
    print(session.get('username'))
    print(session.get('info'))
    return "get session"
```

在cookie中可以看到加密的session

```py
@app.route('/register')
def register():
    print("request.cookies",request.cookies) 
    print("Welcome")
    print("session",session)    # 拿到所以的session,
    response=Response("ok", 200)
    username=session.get("username")
    print(username) 
    return response

"""
有本身的cookie和加密的session
request.cookies ImmutableMultiDict([('username', 'shenzhao'), ('session', '.eJyrVspLzE2Nz0xRsoo21DHSMdYx0THVMdMx17HQsdQxNIjVUSotTi0CKzCEsEEalKyUijNS86pSMxLzlWoBpHkUnw.ZU4jQw.oLQBszuNc7HZrsOqiF8niJot9NQ')])
"""

```

#### 删除session

```python
@app.route("/del_session")
def del_session():
    """删除session，键如果不存在，则会抛出异常，所以删除之前需要判断键是否存在。"""
    if "username" in session:
        session.pop("username")
    if "info" in session:
        session.pop("info")
    return "del_session"
```

使用过程中，session是依赖于Cookie的，所以当cookie在客户端被删除时，对应的session就无法被使用了。

# 请求全局钩子

此处的全局钩子，其实就是类似django里面的中间件。 也就是只要调用或者注册了，在http请求响应中是必然执行的。

在客户端和服务器交互的过程中，有些准备工作或扫尾工作需要处理，比如：

- 在项目运行开始时，建立数据库连接，或创建连接池；
- 在客户端请求开始时，根据需求进行身份识别，权限校验；
- 在请求结束视图返回数据时，指定转换数据的格式，或者记录操作日志；

为了让每个视图函数避免编写重复功能的代码，Flask提供了通用设置的功能，即请求钩子。

请求钩子是**通过装饰器的形式**实现，Flask支持如下四种请求钩子（注意：钩子的装饰器名字是固定)：

- before_first_request

    - 在处理==第一个==请求前执行[项目刚运行第一次被客户端请求时执行的钩子]

- before_request

    - 在每一次请求前执行[项目运行后，每一次接收到客户端的request请求都会执行一次]
    - 如果在某修饰的函数中返回了一个响应，视图函数将不再被调用

- after_request

    - 如果没有抛出错误，在每次请求后执行
    - 接受一个参数：视图函数作出的响应
    - 在此函数中可以对响应值在返回之前做最后一步修改处理
    - 需要将参数中的响应在此参数中进行返回

- teardown_request：

    - 在每一次请求后执行
    - 接受一个参数：错误信息，如果有相关错误抛出
    - falsk低版本需要设置flask的配置DEBUG=False，现在3.0版本不需要配置配置DEBUG=False，teardown_request也会接受到异常对象。

    

    代码

    ```py
    
    from flask import Flask
    
    
    app = Flask(__name__)
    
    # def before_first_request():
    
    #     print("before_first_request")
    
    # app.before_first_request_funcs.append(before_first_request)
    
    # 这个函数问题，版本
    @app.before_request
    def before_request():
        """
        before_request不能有return。否则会出现bug。
        """
            """
        这个钩子会在每次客户端访问视图的时候执行
        # 可以在请求之前进行用户的身份识别，以及对于本次访问的用户权限等进行判断。..
        """
        print("----before_request----")
        print("每一次接收到客户端请求时,执行这个钩子方法")
        print("一般可以用来判断权限,或者转换路由参数或者预处理客户端请求的数据")
        print("11111111.before_request")
    
    @app.after_request
    def after_request(response):
        print("222222222.after_request")
        print("----after_request----")
        print("在处理请求以后,执行这个钩子方法")
        print("一般可以用于记录会员/管理员的操作历史,浏览历史,清理收尾的工作")
        # 向相应头添加数据。
        response.headers["Content-Type"] = "application/json" 
        # 修改Content-Type
        response.headers["Company"] = "python.Edu..."
        return response
    
    @app.teardown_request
    def teardown_request(exc):
         print("----teardown_request----")
         print("在每一次请求以后,执行这个钩子方法")
         print("如果有异常错误,则会传递错误异常对象到当前方法的参数中")
        # 异常信息就会被传递到exc中，我们可以记录异常信息到日志文件中
        print(f"错误提示：{exc}")  # 异常提示
    @app.route("/")
    def index():
        print("333333333.访问index")
        # 1/0用于验证@app.teardown_request的代码。
        return "<h1>hello flask</h1>"
    
    
    if __name__ == '__main__':
        # 3. 运行flask提供的测试web服务器程序
        app.run()
    ```

    执行效果：

    ```py
    """
    先执行before_request函数，在执行视图，最后是after_request函数
    没有错误，@app.teardown_request中的exc是None
    """
    
    11111111.before_request
    333333333.访问index
    222222222.after_request
    错误提示：None
    ```

    将实列代码中的1/0执行了。

    ```py
    """
    代码中有错误，就不会执行after_request，并且会打印错误信息。
    """
    11111111.before_request
    333333333.访问index
    错误提示：division by zero
    ```


# 异常抛出和捕获异常

## 主动抛出HTTP异常

- abort 方法

    - 抛出一个给定状态代码的 HTTPException 或者 指定响应，例如想要用一个页面未找到异常来终止请求，你可以调用 abort(404)

- 参数：

    - code – HTTP的错误状态码

    ```py
    from flask import Flask,abort,request
    app = Flask(import_name=__name__)
    
    
    # 配置类
    class Config(object):
        DEBUG = True     # 开启调试模式
    
    # 加载配置
    app.config.from_object(Config)
    
    
    @app.route("/")
    def index():
        # try:
        #     1/0
        # except:
        #     abort(500)
    
        username = request.args.get("username")
        if username is None:
            abort(400)
    
        return "ok"
    
    if __name__ == '__main__':
        app.run()
    
    ```

    abort，只能抛出 HTTP 协议的错误状态码，一般用于权限等页面上错误的展示提示.

    abort 在有些前后端分离的项目里面不会被使用，往往在业务错误的时候使用raise进行抛出错误类型，而不是抛出http异常。

## 捕获错误

- app.errorhandler 装饰器
    - 注册一个错误处理程序，当程序抛出指定错误状态码的时候，就会调用该装饰器所装饰的方法
- 参数：
    - code_or_exception – HTTP的错误状态码或指定异常
- 例如统一处理状态码为500的错误给用户友好的提示：

```py
@app.errorhandler(500)
def internal_server_error(exc):
    return '服务器搬家了'
```

- 捕获指定异常类型

```py
@app.errorhandler(接受自定义错误)
def zero_division_error(exc):
    return '除数不能为0'
```

代码，也可以捕获系统抛出的错误，

```py
from flask import Flask, request, abort

# 应用实例对象
app = Flask(__name__)

class APIError(Exception):
    # 继承Exception类
    pass

"""异常抛出"""
@app.route("/")
def index():
    username = request.args.get("user")
    if username is None:
        abort(400)
    if username != "xiaoming":
        raise APIError
       # raise APIError("网络请求出错")
    return "ok"


@app.errorhandler(400)
def internal_server_error(exc):
    print(11111111,exc.code)    # 错误信息  
    print(dir(exc.args))
    return {
        "errno": 400,
        "errmsg": "参数有误！",
    }


@app.errorhandler(APIError)
def api_error(exc):
    
    return {
        "errno": 500,
        "errmsg": "接口访问有误！",
        # "errmsg": f"{exc}",  #这个exc就是{网络请求出错}
    }


if __name__ == '__main__':
    # 启动项目的web应用程序
    app.run(host="0.0.0.0", port=5000, debug=True)

```

# context

执行上下文：即语境，语意，在程序中可以理解为在代码执行到某一行时，根据之前代码所做的操作以及下文即将要执行的逻辑，可以决定在当前时刻下可以使用到的变量，或者可以完成的事情。

Flask中提供的执行上下文对象：相当于一个容器，保存了 Flask 程序运行过程中的一些信息[变量、函数、类与对象等信息]。

Flask中有两种上下文，请求上下文(request context)和应用上下文(application context)。

1. *application* 指的就是当你调用`app = Flask(__name__)`创建的这个对象`app`；
2. *request* 指的是每次`http`请求发生时，`WSGI server`(比如gunicorn/uwsgi)调用`Flask.__call__()`之后，在`Flask`对象内部创建的`Request`对象；
3. *application* 表示用于响应WSGI请求的应用本身，*request* 表示服务端每次响应客户单的http请求；
4. *application*的生命周期大于*request*，一个*application*存活期间，可能发生多次http请求，所以也就会有多个*request*

## 请求上下文(request context)

思考：在视图函数中，如何取到当前请求的相关数据？比如：请求地址，请求方式，cookie等等

在 flask 中，可以直接在视图函数中使用 **request** 这个对象进行获取相关数据，而 **request** 就是请求上下文提供的对象，保存了当前本次请求的相关数据，请求上下文提供的对象有：request、session

所以每次客户端不同的请求，得到的request和session的对象都是同一个，但是内部的数据都是不一样的。

- request
    - 封装了HTTP请求的内容，针对的是http请求。举例：user = request.args.get('user')，获取的是get请求的参数。
- session
    - 用来记录请求会话中的信息，针对的是用户信息。举例：session['name'] = user.id，可以记录用户的状态信息。还可以通过session.get('name')获取用户的状态信息。

**请求上下文提供的变量/属性/方法/函数/类与对象，只能在视图中或者被视图调用的地方使用**

```py
from flask import Flask, request, session


app = Flask(__name__)
config={
    "SERVER_KEY": "123123",
}

app.config.update(config)

@app.route('/')
def index():
    print(request)
    print(session)
    """
    输出
    Request 'http://127.0.0.1:5000/?user=shenzehao' [GET]>
	<NullSession {}>
    """
    return "ok"


if __name__ == '__main__':
    # print(request) # 会报错 ，写在这里,就表示超出了用户请求和响应流程之外的地方了.会报错.
    app.run(host="0.0.0.0", port=5000, debug=True)

```

## 应用上下文(application context)

它的字面意思是 应用上下文，但它不是一直存在的，它只是request context 中操作当前falsk应用对象 app 的代理对象，就是所谓本地代理(local proxy)。它的作用主要是帮助 request 获取当前的flask应用相关的信息，它是伴 request 而生，随 request 而灭的。

应用上下文提供的对象有：current_app，g

### current_app

应用程序上下文,用于存储flask应用实例对象中的变量，可以通过current_app.name打印当前app的名称，也可以在current_app中存储一些变量，例如：

- 应用的启动脚本是哪个文件，启动时指定了哪些参数
- 加载了哪些配置文件，导入了哪些配置
- 连接了哪个数据库
- 有哪些可以调用的工具类、常量
- 当前flask应用在哪个机器上，哪个IP上运行，内存多大

```py
from flask import Flask,request,session,current_app,g

# 初始化
app = Flask(import_name=__name__)

# 声明和加载配置
class Config():
    DEBUG = True
app.config.from_object(Config)

# 编写路由视图
@app.route(rule='/')
def index():
    # 应用上下文提供给我们使用的变量，也是只能在视图或者被视图调用的地方进行使用，
    # 但是应用上下文的所有数据来源于于app，每个视图中的应用上下文基本一样
    print(current_app.config)   # 获取当前项目的所有配置信息
    print(current_app.url_map)  # 获取当前项目的所有路由信息
    print(current_app==app)     # True这两个是一样的，
    #app是用户自己定义的， 无论用户将app换成其他名字，current_app都是用户定义后的。
	"""
	输出
	current_app.config这个输出太多了，
	<Rule '/' (GET, OPTIONS, HEAD) -> index>])
	True 
	"""
    return "<h1>hello world!</h1>"

if __name__ == '__main__':
        # 默认情况下，应用上下文提供的对象，也只能在客户端的请求与响应阶段进行调用。
    # 但是工作中往往，需要在请求响应之外，调用服务端信息，此时，就必须要在请求响应以外的地方调用current_app
    with app2.app_context():
        print(current_app)
    app.run(host="0.0.0.0")
```

### g变量

g 作为 flask 程序全局的一个临时变量,充当者中间媒介的作用,我们可以通过它传递一些数据，g 保存的是当前请求的全局变量，不同的请求会有不同的全局变量，通过不同的thread id区别

```py
g.name='abc' # name是举例，实际要保存什么数据到g变量中，可以根据业务而定，你可以任意的数据进去
```

**注意：不同的请求，会有不同的全局变量g**

```py
from flask import Flask,request,session,current_app,g

# 初始化
app = Flask(import_name=__name__)

# 声明和加载配置
class Config():
    DEBUG = True
app.config.from_object(Config)

@app.before_request
def before_request():
    g.name = "root"

# 编写路由视图
@app.route(rule='/')
def index():
    # 请求上下文提供的变量/属性/方法/函数/类与对象，只能在视图中或者被视图调用的地方使用
    # 请求上下文里面信息来源于每次客户端的请求，所以每个视图中请求上下文的信息都不一样
    # print(session)

    # 应用上下文提供给我们使用的变量，也是只能在视图或者被视图调用的地方进行使用，
    # 但是应用上下文的所有数据来源于于app，每个视图中的应用上下文基本一样
    print(current_app.config)   # 获取当前项目的所有配置信息
    print(current_app.url_map)  # 获取当前项目的所有路由信息
    index2()
    index3()
    return "ok!"


def index2():
    print(g.name)

def index3():
    print(g.name)


if __name__ == '__main__':
    # 默认情况下，应用上下文提供的对象，也只能在客户端的请求与响应阶段进行调用。
    # 但是工作中往往，需要在请求响应之外，调用服务端信息，此时，就必须要在请求响应以外的地方调用current_app
    # 例如：回头使用celery实现异步任务或是定时任务，那么如果任务里面需要操作数据，则必须调用项目配置，那么就一定要使用current_app
    with app2.app_context():
        print(current_app)
        print(g)
    app2.run()
```

## 两者区别：

- 请求上下文：保存了客户端和服务器交互的数据，一般来自于客户端。

- 应用上下文：flask 应用程序运行过程中，保存的一些配置信息，比如路由列表，程序名、数据库连接、应用信息等

    应用上下文提供的对象，可以直接在请求上下文中使用，但是如果在请求上下文之外调用，则需要使用

    `with app.app_context()`创建一个应用上下文环境才能调用。

# 终端脚本命令

## flask2.0的终端命令使用

flask0.11.0版本以后，flask内置了一个Click模块，这个模块是终端命令模块，可以让我们直接通过Click的装饰器，编写和运行一些终端命令。在flask2.0版本已经不能兼容flask-script模块了，所以需要改成使用Click模块来运行和自定义管理终端命令了。

文档地址：https://dormousehole.readthedocs.io/en/latest/cli.html#id10

click文档：https://click.palletsprojects.com/en/8.0.x/

安装了flask2.0以后，当前项目所在的python环境就提供了一个全局的flask命令，这个flask命令是Click提供的。

```py
使用这个前需要
# 设置flask项目的启动脚本位置，例如我们现在的脚本叫manage.py
export FLASK_APP=manage.py
```



```py
import click
from flask import Flask, views

app = Flask(__name__)
# 配置
app.config.update({
    "DEBUG": False,
})


# 自定义终端命令
@app.cli.command("faker")                                               
# 假设这个用于生成测试数据
@click.argument("data", default="user")  
# @click.argument() 可以写多个
# data表示生成数据的类型[参数argument是命令调用时的必填参数]
@click.option('-n', 'number', type=int, default=1, help='生成的数据量.')  
# @click.option() 可以写多个
# num表示测试数据的生成数量[选项option是命令调用时的可选参数]
def faker_command(data, number):
    """添加测试信息"""
    print("添加测试信息")
    print(f"数据类型：data={data}")
    print(f"生成数量：number={number}")


@app.route("/")
def index():
    return "ok"


if __name__ == '__main__':
    app.run()
    
"""
flask faker --help
flask faker -n10 user
flask faker user
"""


```

`@click.argument()  `是位置参数，终端直接写就ok

`@click.option()`是选项参数，终端输入命令是需要将选项添加

eg：上面的选项参数`flask faker -n10 user`，必须写`-n`，在写后面的参数否则会报错。

# 原生SQLAlchemy

`sql.py`

```py
from sqlalchemy import create_engine   # 驱动引擎
from sqlalchemy.ext.declarative import declarative_base # 数据库基类
from sqlalchemy import Column, Integer, String, Boolean, Numeric, Text # 字段、整型
from sqlalchemy.orm import sessionmaker  # 连接会话

engine = create_engine(
    # 连接数据库的URL
    url="mysql+pymysql://root:123@127.0.0.1:3306/flask_orm?charset=utf8mb4",  # 如果底层驱动是pymysql
    # url="mysql://root:123@127.0.0.1:3306/students?charset=utf8mb4",    # 如果底层驱动是MysqlDB
    echo=True, # 当设置为True时会将orm语句转化为sql语句打印，一般debug的时候可用
    pool_size=4, # 连接池的大小，默认为5个，设置为0时表示连接无限制
    pool_recycle=60*30 # 设置时间以限制数据库多久没连接自动断开
)

# 创建数据库连接
DbSession = sessionmaker(bind=engine)
session = DbSession()

# 创建数据基类
Model = declarative_base()

```

导入上的代码，实现增删改查

```py
import sql

class Student(sql.Model):
    __tablename__ = "tb_student"
    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(255))
    sex  = sql.Column(sql.Boolean)
    age  = sql.Column(sql.Integer)
    # 在python中的class是关键字，所以我们不能使用class为字段名，但是我们却需要class这个名字，就下面的写法，会将class映射成表的字段名。
    class_name = sql.Column("class", sql.String(255),)
    description = sql.Column(sql.Text)
    is_delete = sql.Column(sql.Boolean, nullable=True, default=False)

    def __repr__(self):  # 在sqlalchemy中使用repr,在django中使用str
        return f"{self.name},{self.__class__.__name__}"

if __name__ == '__main__':
    # 如果没有提前声明模型中的数据表，则可以采用以下代码生成数据表，
    # 如果数据库中已经声明了有数据表，则不会继续生成
    sql.Model.metadata.create_all(sql.engine)
    
    # 拿到Student类中的表的所有数据
    # da_list=sql.session.query(Student).all()
    # for i in da_list:
    #     print(i.name,i.age)
    
    # 查询单独的一个，按照id查询。
    # da_list=sql.session.query(Student).get(10)
    # if da_list:
        # print(i.name,i.age)
    # print("没有这个人")
    
    # 按照条件查询
    # da_list=sql.session.query(Student).filter(Student.class_name==305).first()
    # print(da_list.age)
    
    # 添加数据  
    # student = Student(
        #  name="xiaohua",
        #  class_name="305",
        #  sex=False,
        #  age=18,
        #  description="美美的..",
    #  )
    
    # 先添加在添加数据
    # sql.session.add(student)
    # sql.session.commit()
    
    # 添加多条数据
    # student_list=[
    #     Student(name="xiaoming", sex=False, age=18, description="挺好的"),
    #     Student(name="xiaolan", sex=True, age=19, description="挺好好的"),
    # ]
    # sql.session.add_all(student_list)
    # sql.session.commit()
    
    # 更新数据
    # da_list=sql.session.query(Student).filter_by(name="shenzehao").first()
    # print(da_list)
    # if da_list:
    #     da_list.class_name="202"
    #     da_list.name="shen"
    #     sql.session.commit()
    # else:
    #     print("没有这个人")
    
    # 更新多条数据
    # sql.session.query(Student).filter(Student.class_name=="305").update({Student.age:Student.age+1})
    # sql.session.commit()

    # 删除数据
    # da_list=sql.session.query(Student).get(2)
    # print(da_list)
    # sql.session.delete(da_list)
    # sql.session.commit()
    
    # 删除多条数据
    # da_list=sql.session.query(Student).filter(Student.id<2).delete()
    # sql.session.commit()

    
        # 原生SQL语句
    # 读
    cursor = db.session.execute('select * from tb_student')
    # 一条
    # data = cursor.fetchone()
    # print(data)

    # 多条
    # data_list = cursor.fetchall()
    # print(data_list)

    # 写[添加、删除、修改]
    cursor = db.session.execute(
        'insert into tb_student(name, class, age, sex, description) values(:name, :class, :age, :sex, :description)',
        params={
            "name": "xiaohong",
            "class": "307",
            "age": 19,
            "sex": 0,
            "description": ".....",
        })
    db.session.commit()
    print(cursor.lastrowid) # 获取最后添加的主键ID
```

# flask_sqlalchemy

SQLAlchemy：https://docs.sqlalchemy.org/en/14/

中文文档：https://www.osgeo.cn/sqlalchemy/orm/index.html

flask-SQLAlchemy：https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

### 常用的SQLAlchemy字段类型

| 模型字段类型名   | python中数据类型  | 说明                                                         |
| :--------------- | :---------------- | :----------------------------------------------------------- |
| **Integer**      | int               | 普通整数，一般是32位                                         |
| **SmallInteger** | int               | 取值范围小的整数，一般是16位                                 |
| BigInteger       | int               | 不限制精度的整数                                             |
| Float            | float             | 浮点数                                                       |
| **Numeric**      | decimal.Decimal   | 普通数值，一般是32位                                         |
| **String**       | str               | 变长字符串                                                   |
| **Text**         | str               | 变长字符串，对较长或不限长度的字符串做了优化                 |
| Unicode          | unicode           | 变长Unicode字符串                                            |
| UnicodeText      | unicode           | 变长Unicode字符串，对较长或不限长度的字符串做了优化          |
| **Boolean**      | bool              | 布尔值                                                       |
| **DateTime**     | datetime.datetime | 日期和时间                                                   |
| Date             | datetime.date     | 日期                                                         |
| Time             | datetime.time     | 时间                                                         |
| LargeBinary      | bytes             | 二进制文件内容                                               |
| **Enum**         | enum.Enum         | 枚举类型，相当于django的choices，但是功能没有choices那么强大 |



### 常用的SQLAlchemy列约束选项

| 选项名      | 说明                                                        |
| :---------- | :---------------------------------------------------------- |
| primary_key | 如果为True，代表当前数据表的主键                            |
| unique      | 如果为True，为这列创建唯一 索引，代表这列不允许出现重复的值 |
| index       | 如果为True，为这列创建普通索引，提高查询效率                |
| nullable    | 如果为True，允许有空值，如果为False，不允许有空值           |
| default     | 为这列定义默认值                                            |

## 数据库基本操作

- 在SQLAlchemy中，添加、修改、删除操作，均由数据库会话(sessionSM)管理。
    - 会话用 db.session 表示。在准备把数据写入数据库前，要先将数据添加到会话中然后调用 db.commit() 方法提交会话。
- 在SQLAlchemy 中，查询操作是通过 query 对象操作数据。
    - 最基本的查询是返回表中所有数据，也可以通过filter过滤器进行更精确的数据库查询。

需要先创建库

```py
create database 库名字 charset=utf8mb4;
```

flask_sqlalchemy的配置

```py
class config(object):
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = True

app.config.from_object(config)
"""模型类定义"""
db = SQLAlchemy(app=app)
# 等同于
# db = SQLAlchemy()
# db.init_app(app) # 加载配置并完成初始化过程
```

## 模型类定义

## 创建表

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
class Config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    #使用的mysqldb
    #SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    #使用的pymysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = True


app.config.from_object(Config)


"""模型类定义"""
db = SQLAlchemy(app=app)
# 等同于
# db = SQLAlchemy()
# db.init_app(app) # 加载配置并完成初始化过程

class Student(db.Model):
    """学生信息模型"""
    # 声明与当前模型绑定的数据表名称
    __tablename__ = "tb_student"
    """
    # 企业中，往往大部分的公司会出现以下2种不同的数据库开发情况。
    # 1. 企业中有DBA，DBA会提前创建数据库和项目中具体业务的数据表。
         也就是说我们不需要自己手动建库建表，只需要根据数据库表结构，使用python声明对应的模型与之匹配，就可以操作数据库了。
    # 2. 企业没有DBA，比较坑爹：
    #    2.1 开发人员，自己手撸SQL语句，手动建库建表。
    #    2.2 开发人员，编写模型，使用数据迁移，手动建库和数据迁移建表。
    
    # 原生SQL语句
    create table db_student(
      id int primary key auto_increment comment "主键",
      name varchar(15) comment "姓名",
      age smallint comment "年龄",
      sex tinyint default 1 comment "性别",
      email varchar(128) comment "邮箱地址",
      money NUMERIC(10,2) default 0.0 comment "钱包",
      key (name),
      unique key (email)
    );
    # 字段根据SQL语句来声明
    """
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), unique=True, comment="邮箱地址")
    money = db.Column(db.Numeric(10,2), default=0.0, comment="钱包")

    def __repr__(self): # 相当于django的__str__
        return f"{self.name}<{self.__class__.__name__}>"


# 所有的模型必须直接或间接继承于db.Model
class Course(db.Model):
    """课程数据模型"""
    __tablename__ = "db_course"
    """
    # 原生SQL语句
    create table db_course (
        id int primary key auto_increment comment "主键",
        name varchar(64) comment "课程",
        price NUMERIC(7,2) comment "价格",
        unique (name)
    );
    # 字段根据SQL语句来声明
    """
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(64), unique=True, comment="课程")
    price = db.Column(db.Numeric(7, 2), comment="价格")
    # repr()方法类似于django的__str__，用于打印模型对象时显示的字符串信息
    def __repr__(self):
        return f"{self.name}<{self.__class__.__name__}>"

class Teacher(db.Model):
    """老师数据模型"""
    __tablename__ = "db_teacher"
    """
    # 原生SQL语句
    create table db_teacher (
        id int primary key auto_increment comment "主键",
        name varchar(64) comment "姓名",
        option enum("讲师", "助教", "班主任") comment "职位",
        unique (`name`)
    );
    # 字段根据SQL语句来声明
    """
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(64), unique=True, comment="姓名")
    option = db.Column(db.Enum("讲师", "助教", "班主任"), default="讲师")

    def __repr__(self):
        return f"{self.name}<{self.__class__.__name__}>"

@app.route("/")
def index():
    return "ok"

if __name__ == '__main__':
    app.run()
```

运行上面的代码是不会在数据库中创建表的，

需要执行` db.create_all()`，但是这个命令只能在视图运行，需要在视图外运行需要下面的代码

```py
if __name__ == '__main__':
    	with app.app_context():
        # create_all()方法执行的时候，需要放在模型的后面
        # 检测数据库中是否存在和模型匹配的数据表。
        # 如果没有，则根据模型转换的建表语句进行建表。
        # 如果找到，则不会进行额外处理
        db.create_all()
        app.run()
```

## 数据表操作

### 创建和删除表

#### 创建表

```py
# 在视图内调用：
@app.route("/create")
def create_table():
    db.create_all() # 为项目中被识别的所有模型创建数据表
    return "ok"


# 在视图以外的地方调用：
	with app.app_context():
        # create_all()方法执行的时候，需要放在模型的后面
        # 检测数据库中是否存在和模型匹配的数据表。
        # 如果没有，则根据模型转换的建表语句进行建表。
        # 如果找到，则不会进行额外处理
        db.create_all()
```

#### 删除表

```py
# 在视图内调用：
@app.route("/drop")
def drop_table():
    db.drop_all()   # 为项目中被识别的所有模型删除数据表
    return "ok"


# 在视图以外的地方调用：
    with app.app_context():
        db.drop_all()  # 慎用，很给力的！！这表示删除数据库中所有模型对应的表。
```



### 添加数据

```py
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
class config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = True

app.config.from_object(config)
db = SQLAlchemy(app=app)



class Student(db.Model):
    __tablename__ = "tb_student"
    id=db.Column(db.Integer, primary_key=True,comment="主键")
    name=db.Column(db.String(64), nullable=False,comment="姓名")
    age=db.Column(db.Integer, nullable=False,comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), unique=True, comment="邮箱地址")

class Teacher(db.Model):
    __tablename__ = "tb_teacher"
    id=db.Column(db.Integer, primary_key=True,comment="主键")
    name=db.Column(db.String(64), nullable=False,comment="姓名")
    age=db.Column(db.Integer, nullable=False,comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), unique=True, comment="邮箱地址")
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"
@app.route('/index', methods=['GET'])
def index():
    db.create_all()
    return "ok"


@app.route('/add')
def data_add():
    # 添加一条数据
    student = Student(name="小明", age=17, email="xiaoming@qq.com") # 实例化模型对象
    db.session.add(student) # 把模型对象添加数据库session会话对象中。db.session是SQLAlchemy中内置的会话管理对象sessionSM的成员
    db.session.commit()     # 提交会话
    # 添加多条数据
    student_list = [
        Student(name='wang', email='wang@163.com', age=20),
        Student(name='zhang', email='zhang@189.com', age=21),
        Student(name='chen', email='chen@126.com', age=19),
        Student(name='zhou', email='zhou@163.com', age=18),
        Student(name='tang', email='tang@163.com', age=16),
        Student(name='wu', email='wu@gmail.com', age=20),
        Student(name='qian', email='qian@gmail.com', age=21),
        Student(name='liu', email='liu@163.com', age=21),
        Student(name='li', email='li@163.com', age=18),
        Student(name='sun', email='sun@163.com', age=17),
        ]
    db.session.add_all(student_list)
    db.session.commit()
    return "添加成功"


if __name__ == '__main__':

        app.run()
```

### 修改数据

```py
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
class config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = True

app.config.from_object(config)
db = SQLAlchemy(app=app)



class Student(db.Model):
    __tablename__ = "tb_student"
    id=db.Column(db.Integer, primary_key=True,comment="主键")
    name=db.Column(db.String(64), nullable=False,comment="姓名")
    age=db.Column(db.Integer, nullable=False,comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), unique=True, comment="邮箱地址")

class Teacher(db.Model):
    __tablename__ = "tb_teacher"
    id=db.Column(db.Integer, primary_key=True,comment="主键")
    name=db.Column(db.String(64), nullable=False,comment="姓名")
    age=db.Column(db.Integer, nullable=False,comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), unique=True, comment="邮箱地址")
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"


@app.route('/updata')
def data_add():
    student=Student.query.filter(Student.id==2).update({"name":"shenzehao123123123123"})
    db.session.commit()
    return "修改成功"

@app.route('/updata2')
def data_add2():
    # 字段引用[利用当前一条数据的字典值进行辅助操作,实现类似django里面F函数的效果]
    # 每次自增100
    student=Student.query.filter(Student.name=="zhang").update({"age":Student.age+1})
    db.session.commit()
    return "修改成功"

@app.route("/update4")
def update4():
    # 字段引用[利用当前一条数据的字典值进行辅助操作,实现类似django里面F函数的效果]
    # 在原有money的基础上按age补贴1000*age
    Student.query.filter(Student.name == "zhang").update({"age": Student.age + 10 * Student.age})
    db.session.commit()
    return "ok"

if __name__ == '__main__':

        app.run()
        
        
 # 另外
```

### 删除数据

```py
# 方法1[先查询后删除，2条语句完成删除操作]
# 先查询出来
student = Student.query.first()
print(student)
# 再进行删除
db.session.delete(student)
db.session.commit()

# 方法2【1条语句完成删除操作，性能更好更高效】     
# 类似乐观锁，在数据改动时添加条件并判断条件成立以后才进行数据操作，这种用法就是乐观锁
Student.query.filter(Student.id == 5).delete()
db.session.commit()


"""
悲观锁，是属于数据库中的一种锁机制，但是乐观锁并非真正的数据库锁。
2种锁都是数据库在应对并发操作时，防止出现资源抢夺的，基于不同人生观所实现2种解决方案。
悲观锁的基本使用：
    >>> 数据库终端开始

    begin;  -- 开启事务
    select * from db_student where student_id = 5 for update; -- 添加一把更新锁【悲观锁】
    ....    -- 在事务提交之前，任何第三方连接都不能修改 student_id = 5这条数据 
    commit; -- 提交事务

    <<< 数据库终端开始

悲观锁的问题：
1. 提前锁定数据，形成串行化，形成阻塞，不利于性能发挥，不适用高并发场景。
2. 悲观锁只能保证数据的一致性，不能保证脏数据的出现

乐观锁的出现就是为了解决悲观锁的问题。
举例：双11活动，商城里面id=5的商品的库存=10了，现在我们要基于乐观锁和悲观锁来解决下单过程中，出现的资源抢夺现象，避免出现超卖（商品数量不能为负数）。

乐观锁：
---> begin;  开启事务
---> 先查看库存，记录当前库存 num=10
---> 进行下单操作，买6件
---> 付款
---> 扣除库存 update goods set num=num-6 where num=10 and id=5;  # 增加更新条件，判断库存是否还是原来
---> 如果执行成功，则表示没有人抢，购买成功
     如果执行事变，则表示已经有人先抢购
---> commit;

悲观锁：
---> begin; 开启事务
---> 先给id=5的数据，加锁
     select * from goods where id=5 for update;
---> 进行下单操作，买6件
---> 付款
---> 扣除库存  update goods set num=num-6 where id=5
---> 执行成功解锁
---- commit;  提交事务
"""
```

### 基本查询

#### SQLAlchemy常用的查询过滤器

| 过滤器         | 说明                                                         |
| :------------- | :----------------------------------------------------------- |
| **filter()**   | 把过滤器添加到原查询上，返回一个新查询                       |
| filter_by()    | 把等值过滤器添加到原查询上，返回一个新查询                   |
| **limit()**    | 使用指定的值限定原查询返回的**结果数量**                     |
| **offset()**   | 设置结果范围的**开始位置**，偏移原查询返回的结果，返回一个新查询 |
| **order_by()** | 根据指定条件对原查询结果进行**排序**，返回一个新查询         |
| **group_by()** | 根据指定条件对原查询结果进行**分组**，返回一个新查询         |

#### SQLAlchemy常用的查询结果方法

| 方法           | 说明                                                         |
| :------------- | :----------------------------------------------------------- |
| **all()**      | 以**列表形式**返回查询的所有结果                             |
| **first()**    | 返回查询的第一个结果，**模型对象**，如果未查到，返回**None** |
| first_or_404() | 返回查询的第一个结果，**模型对象**，如果未查到，通过abort 返回404异常 |
| **get()**      | 返回**指定主键**对应的**模型对象**，如不存在，返回None       |
| get_or_404()   | 返回指定主键对应的行，如不存在，abort 返回404                |
| **count()**    | 返回查询结果的**数量**                                       |
| **paginate()** | 返回一个Paginate**分页器对象**，它包含指定范围内的结果       |
| **having()**   | 返回结果中符合条件的数据，**必须跟在group by后面**，其他地方无法使用。 |

get():参数为主键，表示根据主键查询数据，如果主键不存在返回None

```py

@app.route("/get")
def get():
    """按主键获取一条"""
    # student = Student.query.get({"id": 5})
    # student = Student.query.get((5,))
    # student = db.session.query(Student).get(5)
    student = Student.query.get(5)
    print(student)
    return "ok"

```



all()返回查询到的所有对象

```python
模型类.query.all()

"""获取多个数据"""
student = Student.query.all()
print(student) # [dong<Student>, 小红<Student>, wang<Student>, chen<Student>, zhou<Student>, tang<Student>, wu<Student>, qian<Student>, liu<Student>, li<Student>, sun<Student>]

student = Student.query.filter(Student.id<5).all()  # 没有结果返回空列表[]
print(student) # [dong<Student>, 小红<Student>, wang<Student>]

# all()的返回值是一个python列表，可以直接使用切片，与django的QuerySet完全不是一回事。
student = Student.query.filter(Student.id < 5).all()[:-1]  # 没有结果返回空列表[]
print(student) # [dong<Student>, 小红<Student>]
```



count 返回结果的数量

```python
# 返回结果的数量

# 查询Student类中所有数据总和
student = Student.query.count()
print(student)
# 查询id大于5的总数
ret = Student.query.filter(Student.id < 5).count()
print(f"ret={ret}")
```



first()返回查询到的第一个对象【first获取一条数据,all获取多条数据】

```python
模型类.query.first()

"""获取第一个数据"""
student = Student.query.first()
print(student)

student = Student.query.filter(Student.id==5).first() # 没有结果返回None
print(student)
"""获取最后一个数据"""
student = Student.query.filter(Student.age > 17).all()[:]
print(student)
```



filter条件查询，支持各种运算符和查询方法或者模糊查询方法。

返回名字结尾字符为g的所有数据。

```python
# 模糊查询
# 使用163邮箱的所有用户
# 以@163.com结尾
student_list = Student.query.filter(Student.email.endswith("@163.com")).all()
print(student_list)

# 姓名以"zh"开头的
student_list = Student.query.filter(Student.name.startswith("zh")).all()
print(student_list)

# 名字中带有"a"字母的数据
student_list = Student.query.filter(Student.name.contains("a")).all()
print(student_list)

"""单条件比较"""
# 则需要指定条件格式为: filter(模型.字段 比较运算符 值)。
# 运算符可以是: ==表示相等, !=不相等，> 表示大于  < 表示小于，>=大于等于，<=小于等于
# student_list = Student.query.filter(Student.age > 18).all()
# print(student_list) # [wang<Student>, chen<Student>, zhou<Student>,...]

"""多条件比较"""
# 要求多个条件都要满足，相当于逻辑查询中的 并且(and)！！
student_list = Student.query.filter(Student.age > 18, Student.sex == True).all()
print(student_list) # [wang<Student>, chen<Student>, qian<Student>, liu<Student>]
```



filter_by精确条件查询

filter_by 只支持字段的**值是否相等**的情况，对于大于、等于、等等其他条件是不支持的。

例如：返回age等于22的学生

```python
# 单条件
student_list = Student.query.filter_by(age=22).all()  # 字段添加不需要附带模型类
print(student_list)

# 多条件
student_list = Student.query.filter_by(age=22,sex=True).all()
print(student_list)
```

### 多条件查询

逻辑`与`，需要导入`and_`，返回`and_()`条件满足的所有数据

等同于

```py
and_(条件1,条件2,....)  等价于  filter(条件1,条件2,.....)
```

```py
from sqlalchemy import and_
Student.query.filter(and_(Student.name!='wang',Student.email.endswith('163.com'))).all()


# # and_(条件1,条件2,....)  等价于  filter(条件1,条件2,.....)
# # age > 18 and email like "%163.com"
# # student_list = Student.query.filter(Student.age > 18, Student.email.endswith("163.com")).all()
# 
# student_list = Student.query.filter(
#     and_(
#         Student.age > 18,
#         Student.email.endswith("163.com")
#     )
# ).all()
```

逻辑`或`，需要导入`or_`

```py
from sqlalchemy import or_
Student.query.filter(or_(Student.name!='wang',Student.email.endswith('163.com'))).all()

# 查询年龄在20岁，使用的邮箱是qq或者163邮箱的
student_list = Student.query.filter(
    Student.age == 20,
    or_(
        Student.email.endswith("qq.com"),
        Student.email.endswith("163.com")
    )
).all()


# 复合条件的查询情况
# 查询年龄>17岁的女生或者年龄>18岁的男生
student_list = Student.query.filter(
    or_(
        and_(Student.age > 17, Student.sex == False),
        and_(Student.age > 18, Student.sex == True),
    )
).all()
print(student_list)

print(student_list)
```

逻辑`非`，返回名字不等于"小白"的所有数据

not_ 相当于取反和`!=`一样

```py
from sqlalchemy import not_
Student.query.filter(not_(Student.name=='小白')).all()

# # 查询年龄不等于22
# student_list = Student.query.filter(Student.age != 22).all()
# print(student_list)
# student_list = Student.query.filter(not_(Student.age==22)).all()
# print(student_list)
```

判断数据库中的一条数据是否存在

```py
# 这个查法挺另类的。
db = SQLAlchemy(app=app)

student = db.session.query(Student).filter(Student.age==17)
student_is=db.session.query(student.exists()).scalar()
# 最后返回Ture或者False

# 这样写，判断age==17的数据是否存在，最后返回Ture
student = Student.query.filter(Student.age==17).first()
print(bool(student))    # Ture
```

范围查询

```py
# 查询id是[1,2,5,8]的数据
#in_是不需要导包的，直接就可以用in_
student = Student.query.filter(Student.id.in_([1,2,5,8])).all()
print(student) 
```

is_判断值查询

```python
    """判断值查询"""
    student_list = Student.query.filter(Student.email.is_(None)).all()
    print(student_list)

    student_list = Student.query.filter(Student.email == None).all()
    print(student_list)
```



order_by 排序

```python
# 倒序[值从大到小]
student_list = Student.query.order_by(Student.id.desc()).all()
# 升序[值从小到大]
student_list = Student.query.order_by(Student.id.asc()).all()

# 多字段排序[第一个字段值一样时，比较第二个字段，进行排序]
student_list = Student.query.order_by(Student.money.asc(), Student.age.asc(), Student.id.asc()).all()
print(student_list)
```



count统计

```python
# 查询age>=19的男生的数量
from sqlalchemy import and_
# ret = Student.query.filter( and_(Student.age>=19,Student.sex==True) ).count()
ret = Student.query.filter( Student.age>=19, Student.sex==True ).count()
```



对结果进行偏移量和数量的限制

```python
# 查询年龄最大的3个学生
student_list = Student.query.order_by(Student.age.desc()).limit(3).all()
print(student_list)

# 查询年龄排第4到第7名的学生
student_list = Student.query.order_by(Student.age.desc()).offset(3).limit(4).all()
print(student_list)

# 查询年龄最小的3个人
student_list = Student.query.order_by(Student.age.asc()).limit(3).all()
print(student_list)
```

### 分页器

```py
ret=Student.query.filter(过滤条件).paginate(页码，单页数据量)
```



```py
@app.route("/")
def index():
    """访问这个地址http://127.0.0.1:5000/?page=2&per_page=5"""
    page=int(request.args.get('page', 1))
    per_page=int(request.args.get('size', 5))
    ret=Student.query.filter(Student.age>10)
	.paginate(page=page,per_page=per_page,max_per_page=100)
    # 常用的参数
    print(ret.total)  # 总数据量
    print(ret.pages)  # 总页码

    print(ret.has_prev)   # 是否有上一页对象
    print(ret.prev())    #上一页对象。  
    print(ret.prev().items)   # 拿上一页的数据。
    print(ret.has_next)   # 是否有上一页对象
    print(ret.next())    #上一页对象。  
    print(ret.next().items)   # 拿上一页的数据。
    return "ok"
    # """前后端分离"""
    # data = {
    #     "page": pagination.page, # 当前页码
    #     "pages": pagination.pages, # 总页码
    #     "has_prev": pagination.has_prev, # 是否有上一页
    #     "prev_num": pagination.prev_num, # 上一页页码
    #     "has_next": pagination.has_next, # 是否有下一页
    #     "next_num": pagination.next_num, # 下一页页码
    #     "items": [{
    #         "id": item.id,
    #         "name": item.name,
    #         "age": item.age,
    #         "sex": item.sex,
    #         "money": item.money,
    #     } for item in pagination.items]
    # }
    # return data
# 前后端分离的
	# return render_template("xxxx.html",**locals())
"""
paginate是返回了一个对象，下面是这个函数源码
"""
```



```py
   def paginate(
        self,
        *,
        page: int | None = None,
        per_page: int | None = None,
        max_per_page: int | None = None,
        error_out: bool = True,
        count: bool = True,
    ) -> Pagination:
 """
 page是页码
 per_page是这一个展示展示数据
 max_per_page是最大展示数据
 """
# 下面在进入到这个函数的返回值是QueryPagination但是QueryPagination继承了Pagination
# 所以我们直接看Pagination

class Pagination:
    """
    这个类中写了很多的@property，这些我们可以直接调用。
    eg：如下面的这个pages，是输出这个页面的总页码。我们可以直接调用。
    """
    @property
    def pages(self) -> int:
        """The total number of pages."""
        if self.total == 0 or self.total is None:
            return 0

        return ceil(self.total / self.per_page)
```

### 聚合函数

聚合函数的写法另类

分组查询和分组查询结果过滤

一般分组都会结合**聚合函数**来一起使用。SQLAlchemy中所有的聚合函数都在`func`模块中声明的。

```python
from sqlalchemy import func
```

| 函数名     | 说明     |      |
| ---------- | -------- | ---- |
| func.count | 统计总数 |      |
| func.avg   | 平均值   |      |
| func.min   | 最小值   |      |
| func.max   | 最大值   |      |
| func.sum   | 求和     |      |

代码：

```py
"""聚合函数"""
from sqlalchemy import func
# 获取所有学生的money总数
# SELECT sum(db_student.money) AS sum_1 FROM db_student LIMIT %s
# ret = db.session.query(func.sum(Student.money)).first()[0]
# print(ret) # 3998.0
# # 查询女生的数量
# ret = db.session.query(func.count(Student.id)).filter(Student.sex==False).first()[0]
#     ret = db.session.query(func.count(Student.id)).filter(Student.sex==False).scalar()
# 使用scalar()会更好，
# print(ret) # 7
# # 查询所有学生的平均年龄
# ret = db.session.query(func.avg(Student.age)).first()[0]
# print(ret) # 18.2727

"""
聚合分组
在聚合分组的情况下，db.session.query中的参数只能是被分组的字段或者是被聚合的数据
"""
# # 查询当前所有男生女生的数量
# ret = db.session.query(Student.sex,func.count(Student.id)).group_by(Student.sex).all()
# print(ret) # [(False, 7), (True, 4)]

# # 查询各个年龄段的学生数量
# ret = db.session.query(Student.age, func.count(Student.id)).group_by(Student.age).all()
# print(ret) # [(15, 2), (13, 1), (22, 4), (19, 1), (18, 1), (16, 1), (17, 1)]
#
# # 查看当前男生女生的平均年龄
# ret = db.session.query(Student.sex, func.avg(Student.age)).group_by(Student.sex).all()
# ret = [{"sex":"男" if item[0] else "女","age":float(item[1])} for item in ret]
# print(ret) # [{'sex': '女', 'age': 18.0}, {'sex': '男', 'age': 18.75}]

# # 分组后的过滤操作 having
# # 在所有学生中，找出各个年龄中拥有最多钱的同学，并在这些同学里面筛选出money > 500的数据
# subquery = func.max(Student.money)
# print(subquery) # max(db_student.money)
# ret = db.session.query(Student.age, subquery).group_by(Student.age).having(subquery > 500).all()
# print(ret)  # [(18, Decimal('1000.00')), (22, Decimal('26000.00')), (23, Decimal('1998.00'))]

"""
多字段分组
    字段1   字段2
    1      3
    2      4

    分组如下：
    13
    14
    23
    24
"""
# 各个年龄里，男生和女生的money总数
subquery = func.sum(Student.money)
ret = db.session.query(Student.sex, Student.age, subquery).group_by(Student.sex, Student.age).all()
print(ret) # [(False, 15, 1000.0), (False, 13, 600.0), (True, 15, 0.0), (True, 22, 1998.0), (False, 19, 0.0), (False, 22, 400.0), (False, 18, 0.0), (True, 16, 0.0), (False, 17, 0.0)]
```

### 执行原生SQL语句

```py
"""执行原生SQL语句"""
# # 查询多条数据
# ret = db.session.execute("select * from db_student").fetchall()
# print(ret)
# # 查询一条数据
# ret = db.session.execute("select * from db_student").fetchone()
# print(ret)

"""
    name  age  achievement
               80
    小明   17   81
               83

    group_concat 逗号合并
    小明   17   80,81,83

    concat  字符串拼接
    小明   17   808183
    """

# # 添加数据
# db.session.execute("insert db_student (name,age,sex,email,money) select name,age,sex,concat(now(),email),money from db_student")
# db.session.commit()

# # # 更新/删除
# db.session.execute("UPDATE db_student SET money=(db_student.money + %s) WHERE db_student.age = %s" % (200, 22))
# db.session.commit()


"""分组合并"""
# 统计各个年龄段的学生人数，并记录对应年龄段的学生ID
ret = db.session.execute("select age,count(id),group_concat(id) from db_student group by age").fetchall()
print(ret)
return "ok"
```

## 关联查询

### 常用的SQLAlchemy关系选项

| 选项名         | 说明                                                         |
| :------------- | :----------------------------------------------------------- |
| backref        | 在关系的另一模型中添加**反向引用**,用于设置外键名称,在1查多的 |
| primary join   | 明确指定两个模型之间使用的连表条件, 用于1对1 或者1对多连表中 |
| lazy           | 指定如何加载关联模型数据的方式，用于1对1或1对多链表中。<br />参数值:<br>select（立即加载，查询所有相关数据显示，相当于lazy=True）<br>subquery（立即加载，但使用子查询）<br/>dynamic（不立即加载，但提供加载记录的查询对象）这个用的最多。 |
| uselist        | 指定1对1或1对多连表时，返回的数据结果是模型对象还是模型列表，如果为False，不使用列表，而使用模型对象。<br>1对1或多对1关系中，需要设置relationship中的uselist=Flase，1对多或多对多关系中，需要设置relationshio中的uselist=True。 |
| secondary      | 指定多对多关系中关系表的名字。<br>多对多关系中，需建立关系表，设置 secondary=关系表 |
| secondary join | 在SQLAlchemy中无法自行决定时，指定多对多关系中的二级连表条件，绑定主外键。 |

## 模型之间的关联

### 一对一

```py
from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
class config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = False

app.config.from_object(config)
db = SQLAlchemy(app=app)



class Student(db.Model):
    __tablename__ = "tb_1V1_student"
    id=db.Column(db.Integer, primary_key=True,comment="主键")
    name=db.Column(db.String(64), nullable=False,comment="姓名")
    age=db.Column(db.Integer, nullable=False,comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), unique=True, comment="邮箱地址")
    # 这个和关联表中的db.relationship写一个就可以
    # info=db.relationship("Studentinfo",uselist=False,backref=backref("student", uselist=False))

    def __repr__(self) -> str:
        return f"{self.name,self.__class__.__name__}"

class Studentinfo(db.Model):
    __tablename__ = "tb_1V1_student_info"
    id=db.Column(db.Integer, primary_key=True,comment="主键")
    student_id=db.Column(db.Integer,db.ForeignKey("tb_1V1_student.id"),comment="外建")
    # 一对一的设置
    # 关联属性提供给SQLAlchemy，用于查询和反向查询，这个字段在数据库是不会显示，只是为了方便查询的。uselist=False，表示关联一个数据。
    # backref就是可以反向查询，info就是.info反向查询,uselist就是一对一的意思,
    # 通过Studentinfo查Student是.student,
    # 通过student查Studentinfo是通过.info
    student = db.relationship("Student", uselist=False, backref=backref("info", uselist=False))  # ORM关联属性    address=db.Column(db.String(255), nullable=False,index=True,comment="家庭地址")
    moblie=db.Column(db.String(11), nullable=False,index=True,comment="手机号")
    address=db.Column(db.String(255),nullable=False,index=True,comment="家庭地址")
    def __repr__(self) -> str:
        return f"{self.student.name,self.__class__.__name__}"
```

关键的两句

```python
"""省略其中的一些代码"""
student_id=db.Column(db.Integer,db.ForeignKey("tb_1V1_student.id"),comment="外建")
student = db.relationship("Student", uselist=False, backref=backref("info", uselist=False))

# student_id=db.Column(db.Integer,db.ForeignKey(表明.字段"),comment="外建")
# student = db.relationship("表所在的类", uselist=False, backref=backref("自己起的名字", uselist=False)) 
```

这两句的解读

```py
第一句
# student_id=db.Column(db.Integer,db.ForeignKey(表明.字段"),comment="外建")
关联tb_1V1_student表中的id字段。通过第二句中的uselist=False来确定是一对一，uselist=Ture是一对多。
第二句
student = db.relationship("Student", uselist=False, backref=backref("info", uselist=False))
	# db.relationship("Student")，这个字段可以正向关联查Student类中的表，backref是"info",所以可以反向通过.info来查主键模型的数据。
	# 因为这个字段叫student，所以外键通student查，我们设置的info，就是主键通过info查。
	# 这个字段在数据库中数据库中不会显示出来的， 
    # 一对一的设置
    # 关联属性提供给SQLAlchemy，用于查询和反向查询，这个字段在数据库是不会显示，只是为了		方便查询的。uselist=False，表示关联一个数据。
    # backref就是可以反向查询，,uselist就是一对一的意思,
```

通过Studentinfo查Student是`.student`。

 通过student查Studentinfo是通过`.info`。

第二句可以写在主键模型，也可以写在外键模型中，写法一样，上面是写在外键模型中。

```py
# 这个是写在主键模型中的。
# 因为字段名字是info，所以主键通过.info来查外模型Studentinfo类中表的数据，backref=”student“，所以外键模型通过student来查主键表的数据
# 
info=db.relationship("Studentinfo",uselist=False,backref=backref("student", uselist=False))
```

#### 一对一的一些操作

```py
from flask import Flask,request
from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
class config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = False

app.config.from_object(config)
db = SQLAlchemy(app=app)



class Student(db.Model):
    __tablename__ = "tb_1V1_student"
    id=db.Column(db.Integer, primary_key=True,comment="主键")
    name=db.Column(db.String(64), nullable=False,comment="姓名")
    age=db.Column(db.Integer, nullable=False,comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), unique=True, comment="邮箱地址")
    # 这个和关联表中的db.relationship写一个就可以
    # info=db.relationship("Studentinfo",uselist=False,backref=backref("student", uselist=False))

    def __repr__(self) -> str:
        return f"{self.name,self.__class__.__name__}"

class Studentinfo(db.Model):
    __tablename__ = "tb_1V1_student_info"
    id=db.Column(db.Integer, primary_key=True,comment="主键")
    student_id=db.Column(db.Integer,db.ForeignKey("tb_1V1_student.id"),comment="外建")
    # 一对一的设置
    # 关联属性提供给SQLAlchemy，用于查询和反向查询，这个字段在数据库是不会显示，只是为了方便查询的。uselist=False，表示关联一个数据。
    # backref就是可以反向查询，info就是.info反向查询,uselist就是一对一的意思,
    # 通过Studentinfo查Student是.student,
    # 通过student查Studentinfo是通过.info
    student = db.relationship("Student", uselist=False, backref=backref("info", uselist=False))  # ORM关联属性    address=db.Column(db.String(255), nullable=False,index=True,comment="家庭地址")
    moblie=db.Column(db.String(11), nullable=False,index=True,comment="手机号")
    address=db.Column(db.String(255),nullable=False,index=True,comment="家庭地址")
    def __repr__(self) -> str:
        return f"{self.student.name,self.__class__.__name__}"
    
@app.route("/create")
def create_table():
    db.create_all() # 为项目中被识别的所有模型创建数据表
    return "ok"
@app.route("/index")
def index():
    # 添加数据
    # student=Student(
    #     name="xiaohong",
    #     age=23,
    #     sex=True,
    #     email="xiaohong@qq.com",
    #     # 在创建表时创建的db.relationship(backref="info"),所以可以通过info来操作关联表。
    #     info=Studentinfo(
    #         address="北京海淀",
    #         moblie=12345678903,
    #     )
    # )

    # db.session.add(student)
    # db.session.commit()
    # Student中已经有了数据，在给Studentinfo中添加数据。
    student=Student(name="xiaobai",age=23,sex=True,email="xiaobai@qq.com",)
    # db.session.add(student)
    # db.session.commit()
    student.info=Studentinfo(address="北京朝阳",moblie=12345678904)
    db.session.commit()
    return "ok"
@app.route("/select")
def select_data():
    """查询数据"""
    # # 通过主键模型调用外建模型
    # student=Student.query.filter(Student.age<20).first()
    # print("student.name12312312",student.name)
    # print("student.info123123123123",student.info.address)
    # # 通过外建模型调用主键模型
    # info=Studentinfo.query.filter(Studentinfo.moblie==12345678902).first()
    # print("info1312312123",info)
    # print(info.student.name)

    # 以外建的模型数据,去查主键的模型数据.
    student=Student.query.filter(Studentinfo.moblie==12345678902).first()
    print(student.name)
    return "ok"
@app.route("/add_data")
def add_data():
    """根据主键模型的数据,修改外建模型的数据"""
    # student=Student.query.filter(Student.age==23).first()
    # print(student.name)
    # # 修改数据
    # student.info.address="北京密云"
    # db.session.commit()
    """根据外键模型的数据,修改主建模型的数据"""
    info=Studentinfo.query.filter(Studentinfo.moblie==12345678902).first()
    info.student.name="xiaohhei"
    db.session.commit()
    return "修改成功"

@app.route("/del_data")
def del_data():
    # 删除数据
    # 1. 如果删除主模型数据，则会先将外键模型的外键字段设置为null，其他的不变，然后才会删除主模型对象
    student=Student.query.get(4)
    db.session.delete(student)
    db.session.commit()
    # 2. 如果删除外键模型数据，则直接删除，不会修改主模型数据
    StudentInfo.query.filter(StudentInfo.mobile == "13312345678").delete()
    db.session.commit()
    return "ok"
    return "ok"
if __name__ == '__main__':

    app.run()
```

### 一对多

```py

class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    username = db.Column(db.String(50), unique=True, comment="用户名")
    nickname = db.Column(db.String(50), index=True, comment="昵称")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    money = db.Column(db.Numeric(8,2), default=0.0, comment="钱包余额")
    # address_list = db.relationship("UserAddress", uselist=True, backref=backref("user",uselist=False), lazy="dynamic")

    def __repr__(self):
        return f"{self.username,self.__class__.__name__}"


class UserAddress(db.Model):
    __tablename__ = "tb_user_address"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(50), default="默认", comment="名称")
    province = db.Column(db.String(50), comment="省份")
    city = db.Column(db.String(50), comment="城市")
    area = db.Column(db.String(50), comment="地区")
    address = db.Column(db.String(500), comment="详细地址")
    mobile = db.Column(db.String(15), comment="收货人电话")
    user_id = db.Column(db.Integer, db.ForeignKey("tb_user.id"), comment="User外键")
    user = db.relationship("User", uselist=False, backref=backref("UserAddress",uselist=True,lazy="dynamic"))
    def __repr__(self):
        return f"{self.user.username,self.__class__.__name__}"
```

- 其中realtionship描述了Student和StudentAddress的关系。第1个参数为对应参照的类"StudentAddress"
- 第3个参数backref为类StudentAddress声明关联属性
- 第4个参数lazy决定了什么时候SQLALchemy什么时候执行读取关联模型的SQL语句
    - lazy='subquery'，查询当前数据模型时，采用子查询(subquery)，把外键模型的属性也同时查询出来了。
    - lazy=True或lazy='select'，查询当前数据模型时，不会把外键模型的数据查询出来，只有操作到外键关联属性时，才进行连表查询数据[执行SQL]
    - lazy='dynamic'，查询当前数据模型时，不会把外键模型的数据立刻查询出来，只有操作到外键关联属性并操作外键模型具体字段时，才进行连表查询数据[执行SQL]
- 常用的lazy选项：dynamic和select

关键的两句

```py
user_id = db.Column(db.Integer, db.ForeignKey("tb_user.id"), comment="User外键")
user = db.relationship("User", uselist=False, backref=backref("UserAddress",uselist=True,lazy="dynamic"))
```

解读上面两句

```py
user_id = db.Column(db.Integer, db.ForeignKey("tb_user.id"), comment="User外键")
关联tb_user表的id字段，


user = db.relationship("User", uselist=False, backref=backref("UserAddress",uselist=True,lazy="dynamic"))
这个字段是不会在数据库中显示的。
上面这句是写在外键中的。外建找主键只能找到一条数据，所以uselist=False，主键找外键可以找到多条数据，所以uselist=True,

下面这个是写在主键中的，uselist和外键中的相反。
address_list = db.relationship("UserAddress", uselist=True,backref=backref("user",uselist=False), lazy="dynamic")
```

更多操作

```py
from flask import Flask,request
from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
class config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = False

app.config.from_object(config)
db = SQLAlchemy(app=app)


class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    username = db.Column(db.String(50), unique=True, comment="用户名")
    nickname = db.Column(db.String(50), index=True, comment="昵称")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    money = db.Column(db.Numeric(8,2), default=0.0, comment="钱包余额")
    # address_list = db.relationship("UserAddress", uselist=True, backref=backref("user",uselist=False), lazy="dynamic")

    def __repr__(self):
        return f"{self.username,self.__class__.__name__}"


class UserAddress(db.Model):
    __tablename__ = "tb_user_address"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(50), default="默认", comment="名称")
    province = db.Column(db.String(50), comment="省份")
    city = db.Column(db.String(50), comment="城市")
    area = db.Column(db.String(50), comment="地区")
    address = db.Column(db.String(500), comment="详细地址")
    mobile = db.Column(db.String(15), comment="收货人电话")
    user_id = db.Column(db.Integer, db.ForeignKey("tb_user.id"), comment="User外键")
    user = db.relationship("User", uselist=False, backref=backref("UserAddress",uselist=True,lazy="dynamic"))
    def __repr__(self):
        return f"{self.user.username,self.__class__.__name__}"



@app.route("/create")
def create_table():
    db.create_all() # 为项目中被识别的所有模型创建数据表
    return "ok"

@app.route("/")
def indeex():
    return "<h1>欢迎来到flask的世界</h1>"

@app.route("/add")
def add_data():
    """添加数据"""
    # 同时添加数据
    # user=User(sqlalchemy.exc.InvalidRequestError: One or more mappers failed to initialize - can't proceed with initialization of other mappers. Triggering mapper: 'Mapper[UserAddress(tb_user_address)]'. Original exception was: On relationship UserAddress.user, 'dynamic' loaders cannot be used with many-to-one/one-to-one relationships and/or uselist=False.
    #     username="xiaoZHAO",
    #     nickname="xiaoZHAO",
    #     sex=True,
    #     money=2000,
    #     useraddress=[
    #         UserAddress(name="公司", province="北京市", city="北京市", area="昌平区", address="百沙路201", mobile="13012345678"),
    #         UserAddress(name="门口小卖部", province="北京市", city="北京市", area="昌平区", address="百沙路202", mobile="13012345677"),
    #         UserAddress(name="小区门口", province="北京市", city="北京市", area="昌平区", address="百沙路203", mobile="13012345676"),
    #       ]
    # )
    # db.session.add(user)
    # db.session.commit()



    # 主键有数据后在给外建添加数据sqlalchemy.exc.InvalidRequestError: One or more mappers failed to initialize - can't proceed with initialization of other mappers. Triggering mapper: 'Mapper[UserAddress(tb_user_address)]'. Original exception was: On relationship UserAddress.user, 'dynamic' loaders cannot be used with many-to-one/one-to-one relationships and/or uselist=False.
    user=User(
        username="xiaoLI",
        nickname="xiaoLI",
        sex=True,
        money=2000,)
    # db.session.add(user)
    # db.session.commit()
    # user.useraddress.append(UserAddress(nam1,129 INFO sqlalchemy.engine.Engine ROLLBACKe="公司", province="北京市", city="北京市", area="昌平区", address="百沙路201", mobile="13012345678"))
    user.useraddress=[
             UserAddress(name="公司", province="北京市", city="北京市", area="昌平区", address="百沙路201", mobile="13012345678"),
             UserAddress(name="门口小卖部", province="北京市", city="北京市", area="昌平区", address="百沙路202", mobile="13012345677"),
             UserAddress(name="小区门口", province="北京市", city="北京市", area="昌平区", address="百沙路203", mobile="13012345676"),
         ]
    db.session.commit()
    return "添加成功"

@app.route("/select")
def select_data():
    """查看数据"""
    user = User.query.filter(User.username == "xiaoshen").first()
    student=UserAddress.query.filter(UserAddress.name == "公司").first()
    print(student.user.username)
    # 因为是一对一的数据，所以取出了多个拿一个。
    print(user.UserAddress[0].city)
    return "SELECT * FROM"
if __name__ == '__main__':

    app.run()
```

### 多对多

```py
# 关系表[这种表，无法提供给python进行操作的，仅仅用于在数据库中记录两个模型之间的关系]
# 创建第三张表，来存储多对多，
# 通过db.Table来创建第三表
student_and_course = db.Table(
    "table_student_course",
    db.Column("id", db.Integer, primary_key=True, comment="主键ID"),
    db.Column("sid", db.Integer, db.ForeignKey("table_student.id"), comment="学生"),
    db.Column("cid", db.Integer, db.ForeignKey("table_course.id"), comment="课程"),
    db.Column("created_time", db.DateTime, default=datetime.now, comment="购买时间"), # 当前字段无法操作
)

# 通过db.relationship来操作第三张表。
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    ...
    course_list = db.relationship("Course", secondary=student_and_course, backref="student_list", lazy="dynamic")
```



##### 基于第三方关系表构建多对多

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from datetime import datetime

app = Flask(__name__)
class Config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    #使用的mysqldb
    #SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    #使用的pymysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = True


app.config.from_object(Config)
db = SQLAlchemy(app=app)


# 关系表[这种表，无法提供给python进行操作的，仅仅用于在数据库中记录两个模型之间的关系]
student_and_course = db.Table(
    "table_student_course",      # 第三张表名字
    db.Column("id", db.Integer, primary_key=True, comment="主键ID"),
    db.Column("sid", db.Integer, db.ForeignKey("table_student.id"), comment="学生"),
    db.Column("cid", db.Integer, db.ForeignKey("table_course.id"), comment="课程"),
    db.Column("created_time", db.DateTime, default=datetime.now, comment="购买时间"), # 当前字段无法操作
)


class Student(db.Model):
    """学生信息模型"""
    # 声明与当前模型绑定的数据表名称
    __tablename__ = "table_student"
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")
    """
    只有写上下面这行，flask才会知道是这两个表是多对多的关系。							secondary=student_and_course
    """
    course_list = db.relationship("Course", secondary=student_and_course, backref="student_list", lazy="dynamic")


    def __repr__(self):
        return f"{self.name},{self.__class__.__name__}"


class Course(db.Model):
    """课程数据模型"""
    __tablename__ = "table_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(64), unique=True, comment="课程")
    price = db.Column(db.Numeric(7, 2), default=0.0, comment="价格")

    def __repr__(self):
        return f"{self.name},{self.__class__.__name__}"

@app.route("/create")
def create_data():
    db.create_all()
    return "ok"


if __name__ == "__main__":
    app.run()
```

**关键的一个表和一行代码**

创建第三张表，用来实现多对多，db.ForeignKey("表名.id")，这个表只能有这几个字段。

```py
from datetime import datetime


student_and_course = db.Table(
    "table_student_course",   # 第三张表名字
    db.Column("id", db.Integer, primary_key=True, comment="主键ID"),
    
    db.Column("sid", db.Integer, db.ForeignKey("table_student.id"), comment="学生"),
    db.Column("cid", db.Integer, db.ForeignKey("table_course.id"), comment="课程"),
    db.Column("created_time", db.DateTime, default=datetime.now, comment="购买时间"), # 当前字段无法操作，datetime.now不能括号，
)
```

一行重要代码

```py
# 这行代码，和一对一，一对多的作用一样，用于正向查询，和反向查询，可以在任意的一张表中。
# secondary=第三张表的类，用来告诉flask。多对多。
# 写在Student类中
course_list = db.relationship("Course", secondary=student_and_course, backref="student_list", lazy="dynamic")
# 写在Course类中
student_list = db.relationship("Student", secondary=student_and_course, backref="course_list", lazy="dynamic")
```

更多操作

```py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from datetime import datetime

app = Flask(__name__)
class Config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    #使用的mysqldb
    #SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    #使用的pymysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = True


app.config.from_object(Config)
db = SQLAlchemy(app=app)


# 关系表[这种表，无法提供给python进行操作的，仅仅用于在数据库中记录两个模型之间的关系]
student_and_course = db.Table(
    "table_student_course",
    db.Column("id", db.Integer, primary_key=True, comment="主键ID"),
    db.Column("sid", db.Integer, db.ForeignKey("table_student.id"), comment="学生"),
    db.Column("cid", db.Integer, db.ForeignKey("table_course.id"), comment="课程"),
    db.Column("created_time", db.DateTime, default=datetime.now, comment="购买时间"), # 当前字段无法操作
)


class Student(db.Model):
    """学生信息模型"""
    # 声明与当前模型绑定的数据表名称
    __tablename__ = "table_student"
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")
    course_list = db.relationship("Course", secondary=student_and_course, backref=backref("student_list"), lazy="dynamic")


    def __repr__(self):
        return f"{self.name},{self.__class__.__name__}"


class Course(db.Model):
    """课程数据模型"""
    __tablename__ = "table_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(64), unique=True, comment="课程")
    price = db.Column(db.Numeric(7, 2), default=0.0, comment="价格")

    def __repr__(self):
        return f"{self.name},{self.__class__.__name__}"

@app.route("/create")
def create_data():
    db.create_all()
    return "ok"

@app.route("/adddata")
def add_data():
    # student=Student(
    #     name="xiaoming",
    #     age=22,
    #     sex=True,
    #     email="xiaoming@163.com",
    #     money="103",
    #     course_list=[
    #         Course(name="C",price=4),
    #         Course(name="golang",price=5),
    #         Course(name="c++",price=6),
    #        ]
    #     )
    # db.session.add(student)
    # db.session.commit()

    """在已经有学生的基础上增加课程"""
    student=Student(
        name="xiaoming",
        age=22,
        sex=True,
        email="xiaoming@163.com",
        money="103",
        )
    student=Student.query.filter(Student.age==22).first()
    # print(student.course_list[0])
    student.course_list.append(Course.query.get(8))
    # student.course_list.append(Course(name="python高级"))
    db.session.commit()
    return "添加成功"


@app.route("/select")
def select_course():
    """正向查询,需要加all"""
    # student=Student.query.get(2)
    # print(student.course_list.all())
    """反向查询,不需要加all"""
    course=Course.query.get(1)
    print(course.student_list)
    return "查询成功"


@app.route("/update")
def update_data():
    """更新数据"""
    cour=Course.query.get(1)
    cour.student_list[0].money+=100
    print(cour.student_list[0].money)

    return "更新成功"
if __name__ == "__main__":
    app.run()
```

db.Table的缺陷: 无法通过主模型直接操作db.Table中的外键之外的其他字段，例如：报读课程的时间

解决： 在声明2个模型是多对多的关联关系时，把关联关系使用第三个模型来创建声明，
     		就是不要使用db.Table改成模型来绑定关系，把模型的对多对拆分成2个1对多

就是使用下的方法，创建多对多。

##### 基于第三方关系模型构建多对多

在SQLAlchemy中，基于db.Table创建的关系表，如果需要新增除了外键以外其他字段，无法操作。所以将来实现多对多的时候，除了上面db.Table方案以外，还可以把关系表声明成模型的方法，如果声明成模型，则原来课程和学生之间的多对多的关系，就会变成远程的1对多了。

创建表

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from datetime import datetime

app = Flask(__name__)
class Config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    #使用的mysqldb
    #SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    #使用的pymysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = False


app.config.from_object(Config)
db = SQLAlchemy(app=app)


class StudentCourse(db.Model):
    __tablename__ = "table_student_course"
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    sid=db.Column(db.Integer, db.ForeignKey("table_student.id"),comment="学生表的外建")
    cid=db.Column(db.Integer, db.ForeignKey("table_course.id"),comment="课程表的外建")
    # 
    created_time = db.Column(db.DateTime, default=datetime.now, comment="购买时间")
    # 关联属性
    student = db.relationship("Student", uselist=False, backref=backref("to_relation", uselist=True))
    course = db.relationship("Course", uselist=False, backref=backref("to_relation", uselist=True))



class Student(db.Model):
    """学生信息模型"""
    # 声明与当前模型绑定的数据表名称
    __tablename__ = "table_student"
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    def __repr__(self):
        return f"{self.name},{self.__class__.__name__}"


class Course(db.Model):
    """课程数据模型"""
    __tablename__ = "table_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(64), unique=True, comment="课程")
    price = db.Column(db.Numeric(7, 2), default=0.0, comment="价格")

    def __repr__(self):
        return f"{self.name},{self.__class__.__name__}"
```

关键的第三张表

```py
class StudentCourse(db.Model):
    __tablename__ = "table_student_course"   			# 表名字
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    sid=db.Column(db.Integer, db.ForeignKey("table_student.id"),comment="学生表的外建")
    cid=db.Column(db.Integer, db.ForeignKey("table_course.id"),comment="课程表的外建")
    # 
    created_time = db.Column(db.DateTime, default=datetime.now, comment="购买时间")
    # 关联属性
    # 和Student关联，
    student = db.relationship("Student", uselist=False, backref=backref("to_relation", uselist=True))
    # 和Course关联。
    course = db.relationship("Course", uselist=False, backref=backref("to_relation", uselist=True))
```

操作表的时候，先反向操作第三张表，在通过反向查询查关联表。

eg1：增加数据

```py
    student=Student(
        name="xiaoming",
        age=22,
        sex=True,
        email="xiaoming@163.com",
        money="103",
	# to_relation操作第三张表。通过第三张表来给关联表添加数据。
        to_relation=[
            StudentCourse(course=Course(name="C",price=4)),
            StudentCourse(course=Course(name="python",price=4)),
            StudentCourse(course=Course(name="golang",price=4)),
           ]
        )
    db.session.add(student)
    db.session.commit()
```

eg2：查找数据

```py
    """查询学生购买的课程"""
    # student=Student.query.get(1)
    # print([i.course for i in student.to_relation])
    """查询指定课程被那些学生购买了"""
    # 在Course找到id=1的数据
    # course=Course.query.get(1)
    # course.to_relation因为有多个，循环第三张表，在第三张表中正向查找，找到每一的数据。
    # print([i.student for i in course.to_relation])
    """查询时间"""
    course=Course.query.get(1)
    for i in course.to_relation:
        print(i.created_time)
```

更多操作

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from datetime import datetime

app = Flask(__name__)
class Config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    #使用的mysqldb
    #SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    #使用的pymysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = False


app.config.from_object(Config)
db = SQLAlchemy(app=app)


class StudentCourse(db.Model):
    __tablename__ = "table_student_course"
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    sid=db.Column(db.Integer, db.ForeignKey("table_student.id"),comment="学生表的外建")
    cid=db.Column(db.Integer, db.ForeignKey("table_course.id"),comment="课程表的外建")
    # 
    created_time = db.Column(db.DateTime, default=datetime.now, comment="购买时间")
    # 关联属性
    student = db.relationship("Student", uselist=False, backref=backref("to_relation", uselist=True,lazy="dynamic"))
    course = db.relationship("Course", uselist=False, backref=backref("to_relation", uselist=True,lazy="dynamic"))



class Student(db.Model):
    """学生信息模型"""
    # 声明与当前模型绑定的数据表名称
    __tablename__ = "table_student"
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    def __repr__(self):
        return f"{self.name},{self.__class__.__name__}"


class Course(db.Model):
    """课程数据模型"""
    __tablename__ = "table_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(64), unique=True, comment="课程")
    price = db.Column(db.Numeric(7, 2), default=0.0, comment="价格")

    def __repr__(self):
        return f"{self.name},{self.__class__.__name__}"

@app.route("/create")
def create_data():
    db.create_all()
    return "ok"

@app.route("/adddata")
def add_data():
    student=Student(
        name="xiaoming",
        age=22,
        sex=True,
        email="xiaoming@163.com",
        money="103",
        to_relation=[
            StudentCourse(course=Course(name="C",price=4)),
            StudentCourse(course=Course(name="python",price=4)),
            StudentCourse(course=Course(name="golang",price=4)),
           ]
        )
    db.session.add(student)
    db.session.commit()

    """在已经有学生的基础上增加课程"""

    """在学生报读课程的基础上，新增报读课程。"""
    # student = Student(
    #     name="shenzehao",
    #     age=14,
    #     sex=False,
    #     money=30000,
    #     email="300000@qq.com",
    # )
    # db.session.add(student)
    # db.session.commit()

    student = Student.query.filter(Student.name == "shenzehao").first()
    # 直接采用python内置的list方法操作
    student.to_relation.extend([
        StudentCourse(
            course=Course.query.get(1) # 已经存在的课程，给学生报读
        ),
        StudentCourse(
            course=Course(name="python进阶", price=399.99)  # 新增课程，并让当前学生报读该课程
        )
    ])
    
    db.session.commit()

    return "添加成功"


@app.route("/select")
def select_course():
    """查询学生购买的课程"""
    # student=Student.query.get(1)
    # print([i.course for i in student.to_relation])
    """查询指定课程被那些学生购买了"""
    # course=Course.query.get(1)
    # print([i.student for i in course.to_relation])
    """查询时间"""
    course=Course.query.get(1)
    for i in course.to_relation:
        print(i.created_time)
    return "查询成功"


@app.route("/update")
def update_data():
    """更新数据"""
    cour=Course.query.get(1)
    for i in cour.to_relation:
        print(i.student.name)
        print(i.student.money)
        i.student.money+=100
        print(i.student.money)
    # print(cour.student_list [0].money)

    return "更新成功"

if __name__ == "__main__":
    app.run()
```

relationship还有一个设置外键级联的属性：cascade="all或 delete 或 delete-orphan"

all 就是

delete 就是，在删除主键时外键也会删除。

delete-orphan 就是，

eg:

```python
course = db.relationship("Course", uselist=False, cascade=delete ,backref=backref("to_relation", uselist=True))
```

## 逻辑外键

## 逻辑外键

也叫虚拟外键。主要就是在开发中为了减少数据库的性能消耗，提升系统运行效率，一般项目中如果单表数据太大[千万级别]就不会使用数据库本身维护的物理外键，而是采用由ORM或者我们逻辑代码进行查询关联的逻辑外键。

不适用mysql的物理外键，会对数据一致性带来一定的风险。

SQLAlchemy设置外键模型的虚拟外键，有2种方案：

方案1，查询数据时**临时指定逻辑外键**的映射关系：

每次使用都需要声明。

```python
模型类.query.join(模型类,主模型.主键==外键模型.外键).join(模型类,主模型.主键==外键模型.外键).with_entities(字段1,字段2.label("字段别名"),....).all()
```

方案2，在**模型声明时指定逻辑外键的映射关系**(最常用，这种设置方案，在操作模型时与原来默认设置的物理外键的关联操作是一模一样的写法)：

这种写法是可以一直使用的。

```python
"""
创建模型类时，在第三张关系表中的物理外键中添加两个设置
比原来设置物理外建多了两个属性，primaryjoin和foreign_keys，
primaryjoin,  指定2个模型之间的主外键关系，相当于原生SQL语句中的join
foreign_keys，指定外键

# 将主表的主键，和关系表中的关联字段作一个关联
primaryjoin="Student.id==StudentCourse.student_id",
设置哪一个虚拟外间。
foreign_keys="StudentCourse.student_id"
查询时和正常的关联一样，但是查询过程是走的虚拟外键
"""


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import backref
   
    
    
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    """学生信息模型"""
    # 声明与当前模型绑定的数据表名称
    __tablename__ = "td_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    def __repr__(self):
        return f"{self.name}<Student>"


class Course(db.Model):
    """课程数据模型"""
    __tablename__ = "td_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(64), unique=True, comment="课程")
    price = db.Column(db.Numeric(7, 2))

    def __repr__(self):
        return f'{self.name}<{self.__class__.__name__}>'


class StudentCourse(db.Model):
    __tablename__ = "td_student_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    student_id = db.Column(db.Integer, index=True)
    course_id = db.Column(db.Integer, index=True)
    score = db.Column(db.Numeric(4, 1), default=0, comment="成绩")
    time = db.Column(db.DateTime, default=datetime.now, comment="考试时间")
    student = db.relationship(
        "Student",
        uselist=False,
        backref=backref("to_course", uselist=True),
        lazy="subquery",
        # 比原来设置物理外建多了两个属性，primaryjoin和foreign_keys，
        # primaryjoin, 指定2个模型之间的主外键关系，相当于原生SQL语句中的join
        # foreign_keys，指定外键
        primaryjoin="Student.id==StudentCourse.student_id",
        # 设置哪一个虚拟外间。
        foreign_keys="StudentCourse.student_id"
    )

    course = db.relationship(
        "Course",
        uselist=False,
        backref=backref("to_student", uselist=True),
        lazy="subquery",
        primaryjoin="Course.id==StudentCourse.course_id",
        foreign_keys="StudentCourse.course_id"
    )
```



方案1举类，虚拟外键使用的方案1，代码：

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# 配置
app.config.update({
    "DEBUG": True,
    # "SQLALCHEMY_DATABASE_URI": "mysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4",
    # 如果使用pymysql，则需要在连接时指定pymysql
    "SQLALCHEMY_DATABASE_URI": "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4",
    # 动态追踪修改设置，如未设置只会提示警告，设置False即可
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    # ORM执行SQL查询时是哦否显示原始SQL语句，debug模式下可以开启
    "SQLALCHEMY_ECHO": False,
})
db = SQLAlchemy()
db.init_app(app)

# 每个表中没有关联。
class Student(db.Model):
    """学生信息模型"""
    # 声明与当前模型绑定的数据表名称
    __tablename__ = "td_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    def __repr__(self):
        return f"{self.name}<Student>"


class Course(db.Model):
    """课程数据模型"""
    __tablename__ = "td_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(64), unique=True, comment="课程")
    price = db.Column(db.Numeric(7, 2))

    def __repr__(self):
        return f'{self.name}<{self.__class__.__name__}>'


class StudentCourse(db.Model):
    __tablename__ = "td_student_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    student_id = db.Column(db.Integer, index=True)
    course_id = db.Column(db.Integer, index=True)
    score = db.Column(db.Numeric(4, 1), default=0, comment="成绩")
    time = db.Column(db.DateTime, default=datetime.now, comment="考试时间")

    def __repr__(self):
        return f'<{self.__class__.__name__}>'


@app.route("/create")
def create_table():
    db.create_all()  # 为项目中被识别的所有模型创建数据表
    return "ok"


#
#
@app.route("/drop")
def drop_table():
    db.drop_all()  # 为项目中被识别的所有模型删除数据表
    return "ok"


@app.route("/")
def index():
    return "ok"


@app.route("/a1")
def a1():
    # 添加测试数据
    stu0 = Student(name="xiaoming-0", age=15, sex=True, email="xiaoming0@qq.com", money=1000)
    stu1 = Student(name="xiaoming-1", age=15, sex=True, email="xiaoming1@qq.com", money=1000)
    stu2 = Student(name="xiaoming-2", age=15, sex=True, email="xiaoming2@qq.com", money=1000)
    stu3 = Student(name="xiaoming-3", age=15, sex=True, email="xiaoming3@qq.com", money=1000)
    stu4 = Student(name="xiaoming-4", age=15, sex=True, email="xiaoming4@qq.com", money=1000)

    db.session.add_all([stu0, stu1, stu2, stu3, stu4])
    course1 = Course(name="python基础第1季", price=1000)
    course2 = Course(name="python基础第2季", price=1000)
    course3 = Course(name="python基础第3季", price=1000)
    course4 = Course(name="python基础第4季", price=1000)
    course5 = Course(name="python基础第5季", price=1000)
    db.session.add_all([course1, course2, course3, course4, course5])

    data = [
        StudentCourse(student_id=1, course_id=1, score=60, time=datetime.now()),
        StudentCourse(student_id=1, course_id=2, score=60, time=datetime.now()),
        StudentCourse(student_id=1, course_id=3, score=60, time=datetime.now()),
        StudentCourse(student_id=2, course_id=1, score=60, time=datetime.now()),
        StudentCourse(student_id=2, course_id=2, score=60, time=datetime.now()),
        StudentCourse(student_id=3, course_id=3, score=60, time=datetime.now()),
        StudentCourse(student_id=3, course_id=4, score=60, time=datetime.now()),
        StudentCourse(student_id=4, course_id=5, score=60, time=datetime.now()),
        StudentCourse(student_id=4, course_id=1, score=60, time=datetime.now()),
        StudentCourse(student_id=4, course_id=2, score=60, time=datetime.now()),
        StudentCourse(student_id=5, course_id=1, score=60, time=datetime.now()),
        StudentCourse(student_id=5, course_id=2, score=60, time=datetime.now()),
        StudentCourse(student_id=5, course_id=3, score=60, time=datetime.now()),
        StudentCourse(student_id=5, course_id=4, score=60, time=datetime.now()),
    ]
    db.session.add_all(data)
    db.session.commit()

    return "ok"


#
#
@app.route("/q1")
def q1():
    # 查询3号学生购买了那些课程,没有写关联关系,查的比较麻烦.
    # student_list = StudentCourse.query.filter(StudentCourse.student_id == 3).all()
    # print(student_list)
    # name_list = [i.course_id for i in student_list]
    # print(name_list)
    # course_list = Course.query.filter(Course.id.in_(name_list)).all()
    # print(course_list)
    """"""""""""""""""""""""""""""""""""""""""""""""
    # 上面的方式太发麻烦,使用逻辑外建来查询
    # 使用逻辑外键来查询数据,就是给两个表临时建立关联关系.
    # 模型.query.join(从模型类名, 关系语句)
    # 主模型.query.join(从模型类名, 主模型.主键==从模型类名.外键)
    # join是建立关系,with_entities是需要查什么,join可以写多次.
    # 建立Student.id和StudentCourse.student_id的关联关系.
    # data = (Student.query.join(StudentCourse, Student.id == StudentCourse.student_id)
    #         .with_entities(Student.id, Student.name, StudentCourse.student_id).filter(Student.id == 3).all())
    # print(data)
    # 建立Student.id和StudentCourse.student_id的关联关系.和
    data = (Student.query.join(StudentCourse, Student.id == StudentCourse.student_id).join(Course,StudentCourse.course_id==Course.id)
            .with_entities(Student.id, Student.name, StudentCourse.student_id,Course.name).filter(Student.id == 3).all())
    print(data)

    return "ok"
```



方案2举类，虚拟外键使用的方案2，代码：

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.orm import backref

app = Flask(__name__)

# 配置
app.config.update({
    "DEBUG": True,
    # "SQLALCHEMY_DATABASE_URI": "mysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4",
    # 如果使用pymysql，则需要在连接时指定pymysql
    "SQLALCHEMY_DATABASE_URI": "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4",
    # 动态追踪修改设置，如未设置只会提示警告，设置False即可
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    # ORM执行SQL查询时是哦否显示原始SQL语句，debug模式下可以开启
    "SQLALCHEMY_ECHO": False,
})
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    """学生信息模型"""
    # 声明与当前模型绑定的数据表名称
    __tablename__ = "td_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    def __repr__(self):
        return f"{self.name}<Student>"


class Course(db.Model):
    """课程数据模型"""
    __tablename__ = "td_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(64), unique=True, comment="课程")
    price = db.Column(db.Numeric(7, 2))

    def __repr__(self):
        return f'{self.name}<{self.__class__.__name__}>'


class StudentCourse(db.Model):
    __tablename__ = "td_student_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    student_id = db.Column(db.Integer, index=True)
    course_id = db.Column(db.Integer, index=True)
    score = db.Column(db.Numeric(4, 1), default=0, comment="成绩")
    time = db.Column(db.DateTime, default=datetime.now, comment="考试时间")
    student = db.relationship(
        "Student",
        uselist=False,
        backref=backref("to_course", uselist=True),
        lazy="subquery",
        # 比原来设置物理外建多了两个属性，primaryjoin和foreign_keys，
        # primaryjoin, 指定2个模型之间的主外键关系，相当于原生SQL语句中的join
        # foreign_keys，指定外键
        primaryjoin="Student.id==StudentCourse.student_id",
        # 设置哪一个虚拟外间。
        foreign_keys="StudentCourse.student_id"
    )

    course = db.relationship(
        "Course",
        uselist=False,
        backref=backref("to_student", uselist=True),
        lazy="subquery",
        primaryjoin="Course.id==StudentCourse.course_id",
        foreign_keys="StudentCourse.course_id"
    )

    def __repr__(self):
        return f'<{self.student.name}{self.__class__.__name__}>'


@app.route("/create")
def create_table():
    db.create_all()  # 为项目中被识别的所有模型创建数据表
    return "ok"


#
#
@app.route("/drop")
def drop_table():
    db.drop_all()  # 为项目中被识别的所有模型删除数据表
    return "ok"


@app.route("/")
def index():
    return "ok"


@app.route("/a1")
def a1():
    # 添加测试数据
    stu0 = Student(name="xiaoming-0", age=15, sex=True, email="xiaoming0@qq.com", money=1000)
    stu1 = Student(name="xiaoming-1", age=15, sex=True, email="xiaoming1@qq.com", money=1000)
    stu2 = Student(name="xiaoming-2", age=15, sex=True, email="xiaoming2@qq.com", money=1000)
    stu3 = Student(name="xiaoming-3", age=15, sex=True, email="xiaoming3@qq.com", money=1000)
    stu4 = Student(name="xiaoming-4", age=15, sex=True, email="xiaoming4@qq.com", money=1000)

    db.session.add_all([stu0, stu1, stu2, stu3, stu4])
    course1 = Course(name="python基础第1季", price=1000)
    course2 = Course(name="python基础第2季", price=1000)
    course3 = Course(name="python基础第3季", price=1000)
    course4 = Course(name="python基础第4季", price=1000)
    course5 = Course(name="python基础第5季", price=1000)
    db.session.add_all([course1, course2, course3, course4, course5])

    data = [
        StudentCourse(student_id=1, course_id=1, score=60, time=datetime.now()),
        StudentCourse(student_id=1, course_id=2, score=60, time=datetime.now()),
        StudentCourse(student_id=1, course_id=3, score=60, time=datetime.now()),
        StudentCourse(student_id=2, course_id=1, score=60, time=datetime.now()),
        StudentCourse(student_id=2, course_id=2, score=60, time=datetime.now()),
        StudentCourse(student_id=3, course_id=3, score=60, time=datetime.now()),
        StudentCourse(student_id=3, course_id=4, score=60, time=datetime.now()),
        StudentCourse(student_id=4, course_id=5, score=60, time=datetime.now()),
        StudentCourse(student_id=4, course_id=1, score=60, time=datetime.now()),
        StudentCourse(student_id=4, course_id=2, score=60, time=datetime.now()),
        StudentCourse(student_id=5, course_id=1, score=60, time=datetime.now()),
        StudentCourse(student_id=5, course_id=2, score=60, time=datetime.now()),
        StudentCourse(student_id=5, course_id=3, score=60, time=datetime.now()),
        StudentCourse(student_id=5, course_id=4, score=60, time=datetime.now()),
    ]
    db.session.add_all(data)
    db.session.commit()

    return "ok"


@app.route("/q3")
def q3():
    student = Student.query.get(3)
    # print(student)
    data = [
        {
            "course_name": item.course.name,
            "score": item.score,
            "student_name": item.student.name, } for item in student.to_course]
    print(data)
    return "ok"


if __name__ == '__main__':
    app.run()

```



# 数据迁移

- 在开发过程中，需要修改数据库模型，而且还要在修改之后更新数据库。最直接的方式就是删除旧表，但这样会丢失数据，所以往往更常见的方式就是使用alter来改变数据结构，原有数据中的新字段值设置默认值或null=True.
- 更好的解决办法是使用数据迁移，它可以追踪数据库表结构的变化，然后把变动应用到数据库中。
- 在Flask中可以使用Flask-Migrate的第三方扩展，来实现数据迁移。并且集成到Flask终端脚本中，所有操作通过flask db 命令就能完成。
- 为了导出数据库迁移命令，Flask-Migrate提供了一个MigrateCommand类，可以附加到flask框架中。

首先要在虚拟环境中安装Flask-Migrate。

```py
pip install Flask-Migrate
```

官网地址：https://flask-migrate.readthedocs.io/en/latest/

Flask-Migrate的使用

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# 引入Migrate ，并实例化这个类。
# 下面这两句和migrate = Migrate(app, db)是一样的。
# migrate = Migrate()
# migrate.init_app(app, db)
```

完整代码

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
class Config(object):
    DEBUG = True
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    #使用的mysqldb
    #SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4"
    #使用的pymysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flask_orm?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ORM运行时会显示ORM生成的原始SQL语句[调试]
    SQLALCHEMY_ECHO = False


app.config.from_object(Config)
db = SQLAlchemy(app=app)
# 初始化数据迁移,
migrate = Migrate(app, db)

class StudentCourse(db.Model):
    __tablename__ = "Migrate_table_student_course"
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    sid=db.Column(db.Integer, db.ForeignKey("Migrate_table_student.id"),comment="学生表的外建")
    cid=db.Column(db.Integer, db.ForeignKey("Migrate_table_course.id"),comment="课程表的外建")
    # 
    created_time = db.Column(db.DateTime, default=datetime.now, comment="购买时间")
    # 关联属性
    student = db.relationship("Student", uselist=False, backref=backref("to_relation", uselist=True))
    course = db.relationship("Course", uselist=False,backref=backref("to_relation", uselist=True))



class Student(db.Model):
    """学生信息模型"""
    # 声明与当前模型绑定的数据表名称
    __tablename__ = "Migrate_table_student"
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    # email = db.Column(db.String(128), comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    def __repr__(self):
        return f"{self.name},{self.__class__.__name__}"


class Course(db.Model):
    """课程数据模型"""
    __tablename__ = "Migrate_table_course"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(64), unique=True, comment="课程")
    price = db.Column(db.Numeric(7, 2), default=0.0, comment="价格")

    def __repr__(self):
        return f"{self.name},{self.__class__.__name__}"

@app.route("/index")
def index():
    return "ok"



if __name__ == "__main__":
    app.run()
```

## 创建迁移版本仓库

```py
# 切换到项目根目录下
cd ~/Desktop/flaskdemo
# 设置flask项目的启动脚本位置，例如我们现在的脚本叫manage.py
export FLASK_APP=manage.py
# 数据库迁移初始化，这个命令会在当前项目根目录下创建migrations文件夹，将来所有数据表相关的迁移文件都放在里面。
flask db init
```

执行完flask db init会创建一个文件夹叫`migrations`。

![截图 2023-11-23 16-12-29](D:\笔记\Flask\assets\截图 2023-11-23 16-12-29.png)

## 创建迁移版本

- 自动创建迁移版本文件中有两个函数，用于进行数据迁移同步到数据库操作的。
    - upgrade()：把迁移中的改动代码同步到数据库中。
    - downgrade()：则将改动代码从数据库中进行还原。
- 自动创建的迁移脚本会根据模型定义和数据库当前状态的差异，生成upgrade()和downgrade()函数的内容。
- 生成的迁移文件不一定完全正确，有可能代码中存在细节遗漏导致报错，需要开发者进行检查，特别在多对多的时候

```py
# 根据flask项目的模型生成迁移文件 -m的后面你不要使用中文！！
# 类似git 的新建一个版本。 
flask db migrate -m 'initial migration'
# 这里等同于django里面的 makemigrations，生成迁移版本文件
# 执行上面的代码：
# 1. 在migrations/versions生成一个数据库迁移文件，migrations就是我们执行了 init后创建出的文件夹。
# 2. 如果是首次生成迁移文件的项目，则迁移工具还会在数据库创建一个记录数据库版本的version表
```

## 升级版本库的版本

把当前ORM模型中的代码改动同步到数据库。

```bash
# 从migations目录下的versions中根据迁移文件upgrade方法把数据表的结构同步到数据库中。
flask db upgrade
```

## 降级版本库的版本

```bash
# 从migations目录下的versions中根据迁移文件downgrade把数据表的结构同步到数据库中。
flask db downgrade
```

## 版本库的历史管理

可以根据history命令找到版本号,然后传给downgrade命令:

```bash
flask db history

输出格式：<base> ->  版本号 (head), initial migration
```



## 回滚到指定版本

```bash
flask db downgrade # 默认返回上一个版本
flask db downgrade 版本号   # 回滚到指定版本号对应的版本
flask db upgrade 版本号     # 升级到指定版本号对应的版本
```



## 数据迁移的步骤：

```bash
1. 初始化数据迁移的目录
export FLASK_APP=manage.py
flask db init

2. 数据库的数据迁移版本初始化，生成迁移文件
flask db migrate -m 'initial migration'

3. 升级版本[新增一个迁移记录]
flask db upgrade 

4. 降级版本[回滚一个迁移记录]
flask db downgrade
```

**注意：使用数据库迁移的过程中，无论是upgrade还是downgrade只会影响表的结构，不会对源代码的模型造成影响。所有执行了回滚后，还需要开发者，自己修改源代码。**





# 常用模块

## Faker

自动添加测试数据。

文档: https://faker.readthedocs.io/en/master/locales/zh_CN.html

批量生成测试数据: https://github.com/joke2k/faker

```bash
pip install faker -i https://pypi.douban.com/simple
```

代码：

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random,click
from faker import Faker
app = Flask(__name__)

class Config(object):
    DEBUG = True
    # 数据库连接配置
    # SQLALCHEMY_DATABASE_URI = "数据库类型://数据库账号:密码@数据库地址:端口/数据库名称?charset=utf8mb4"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@127.0.0.1:3306/flask_orm?charset=utf8mb4"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = False

app.config.from_object(Config)

db = SQLAlchemy(app=app)

class Student(db.Model):
    """学生信息模型"""
    __tablename__ = "db_student"
    id = db.Column(db.Integer, primary_key=True,comment="主键")
    name = db.Column(db.String(15), comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), comment="邮箱地址")
    money = db.Column(db.Numeric(10,2), default=0.0, comment="钱包")

    def __repr__(self):
        return f"{self.name}<Student>"

# 自定义批量生成学生

# 自定义终端命令
@app.cli.command("faker_user")     # 指定终端命令的调用名称
@click.argument("num", default=5, type=int)  # 命令的选项
def faker_user_command(num):
    """生成测试学生信息"""
    faker = Faker(locale="ZH_CN")
    for i in range(num):
        sex = bool( random.randint(0,1) )
        student = Student(
            name= faker.name_male() if sex else faker.name_female(),
            age=random.randint(15,60),
            sex=sex,
            email=faker.free_email(),
            money= float( random.randint(100,100000) / 100 ),
        )
        db.session.add(student)
    # 在循环外面统一提交
    db.session.commit()

@app.route("/")
def index():
    return "ok"

if __name__ == '__main__':

    app.run()


"""
export FLASK_APP=manage.py
flask faker-user 10
"""
```

## flask-session

flask-session，允许设置session到指定的存储空间中，例如：redis/mongoDB/mysql。

文档: https://flask-session.readthedocs.io/en/latest/

```
pip install Flask-Session
pip install flask-redis  -i https://pypi.douban.com/simple
```

```py
Flask         2.3.0
flask-redis   0.4.0
Flask-Session 0.5.0

在flask的设置总SESSION_USE_SIGNER=True就会报错，
```



使用session之前,必须配置一下配置项:

```python
# session秘钥
app.config["SECRET_KEY"] = "*(%#4sxcz(^(#$#8423"
```

### 将session存到sqlalchemy中

需要手动创建session表，在项目第一次启动的时候，使用`db.create_all()`来完成创建。

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 引入session存储驱动类
from flask_session import Session
# 引入sessio操作类，注意：引入路径不同，大小写不同的。
from flask import session
#
from flask_session import Session as SessionStore

app = Flask(__name__, template_folder="templates", static_folder="static")
db = SQLAlchemy()

# 实例化session存储类
session_store = Session()

# 配置
app.config.update({
    "DEBUG": True,
    # 使用session之前,必须配置一下秘钥
    "SECRET_KEY": "*(%#4sxcz(^(#$#8423",
    # 要把存储到SQLAlchemy，必须配置数据库连接
    # "SQLALCHEMY_DATABASE_URI": "数据库类型://数据库账号:密码@数据库地址:端口/数据库名称?charset=utf8mb4"
    "SQLALCHEMY_DATABASE_URI" : "mysql+pymysql://root:123@127.0.0.1:3306/flaskdemo?charset=utf8mb4",    # 动态追踪修改设置，如未设置只会提示警告
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    # 查询时会显示原始SQL语句
    "SQLALCHEMY_ECHO": False,

    # 把session通过SQLAlchmey保存到mysql中
    "SESSION_TYPE": "sqlalchemy",  # session类型为sqlalchemy
    "SESSION_SQLALCHEMY": db,  # SQLAlchemy的数据库连接对象
    "SESSION_SQLALCHEMY_TABLE": 'db_session',  # session要保存的表名称
    "SESSION_PERMANENT": True,    # 如果设置为True，则关闭浏览器session就失效
    "SESSION_KEY_PREFIX": "session:"  # session数据表中sessionID的前缀，默认就是 session:
})

db.init_app(app)

# 务必保证在数据库配置初始化以后才进行session存储类的初始化
session_store.init_app(app)


# 如果要把session保存到数据库中，则必须先执行db.create_all() 让数据库提前创建session表。否则使用session时报错。
"""
使用这个，或者直接使用路由，创建表，不能直接进去http://127.0.0.1:5000/，会报错的。
    with app.app_context():
        db.create_all()
"""
@app.route("/create")
def create_table():
    db.create_all()  # 为项目中被识别的所有模型创建数据表
    return "ok"


@app.route("/drop")
def drop_table():
    db.drop_all()  # 为项目中被识别的所有模型删除数据表
    return "ok"

@app.route("/")
def index():
    return "ok"

@app.route("/set")
def set_session():
    session["uname"] = "xiaoming"
    session["age"] = 18
    return "ok"

@app.route("/get")
def get_session():
    print(session.get("uname"))
    print(session.get("age"))
    return "ok"

@app.route("/del")
def del_session():
    # 此处的删除，不是删除用户对应的session表记录，而是删除session值而已。
    print(session.pop("uname"))
    print(session.pop("age"))
    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
```









### 将session存到redis中

这样是不会报错的。可以将redis存到session中

```py
from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = "*(%#4sxcz(^(#$#8423"
SESSION_TYPE = 'redis'
app.config["SECRET_KEY"] = "*(%#4sxcz(^(#$#8423"
app.config.from_object(__name__)
Session(app)


@app.route('/set')
def set():
    session['name'] = 'shenzehao'
    session['age'] = 22
    session['class'] = 202
    session['JUZ'] = "OK"
    session['qqq'] = "qqq"
    session['aaa'] = "aaa"
    return 'ok'


@app.route('/get')
def get():
    print(session.get('name', 'not set'))
    print(session.get('age', 'not set'))
    print(session.get('class', 'not set'))
    print(session.get('JUZ', 'not set'))
    print(session.get('qqq', 'not set'))
    print(session.get('aaa', 'not set'))
    return session.get('name', 'not set')


@app.route("/")
def index():
    return "ok"


if __name__ == "__main__":
    app.run()

```


session可以保存到session中，

```py
from flask import Flask,session
from flask_redis import FlaskRedis
from flask_session import Session

# 实例化
app = Flask(__name__)



session_redis = FlaskRedis(config_prefix="SESSION")
user_redis = FlaskRedis(config_prefix="USER")
order_redis = FlaskRedis(config_prefix="ORDER")

app.config.update({
    "DEBUG": True,
    # 使用session之前,必须配置一下秘钥
    "SECRET_KEY": "*xcz(^(#$#8423",
    # 创建三个redis库分别村不同的数据
    # 存session
    "SESSION_URL": "redis://:@127.0.0.1:6379/1",
    # 存用户
    "USER_URL": "redis://:@127.0.0.1:6379/2",
    #  存订单
    "ORDER_URL": "redis://:@127.0.0.1:6379/4",

    # 把session保存到redis中
    "SESSION_TYPE": "redis",  # session类型为sqlalchemy
    "SESSION_PERMANENT": True,  # 如果设置为True，则关闭浏览器session就失效
    # 下面的这个设置打开就会报错。
    # "SESSION_USE_SIGNER": True,  # 是否对发送到浏览器上session的cookie值进行添加签名，防止串改。
    "SESSION_KEY_PREFIX": "session:",  # session数据表中sessionID的前缀，默认就是 session:
    # session保存数据到redis时启用的链接对象
    "SESSION_REDIS": order_redis,  # 用于连接redis的配置
})

# 初始化 flask_redis
session_redis.init_app(app)
user_redis.init_app(app)
order_redis.init_app(app)

Session(app)



@app.route("/")
def index():
    return "ok"


@app.route("/create1")
def q2():
    user_redis.setnx("name", "shen")
    user_redis.setnx("age", 21)
    return "添加成功"


@app.route("/create2")
def create_data():
    # 存到session_redis中
    session_redis.setnx("class", 100)
    # 存在user_redis中
    user_redis.setnx("name", "shenzhao")
    order_redis.setnx("age", 22)
    return "ok"


@app.route("/set")
def set_session():
    session["name"]="shenzhao123"
    session["age"]="123"
    return "ok"

@app.route("/get")
def get_session():
    print(session.get("name","没有这个"))
    print(session.get("age", "没有这个"))
    return "ok"

if __name__ == '__main__':
    app.run()

```

# 蓝图 Blueprint

简单来说，Blueprint 是一个存储视图方法/模型代码的容器（目录），这些操作在这个Blueprint 被注册到flask的APP实例对象应用之后就可以被调用，Flask 可以通过Blueprint来组织URL以及处理客户端请求的视图。

Flask使用Blueprint让应用实现模块化，在Flask中Blueprint具有如下属性：

- 一个项目可以具有多个Blueprint
- 可以将一个Blueprint注册到任何一个未使用的URL下比如 “/”、“/sample”或者子域名，也就是说每一个蓝图都可以像django那样有属于自己的路由前缀
- 在一个flask项目中，同一个BluePrint模块可以注册多次，也就是说一个蓝图可以对应多个不同的url地址。
- Blueprint目录可以保存单独属于自己的模板目录保存自己的模板文件、静态文件或者其它的通用操作方法，它并不是必须要实现应用的视图和函数的
- 在一个flask项目初始化时，就应该要注册需要使用的Blueprint，否则项目不识别Blueprint蓝图

注意：flask中的Blueprint并不是一个完整的项目应用，它不能独立运行，而必须要把蓝图blueprint注册到某一个flask项目中才能使用。

**就是：帮助flask目录结构的划分。类似django中的创建app，方便管理，**

## 蓝图的使用

![截图 2023-11-24 20-51-50](D:\笔记\Flask\assets\截图 2023-11-24 20-51-50.png)

蓝图的使用，使用完django非常的像

创建一个文件夹必须要`__init__`就是创建一个包，比如`users`

在users包中的`__init__`中写

```py
from flask import Blueprint
from . import views

# 等同于 app = Flask(__name__)，只是这里并非一个独立的flask项目，所以需要在第一个参数中，指定蓝图名称，其他参数与之前实例化app应用对象是一样的。
users_Blueprint=Blueprint("users",__name__)


users_Blueprint.add_url_rule(rule="/login",view_func=views.login)
users_Blueprint.add_url_rule(rule="/logout",view_func=views.logout)

```

在users包中写创建一个视图函数`views`。

在users包中的`views.py`中写

```py
def login():
    return "login,用户登陆函数"


def logout():
    return "logout,用户退出函数"

```

在根目录下创建`manage.py`，是flask的入口文件。

```py
from flask import Flask
from users import users_Blueprint

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(users_Blueprint, url_prefix='/users')

@app.route("/")
def index():
    return "我是ok"


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
```

上面的三个文件就和django的很像，一个文件是总的路由，一个文件是路由分发，一个文件是视图文件。



## 蓝图运行机制

- 蓝图Blueprint实际上的作用就是，充当当前蓝图目录下的所有视图和url路由地址的绑定关系的临时容器
- 在视图函数被蓝图的add_url_rule方法注册时,这个操作本质就是将视图和url地址的映射关系添加到蓝图的子路由列表deferred_functions中。
- 蓝图对象根本没有路由表，当我们在蓝图中的视图函数上调用route装饰器（或者add_url_role函数）注册路由时,它只是在蓝图对象的内部的deferred_functions（子路由列表）中添加了一个路由项（路由项实际上就是一个绑定了视图和url地址的lambda匿名函数）
- 当执行app.register_blueprint()注册蓝图时，app应用实例对象会将从蓝图对象的 deferred_functions列表中循环取出每一个之前注册的路由项，并把app应用实例对象自己作为参数执行路由项对应的lambda匿名函数，lambda匿名函数执行以后就会调用app.add_url_rule() 方法，这就将蓝图下子路由列表之前暂存的路由全部添加到了app应用实例对象的url_map总路由表中了，所以用户就可以在flask中访问到了蓝图中的视图。当然，能访问蓝图下的视图，自然也就可以通过视图调用其他的功能，例如：蓝图下的其他功能函数或其他的模型对象了。



## 蓝图的url拼接

当我们在app应用实例对象上注册一个蓝图时，可以指定一个url_prefix关键字参数（这个参数默认是/）

![image-20220105173129138](D:\笔记\Flask\assets\image-20220105173129138.png)

在app应用实例对象的最终的路由表 url_map中，在蓝图上注册的路由URL自动被加上了这个路由前缀，这个可以保证在多个蓝图中使用相同的子路由而不会最终引起冲突，只要在注册蓝图时将不同的蓝图挂接到不同的自路径即可。

注意：有了蓝图以后，在flask使用url_for在使用时，如果要生成一个蓝图里面的视图对应的路由地址，则需要声明当前蓝图名称+视图名称

```python
# url_for('蓝图名称.视图函数名')
url_for('users.login') # /users + /login   /users就是蓝图中的路由前缀  /login就是子路由
```

users/views.py，代码：

```python
from flask import url_for


def login():
    return "用户登录视图"


def register():
    print(url_for("users.login"))
    return "用户注册视图"

```

访问：

![image-20220105173329978](D:\笔记\Flask\assets\image-20220105173329978.png)



## 注册蓝图下的静态文件[很少使用]

和app应用对象不同，蓝图对象创建时不会默认注册静态目录的路由。需要我们在创建时手动指定 static_folder 参数。

下面的代码将蓝图所在目录下的static_users目录设置为静态目录

`users/__init__.py`,代码：

```python
from flask import Blueprint
from . import views

# 等同于 app = Flask(__name__)，只是这里并非一个独立的flask项目，所以需要在第一个参数中，指定蓝图名称，其他参数与之前实例化app应用对象是一样的。
users_blueprint = Blueprint("users", __name__, static_folder="static")
# users_blueprint = Blueprint('users',__name__,static_folder="users_static")

# 给蓝图注册视图与绑定视图的路由，路由必须以/斜杠开头
users_blueprint.add_url_rule("/login", view_func=views.login)
users_blueprint.add_url_rule("/reg", view_func=views.register)

# 子路由
print(users_blueprint.deferred_functions)
```

![image-20220105180218123](D:\笔记\Flask\assets\image-20220105180218123.png)

现在就可以使用http://127.0.0.1:5000/users/static/images/avatar.jpg 访问users/static/目录下的静态文件了.

当然，也可以修改访问静态文件的路径 ：可以在创建蓝图对象时使用 static_url_path 来改变静态目录的url地址。

```python
from flask import Blueprint
from . import views

# 等同于 app = Flask(__name__)，只是这里并非一个独立的flask项目，所以需要在第一个参数中，指定蓝图名称，其他参数与之前实例化app应用对象是一样的。
users_blueprint = Blueprint("users", __name__, static_folder="static", static_url_path="/assets")
# users_blueprint = Blueprint('users',__name__,static_folder="users_static")

# 给蓝图注册视图与绑定视图的路由，路由必须以/斜杠开头
users_blueprint.add_url_rule("/login", view_func=views.login)
users_blueprint.add_url_rule("/reg", view_func=views.register)

# 子路由
print(users_blueprint.deferred_functions)
```

现在就可以使用http://127.0.0.1:5000/users/static/assets/avatar.jpg访问users/static/目录下的静态文件了.

![image-20220105180417738](D:\笔记\Flask\assets\image-20220105180417738.png)



## 设置蓝图下的html模版[很少使用]

创建蓝图中的模板目录templates，`users/__init__.py`，代码：

```python
from flask import Blueprint
from . import views

# 等同于 app = Flask(__name__)，只是这里并非一个独立的flask项目，所以需要在第一个参数中，指定蓝图名称，其他参数与之前实例化app应用对象是一样的。
users_blueprint = Blueprint("users", __name__, static_folder="static", static_url_path="/assets", template_folder="templates")
# users_blueprint = Blueprint('users',__name__,static_folder="users_static")

# 给蓝图注册视图与绑定视图的路由，路由必须以/斜杠开头
users_blueprint.add_url_rule("/login", view_func=views.login)
users_blueprint.add_url_rule("/reg", view_func=views.register)

# 子路由
print(users_blueprint.deferred_functions)
```

视图`users/views.py`，代码：

```python
from flask import url_for
from flask import render_template

def login():
    title = "用户登录视图"
    return render_template("login.html", **locals())


def register():
    print(url_for("users.login"))
    return "用户注册视图"

```

模板代码，`users/templates/index.html`，代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>{{ title }}</h1>
</body>
</html>
```

![image-20220105181038194](D:\笔记\Flask\assets\image-20220105181038194.png)

注意：如果公司使用了flask1.x版本，则不能出现项目根目录下和蓝图目录下2个templates目录的情况，否则项目根目录下的templates模板会覆盖蓝图目录下的同名模板，flask会优先加载项目根目录下的模板。@app.route(rule="/index",methods=["GET","POST"])

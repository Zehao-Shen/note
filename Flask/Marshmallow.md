# Marshmallow

官方文档：https://marshmallow.readthedocs.io/en/latest/

Marshmallow，中文译作：棉花糖。是一个轻量级的数据格式转换的模块，也叫序列化和反序列化模块，常用于将复杂的orm模型对象与python原生数据类型之间相互转换。marshmallow提供了丰富的api功能。如下：

>   1.  **Serializing**
>
>       序列化[可以把数据对象转化为可存储或可传输的数据类型，例如：objects/object->list/dict，dict/list->string]
>
>   2.  **Deserializing**
>
>       反序列化器[把可存储或可传输的数据类型转换成数据对象，例如：list/dict->objects/object，string->dict/list]
>
>   3.  **Validation**
>
>       数据校验，可以在反序列化阶段，针对要转换数据的内容进行类型验证或自定义验证。

Marshmallow本身是一个单独的库，基于我们当前项目使用框架是flask并且数据库ORM框架使用SQLAlchemy，所以我们可以通过安装flask-sqlalchemy和marshmallow-sqlalchemy集成到项目就可以了。

## 基本安装和配置

模块安装：

```bash
pip install -U marshmallow-sqlalchemy
pip install -U flask-sqlalchemy
pip install -U flask-marshmallow
```

Marshmallow模块快速使用，单独创建一个python文件进行基本的使用，main.py：

```python
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:123@127.0.0.1:3306/mofang?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    username = db.Column(db.String(255), index=True, comment="用户名")
    password = db.Column(db.String(255), comment="登录密码")
    mobile = db.Column(db.String(15), index=True, comment="手机号码")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(255), index=True, comment="邮箱")
    created_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    updated_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.name,self.username)


@app.route("/")
def index():
    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=5555)
```



## 基本构造器(Schema)

也可以叫基本模式类或基本序列化器类。

marshmallow转换数据格式主要通过构造器类（序列化器）来完成。在marshmallow使用过程中所有的构造器类必须直接或间接继承于Schema基类，而Schema基类提供了数据转换的基本功能：序列化，验证数据和反序列化。



### 基于Schema完成数据序列化转换

```python
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.update({
    "DUBUG": True,
    "SQLALCHEMY_DATABASE_URI": "mysql+pymysql://root:123@127.0.0.1:3306/mofang?charset=utf8mb4",
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
})

db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow()
ma.init_app(app)


class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    username = db.Column(db.String(255), index=True, comment="用户名")
    password = db.Column(db.String(255), comment="登录密码")
    mobile = db.Column(db.String(15), index=True, comment="手机号码")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(255), index=True, comment="邮箱")
    created_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    updated_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.name, self.username)


from marshmallow import Schema, fields


class UserSchema(Schema):
    username = fields.String()
    mobile = fields.String()
    sex = fields.Boolean()
    email = fields.Email()
    created_time = fields.DateTime()
    updated_time = fields.DateTime()


@app.route("/")
def index():
    return "ok"


@app.route("/add-data")
def add():
    for i in range(10):
        user = User(
            username=f"shenzehao{i}",
            password=123456 + i,
            mobile=12345678910 + i,
            sex=True,
            email=f"123456789{i}@qq.com",
        )
    print("添加成功")
    return "添加成功"


@app.route("/2")
def index2():
    user1 = User.query.get(1)
    user2 = User.query.get(2)
    user3 = User.query.get(3)
    user4 = User.query.filter(User.id > 2).all()
    us = UserSchema()

    """序列化成一个字典"""
    result = us.dump(user1)
    print(result, type(result))

    """序列化器成一个字符串[符合json语法]"""
    result = us.dumps(user1)
    print(result, type(result))

    # 如果要序列化多个模型对象，可以使用many=True
    result = us.dump([user1, user2, user3], many=True)   	  # 可放多个对象，
    print(result)
    result = us.dump(user4, many=True)                        # 也可以方一个对象，里面有多条数据。
    for i in result:
        print(i, type(i))
    result = us.dumps([user1, user2, user3], many=True)
    print(result)
    return "查询成功"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)

```



**schema常用属性数据类型**

| 类型                                                         | 描述                                     |
| ------------------------------------------------------------ | ---------------------------------------- |
| fields.[`Dict`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Dict)(keys, type]] = None, values, …) | 字典类型，常用于接收json类型数据         |
| fields.[`List`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.List)(cls_or_instance, type], **kwargs) | 列表类型，常用于接收数组数据             |
| fields.[`Tuple`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Tuple)(tuple_fields, *args, **kwargs) | 元组类型                                 |
| fields.[`String`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.String)(*, default, missing, data_key, …) | 字符串类型                               |
| fields.[`UUID`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.UUID)(*, default, missing, data_key, …) | UUID格式类型的字符串                     |
| fields.[`Number`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Number)(*, as_string, **kwargs) | 数值基本类型                             |
| fields.[`Integer`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Integer)(*, strict, **kwargs) | 整型                                     |
| fields.[`Decimal`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Decimal)(places, rounding, *, allow_nan, …) | 数值型                                   |
| fields.[`Boolean`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Boolean)(*, truthy, falsy, **kwargs) | 布尔型                                   |
| fields.[`Float`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Float)(*, allow_nan, as_string, **kwargs) | 浮点数类型                               |
| fields.[`DateTime`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.DateTime)(format, **kwargs) | 日期时间类型                             |
| fields.[`Time`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Time)(format, **kwargs) | 时间类型                                 |
| fields.[`Date`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Date)(format, **kwargs) | 日期类型                                 |
| fields.[`Url`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Url)(*, relative, schemes, Set[str]]] = None, …) | url网址字符串类型，自带url地址的校验规则 |
| fields.[`Email`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Email)(*args, **kwargs) | 邮箱字符串类型，自带email地址的校验规则  |
| fields.[`IP`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.IP)(*args[, exploded]) | IP地址字符串类型                         |
| fields.[`IPv4`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.IPv4)(*args[, exploded]) | IPv4地址字符串类型                       |
| fields.[`IPv6`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.IPv6)(*args[, exploded]) | IPv6地址字符串类型                       |
| fields.[`Method`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Method)(serialize, deserialize, **kwargs) | 基于Schema类方法返回值的字段             |
| fields.[`Function`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Function)(serialize, Any], Callable[[Any, …) | 基于函数返回值得字段                     |
| fields.[`Nested`](https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Nested)(nested, type, str, Callable[[], …) | 嵌套类型或外键类型                       |

**Schema数据类型的常用通用属性**

| 属性名             | 描述                                                         |
| ------------------ | ------------------------------------------------------------ |
| **default**        | 序列化阶段中设置字段的默认值                                 |
| **missing**        | 反序列化阶段中设置字段的默认值                               |
| **validate**       | 反序列化阶段调用的内置数据验证器或者内置验证集合             |
| **required**       | 反序列化阶段调用的，设置当前字段的必填字段                   |
| **allow_none**     | 反序列化阶段调用的，是否允许为空                             |
| **load_only**      | 是否在反序列化阶段才使用到当前字段，相当于drf框架的write_only |
| **dump_omly**      | 是否在序列化阶段才使用到当前字段，相当于drf框架的read_only   |
| **error_messages** | 使用校验值validate选项以后设置的错误提示，字典类型，可以用来替代默认的字段异常提示语，格式：<br>error_messages={“required”: “用户名为必填项。”} |



#### 构造器嵌套使用

```python
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123@127.0.0.1:3306/mofang?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)


"""模仿ORM的模型"""
class Model(object):
    pass

class User(Model):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()
        self.books = []    			# 用来代替MySQL中的外建关系，实现1对多或多对多
        self.friends = []  			# 用来代替MySQL中的外建关系，实现自关联


class Book(Model):
    def __init__(self, title, author):
        self.title = title
        self.author = author  		# 用来代替MySQL中的外键关系，1对1

"""序列化器"""
from marshmallow import Schema, fields


class UserSchema(Schema):
    """用户的序列化器"""
    name = fields.String()
    email = fields.Email()
    """1对多，多对多"""
    # 在fields.Nested外围包裹一个List列表字段，则可以返回多个结果了。exclude表示排除
    # books = fields.List(fields.Nested(lambda: BookSchema(exclude=["author"])))
    # 简写方式:
    books = fields.Nested(lambda : BookSchema(many=True, exclude=["author"]))
    """自关联"""
    # 自关联就是一个模型中既存在主键关系，也存在外键关系的情况
    # 方式1：使用自身"self"作为外键的方式，并可以指定序列化模型的多个字段
    friends = fields.Nested(lambda: "self", only=("name", "email", "books"), many=True)
    # 方式2：使用Pluck字段可以用单个值来替换嵌套的数据，只可以得到模型的单个字段值
    # friends = fields.Pluck(lambda: "self", "name", many=True)

class BookSchema(Schema):
    """图书的序列化器"""
    title = fields.String()
    author = fields.Nested(lambda: UserSchema(exclude=["books"]))

@app.route("/1")
def index1():
    """构造器嵌套使用"""
    # 假设根据当前作者，查找对应的作者发布的图书列表
    user0 = User(name="南派三叔", email="sanshu@163.com")
    user1 = User(name="南派三叔", email="sanshu@163.com")
    user2 = User(name="南派三叔", email="sanshu@163.com")
    book1 = Book(title="盗墓笔记1", author=user0)
    book2 = Book(title="盗墓笔记2", author=user1)
    book3 = Book(title="盗墓笔记3", author=user2)
    user0.books = [book1, book2, book3]
    # user0.friends=[user0,user1,user2]

    us = UserSchema()
    result = us.dump(user0)
    print(result)

    bs = BookSchema()
    result = bs.dump([book1, book2, book3], many=True)
    print(result)

    return "ok"


@app.route("/2")
def index2():
    """自关联"""
    user0 = User(name="南派三叔", email="sanshu@163.com")
    user1 = User(name="刘慈欣", email="sanshu@163.com")
    user2 = User(name="天下霸唱", email="sanshu@163.com")
    user0.friends = [user1, user2]
    us = UserSchema()
    result = us.dump(user0)
    print(result)
    return "ok"




if __name__ == '__main__':
    app.run(debug=True, port=5555)
```



### 基于Schema完成数据反序列化转换

```python
"""
validate 是marshMallow内置校验器模块，提供了部分内置写好的验证规则。
validate.Length 字符串长度验证，或者文件内容长度验证
validate.Range  数值范围验证
validate.Regexp 正则验证，底层使用的是python内置的re模块
validate.OneOf  选项取值，通过choices选项指定值只能是其中一个
validate.Email    邮箱规则校验，底层实际上就是一个邮箱的正则校验
validate.URL      网址规则校验，底层实际上就是一个网址的正则校验
validate.Equal    判断是否与指定的值相等
"""
```



代码：

```python
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123@127.0.0.1:3306/mofang?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)

"""序列化器"""
from marshmallow import Schema, fields, validate, ValidationError
from datetime import datetime

"""模仿ORM的模型"""
class Model(object):
    pass

class User(Model):
    def __init__(self, name, age, role, email, mobile):
        self.name = name
        self.age = age
        self.role = role
        self.email = email
        self.mobile = mobile


class UserSchema(Schema):
    """用户的序列化器"""
    # required = True, 设置当前字段为必填项
    name = fields.String(required=True, validate=validate.Length(min=3, max=16,
                                                                 error="用户名有误！name必须在{min}~{max}个字符长度之间"))
    age = fields.Integer(load_only=True,
                         validate=validate.Range(min=12, max=55, error="用户年龄必须在{min}~{max}岁之间!"))
    role = fields.String(
        validate=validate.OneOf(choices=["老师", "学生", "路人"], error="身份只能在{choices}中选择其中一个！"))
    email = fields.Email(validate=validate.Email(error="邮件格式有误！！"))
    mobile = fields.String(validate=validate.Regexp(regex="1[3-9]\d{9}", error="手机号格式有误！"))


@app.route("/1")
def index1():
    """反序列化"""
    # 模拟客户端提交过来的数据
    user_data = {"name": "xiao", "role": "老师", "email": "ronnie@stones.com", "age": 12, "mobile": "13311234455"}
    # 因为name设置了required=True,其字段可以不写。
    # user_data={"name": "xiao"}
    us = UserSchema()
    # try:
    #     # 校验一个数据
    #     result = us.load(user_data)
    #     print("校验通过，校验结果result=", result)
    # except ValidationError as e:
    #     return f"校验失败：{e}"

    data_list = [user_data, user_data, user_data]
    try:
        # 校验多个数据
        result = us.load(data_list, many=True)
        print("校验通过，校验结果result=", result)
    except ValidationError as e:   # ValidationError是marshmallow导入的
        return f"校验失败：{e}"

    return "ok"
"""一个序列化类既可以序列化也可以反序列化"""
@app.route("/2")
def index():
    user=User(name="shenzeaho",age=3,role="老师",email="1234567@qq.com",mobile=12345678910)
    us=UserSchema()
    print(user.age)
    res=us.dump(user)
    print(res,type(res))
    return "ok"
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)

```



#### 基于内置验证器进行数据验证

| 内置验证器                                                   | 描述            |
| ------------------------------------------------------------ | --------------- |
| validate.[`Email`](https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#marshmallow.validate.Email)(*, error) | 邮箱验证        |
| validate.[`Equal`](https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#marshmallow.validate.Equal)(comparable, *, error) | 判断值是否相等  |
| validate.[`Length`](https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#marshmallow.validate.Length)(min, max, *, equal, error) | 值长度/大小验证 |
| validate.[`OneOf`](https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#marshmallow.validate.OneOf)(choices, labels, *, error) | 选项验证        |
| validate.[`Range`](https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#marshmallow.validate.Range)([min, max]) | 范围验证        |
| validate.[`Regexp`](https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#marshmallow.validate.Regexp)(regex, bytes, Pattern][, flags]) | 正则验证        |
| validate.[`URL`](https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#marshmallow.validate.URL)(*, relative, schemes, Set[str]]] = None, …) | 验证是否为URL   |

代码：

```python
from marshmallow import Schema, fields, validate, ValidationError
class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))
    age = fields.Int(validate=validate.Range(min=18, max=40))

if __name__ == '__main__':
    data = {"name": "", "permission": "hello", "age": 71}
	try:
    	UserSchema().load(data)
	except ValidationError as err:
    	print(err.messages)  # err.messages就是上面的错误信息。
```



#### 反序列化时对指定部分字段忽略不校验

```python
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123@127.0.0.1:3306/mofang?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)

"""序列化器"""
from marshmallow import Schema, fields, validate, ValidationError

class UserSchema(Schema):
    """用户的序列化器"""
    name = fields.String(required=True, validate=validate.Length(min=3, max=16, error="用户名有误！name必须在{min}~{max}个字符长度之间"))
    age = fields.Integer(required=True)
    avatar = fields.String(required=True, error_messages={"required": "avatar必须填写！"})

@app.route("/1")
def index1():
    """反序列化时对部分字段进行忽略不校验"""
    # 模拟客户端提交的数据
    user_data = {"name": "xiaoming", "age": 12}
    us = UserSchema()
    result = us.load(user_data, partial=["avatar"])    # partial=["xxx"]的设置可以让这个字段校验
    print(result)
    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)
```



#### 设置指定字段只在序列化或反序列化阶段才启用

就是设置序列化器中的字段只读(dump_only，相当于drf的read_only)或只写(load_only，相当于drf的write_only)

```python
import re
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123@127.0.0.1:3306/mofang?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)

"""模型"""


class Model(object):
    pass


class User(Model):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.created_time = datetime.now()


"""序列化器"""
from marshmallow import Schema, fields, validate, ValidationError


class UserSchema(Schema):
    username = fields.String()
    password = fields.String(required=True, load_only=True)  # 相当于只写字段 "write-only"
    created_time = fields.DateTime(dump_only=True)  # 相当于只读字段 "read-only"


@app.route("/1")
def index1():
    """设置指定字段只能用于序列化或反序列化中"""
    # 反序列化阶段
    user_data = {"username": "xiaoming", "password": "123456"}
    us = UserSchema()
    result = us.load(user_data)
    print(result)

    # 序列化阶段
    # user = User(username="xiaohong", password="123456")
    # us = UserSchema()
    # result = us.dump(user)
    # print(result)

    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)

```



#### MarshMallow提供的钩子方法

marshmallow提供了6个钩子在反序列化或者序列化阶段时自动执行，这些钩子都是以装饰器的形式提供出来的。

```bash
# 序列化之前执行的钩子方法
pre_dump([fn，pass_many]) 注册要在序列化对象之前调用的方法，它会在序列化对象之前被调用。
# 序列化之后执行的钩子方法
post_dump([fn，pass_many，pass_original]) 注册要在序列化对象后调用的方法，它会在对象序列化后被调用。

# 反序列化之前执行的钩子方法
pre_load([fn，pass_many]) 在反序列化对象之前，注册要调用的方法，它会在验证数据之前调用
# 反序列化之后执行的钩子方法
post_load([fn，pass_many，pass_original]) 注册反序列化对象后要调用的方法，它会在验证数据之后被调用。

# 校验指定字段的装饰器，相当于drf的 单字段校验 validate_<字段名>(data)
validates(field_name)

# 校验整个构造器中所有数据的装饰器，相当于drf的全字段校验 validate(data)
validates_schema([fn, pass_many, ...])
```

```python
import re
from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123@127.0.0.1:3306/mofang?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)

"""假装模型模型"""
class Model(object):
    pass


class User(Model):
    def __init__(self, username, password, avatar):
        self.username = username
        self.password = password
        self.avatar = avatar
        self.created_time = datetime.now()
        self.views_count = 0

    def __str__(self):
        return f"<{self.__class__.__name__} [{self.username}]>"


"""序列化器"""
from marshmallow import Schema, fields, validate, ValidationError, \
    pre_dump, pre_load, post_dump, post_load, validates, validates_schema
from werkzeug.security import generate_password_hash, check_password_hash


class UserSchema(Schema):
    username = fields.String()
    password = fields.String(required=True, load_only=True)  # 相当于只写字段 "write-only"
    avatar = fields.String()
    re_password = fields.String(required=True)
    created_time = fields.DateTime(dump_only=True)  # 相当于只读字段 "read-only"

    # pass_many 表示是否接受传递进来的many参数
    # @pre_dump(pass_many=True)
    # def pre_dump(self, instance, many, **kwargs):
    #     """序列化之前自动执行的钩子函数"""
    #     """instance就是上面的User类"""
    #     print("序列化之前，instance是模型对象，从数据库拿到数据，返回给客户端时，对数据进行预处理。")
    #     print(instance.avatar)  # 数据库中的数据。 /1.png
    #     print("many",many)      # False
    #     instance.avatar = f"//{request.environ['HTTP_HOST']}{instance.avatar}"
    #     print(instance.avatar)  # 修改后的数据    //127.0.0.1:5555/1.png
    #     # 此处可以调用模型对象，保存或操作模型数据，保存到数据库
    #     instance.views_count = instance.views_count + 1
    #     return instance

    # @post_dump(pass_many=True)
    # def post_dump(self, data, many, **kwargs):
    #     """序列化之后自动执行的钩子函数"""
    #     print("序列化之后，data是字典，对服务端要返回给客户端的数据进行预处理")
    #     # 此处无法调用到模型对象
    #     # data是序列化后的字典
    #     print(data)             # {'username': '小明', 'avatar': '/1.png', 'created_time': '2023-12-14T20:34:16.541041'}
    #     data["test"] = "abc"    # 给序列化后的字典中添加数据
    #     print(data)             # {'username': '小明', 'avatar': '/1.png', 'created_time': '2023-12-14T20:34:16.541041', 'test': 'abc'}
    #     return data

    # @pre_load(pass_many=True)
    # def pre_load(self, data, *args, **kwargs):
    #     """反序列化之前，校验数据之前的钩子操作"""
    #     print("反序列化之前，data是字典，对客户端提交的数据进行校验前的调整或修改")
    #     print(f"保存上传文件：data['avatar']={data['avatar']}")
    #     print("执行pre_load前", data["avatar"])
    #     data["avatar"] = f"//{request.environ['HTTP_HOST']}/{data['avatar']}"
    #     print("执行pre_load后", data["avatar"])
    #     return data

    # @post_load(pass_many=True)
    # def post_load(self, data, *args, **kwargs):
    #     """反序列化之后，校验数据之后的钩子操作"""
    #     print("反序列化之前，data是字典，一般在这个钩子里面进行数据库的操作，把字典转换成模型")
    #     print(data)
    #     data.pop("re_password")                                                 # 例如删除不必要的字段
    #     print(data)
    #     data["password"] = generate_password_hash(password=data["password"])    # 例如密码加密，
    #     user = User(**data)                                                     # 加密后添加到数据库中
    #     return user

    # @validates(field_name="username")
    # def validates1(self, data):
    #     """单字段校验：校验的字段名必须写在装饰器，与函数名没有什么关系"""
    #     print(f"username={data}")
    #     if data == "root":
    #         raise ValidationError(message="用户名不能叫root！！！", field_name="username")
    #     return data


    # @validates(field_name="avatar")
    # def validates2(self, data):
    #     """单字段校验：校验的字段名必须写在装饰器，与函数名没有什么关系2"""
    #     print(f"avatar={data}")
    #     type_list = ["png", "jpeg", "jpg"]
    #     if data.split(".")[-1] not in type_list:
    #         raise ValidationError(message=f"头像格式有误！只允许使用{type_list}之中的一种格式！！！！", field_name="username")
    #     return data

    @validates_schema(pass_many=True)
    def validates_schema(self, data, *args, **kwargs):
        """全字段校验："""
        print(f"data={data}")
        # 多个字段之间进行相互校验，例如：密码与确认密码
        if data["password"] != data["re_password"]:
            raise ValidationError(message="密码与确认密码不一致！", field_name="password")
        return data


@app.route("/1")
def index1():
    """marshmallow提供的钩子操作"""
    # 模拟从数据库得到的模型对象
    # user = User(username="小明", password="123456", avatar="/1.png")
    # us = UserSchema()
    # result = us.dump(user)
    # print("result",result)
    # print("user.views_count",user.views_count)
    # return "ok"

    # 模拟客户端提交过来的数据
    user_data = {"username": "roo", "password": "123456", "re_password": "1123456", "avatar": "2.png"}
    us = UserSchema()
    res = us.load(user_data)
    print(res)
    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)

```



## 模型构造器(ModelSchema)

类似drf提供的ModelSerializer，ModelSchema主要是方便开发者可以方便的操作数据库的。

官方提供了**SQLAlchemyAutoSchema**和**SQLAlchemySchema**这2个模型构造类提供给我们用于编写模型构造器。

官方文档：https://github.com/marshmallow-code/marshmallow-sqlalchemy

​                   https://marshmallow-sqlalchemy.readthedocs.io/en/latest/



### SQLAlchemySchema

```python
import re
from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123@127.0.0.1:3306/mofang?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)


class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    username = db.Column(db.String(255), index=True, comment="用户名")
    password = db.Column(db.String(255), comment="登录密码")
    mobile = db.Column(db.String(15), index=True, comment="手机号码")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(255), index=True, comment="邮箱")
    created_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    updated_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.username)

"""模型类序列化器"""
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields
from marshmallow import post_load


class UserModelSchema(SQLAlchemySchema):
    """
    SQLAlchemySchema提供了一个auto_field方法可以自动从模型中提取当前对应字段声明信息到构造器中，
    但是，我们需要手动声明序列化器中调用的哪些字段，每一个都要写上
    """
    id = auto_field()
    username = auto_field()
    password = auto_field(load_only=True)
    mobile = auto_field()
    email = auto_field()
    created_time = auto_field()
    sex = auto_field()

    class Meta:
        model = User                # 设置当前序列化器绑定操作的模型对象
        load_instance = True        # 是否在序列化器中自动实例化模型实例对象

@app.route("/1")
def index1():
    """模型类构造器：SQLAlchemySchema"""
    # 模拟客户端提交的数据
    # user_data1 = {'username': '小明', 'email': '123@qq.com',"password": "123456", 'sex': True, 'mobile': '13312345678'}
    # user_data2 = {'username': '小红', 'email': '456@qq.com',"password": "123456", 'sex': False, 'mobile': '13355545678'}
    # user1 = User(**user_data1)
    # user2 = User(**user_data2)
    # db.session.add_all([user1, user2])
    # db.session.commit()

    """序列化一个数据"""
    # 读取数据库中的用户
    # user = User.query.get(1)
    # us = UserModelSchema()
    # data = us.dump(user)
    # print(data)

    # """序列化多个数据"""
    # user_list = User.query.all()
    # us = UserModelSchema()
    # data = us.dump(user_list, many=True)
    # print(data)

    # """反序列化一个数据"""
    # user_data = {'username': '小辉', 'email': '123@qq.com', "password": "123456", 'sex': True, 'mobile': '13312345678'}
    # us = UserModelSchema()
    # user = us.load(user_data, session=db.session)
    # db.session.add(user)
    # db.session.commit()
    # print(user)

    """反序列化多个数据"""
    # user_data = {'username': '小辉', 'email': '123@qq.com', "password": "123456", 'sex': True, 'mobile': '13312345678'}
    # us = UserModelSchema()
    # user_list = us.load([user_data, user_data, user_data], session=db.session, many=True)
    # db.session.add_all(user_list)
    # db.session.commit()
    # print(user_list)



    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)

```



### SQLAlchemyAutoSchema

```python
import re
from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field, fields
from marshmallow import post_load

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:123@127.0.0.1:3306/yingming?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)


class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    username = db.Column(db.String(255), index=True, comment="用户名")
    password = db.Column(db.String(255), comment="登录密码")
    mobile = db.Column(db.String(15), index=True, comment="手机号码")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(255), index=True, comment="邮箱")
    created_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    updated_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.username)


"""模型类序列化器"""
class UserModelSchema(SQLAlchemyAutoSchema):
    password = auto_field(load_only=True)

    class Meta:
        model = User
        include_relationships = True  # 输出模型对象时同时对外键，是否也一并进行处理，True表示一并进行序列化器，用于针对序列化器嵌套调用的情况
        include_fk = True  # 序列化阶段是否也一并返回主键
        sqla_session = db.session  # 数据库连接会话对象，针对在钩子装饰器中如果希望调用db数据库回话对象，可以在此处声明完成以后，使用时通过sql_session直接调用
        fields = ["id", "username", "mobile", "email", "created_time", "sex", "password"]

    @post_load(pass_many=True)
    def post_load(self, data, *args, **kwargs):
        if type(data) is list:
            """批量添加模型"""
            instance = []
            for item in data:
                instance.append(self.Meta.model(**item))
            self.session.add_all(instance)
        else:
            """单个添加模型"""
            instance = self.Meta.model(**data)
            self.session.add(instance)
        self.session.commit()
        return instance

@app.route("/1")
def index1():
    """模型类构造器：SQLAlchemyAutoSchema"""
    # """序列化一个数据"""
    # user = User.query.get(1)
    # us = UserModelSchema()
    # data = us.dump(user)
    # print(data)

    # """序列化多个数据"""
    # user_list = User.query.all()
    # us = UserModelSchema()
    # data = us.dump(user_list, many=True)
    # print(data)


    """反序列化一个数据"""
    user_data = {'email': '123@qq.com', 'username': 'xiaoming', 'sex': True, 'mobile': '13312345678', 'password': '56566666'}
    us = UserModelSchema()
    instance = us.load(user_data)
    print(instance)

    # """反序列化多个数据"""
    # user_data = {'email': '123@qq.com', 'username': 'xiaoming', 'sex': True, 'mobile': '13312345678', 'password': '56566666'}
    # us = UserModelSchema()
    # instance_list = us.load([user_data, user_data, user_data], many=True)
    # print(instance_list)

    return "ok"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5555)

```


drf用于django的前后端分离的

# 1.api接口

应用程序编程接口（Application Programming Interface，API接口），就是应用程序对外提供了一个操作数据的入口，这个入口可以是一个函数或类方法，也可以是一个url地址或者一个网络地址。当客户端调用这个入口，应用程序则会执行对应代码操作，给客户端完成相对应的功能。

当然，api接口在工作中是比较常见的开发内容，有时候，我们会调用其他人编写的api接口，有时候，我们也需要提供api接口给其他人操作。由此就会带来一个问题，api接口往往都是一个函数、类方法、或者url或其他网络地址，不断是哪一种，当api接口编写过程中，我们都要考虑一个问题就是这个接口应该怎么编写？接口怎么写的更加容易维护和清晰，这就需要大家在调用或者编写api接口的时候要有一个明确的编写规范！！！



为了在团队内部形成共识、防止个人习惯差异引起的混乱，我们都需要找到一种大家都觉得很好的接口实现规范，而且这种规范能够让后端写的接口，用途一目了然，减少客户端和服务端双方之间的合作成本。

目前市面上大部分公司开发人员使用的接口实现规范主要有：restful、RPC。

RPC（ Remote Procedure Call ）: 翻译成中文:远程过程调用[远程服务调用]. 从字面上理解就是访问/调用远程服务端提供的api接口。这种接口一般以服务或者过程式代码提供。

+ 服务端提供一个**唯一的访问入口地址**：http://api.xxx.com/ 或 http://www.xx.com/api 或者基于其他协议的地址

+ 客户端请求服务端的时候，所有的操作都理解为**动作**(action)，一般web开发时，对应的就是HTTP请求的post请求

+ 通过**请求体**参数，指定要调用的接口名称和接口所需的参数

  action=get_all_student&class=301&sex=1

  m=get_all_student&sex=1&age=22

  command=100&sex=1&age=22

+ 基本上现有rpc的数据格式：protobuf（gRPC）、json、xml

rpc接口多了,对应函数名和参数就多了,前端在请求api接口时难找.对于年代久远的rpc服务端的代码也容易出现重复的接口

restful: 翻译成中文: 资源状态转换.(表征性状态转移)

+ 把服务端提供的所有的数据/文件都看成资源， 那么通过api接口请求数据的操作，本质上来说就是对资源的操作了.

  因此，restful中要求，我们把当前接口对外提供哪种资源进行操作，就把**资源的名称写在url地址**。

  /students/

  /avatars/

+ web开发中操作资源，最常见的最通用的无非就是增删查改，所以restful要求在地址栏中声明要操作的资源是什么。然后通过**http请求动词**来说明对该资源进行哪一种操作.

  POST http://www.xxx.com/api/students/   添加学生数据

  GET    http://www.xxx.com/api/students/   获取所有学生

  DELETE http://www.xxx.com/api/students/<pk>/   删除id=pk的一个学生

  PUT   http://www.xxx.com/api/students/<pk>/       修改一个学生的全部信息 [id,name,sex,age,]

  PATCH  http://www.xxx.com/api/students/<pk>/    修改一个学生的部分信息[age]

也就是说，我们仅需要通过url地址上的资源名称结合HTTP请求动作，就可以说明当前api接口的功能是什么了。

**restful是以资源为主的api接口规范，体现在地址上就是资源就是以名词表达。**

**rpc则以动作为主的api接口规范，体现在接口名称上往往附带操作数据的动作。**

# 2. RESTful API规范



REST全称是Representational State Transfer，中文意思是表述（编者注：通常译为表征）性状态转移。 它首次出现在2000年Roy Fielding的博士论文中。

RESTful是一种专门为Web 开发而定义API接口的设计风格，尤其适用于前后端分离的应用模式中。

而对于数据资源分别使用POST、DELETE、GET、UPDATE等请求动作来表达对数据的增删查改。

| GET      | /students      | 获取所有学生       |
| -------- | -------------- | ------------------ |
| 请求方法 | 请求地址       | 后端操作           |
| POST     | /students      | 增加学生           |
| GET      | /students/<pk> | 获取编号为pk的学生 |
| PUT      | /students/<pk> | 修改编号为pk的学生 |
| DELETE   | /students/<pk> | 删除编号为pk的学生 |

restful规范是一种通用的规范，不限制语言和开发框架的使用。事实上，我们可以使用任何一门语言，任何一个框架都可以实现符合restful规范的API接口。

参考文档：http://www.runoob.com/w3cnote/restful-architecture.html

## 幂等性

接口实现过程中，会存在**幂等性**。所谓幂等性是指代**客户端发起多次同样请求时，是否对于服务端里面的资源产生不同结果**。如果**多次请求**，服务端**结果**还是**一样**，则属于**幂等接口**，如果多次请求，服务端产生结果是不一样的，则属于非幂等接口。

| 请求方式  | 是否幂等 | 是否安全 |
| --------- | -------- | -------- |
| GET       | 幂等     | 安全     |
| POST      | 不幂等   | 不安全   |
| PUT/PATCH | 幂等     | 不安全   |
| DELETE    | 幂等     | 不安全   |

# 3. 序列化

api接口开发，最核心最常见的一个代码编写过程就是序列化，所谓序列化就是把**数据转换格式**。常见的序列化方式：

json，pickle，base64，struct，….

序列化可以分两个阶段：

**序列化**： 把我们识别的数据转换成指定的格式提供给别人。

例如：我们在django中获取到的数据默认是模型对象，但是模型对象数据无法直接提供给前端或别的平台使用，所以我们需要把数据进行序列化，变成字符串或者json数据，提供给别人。

**反序列化**：把别人提供的数据转换/还原成我们需要的格式。

例如：前端js提供过来的json数据，对于python而言json就是字符串，我们需要进行反序列化换成字典，然后接着字典再进行转换成模型对象，这样我们才能把数据保存到数据库中。



# 4. Django Rest Framework

> ```python
> GET    /demo/student/      获取所有学生信息 
> POST   /dome/student/      添加一个学生信息
> 
> GET   /demo/student/<pk>   获取一个学生信息 
> PUT   /demo/student/<pk>   更新一个学生信息
> DELETE /demo/student/<pk>  删除一个学生信息
> # drf就是主要就是提供了这5个接口。
> ```

核心思想: 大量缩减编写api接口的代码

Django REST framework是一个建立在Django基础之上的Web 应用开发框架，可以快速的开发REST API接口应用。在REST framework中，提供了序列化器Serialzier的定义，可以帮助我们简化序列化与反序列化的过程，不仅如此，还提供丰富的类视图、扩展类、视图集来简化视图的编写工作。REST framework还提供了认证、权限、限流、过滤、分页、接口文档等功能支持。REST framework还提供了一个调试API接口 的Web可视化界面来方便查看测试接口。

中文文档：https://q1mi.github.io/Django-REST-framework-documentation/#django-rest-framework

github: https://github.com/encode/django-rest-framework/tree/master

### 特点

- 提供了定义序列化器Serializer的方法，可以快速根据 Django ORM 或者其它库自动序列化/反序列化；
- 提供了丰富的类视图、Mixin扩展类，简化视图的编写；
- 丰富的定制层级：函数视图、类视图、视图集合到自动生成 API，满足各种需要；
- 多种身份认证和权限认证方式的支持；[jwt]
- 内置了限流系统；
- 直观的 API web 界面；【方便我们调试开发api接口】
- 可扩展性，插件丰富

# 5. 环境安装与配置

```bash
pip install djangorestframewor
```

DRF需要以下依赖：

- Python (3.5 以上)
- Django (2.2 以上)

**DRF是以Django子应用的方式提供的，所以我们可以直接利用已有的Django环境而无需从新创建。（若没有Django环境，需要先创建环境安装Django）**

#  6.添加rest_framework应用

在**settings.py**的**INSTALLED_APPS**中添加'rest_framework'。

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

在项目中如果使用rest_framework框架实现API接口，主要有以下三个步骤：

- 将请求的数据（如JSON格式）转换为模型类对象
- 操作数据库
- 将模型类对象转换为响应的数据（如JSON格式）

# 6.创建序列化器-Serializer

## 6.1创建序列化器的常见参数

**常用字段类型**：

| 字段                    | 字段构造方式                                                 |
| ----------------------- | ------------------------------------------------------------ |
| **BooleanField**        | BooleanField()                                               |
| **NullBooleanField**    | NullBooleanField()                                           |
| **CharField**           | CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace(是否去掉两边空格)=True) |
| **EmailField**          | EmailField(max_length=None, min_length=None, allow_blank(是否为空)=False) |
| **RegexField**          | RegexField(regex, max_length=None, min_length=None, allow_blank=False) |
| **SlugField**           | SlugField(max*length=50, min_length=None, allow_blank=False) 正则字段，验证正则模式 [a-zA-Z0-9*-]+ |
| **URLField**            | URLField(max_length=200, min_length=None, allow_blank=False) |
| **UUIDField**           | UUIDField(format='hex_verbose')  format:  1) `'hex_verbose'` 如`"5ce0e9a5-5ffa-654b-cee0-1238041fb31a"`  2） `'hex'` 如 `"5ce0e9a55ffa654bcee01238041fb31a"`  3）`'int'` - 如: `"123456789012312313134124512351145145114"`  4）`'urn'` 如: `"urn:uuid:5ce0e9a5-5ffa-654b-cee0-1238041fb31a"` |
| **IPAddressField**      | IPAddressField(protocol='both', unpack_ipv4=False, **options) |
| **IntegerField**        | IntegerField(max_value=None, min_value=None)                 |
| **FloatField**          | FloatField(max_value=None, min_value=None)                   |
| **DecimalField**        | DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None) max_digits: 最多位数 decimal_palces: 小数点位置 |
| **DateTimeField**       | DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None) |
| **DateField**           | DateField(format=api_settings.DATE_FORMAT, input_formats=None) |
| **TimeField**           | TimeField(format=api_settings.TIME_FORMAT, input_formats=None) |
| **DurationField**       | DurationField()                                              |
| **ChoiceField**         | ChoiceField(choices) choices与Django的用法相同               |
| **MultipleChoiceField** | MultipleChoiceField(choices)                                 |
| **FileField**           | FileField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
| **ImageField**          | ImageField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
| **ListField**           | ListField(child=, min_length=None, max_length=None)          |
| **DictField**           | DictField(child=)                                            |

**选项参数：**

| 参数名称            | 作用             |
| ------------------- | ---------------- |
| **max_length**      | 最大长度         |
| **min_lenght**      | 最小长度         |
| **allow_blank**     | 是否允许为空     |
| **trim_whitespace** | 是否截断空白字符 |
| **max_value**       | 最小值           |
| **min_value**       | 最大值           |

通用参数：

| 参数名称           | 说明                                          |
| ------------------ | --------------------------------------------- |
| **read_only**      | 表明该字段仅用于序列化输出，默认False         |
| **write_only**     | 表明该字段仅用于反序列化输入，默认False       |
| **required**       | 表明该字段在反序列化时必须输入，默认True      |
| **default**        | 反序列化时使用的默认值                        |
| **allow_null**     | 表明该字段是否允许传入None，默认False         |
| **validators**     | 该字段使用的验证器                            |
| **error_messages** | 包含错误编号与错误信息的字典                  |
| **label**          | 用于HTML展示API页面时，显示的字段名称         |
| **help_text**      | 用于HTML展示API页面时，显示的字段帮助提示信息 |

## 6.2序列化

作用：

```
1. 序列化,序列化器会把模型对象转换成字典,经过response以后变成json字符串
2. 反序列化,把客户端发送过来的数据,经过request以后变成字典,序列化器可以把字典转成模型
3. 反序列化,完成数据校验功能
```

作用：

例如，在django项目中创建学生子应用。

```python
python manage.py startapp students
```

配置这个students应用和数据库

`models`
在数据库中手动添加数据

```python
from django.db import models


# Create your models here.
class Student(models.Model):
    """学生信息"""
    name = models.CharField(max_length=255, verbose_name="姓名")
    sex = models.BooleanField(default=1, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    classmate = models.CharField(max_length=5, verbose_name="班级编号")
    description = models.TextField(max_length=1000, verbose_name="个性签名")

    class Meta:
        db_table = "tb_students"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
```

在syudents应用目录中新建serializers.py用于保存该应用的序列化器。
序列化和反序列化可以在一个类下。

`serializers`      

```python
from rest_framework import serializers
"""
serializers 是drf提供给开发者调用的序列化器模块类
里面是声明了所有的可用序列化器的基类
Serializer         序列化器基类，drf中所有的序列化器类都必须继承Serializer
ModelSerializer    模型序列化器类，是序列化器基类的子类，在工作中除了Serializer基类以外，最长用的序列化器类基类
"""
class Stuend1Serializer(serializers.Serializer):
    """学生信息序列化器"""
    # 1. 转换的字段声明
    # 字段 = serializers.字段类型(选项=选项值)
    id=serializers.IntegerField()
    name=serializers.CharField()
    sex=serializers.BooleanField()
    age=serializers.IntegerField()
    description=serializers.CharField()
    # 2. 如果序列化器集成的是ModelSerializer，则需要声明调用的模型信息

    # 3. 验证代码

    # 4. 编写添加和更新模型的代码
```

`views`

```python
import json
from django.shortcuts import render
from django.views import View
from .serializers import Stuend1Serializer
from django.http.response import JsonResponse
# Create your views here.
from .models import Student

class StudentView(View):
    def get(self,request):
        """序列化器-序列化阶段的调用"""
        """序列化多个转换对象 many=True """
        # 1.获取数据集
        student_list=Student.objects.all()
        # 2.实例化序列化器，得到序列化对象 序列化多个需要many=True，一个不用
        serializer=Stuend1Serializer(instance=student_list,many=True)
        # 3.调用序列化对象的data属性方法获取转换后的数据
        data=serializer.data
        # 4.响应数据
        return JsonResponse(data=data,status=200,safe=False,json_dumps_params={"ensure_ascii":False})

    def get(self,request):
        """序列化器-序列化阶段的调用"""
        """序列化一个转换对象"""
        # 1.获取数据集
        student_list=Student.objects.first()
        # 2.实例化序列化器，得到序列化对象 序列化多个需要many=True，一个不用
        serializer=Stuend1Serializer(instance=student_list)
        # 3.调用序列化对象的data属性方法获取转换后的数据
        data=serializer.data
        # 4.响应数据
        return JsonResponse(data=data,status=200,safe=False,json_dumps_params={"ensure_ascii":False})
```

`usrls`

在总路由配置

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sers/',include("sers.urls"))
]
```

在局部配置

```python
from django.urls import path
from . import views

urlpatterns=[
    path('student',views.StudentView.as_view()),
]
```

## 6.3反序列化

在syudents应用目录中新建serializers.py用于保存该应用的序列化器。
序列化和反序列化可以在一个类下。

`serializers`    

```python
class Stuend1Serializer(serializers.Serializer):
    """学生信息序列化器"""
    # 1. 转换的字段声明
    # 字段 = serializers.字段类型(选项=选项值)
    id=serializers.IntegerField(read_only=True)   # read_only=True 在客户端提交数据(反序列化阶段不会要求字段有值)
    name=serializers.CharField(required=True)     # required=True 反序列化比填
    sex=serializers.BooleanField(default=True)    # default=True  反序列化阶段客户端没有提交，则默认为Ture
    age=serializers.IntegerField(max_value=100,min_value=0,error_messages={"min_value":"The age filed must be 0<=age<=100"}) # age在反序列化阶段必须是 0<=age<=100    error_messages=报错时的提示
    description=serializers.CharField(allow_null=True,allow_blank=True)   # 允许客户端不填写内容(None)，或者值为""
    # 2. 如果序列化器集成的是ModelSerializer，则需要声明调用的模型信息

    # 3. 验证代码
    def validate_name(self, attrs):
        """验证单个字段
        方法名的格式必须以 validate_<字段名>为名称",否则序列化器不识别!
        validate开头的方法,会自动被is_valid调用
        attrs就是客户端传来的name数据"""
        print(f"name:{attrs}")
        if attrs in ["python","django"]:
            raise serializers.ValidationError(detail="学生姓名名不能是python或者django",code="validate_name")
        return attrs  # 没有写返回值时,name会时None.
    def validate(self,data):
        """
        验证客户端的所有数据,
        类似:密码和确认密码,只能在validate方法中校验
        validate是固定的方法名
        参数:data,是在序列化实例化的data选项数据
        """
        if data["name"]=="shenzeaho" and data["age"]== 21:
            raise serializers.ValidationError(detail="就是不让你加入",code="validate")
        return data
    # 4. 编写添加和更新模型的代码
```

`views`

```python
class StudentView1(View):    
    def get3(self,request):
        """反序列化-采用字段选项来验证数据"""
        # 1.接受客户端提交的数据
        # 模拟来自客户端的数据
        data={
            "name":"shenzehao",
            "age":12,
            "sex":True,
            "classname":"201",
            "description":"这个人很懒",
        }
        # data=json.dumps(request.body)
        # 2.实例化序列化器，获取实例化对象
        serializer=Stuend1Serializer(data=data)
        # 3.调用序列化器进行数据验证。
        ret=serializer.is_valid()
        # 4.验证数据获取验证以后的结果
        if ret:
            print(serializer.validated_data)
            return JsonResponse(dict(serializer.validated_data))
        else:
            print(serializer.errors)
            return JsonResponse(dict(serializer.errors))
        # 5.操作数据库
        # 6.返回数据
        # return JsonResponse({})

    def get(self,request):
        """反序列化-采用字段选项来验证数据"""
        # 1.接受客户端提交的数据
        # data=json.dumps(request.body)
        # 模拟来自客户端的数据
        data={
            "name":"shenzeaho",
            "age":22,
            "sex":True,
            "classname":"201",
            "description":"这个人很懒",
        }
        # 2.实例化序列化器，获取实例化对象
        serializer=Stuend1Serializer(data=data)
        # 3.调用序列化器进行数据验证。
        serializer.is_valid(raise_exception=True)  # 页面抛出异常(直接出黄色框)不在向下运行.
        # 4.验证数据获取验证以后的结果
        print(serializer.validated_data)
        # 5.操作数据库
        # 6.返回数据
        return JsonResponse({})
```

### 6.3.1数据的修改和添加

#### 添加数据

路由和上面的序列化一样

`serializers`   

```python
def create(self, validated_data):
    """添加数据
    添加数据操作，方法名固定为create，固定参数validated_data就是验证成功以后的结果"""
    # validated_data就是前端传入的数据。
    student = Student.objects.create(**validated_data)
    return student
```

`views`

```python
class StudentView1(View):
    def get5(self,request):
        """反序列化-验证成功后让数据入库"""
        # 1.接受客户端提交的数据
        # 模拟来自客户端的数据
        data={
            "name":"shenzeaho",
            "age":22,
            "sex":True,
            "classmate":"201",
            "description":"这个人很懒",
        }
        # data=json.dumps(request.body)
        # 2.实例化序列化器，获取实例化对象
        serializer=Stuend1Serializer(data=data)
        # 3.调用序列化器进行数据验证。
        serializer.is_valid(raise_exception=True)  # 页面抛出异常(直接出黄色框)不在向下运行.
        # 4.验证数据获取验证以后的结果，操作数据库
        serializer.save()   # 会根据实例化序列化器的时候，石头传入instance属性来自动调用create或者update方法，传入instance属性，自动调用update方法，没有传入instacne，会自动调用create方法。
        # 5.返回数据
        return JsonResponse(data=serializer.validated_data,status=201,json_dumps_params={"ensure_ascii":False})
```

#### 修改数据

`views`

```python
def get(self,request):
    """反系列化--验证数据以后更新数据库"""
    # 1.根据客户端访问的url地址，获取pk值
    pk=1
    try:
        student=Student.objects.get(pk=pk)
    except:
        return JsonResponse({"errors":"当前学生不存在！"},status=400)
    # 2.接受客户端提交的数据
    # 模拟来自客户端的数据
    data={
        "name":"cao",
        "age":22,
        "sex":True,
        "classmate":203,
        "description":"这个人很懒",
    }
    # 3.修改操作中的实例化序列化对象
    serializer=Stuend1Serializer(instance=student,data=data)
    # 4.验证数据
    serializer.is_valid(raise_exception=True)
    # 5.入库
    serializer.save() # 会根据实例化序列化器的时候，石头传入instance属性来自动调用create或者update方法，传入instance属性，自动调用update方法，没有传入instacne，会自动调用create方法。
    # 返回结果
    return JsonResponse(serializer.data,status=201)
```

`serializers`

```python
def update(self, instance, validated_data):
    """
    更新数据操作
    方法名是固定为update
    固定参数instance，实例化序列化器对象时，必须传入模型对象
    固定参数validated_data就是验证成功以后的结果。
    更新数据时就自动实现从字典变成模型对象的过程
    """
    print(instance)  # 模型类对象
    print(validated_data)   # 修改后的全部数据
    instance.name = validated_data["name"]
    instance.age = validated_data["age"]
    instance.sex = validated_data["sex"]
    instance.classmate = validated_data["classmate"]
    instance.description = validated_data["description"]
    instance.save()  # 调用模型对象的save方法，和视图中的serialzier.save()不是同一个类的方法
    return instance
```

#### 6.3.2 附加说明

1） 在对序列化器进行save()保存时，可以额外传递数据，这些数据可以在create()和update()中的validated_data参数获取到

```python
# request.user 是django中记录当前登录用户的模型对象
serializer.save(owner=request.user)
```

2）默认序列化器必须传递所有required的字段，否则会抛出验证异常。但是我们可以使用partial参数来允许部分字段更新

```python
# Update `comment` with partial data
serializer = CommentSerializer(comment, data={'content': u'foo bar'}, partial=True)
```

# 7.模型类序列化器-ModelSerializer

ModelSerializer与常规的Serializer相同，但提供了：

- 基于模型类自动生成一系列字段
- 基于模型类自动为Serializer生成validators，比如unique_together
- 包含默认的create()和update()的实现

`serializers`

```python
class StuendModelSerializer(serializers.ModelSerializer):
    """学生信息序列化器"""
    # 1.转换字段声明
    nickname = serializers.CharField(read_only=True)

    # 2. 如果序列化器集成的是ModelSerializer，则需要声明调用的模型信息。
    # 必须给Mate声明两个属性
    class Meta():
         # model = 模型             # 必填
        # fields= 字段列表         # 必填  `__all__`表名包含所有字段
        # read_only_fields = []   # 选填，只读字段列表，表示设置的字段只会在序列化阶段采用。
        # extra_kwargs={          # 选填  字段额外选项声明。
        #     "字段名":{
        #         "选项":选项值
        #     }
        # }
        # exclude = ('image',)    和fields的意思相反(使用exclude可以明确排除掉哪些字段)
        model = Student
        fields = ["id", "name", "age", "sex", "nickname", "classmate","description"]
        extra_kwargs = {
            "age": {
                "max_value": 20,
                "min_value": 5,
                "error_messages": {
                    "min_value": "年龄最小值必须大于等于5",
                    "max_value": "年龄最大值不能超过20"
                }
            }
        }
        read_only_fields=["id",""]
    # def create(self, validated_data):
    #     """ModelSerializer的源码中有添加数据的代码，
    #     但是我们可以重写create的方法"""
    #     pass
    # def update(self, instance, validated_data):
    #     """ModelSerializer的源码中有更新数据的代码，
    #     但是我们可以重写update的方法"""
    #     pass
```

views中的代码，导包后将Stuend1Serializer变成StuendModelSerializer其他的不变.

# 8.http请求响应

代码：

`views`

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class StudentAPIView(APIView):
    def get(self, request):
        print("drf",request.data)
# 这个的request，是属于drf单独声明的请求处理对象，与django提供的HttpRequset不是同一个，甚至可以说毫无关系。
        print(request.data)
        print(request.query_params)
        print(request._request)
        # 获取请求体
        return Response({"msg": "OK"})
    def post(self, request):
        """添加数据
        获取请求体数据"""

        return Response({"msg":"OK"},status=status.HTTP_200_OK)
```

路由

总路由

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('req/', include("req.urls")),]
```

局部路由

```python
from django.urls import path
from . import views
urlpatterns = [
    path("students/",views.StudentAPIView.as_view())
]
```

记住在settings中配置

```python
INSTALLED_APPS = [
	"sers",
    "req",
    "rest_framework"

]
```



内容协商：drf在django原有的基础上，新增了一个request对象继承到了APIVIew视图类，并在django原有的HttpResponse响应类的基础上实现了一个子类rest_framework.response.Response响应类。这两个类，都是基于内容协商来完成数据的格式转换的。

request->parser解析类->识别客户端请求头中的Content-Type来完成数据转换成->类字典(QueryDict，字典的子类)

response->renderer渲染类->识别客户端请求头的"Accept"来提取客户端期望的返回数据格式，-> 转换成客户端的期望格式数据

![image-20211020101829885](https://s2.loli.net/2022/08/13/JlxmuPGNK4Hhbfi.png)

## 8.1 Request

```python
from rest_framework.views import APIView
```

framework提供的扩展了HttpRequest类的**Request**类的对象。

REST framework 提供了**Parser**解析器，在接收到请求后会自动根据Content-Type指明的请求数据类型（如JSON、表单等）将请求数据进行parse解析，解析为类字典[QueryDict]对象保存到**Request**对象中。

**Request对象的数据是自动根据前端发送数据的格式进行解析之后的结果。**

无论前端发送的哪种格式的数据，我们都可以以统一的方式读取数据。

## 8.2 Request常用属性

#### 1）.data

`request.data` 返回解析之后的**请求体**数据。类似于Django中标准的`request.POST`和 `request.FILES`属性，但提供如下特性：

- 包含了解析之后的文件和非文件数据
- 包含了对POST、PUT、PATCH请求方式解析后的数据
- 利用了REST framework的parser解析器，不仅支持表单类型数据，也支持JSON数据

#### 2）.query_params

query_params，查询参数，也叫查询字符串(query string )

`request.query_params`与Django标准的`request.GET`相同，只是更换了更正确的名称而已。

#### 3）request._request 

获取django封装的Request对象

## 8.3 Response

```python
from rest_framework.response import Response
```

REST framework提供了一个响应类`Response`，使用该类构造响应对象时，响应的具体数据内容会被转换（renderer渲染器）成符合前端需求的类型。

REST framework提供了`Renderer` 渲染器，用来根据请求头中的`Accept`（接收数据类型声明）来自动转换响应数据到对应格式。如果前端请求中未进行声明Accept，则会采用Content-Type方式处理响应数据，我们可以通过配置来修改默认响应格式。

可以在**rest_framework.settings**查找所有的drf默认配置项

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器，返回json数据
        'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览器API渲染器，返回调试界面
    )
}
```

#### 构造方式

```python
Response(data, status=None, template_name=None, headers=None, content_type=None)
```

drf的响应处理类和请求处理类不一样，Response就是django的HttpResponse响应处理类的子类。

`data`数据不要是render处理之后的数据，只需传递python的内建类型数据即可，REST framework会使用`renderer`渲染器处理`data`。

`data`不能是复杂结构的数据，如Django的模型类对象，对于这样的数据我们可以使用`Serializer`序列化器序列化处理后（转为了Python字典类型）再传递给`data`参数。

参数说明：

- `data`: 为响应准备的序列化处理后的数据；
- `status`: 状态码，默认200；
- `template_name`: 模板名称，如果使用`HTMLRenderer` 时需指明；
- `headers`: 用于存放响应头信息的字典；
- `content_type`: 响应数据的Content-Type，通常此参数无需传递，REST framework会根据前端所需类型数据来设置该参数。

####  response对象的属性

工作少用，

##### 1）.data

传给response对象的序列化后，但尚未render处理的数据

##### 2）.status_code

状态码的数字

##### 3）.content

经过render处理后的响应数据

####  状态码

```python
from rest_framework import status
```

##### 1）信息告知 - 1xx

```python
HTTP_100_CONTINUE
HTTP_101_SWITCHING_PROTOCOLS
```

##### 2）成功 - 2xx

```python
HTTP_200_OK
HTTP_201_CREATED
HTTP_202_ACCEPTED
HTTP_203_NON_AUTHORITATIVE_INFORMATION
HTTP_204_NO_CONTENT
HTTP_205_RESET_CONTENT
HTTP_206_PARTIAL_CONTENT
HTTP_207_MULTI_STATUS
```

##### 3）重定向 - 3xx

```python
HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT
```

##### 4）客户端错误 - 4xx

##### 

```python
HTTP_400_BAD_REQUEST
HTTP_401_UNAUTHORIZED
HTTP_402_PAYMENT_REQUIRED
HTTP_403_FORBIDDEN
HTTP_404_NOT_FOUND
HTTP_405_METHOD_NOT_ALLOWED
HTTP_406_NOT_ACCEPTABLE
HTTP_407_PROXY_AUTHENTICATION_REQUIRED
HTTP_408_REQUEST_TIMEOUT
HTTP_409_CONFLICT
HTTP_410_GONE
HTTP_411_LENGTH_REQUIRED
HTTP_412_PRECONDITION_FAILED
HTTP_413_REQUEST_ENTITY_TOO_LARGE
HTTP_414_REQUEST_URI_TOO_LONG
HTTP_415_UNSUPPORTED_MEDIA_TYPE
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
HTTP_417_EXPECTATION_FAILED
HTTP_422_UNPROCESSABLE_ENTITY
HTTP_423_LOCKED
HTTP_424_FAILED_DEPENDENCY
HTTP_428_PRECONDITION_REQUIRED
HTTP_429_TOO_MANY_REQUESTS
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
```

##### 5）服务器错误 - 5xx

```python
HTTP_500_INTERNAL_SERVER_ERROR
HTTP_501_NOT_IMPLEMENTED
HTTP_502_BAD_GATEWAY
HTTP_503_SERVICE_UNAVAILABLE
HTTP_504_GATEWAY_TIMEOUT
HTTP_505_HTTP_VERSION_NOT_SUPPORTED
HTTP_507_INSUFFICIENT_STORAGE
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED
```

# 9.视图

drf的视图，完成的结果是一样的。使用不同的drf类，写的代码数量不同，但是输出的结果一样。

看自己的理解，想用那个用哪个。

下面的代码序列化器和数据库用的一样的。

## 9.1  普通视图

REST framework 提供了众多的通用视图基类与扩展类，以简化视图的编写。

### 9.1.1  2个视图基类

#### APIView[基本视图类]

```python
from rest_framework.views import APIView
```

`APIView`是REST framework提供的所有视图类的基类，继承自Django的`View`父类。

`APIView`与`View`的不同之处在于：

- 传入到视图方法中的是REST framework的`Request`对象，而不是Django的`HttpRequeset`对象；

- 视图方法可以返回REST framework的`Response`对象，视图会为响应数据设置（renderer）符合前端期望要求的格式；

- 任何`APIException`异常都会被捕获到，并且处理成合适格式的响应信息返回给客户端；

    django 的View中所有异常全部以HTML格式显示

    drf的APIVIew或者APIView的子类会自动根据客户端的Accept进行错误信息的格式转换。

- 重新声明了一个新的as_view方法并在dispatch()进行路由分发前，会对请求的客户端进行身份认证、权限检查、流量控制。

APIView除了继承了View原有的属性方法意外，还新增了类属性：

- **authentication_classes** 列表或元组，身份认证类
- **permissoin_classes** 列表或元组，权限检查类
- **throttle_classes** 列表或元祖，流量控制类

在`APIView`中仍以常规的类视图定义方法来实现get() 、post() 或者其他请求方式的方法。

##### 代码展示：

`serializer`

```python
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        extra_kwargs = {
            "age": {
                "max_value": 25,
                "error_messages": {
                    "max_value": "年龄不能超过25岁！",
                }
            }
        }
```

`stuapi.models`

```python
class Student(models.Model):
    """学生信息"""
    name = models.CharField(max_length=255, verbose_name="姓名")
    sex = models.BooleanField(default=1, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    classmate = models.CharField(max_length=5, verbose_name="班级编号")
    description = models.TextField(max_length=1000, verbose_name="个性签名")

    class Meta:
        db_table = "tb_students"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
```

路由`urls`

```python
urlpatterns = [
    # APIview
    path("student/", views.StudentAPIviews.as_view()),
    re_path("^student/(?P<pk>\d+)/$", views.StudentInfoAPIviews.as_view()),]
```

`views`

```python
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from stuapi.models import Student
from .serializers import StudentModelSerializer

class StudentAPIviews(APIView):
    def get(self, request):
        """获取所有学生信息"""
        # 1.获取学生信息
        student_list = Student.objects.all()
        # 2.实例化序列化器，获取序列化对象
        serializer = StudentModelSerializer(instance=student_list, many=True)
        # 3.转换数据并返回给客户端
        return Response(serializer.data)

    def post(self, request):
        """添加一条数据"""
        # 1.获取客户端提交的数据，实例化序列化器，获取序列化对象
        serializer = StudentModelSerializer(data=request.data)
        # 2. 反序列化(验证数据，保存数据到数据库)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 3.返回新增的模型数据给客户端
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class StudentInfoAPIviews(APIView):
    def get(self, request, pk):
        """获取一条数据"""
        # 1.使用pk值作为条件获取模型对象
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 2.序列化
        serializer = StudentModelSerializer(instance=student)
        # 3.返回对象
        return Response(serializer.data)

    def put(self, request, pk):
        """更新数据"""
        # 1.使用pk值作为条件获取模型对象
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # 2.获取客户提交数据
        serializer = StudentModelSerializer(instance=student, data=request.data)
        # 3.反序列化(验证数据，数据保存)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 3.返回对象
        return Response(serializer.data)

    def delete(self, request, pk):
        """删除数据"""
        # 1. 根据PK值获取要删除的数据并删除
        try:
            Student.objects.get(pk=pk).delete()
        except Student.DoesNotExist:
            pass

        # 2. 返回结果
        return Response(status=status.HTTP_204_NO_CONTENT)
```

#### GenericAPIView[通用视图类]

通用视图类主要作用就是把视图中的**独特的代码抽取出来**，让视图方法中的代码更加通用，方便把通用代码进行简写。

```python
from rest_framework.generics import GenericAPIView
```

继承自`APIView`，**主要增加了操作序列化器和数据库查询的方法，作用是为下面Mixin扩展类的执行提供方法支持。通常在使用时，可搭配一个或多个Mixin扩展类。**

提供的关于序列化器使用的属性与方法

- 属性：

    - **serializer_class** 指明视图使用的序列化器类

- 方法：

    - **get_serializer_class(self)**

        当出现一个视图类中调用多个序列化器时,那么可以通过条件判断在get_serializer_class方法中通过返回不同的序列化器类名就可以让视图方法执行不同的序列化器对象了。

        可以重写，例如：

        ```python
        class Student2GenericAPIView(GenericAPIView):
            # 整个视图类只使用一个序列化器的情况
            # serializer_class = StudentModelSerializert
            # 整个视图类中使用多个序列化器的情况
            def get_serializer_class(self):
              if self.request.method.lower() == "put":
                    return StudentModelSerializer
              else:
                    return Student2ModelSerializer
        
            queryset = Student.objects
        
            def get(self, request, pk):
                """获取一个模型信息"""
                serializer = self.get_serializer(instance=self.get_object())
                return Response(serializer.data)
        
            def put(self, request, pk):
                """更新一个模型信息"""
                serializer = self.get_serializer(instance=self.get_object(), data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
        ```

    - **get_serializer(self, *args, \**kwargs)**

        返回序列化器对象，主要用来提供给Mixin扩展类使用，如果我们在视图中想要获取序列化器对象，也可以直接调用此方法。

        **注意，该方法在提供序列化器对象的时候，会向序列化器对象的context属性补充三个数据：request、format、view，这三个数据对象可以在定义序列化器时使用。**

        - **request** 当前视图的请求对象
        - **view** 当前请求的类视图对象
        - format 当前请求期望返回的数据格式

提供的关于数据库查询的属性与方法

- 属性：

    - **queryset** 指明使用的数据查询集

- 方法：

    - **get_queryset(self)**

        返回视图使用的查询集，主要用来提供给Mixin扩展类使用，是列表视图与详情视图获取数据的基础，默认返回`queryset`属性，

        可以重写，例如：

    ```python
    def get_queryset(self):
        user = self.request.user
        return user.accounts.all()
    ```

    - **get_object(self)**

        返回详情视图所需的模型类数据对象，主要用来提供给Mixin扩展类使用。

        在试图中可以调用该方法获取详情信息的模型类对象。

        **若详情访问的模型类对象不存在，会返回404。**

        该方法会默认使用APIView提供的check_object_permissions方法检查当前对象是否有权限被访问。

        举例：

        ```python
        # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
        
        class BookDetailView(GenericAPIView):
            queryset = BookInfo.objects.all()
            serializer_class = BookInfoSerializer
        def get(self, request, pk):
            book = self.get_object() # get_object()方法根据pk参数查找queryset中的数据对象
            serializer = self.get_serializer(book)
            return Response(serializer.data)
        ```

其他可以设置的属性

- **pagination_class** 指明分页控制类
- **filter_backends** 指明数据过滤控制后端

##### 代码：

数据库和上面的一个

`urls`

```python
# GenericAPI

urlpatterns = [
	path("student2/", views.StudentGenericAPIView.as_view()),
	re_path("^student2/(?P<pk>\d+)/$", views.StudentInfoGenericAPIView.as_view()),]
```

`views`

```python
"""GenericAPIview,通用视图类"""
"""
APIView中的api接口代码，除了部分涉及到调用模型和序列化器的代码以外，其他代码几乎都是固定写法。
所以，当我们将来针对增删查改的通用api接口编写时，完全可以基于原有的代码进行复用，
那么，drf也考虑到了这个问题，所以提供了一个GenericAPIView（通用视图类），让我们可以把接口中独特的代码单独提取出来作为属性存在。
rest_framework.generics.GenericAPIView是APIView的子类，在APIView的基础上进行属性扩展提供了2个属性，4个方法，方便我们针对通用接口进行编写。
"""
from rest_framework.generics import GenericAPIView


class StudentGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    # print(queryset)
    print(serializer_class)   # <class 'demo.serializers.StudentModelSerializer'>
    def get(self, request):
        """获取所有学生信息"""
        # 1.获取学生信息
        queryset = self.get_queryset()
        print("queryset",queryset)
        # 2.实例化序列化器，获取序列化对象
        serializer = self.get_serializer(instance=queryset, many=True)
        print("serializer",serializer)
        # 3.转换数据并返回给客户端
        return Response(serializer.data)

    def post(self, request):
        """添加一条数据"""
        # 1.获取客户端提交的数据，实例化序列化器，获取序列化对象
        serializer = self.get_serializer(data=request.data)
        # 2. 反序列化(验证数据，保存数据到数据库)
        serializer.is_valid(raise_exception=True,)
        serializer.save()
        # 3.返回新增的模型数据给客户端
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentInfoGenericAPIView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, pk):
        """获取一个数据"""
        # 1. 使用pk作为条件获取模型对象
        instance = self.get_object()

        # 2.序列化
        serializer = self.get_serializer(instance=instance)

        # 3. 返回结果
        return Response(serializer.data)

    def put(self, request, pk):
        """更新一个数据"""
        # 1. 使用pk作为条件获取模型对象
        instance = self.get_object()

        # 2. 获取客户端提交的数据
        serializer = self.get_serializer(instance=instance, data=request.data)

        # 3. 反序列化[验证数据和数据保存]
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 4. 返回结果
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        """删除一个数据"""
        # 1. 根据PK值获取要删除的数据并删除
        self.get_object().delete()

        # 2. 返回结果
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### 9.2  5个视图扩展类

也叫混入类。

作用：

提供了几种后端视图（对数据资源进行增删改查）处理流程的实现，如果需要编写的视图属于这五种，则视图可以通过继承相应的扩展类来复用代码，减少自己编写的代码量。

这五个扩展类需要搭配GenericAPIView通用视图基类，因为五个扩展类的实现需要调用GenericAPIView提供的序列化器与数据库查询的方法。



```python
"""
使用drf内置的模型扩展类[混入类]结合GenericAPIView实现通用视图方法的简写操作
from rest_framework.mixins import ListModelMixin   获取多条数据，返回响应结果    list
from rest_framework.mixins import CreateModelMixin 添加一条数据，返回响应结果    create
from rest_framework.mixins import RetrieveModelMixin 获取一条数据，返回响应结果  retrieve
from rest_framework.mixins import UpdateModelMixin 更新一条数据，返回响应结果    update(更新全部字段)和partial_update(更新单个或部分字段，例如修改密码，修改头像)
from rest_framework.mixins import DestroyModelMixin 删除一条数据，返回响应结果   destroy
"""
```

#### 1）ListModelMixin

列表视图扩展类，提供`list(request, *args, **kwargs)`方法快速实现列表视图，返回200状态码。

该Mixin的list方法会对数据进行过滤和分页。

#### 2）CreateModelMixin

创建视图扩展类，提供`create(request, *args, **kwargs)`方法快速实现创建资源的视图，成功返回201状态码。

如果序列化器对前端发送的数据验证失败，返回400错误。

路由

`urls`

```python
urlpatterns = [
	path("student3/", views.StudentMixinView.as_view()),
	re_path("^student3/(?P<pk>\d+)/$", views.StudentInfoGenericAPIView.as_view()),]
```

`views`

```python
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from stuapi.models import Student
from .serializers import StudentModelSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin


class StudentMixinView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request):
        """获取所有数据"""
        return self.list(request)

    def post(self, request):
        """添加一条数据"""
        return self.create(request)
```



#### 3）RetrieveModelMixin

详情视图扩展类，提供`retrieve(request, *args, **kwargs)`方法，可以快速实现返回一个存在的数据对象。

如果存在，返回200， 否则返回404。

#### 4）UpdateModelMixin

更新视图扩展类，提供`update(request, *args, **kwargs)`方法，可以快速实现更新一个存在的数据对象。

同时也提供`partial_update(request, *args, **kwargs)`方法，可以实现局部更新。

成功返回200，序列化器校验数据失败时，返回400错误。

#### 5）DestroyModelMixin

删除视图扩展类，提供`destroy(request, *args, **kwargs)`方法，可以快速实现删除一个存在的数据对象。

成功返回204，不存在返回404。

```python
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from stuapi.models import Student
from .serializers import StudentModelSerializer
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class StudentInfoMixinView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
```

### 9.3  9个视图子类

#### 1）CreateAPIView

提供了post方法，内部调用了create方法

继承自： GenericAPIView、CreateModelMixin

#### 2）ListAPIView

提供了get方法，内部调用了list方法

继承自：GenericAPIView、ListModelMixin

#### 3）RetrieveAPIView

提供了get方法，内部调用了retrieve方法

继承自: GenericAPIView、RetrieveModelMixin

#### 4）DestoryAPIView

提供了delete方法，内部调用了destory方法

继承自：GenericAPIView、DestoryModelMixin

#### 5）UpdateAPIView

提供了put和patch方法，内部调用了update和partial_update方法

继承自：GenericAPIView、UpdateModelMixin

#### 6）ListCreateAPIView

提供了get和post方法，内部调用了list和create方法

继承自：GenericAPIView、ListModelMixin、CreateModelMixin

#### 7）RetrieveUpdateAPIView

提供 get、put、patch方法

继承自： GenericAPIView、RetrieveModelMixin、UpdateModelMixin

#### 8）RetrieveDestoryAPIView

提供 get、delete方法

继承自：GenericAPIView、RetrieveModelMixin、DestoryModelMixin

#### 9）RetrieveUpdateDestoryAPIView

提供 get、put、patch、delete方法

继承自：GenericAPIView、RetrieveModelMixin、UpdateModelMixin、DestoryModelMixin

```python
"""
上面的接口代码还可以继续更加的精简，drf在使用GenericAPIView和Mixins进行组合以后，还提供了视图子类。
视图子类，提供了各种的视图方法调用mixins操作

    ListAPIView = GenericAPIView + ListModelMixin         获取多条数据的视图方法
    CreateAPIView = GenericAPIView + CreateModelMixin     添加一条数据的视图方法
    RetrieveAPIView = GenericAPIView + RetrieveModelMixin 获取一条数据的视图方法
    UpdateAPIView = GenericAPIView + UpdateModelMixin     更新一条数据的视图方法
    DestroyAPIView = GenericAPIView + DestroyModelMixin   删除一条数据的视图方法
组合视图子类
    ListCreateAPIView = ListAPIView + CreateAPIView
    RetrieveUpdateAPIView = RetrieveAPIView + UpdateAPIView
    RetrieveDestroyAPIView = RetrieveAPIView + DestroyAPIView
    RetrieveUpdateDestroyAPIView = RetrieveAPIView + UpdateAPIView + DestroyAPIView
"""
```

### 代码

`views`

```python
from rest_framework.generics import ListCreateAPIView


class StudentListAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


from rest_framework.generics import RetrieveUpdateDestroyAPIView  # 四行代码一样意思


class StudentInfoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
```

`urls`

```python
urlpatterns = [
    path("student4/", views.StudentListAPIView.as_view()),
	re_path("^student4/(?P<pk>\d+)/$", views.StudentInfoAPIView.as_view()),]
```

## 9.2 视图集ViewSet

使用视图集ViewSet，可以将一系列视图相关的代码逻辑和相关的http请求动作封装到一个类中：

- list() 提供一组数据
- retrieve() 提供单个数据
- create() 创建数据
- update() 保存数据
- destory() 删除数据

ViewSet视图集类不再限制视图方法名只允许get()、post()等这种情况了，而是实现允许开发者根据自己的需要定义自定义方法名，例如  list() 、create() 等，然后经过路由中使用http和这些视图方法名进行绑定调用。

视图集只在使用as_view()方法的时候，才会将**action**动作与具体请求方式对应上。如：

```python
"""
针对视图子类这种写法写法虽然已经省略了http请求，但是在开发通用5个api接口时，还是会出现需要2个类来实现5个接口的情况。
这主要的原因是2点：
1. 获取多条数据与获取一条数据的http请求重复了。在django中依赖于请求方法来响应不同的http请求
2. 部分接口需要pk值作为url地址。

drf为了解决上面的2个问题，提供了视图集和路由集。
视图集就可以帮我们实现一个视图类响应多种重复的http请求
路由集就可以帮我们实现自动根据不同的视图方法来生成不同参数的路由地址。
from rest_framework.viewsets import ViewSet  # ViewSet是APIView的子类，是所有drf中的视图集的父类
"""
from rest_framework.viewsets import ViewSet
class StudentViewSet(ViewSet):
    # ViewSet不再需要我们使用http请求作为视图方法了。当然，如果你还希望使用http作为视图方法也可以。
    def get_all(self,request):
        queryset = Student.objects.all()
        # 实例化序列化器对象
        serializer = StudentModelSerializer(instance=queryset, many=True)
        # 返回序列化后的数据列表
        return Response(serializer.data)

    def create(self,request):
        """添加一条数据"""
        # 接收客户端提交的数据
        # 1. 实例化序列化器对象，获取来自客户端的请求数据作为参数
        serializer = StudentModelSerializer(data=request.data)
        # 2. 反序列化, 调用is_valid进行数据校验
        serializer.is_valid(raise_exception=True)
        # 3. 反序列化, 调用save保存数据
        serializer.save()
        # 4. 序列化，把新增后的模型对象返回给客户端
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_one(self,request,pk):
        try:
            # 模型操作，根据pk值获取指定数据
            instance = Student.objects.get(pk=pk)
            # 实例化序列化器对象
            serializer = StudentModelSerializer(instance=instance)
            # 返回序列化后的数据
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({"msg":"当前学生不存在！"}, status=status.HTTP_404_NOT_FOUND)


    def put(self,request,pk):
        """更新一条数据"""
        try:
            # 获取要更新的模型对象
            instance = Student.objects.get(pk=pk)
            # 实例化序列化器对象，参数分别是本次更新的模型对象以及接受来自客户端提交的更新数据
            serializer = StudentModelSerializer(instance=instance, data=request.data)
            # 反序列化，验证数据
            serializer.is_valid(raise_exception=True)
            # 反序列化器，保存数据
            serializer.save()
            # 序列化，返回更新后的数据
            return Response(serializer.data)

        except Student.DoesNotExist:
            return Response({"msg": "当前学生不存在！"}, status=status.HTTP_404_NOT_FOUND)


    def delete(self,request,pk):
        """删除一条数据"""
        try:
            # 获取要更新的模型对象
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"msg": "当前学生不存在！"}, status=status.HTTP_404_NOT_FOUND)
```

## 9.3常用视图集父类

#### 1） ViewSet

继承自`APIView`与`ViewSetMixin`，作用也与APIView基本类似，提供了身份认证、权限校验、流量管理等。

**ViewSet主要通过继承ViewSetMixin来实现在调用as_view()时传入字典{“http请求”：“视图方法”}的映射处理工作，如{'get':'list'}，**

在ViewSet中，没有提供任何动作action方法，需要我们自己实现action方法。

#### 2）GenericViewSet

继承自GenericAPIView和ViewSetMixin，作用让视图集的视图代码变得更加通用，抽离独特代码作为视图类的属性。

使用ViewSet通常并不方便，因为list、retrieve、create、update、destory等方法都需要自己编写，而这些方法与前面讲过的Mixin扩展类提供的方法同名，所以我们可以通过继承Mixin扩展类来复用这些方法而无需自己编写。但是Mixin扩展类依赖与`GenericAPIView`，所以还需要继承`GenericAPIView`。

**GenericViewSet**就帮助我们完成了这样的继承工作，继承自`GenericAPIView`与`ViewSetMixin`，在实现了调用as_view()时传入字典（如`{'get':'list'}`）的映射处理工作的同时，还提供了`GenericAPIView`提供的基础方法，可以直接搭配Mixin扩展类使用。

视图代码：

```python
from rest_framework.viewsets import GenericViewSet

class StudentGenericViewSet(GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    def list(self,request):
        """获取多条数据"""
        # 获取模型对象列表，实例化序列化器对象
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        # 返回序列化后的数据列表
        return Response(serializer.data)

    def post(self,request):
        """添加一条数据"""
        serializer = self.get_serializer(data=request.data)
        # 2. 反序列化, 调用is_valid进行数据校验
        serializer.is_valid(raise_exception=True)
        # 3. 反序列化, 调用save保存数据
        serializer.save()
        # 4. 序列化，把新增后的模型对象返回给客户端
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        """获取一条数据"""
        # 模型操作，根据pk值获取指定数据
        instance = self.get_object() # 上面代码的简写，而且对错误进行格式处理
        # 实例化序列化器对象
        serializer = self.get_serializer(instance=instance)
        # 返回序列化后的数据列表
        return Response(serializer.data)

    def update(self, request, pk):
        """更新一条数据"""
        instance = self.get_object() # 不要漏了pk参数
        serializer = self.get_serializer(instance=instance, data=request.data)
        # 反序列化，验证数据
        serializer.is_valid(raise_exception=True)
        # 反序列化器，保存数据
        serializer.save()
        # 序列化，返回更新后的数据
        return Response(serializer.data)

    def delete(self, request, pk):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

```

路由代码：

```python
from django.urls import path
from . import views

urlpatterns = [
    path("s1/", views.StudentList1APIView.as_view()),
    path("s1/<int:pk>/", views.StudentInfo1APIView.as_view()),
    path("s2/", views.StudentList2GenericAPIView.as_view()),
    path("s2/<int:pk>/", views.StudentInfo2GenericAPIView.as_view()),
    path("s3/", views.StudentList3GenericAPIView.as_view()),
    path("s3/<int:pk>/", views.StudentInfo3GenericAPIView.as_view()),
    path("s4/", views.StudentListAPIView.as_view()),
    path("s4/<int:pk>/", views.StudentInfoAPIView.as_view()),
    # path("url地址/", views.StudentViewSet.as_view({"http请求方法名":"视图方法名","http请求方法名":"视图方法名",....})),
    path("s5/", views.StudentViewSet.as_view({"get":"get_all","post":"create"})),
    path("s5/<int:pk>/", views.StudentViewSet.as_view({"get":"get_one","put":"put","delete":"delete"})),
    path("s6/", views.StudentGenericViewSet.as_view({"get":"list","post":"post"})),
    path("s6/<int:pk>/", views.StudentGenericViewSet.as_view({"get":"retrieve","put":"update","delete":"delete"})),
]
```



集合我们上面学习的模型扩展类，实现简写操作，视图，代码：

```python
"""
GenericViewSet结合Mixins的混入类，直接视图接口，这次连视图子类都不需要了。
ViewSet
GenericViewSet
ModelViewSet = GenericViewSet + ListModelMixin + CreateModelMixin + UpdateModelMixin + RetrieveModelMixin + DestroyModelMixin
ReadOnlyModelViewSet = GenericViewSet + ListModelMixin + RetrieveModelMixin
"""
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
class StudentMixinViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
```

路由，代码：

```python
from django.urls import path
from . import views

urlpatterns = [
    path("s1/", views.StudentList1APIView.as_view()),
    path("s1/<int:pk>/", views.StudentInfo1APIView.as_view()),
    path("s2/", views.StudentList2GenericAPIView.as_view()),
    path("s2/<int:pk>/", views.StudentInfo2GenericAPIView.as_view()),
    path("s3/", views.StudentList3GenericAPIView.as_view()),
    path("s3/<int:pk>/", views.StudentInfo3GenericAPIView.as_view()),
    path("s4/", views.StudentListAPIView.as_view()),
    path("s4/<int:pk>/", views.StudentInfoAPIView.as_view()),
    # path("url地址/", views.StudentViewSet.as_view({"http请求方法名":"视图方法名","http请求方法名":"视图方法名",....})),
    path("s5/", views.StudentViewSet.as_view({"get":"get_all","post":"create"})),
    path("s5/<int:pk>/", views.StudentViewSet.as_view({"get":"get_one","put":"put","delete":"delete"})),
    path("s6/", views.StudentGenericViewSet.as_view({"get":"list","post":"post"})),
    path("s6/<int:pk>/", views.StudentGenericViewSet.as_view({"get":"retrieve","put":"update","delete":"delete"})),
    path("s7/", views.StudentMixinViewSet.as_view({"get":"list","post":"create"})),
    path("s7/<int:pk>/", views.StudentMixinViewSet.as_view({"get":"retrieve","put":"update","delete":"destroy"})),
]
```



#### 3）ModelViewSet

继承自`GenericViewSet`，同时包括了ListModelMixin、RetrieveModelMixin、CreateModelMixin、UpdateModelMixin、DestoryModelMixin。

#### 4）ReadOnlyModelViewSet

继承自`GenericViewSet`，同时包括了ListModelMixin、RetrieveModelMixin。

视图代码：

```python
"""
GenericViewSet结合Mixins的混入类，直接视图接口，这次连视图子类都不需要了。
ViewSet
GenericViewSet
ModelViewSet = GenericViewSet + ListModelMixin + CreateModelMixin + UpdateModelMixin + RetrieveModelMixin + DestroyModelMixin
ReadOnlyModelViewSet = GenericViewSet + ListModelMixin + RetrieveModelMixin
"""
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet # 万能视图集，5个接口的简写
from rest_framework.viewsets import ReadOnlyModelViewSet # 只读视图集，2个接口的简写
class StudentMixinViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
```

路由代码：

```python
from django.urls import path
from . import views

urlpatterns = [
    path("s1/", views.StudentList1APIView.as_view()),
    path("s1/<int:pk>/", views.StudentInfo1APIView.as_view()),
    path("s2/", views.StudentList2GenericAPIView.as_view()),
    path("s2/<int:pk>/", views.StudentInfo2GenericAPIView.as_view()),
    path("s3/", views.StudentList3GenericAPIView.as_view()),
    path("s3/<int:pk>/", views.StudentInfo3GenericAPIView.as_view()),
    path("s4/", views.StudentListAPIView.as_view()),
    path("s4/<int:pk>/", views.StudentInfoAPIView.as_view()),
    # path("url地址/", views.StudentViewSet.as_view({"http请求方法名":"视图方法名","http请求方法名":"视图方法名",....})),
    path("s5/", views.StudentViewSet.as_view({"get":"get_all","post":"create"})),
    path("s5/<int:pk>/", views.StudentViewSet.as_view({"get":"get_one","put":"put","delete":"delete"})),
    path("s6/", views.StudentGenericViewSet.as_view({"get":"list","post":"post"})),
    path("s6/<int:pk>/", views.StudentGenericViewSet.as_view({"get":"retrieve","put":"update","delete":"delete"})),
    path("s7/", views.StudentMixinViewSet.as_view({"get":"list","post":"create"})),
    path("s7/<int:pk>/", views.StudentMixinViewSet.as_view({"get":"retrieve","put":"update","delete":"destroy"})),
]
```

# 10路由Routers

对于视图集ViewSet，我们除了可以自己手动指明请求方式与动作action之间的对应关系外，还可以使用Routers来帮助我们快速实现路由信息。如果是非视图集，不需要使用路由集routers

REST framework提供了两个router，使用方式一致的。结果多一个或少一个根目录url地址的问题而已。

- **SimpleRouter**
- **DefaultRouter**

## 10.1使用方法

1） 创建router对象，并注册视图集，例如

```python
from django.urls import path
from . import views

urlpatterns = [
    # 省略....
    # path("s7/", views.StudentMixinViewSet.as_view({"get":"list","post":"create"})),
    # path("s7/<int:pk>/", views.StudentMixinViewSet.as_view({"get":"retrieve","put":"update","delete":"destroy"})),
]

# 路由集的操作
from rest_framework.routers import DefaultRouter,SimpleRouter
router = DefaultRouter()
# 注册视图(访问前缀，视图集类，调用别名)
router.register("s7", views.StudentMixinViewSet, "s7")
# 把路由对象生成的视图集路由列表合并追加路由列表中
print(router.urls)
urlpatterns += router.urls
```

register(prefix, viewset, basename)

- prefix 该视图集的路由前缀
- viewset 视图集
- basename 路由别名的前缀

## 10.2 视图集中附加action的声明

在视图集中，如果想要让Router自动帮助我们为自定义的动作生成路由信息，需要使用`rest_framework.decorators.action`装饰器。

以action装饰器装饰的方法名会作为action动作名，与list、retrieve等同。

action装饰器可以接收两个参数：

- **methods**: 声明该action对应的请求方式，列表传递

- **detail**: 声明该action的路径是否与单一资源对应

```
路由前缀/<pk>/action方法名/
```

- True 表示路径格式是`xxx/<pk>/action方法名/`

- False 表示路径格式是`xxx/action方法名/`

url_path：声明该action的路由尾缀。

```python
from rest_framework.viewsets import ModelViewSet # 万能视图集，5个接口的简写
from rest_framework.viewsets import ReadOnlyModelViewSet # 只读视图集，2个接口的简写
from rest_framework.decorators import action
class StudentMixinViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    # 路由对象给视图集生成路由信息时，只会生成5个基本api接口，这主要是router只识别5个混入类的原因，
    # 而针对我们开发者自定义的视图方法，路由对象不会自动生成路由信息，
    # 所以下面这个login，如果希望被外界访问到，则必须通过action装饰器告诉路由对象要给它生成一个路由信息。
    @action(methods=["get","post"], detail=False, url_path="login")
    # action的参数
    # methods, 列表，指定允许哪些http请求方法可以访问当前视图方法
    # detail, 布尔值，告诉路由对象在生成路由信息时，是否要自动生成pk值，True表示需要，False表示不需要。
    # url_path，字符串，访问视图的url地址，如果不设置，则默认采用视图方法名作为访问后缀
    # http://127.0.0.1:8000/demo/s7/login/
    def login(self, request):
        """登录视图"""
        return Response({"msg":"登录成功"})

    @action(methods=["get"], detail=True, url_path="login/log")
    # http://127.0.0.1:8000/demo/s7/23/login/log/
    def login_log(self,request,pk):
        """用户登录历史记录"""
        # 视图集类中
        # 可以通过self.method获取本次客户端的http请求
        # 可以通过self.action获取本次客户端请求的视图方法名[ViewSet提供的]
        print(self.action) # login_log
        return Response({"msg": "用户登录历史记录"})
```

由路由器自动为此视图集自定义action方法形成的路由会是如下内容：

```python
url: ^s7/login/$                      basename: s7-login
url: ^s7/(?P<pk>[^/.]+)/login/log/$   basename: s7-login-log
```

## 10.3 路由router形成URL的方式

1） SimpleRouter（prefix=“路由前缀”，viewset=视图集类，basename=“路由别名”）

![SimpleRouter](D:\笔记\Django rest framework\SimpleRouter.png)

2）DefaultRouter

![DefaultRouter](D:\笔记\Django rest framework\DefaultRouter.png)

DefaultRouter与SimpleRouter的区别是，DefaultRouter会多附带一个默认的API根视图，返回一个包含所有列表视图的超链接响应数据。













# 11.认证Authentication

可以在配置文件中配置全局默认的认证方案

常见的认证方式：cookie、session、token

### authentication_classess类属性认证

也可以在具体的视图类中通过设置authentication_classess类属性来设置单独的不同的认证方式

```python
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView

class ExampleView(APIView):
    # 类属性
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self,request):
        pass
```

认证失败会有两种可能的返回值，这个需要我们配合权限组件来使用：

- 401 Unauthorized 未认证
- 403 Permission Denied 权限被禁止

## 自定义认证

需要配置路由

新建一个drfdome文件夹，在这个文件夹下创建一个authentication文件

`drfdome.authentication`

```python
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model


class CustomAuthentication(BaseAuthentication):
    """
    自定义认证方式
    """
    def authenticate(self, request):
        """
        认证方法
        request: 本次客户端发送过来的http请求对象
        """
        user = request.query_params.get("user")
        pwd = request.query_params.get("pwd")
        if user != "root" or pwd != "houmen":
            return None
            # get_user_model获取当前系统中用户表对应的用户模型类
        user = get_user_model().objects.first()
        return (user, None)  # 按照固定的返回格式填写 （用户模型对象, None）
```

`views`

将from drfdome.authentication  import  CustomAuthentication导过来。放到authentication_classes中。即可

```python
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser
from drfdome.authentication import CustomAuthentication

class ExampleView(APIView):
    # 类属性
    authentication_classes = [SessionAuthentication, BasicAuthentication,CustomAuthentication]

    def get(self, request):
        print(request.user)  # 用户的长账号，没有注册的用户是AnonymousUser
        if request.user.id:
            return Response("通过认证")
        else:
            return Response("没有通过认证")
```

## 配置REST_FRAMEWORK

在django的setting配置REST_FRAMEWORK

把REST_FRAMEWORK的配置写在setting下，

```python
'drfdome.authentication.CustomAuthentication',          # 自定义认证
```

需要多对数类认证时将自定义认证写入setting中，
只是小部分，哪个类需要在那个类中写。

```python
"""drf配置信息必须全部写在REST_FRAMEWORK配置项中"""
REST_FRAMEWORK = {
    # 配置认证方式的选项【drf的认证是内部循环遍历每一个注册的认证类，一旦认证通过识别到用户身份，则不会继续循环】
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'drfdome.authentication.CustomAuthentication',          # 自定义认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',    # Basic认证
    )
}
```

# 12. 权限Permissions

权限控制可以限制用户对于视图的访问和对于具有模型对象的访问。

- 在执行视图的as_view()方法的dispatch()方法前，会先进行视图访问权限的判断
- 在通过get_object()获取具体模型对象时，会进行模型对象访问权限的判断

### 使用

可以在配置文件中**全局设置**默认的权限管理类，如

```python
REST_FRAMEWORK = {
    ....
    
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )

```

如果未指明，则采用如下默认配置    默认是AllowAny

```python
 'DEFAULT_PERMISSION_CLASSES': (   'rest_framework.permissions.AllowAny',)
```

### 提供的权限

- AllowAny 允许所有用户，默认权限
- IsAuthenticated 仅通过登录认证的用户
- IsAdminUser 仅管理员用户
- IsAuthenticatedOrReadOnly 已经登陆认证的用户可以对数据进行增删改操作，没有登陆认证的只能查看数据。



也可以在具体的视图中通过permission_classes属性来进行局部设置，如

```python
# 这个也是属于自定义权限
from rest_framework.viewsets import ModelViewSet
from school.models import Student
from school.serializers import StudentModelSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class Hom2APIView(ModelViewSet):
    authentication_classes = [CustomAuthentication, ]
    # 游客仅能查看数据，登录用户可以进行数据的修改/添加/删除
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
```

路由代码：

```python
from django.urls import path
from . import views
urlpatterns = [
    path("s1/", views.HomeAPIView.as_view()),
]

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("s2", views.Hom2APIView, "s2")
urlpatterns += router.urls
```

### 自定义权限

如需自定义权限，需继承rest_framework.permissions.BasePermission父类，并实现以下两个任何一个方法或全部

- `.has_permission(self, request, view)`

    是否可以访问视图， view表示当前视图对象

- `.has_object_permission(self, request, view, obj)`

    是否可以访问模型对象， view表示当前视图， obj为模型数据对象

在当前子应用下，创建一个权限文件drfdome.permissions.py中声明自定义权限类:

```python
def has_permission(self, request, view):
    """
    视图权限
    返回结果未True则表示允许访问视图类
    request: 本次客户端提交的请求对象
    view: 本次客户端访问的视图类
    """
    # # 写在自己要实现认证的代码过程。
    # user = request.query_params.get("user")
    # # 返回值为True，则表示通行
    # return user == "xiaoming"
    # return True
    print("request.user",request.user )
    print("request.user.username",request.user.username)
    return bool(request.user and request.user.username == "xiaohong") 
def has_object_permission(self, request, view, obj):
    """
    模型权限，写了视图权限(has_permission)方法，一般就不需要写这个了。
    返回结果未True则表示允许操作模型对象
    """
    from school.models import Student
    if isinstance(obj, Student):
        # 限制只有小明才能操作Student模型
        user = request.query_params.get("user")
        return user == "xiaoming"  # 如果不是xiaoming，返回值为False，不能操作
    else:
        # 操作其他模型，直接放行
        return True

```

`views`

```python
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly,AllowAny  #（基本不用，默认就是)
from drfdome.permissions import IsXiaoMingPermission
# 继承只能时APIView或者时APIView的子类。
class HomeInfoAPIview(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]   # 表示当当前视图类中的所有视图方法，只能被已经登录的站点会员访问！
    # permission_classes= [IsAdminUser]    #  表示当前视图类中的所有方法，
    permission_classes= [IsXiaoMingPermission]
    def get(self, request):
        return Response({"msg": "OK"})

    def post(self, request):
        return Response({"msg": "OK"})
```

### 全局配置

```python
"""drf配置信息必须全部写在REST_FRAMEWORK配置项中"""
REST_FRAMEWORK = {
    # 配置认证方式的选项【drf的认证是内部循环遍历每一个注册的认证类，一旦认证通过识别到用户身份，则不会继续循环】
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'drfdemo.authentication.CustomAuthentication',          # 自定义认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',    # 基本认证
    ),
    # 权限设置[全局配置，在视图中可以通过permission_classes进行局部配置，局部配置优先级高于全局配置]
    # 全局设置太狠，
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'drfdome.permissions.IsXiaoMingPermission',
    ),
}
```

认证主要的作用就是识别客户端的访问者的身份，但是不能拦截客户端的访问。

权限是基于认证来实现的，但是权限可以针对不同身份的用户，进行拦截。

# 13. 限流Throttling

可以对接口访问的频次进行限制，以减轻服务器压力，或者实现特定的业务。

一般用于付费购买次数,投票等场景使用。

### 基本使用

可以在配置文件中，使用`DEFAULT_THROTTLE_CLASSES` 和 `DEFAULT_THROTTLE_RATES`进行全局配置，

`DEFAULT_THROTTLE_RATES` 可以使用 `second`, `minute`, `hour` 或`day`来指明周期。

```python
REST_FRAMEWORK = {
    # 限流全局配置
    # 'DEFAULT_THROTTLE_CLASSES':[ # 限流配置类
    #     'rest_framework.throttling.AnonRateThrottle', # 未认证用户[未登录用户]
    #     'rest_framework.throttling.UserRateThrottle', # 已认证用户[已登录用户]
    # ],
    'DEFAULT_THROTTLE_RATES':{ # 频率配置
        'anon': '2/day',  # 针对游客的访问频率进行限制，实际上，drf只是识别首字母，但是为了提高代码的维护性，建议写完整单词
        'user': '5/day', # 针对会员的访问频率进行限制，
    }
}
```

也可以在具体视图中通过throttle_classess属性来配置，如

```python
from rest_framework.throttling import UserRateThrottle
class Student2ModelViewSet(ModelViewSet):
    queryset = Student.objects
    serializer_class = StudentModelSerializer
    # 限流局部配置[这里需要配合在全局配置中的DEFAULT_THROTTLE_RATES来设置频率]
    throttle_classes = [UserRateThrottle]
```

### 可选限流类

1） AnonRateThrottle

限制所有匿名未认证用户，使用IP区分用户。【很多公司这样的，IP结合设备信息来判断，当然比IP要靠谱一点点而已】

使用`DEFAULT_THROTTLE_RATES['anon']` 来设置频次

2）UserRateThrottle

限制认证用户，使用User模型的 id主键 来区分。

使用`DEFAULT_THROTTLE_RATES['user']` 来设置频次

3）ScopedRateThrottle

限制用户对于每个视图的访问频次，使用ip或user id。

`settings`

```python
    # 限流全局配置
    'DEFAULT_THROTTLE_CLASSES':[  # 限流配置类
    #     'rest_framework.throttling.AnonRateThrottle',  # 未认证用户[未登录用户]
    #     'rest_framework.throttling.UserRateThrottle',  # 已认证用户[已登录用户]
        'rest_framework.throttling.ScopedRateThrottle',  # 基于自定义的命名空间来限流
    ],
    'DEFAULT_THROTTLE_RATES': {  # 频率配置
        'anon': '1/s',  # 针对游客的访问频率进行限制，实际上，drf只是识别首字母，但是为了提高代码的维护性，建议写完整单词
        'user': '1/s',  # 针对会员的访问频率进行限制，
        'vip': '3/m',  # 针对自定义命名空间，进行限流
    }

```

`views`

```python
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
class vipAPIView(APIView):
    # authentication_classes = [CustomAuthentication]  # 调用自定义认证
    # 局部配置限流
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # 配置自定义限流
    throttle_scope = "vip"   # 自定义命名空间[少用，因为对于大部分的集体环境下都是公用一个IP地址]
    def get(self,request):
        return Response(f"访问了视图")
```

# 序列化器的嵌套




















































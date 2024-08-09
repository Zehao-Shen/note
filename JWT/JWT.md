# JWT的构成

**一定要注意secret (secret第三部分的秘钥，用来判断是不是自己的jwt，很重要，是保存在后端的，不能暴露给前端)**

JWT就一段字符串，由三段信息构成的，将这三段信息文本用`.`拼接一起就构成了Jwt token字符串。就像这样:

```
eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAiMTUwMTIzNDU1IiwgImlhdCI6ICIxNTAxMDM0NTUiLCAibmFtZSI6ICJ3YW5neGlhb21pbmciLCAiYWRtaW4iOiB0cnVlLCAiYWNjX3B3ZCI6ICJRaUxDSmhiR2NpT2lKSVV6STFOaUo5UWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjkifQ==.815ce0e4e15fff813c5c9b66cfc3791c35745349f68530bc862f7f63c9553f4b
```

第一部分我们称它为头部（header)，第二部分我们称其为载荷（payload, 类似于飞机上承载的物品)，第三部分是签证（signature).

## header

**一定要注意secret (secret第三部分的秘钥，用来判断是不是自己的jwt，很重要，是保存在后端的，不能暴露给前端)**

jwt的头部承载两部分信息：

- typ: 声明token类型，这里是jwt ，typ的值也可以是：Bear
- alg: 声明签证的加密的算法 通常直接使用 HMAC SHA256

完整的头部就像下面这样的JSON：

```
{
  'typ': 'JWT',
  'alg': 'HS256'
}
```

然后将头部进行base64编码，构成了jwt的第一部分头部

python代码举例：

```python
import base64, json
header_data = {"typ": "jwt", "alg": "HS256"}
header = base64.b64encode( json.dumps(header_data).encode() ).decode()
print(header) # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9
```

## payload

**一定要注意secret (secret第三部分的秘钥，用来判断是不是自己的jwt，很重要，是保存在后端的，不能暴露给前端)**

载荷就是存放有效信息的地方。这个名字像是特指飞机上承载的货仓，这些有效信息包含三个部分:

- 标准声明
- 公共声明
- 私有声明

**标准声明**指定jwt实现规范中要求的属性。 (官方建议但不强制使用) ：

- iss: jwt签发者
- sub: jwt所面向的用户
- **aud**: 接收jwt的一方
- **exp**: jwt的过期时间，这个过期时间必须要大于签发时间
- **nbf**: 定义在什么时间之后，该jwt才可以使用
- **iat**: jwt的签发时间
- **jti**: jwt的唯一身份标识，主要用来作为一次性token, 从而回避重放攻击。

**公共声明** ： 公共的声明可以添加任何的公开信息，一般添加用户的相关信息或其他业务需要的必要信息.但不建议添加敏感信息，因为该部分在客户端可直接读取.

**私有声明** ： 私有声明是提供者和消费者所共同定义的声明，一般不建议存放敏感信息，里面存放的是一些可以在服务端或者客户端通过秘钥进行加密和解密的加密信息。往往采用的RSA非对称加密算法。

举例，定义一个payload载荷信息，demo/jwtdemo.py：

```python
import base64, json, time

if __name__ == '__main__':
    # 载荷
    iat = int(time.time())
    payload_data = {
        "sub": "root",
        "exp": iat + 3600,  # 假设一小时过期
        "iat": iat,
        "name": "wangxiaoming",
        "avatar": "1.png",
        "user_id": 1,
        "admin": True,
        "acc_pwd": "QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9",
    }
    # 将其进行base64编码，得到JWT的第二部分。
    payload = base64.b64encode(json.dumps(payload_data).encode()).decode()
    print(payload)
    # eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNjQ3Nzc0Mjk1LCAiaWF0IjogMTY0Nzc3MDY5NSwgIm5hbWUiOiAid2FuZ3hpYW9taW5nIiwgImF2YXRhciI6ICIxLnBuZyIsICJ1c2VyX2lkIjogMSwgImFkbWluIjogdHJ1ZSwgImFjY19wd2QiOiAiUWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5In0=

```

## signature

**一定要注意secret (secret第三部分的秘钥，用来判断是不是自己的jwt，很重要，是保存在后端的，不能暴露给前端)**

JWT的第三部分是一个签证信息，用于辨真伪，防篡改。这个签证信息由三部分组成：

- header (base64后的头部)
- payload (base64后的载荷)
- secret（保存在服务端的秘钥字符串，不会提供给客户端的，这样可以保证客户端没有签发token的能力）

举例，定义一个完整的jwt token，demo/jwtdemo.py：

```python
import base64, json, hashlib

if __name__ == '__main__':
    """jwt 头部的生成"""
    header_data = {"typ": "jwt", "alg": "HS256"}
    header = base64.b64encode( json.dumps(header_data).encode() ).decode()
    print(header) # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9

    """jwt 载荷的生成"""
    payload_data = {
        "sub": "root",
        "exp": "150123455",
        "iat": "150103455",
        "name": "wangxiaoming",
        "admin": True,
        "acc_pwd": "QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9",
    }
    # 将其进行base64编码，得到JWT的第二部分。
    payload = base64.b64encode(json.dumps(payload_data).encode()).decode()
    print(payload) # eyJzdWIiOiAicm9vdCIsICJleHAiOiAiMTUwMTIzNDU1IiwgImlhdCI6ICIxNTAxMDM0NTUiLCAibmFtZSI6ICJ3YW5neGlhb21pbmciLCAiYWRtaW4iOiB0cnVlLCAiYWNjX3B3ZCI6ICJRaUxDSmhiR2NpT2lKSVV6STFOaUo5UWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjkifQ==

    # from django.conf import settings
    # secret = settings.SECRET_KEY
    secret = 'django-insecure-hbcv-y9ux0&8qhtkgmh1skvw#v7ru%t(z-#chw#9g5x1r3z=$p'
    data = header + payload + secret  # 秘钥绝对不能提供给客户端。
    HS256 = hashlib.sha256()
    HS256.update(data.encode('utf-8'))
    signature = HS256.hexdigest()
    print(signature) # 815ce0e4e15fff813c5c9b66cfc3791c35745349f68530bc862f7f63c9553f4b

    # jwt 最终的生成
    token = f"{header}.{payload}.{signature}"
    print(token)
    # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAiMTUwMTIzNDU1IiwgImlhdCI6ICIxNTAxMDM0NTUiLCAibmFtZSI6ICJ3YW5neGlhb21pbmciLCAiYWRtaW4iOiB0cnVlLCAiYWNjX3B3ZCI6ICJRaUxDSmhiR2NpT2lKSVV6STFOaUo5UWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjkifQ==.815ce0e4e15fff813c5c9b66cfc3791c35745349f68530bc862f7f63c9553f4b
```

**注意：secret是保存在服务器端的，jwt的签发生成也是在服务器端的，secret就是用来进行jwt的签发和jwt的验证，所以，它就是你服务端的私钥，在任何场景都不应该流露出去。一旦客户端得知这个secret, 那就意味着客户端是可以自我签发jwt了。**

# 文字说明jwt

## 生成jwt

### 第一段header

第一段header包含算法类型和token类型，

json转化成字符串，然后做base64url加密

```py
{
  'typ': 'JWT',
  'alg': 'HS256'
}
```

### 第二段payload

第二段payload自定义值，

json转化成字符串，然后做base64url加密

### 第三段signature

```py
第一步
将第一段加密后的和第二段加密后的密文通过.拼接起来，

第二步
对前两部密文进行HS256加密+加盐

第三步
对前两步HS256加密后的密文，在进行base64url加密
```

## 验证jwt

### 第一步

对token进行分割

### 第二步

对第二段进行base64url解密，获取到payload的信息，并检验token是否超时

### 第三步

**HS256是不能反解的。**

```
第一步
把第一段header和第二段payload进行拼接
第二步
对前两段的密文进行HS256加密+加盐。
第三步

判断 密文和密文是否一致。
如果相等，验证通过，
不想等，验证不通过。
```

# jwt流程图

**一定要注意secret (secret第三部分的秘钥，用来判断是不是自己的jwt，很重要，是保存在后端的，不能暴露给前端)**

![a9cb888b7712dafea6e1f0e15d7e6e0](D:\笔记\JWT\assets\a9cb888b7712dafea6e1f0e15d7e6e0.png)

## 流程图解释

1. 点击登录后，将数据发送给后端，后端在数据库进行校验。
2. 检验成功，生成jwt，并将jwt返回给前端。前端保存jwt。
3. 当前端点击了某些页面需要进行用户验证时，请求信息中会携带jwt，传给后端。
4. 后端收到jwt后，对jwt进行校验(jwt时候过期，是不是当初后端发给前端jwt)
5. 验证通过，正常访问。

**一定要注意secret (secret第三部分的秘钥，用来判断是不是自己的jwt，很重要，是保存在后端的，不能暴露给前端)**

## js代码解析payload数据

payload就是jwt的第二部分(载荷部分)。

![c8be78b72cfe2baa4c9a4623a290742](D:\笔记\JWT\assets\c8be78b72cfe2baa4c9a4623a290742.png)

# 完整实列

**一定要注意secret (secret第三部分的秘钥，用来判断是不是自己的jwt，很重要，是保存在后端的，不能暴露给前端)**

举例，定义一个完整的jwt token，并认证token，demo/jwtdemo.py：

```python
import base64, json, hashlib
from datetime import datetime

if __name__ == '__main__':
    # 头部生成原理
    header_data = {
        "typ": "jwt",
        "alg": "HS256"
    }
    # print( json.dumps(header_data).encode() )
    # json转成字符串，接着base64编码处理
    header = base64.b64encode(json.dumps(header_data).encode()).decode()
    print(header)  # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9


    # 载荷生成原理
    iat = int(datetime.now().timestamp()) # 签发时间
    payload_data = {
        "sub": "root",
        "exp": iat + 3600,  # 假设一小时过期
        "iat": iat,
        "name": "wangxiaoming",
        "admin": True,
        "acc_pwd": "QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9",
    }

    payload = base64.b64encode(json.dumps(payload_data).encode()).decode()
    print(payload)
    # eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNjM2NTk3OTAzLCAiaWF0IjogMTYzNjU5NDMwMywgIm5hbWUiOiAid2FuZ3hpYW9taW5nIiwgImFkbWluIjogdHJ1ZSwgImFjY19wd2QiOiAiUWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5In0=

    # from django.conf import settings
    # secret = settings.SECRET_KEY
    secret = 'django-insecure-hbcv-y9ux0&8qhtkgmh1skvw#v7ru%t(z-#chw#9g5x1r3z=$p'

    data = header + payload + secret  # 秘钥绝对不能提供给客户端。

    HS256 = hashlib.sha256()
    HS256.update(data.encode('utf-8'))
    signature = HS256.hexdigest()
    print(signature) # ce46f9d350be6b72287beb4f5f9b1bc4c42fc1a1f8c8db006e9e99fd46961156

    # jwt 最终的生成
    token = f"{header}.{payload}.{signature}"
    print(token)
    # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNjM2NTk3OTAzLCAiaWF0IjogMTYzNjU5NDMwMywgIm5hbWUiOiAid2FuZ3hpYW9taW5nIiwgImFkbWluIjogdHJ1ZSwgImFjY19wd2QiOiAiUWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5In0=.ce46f9d350be6b72287beb4f5f9b1bc4c42fc1a1f8c8db006e9e99fd46961156


    # 认证环节
    token = "eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNjM2NTk3OTAzLCAiaWF0IjogMTYzNjU5NDMwMywgIm5hbWUiOiAid2FuZ3hpYW9taW5nIiwgImFkbWluIjogdHJ1ZSwgImFjY19wd2QiOiAiUWlMQ0poYkdjaU9pSklVekkxTmlKOVFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5In0=.ce46f9d350be6b72287beb4f5f9b1bc4c42fc1a1f8c8db006e9e99fd46961156"
    # token = "eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiJyb290IiwiZXhwIjoxNjMxNTI5MDg4LCJpYXQiOjE2MzE1MjU0ODgsIm5hbWUiOiJ3YW5neGlhb2hvbmciLCJhZG1pbiI6dHJ1ZSwiYWNjX3B3ZCI6IlFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5UWlMQ0poYkdjaU9pSklVekkxTmlKOSJ9.b533c5515444c51058557017e433d411379862d91640c8beed6f2617b1da2feb"
    header, payload, signature = token.split(".")

    # 验证是否过期了
    # 先基于base64，接着使用json解码
    payload_data = json.loads( base64.b64decode(payload.encode()) )
    print(payload_data)
    exp = payload_data.get("exp", None)
    if exp is not None and int(exp) < int(datetime.now().timestamp()):
        print("token过期！！！")
    else:
        print("没有过期")

    # 验证token是否有效，是否被篡改
    # from django.conf import settings
    # secret = settings.SECRET_KEY
    secret = 'django-insecure-hbcv-y9ux0&8qhtkgmh1skvw#v7ru%t(z-#chw#9g5x1r3z=$p'
    data = header + payload + secret  # 秘钥绝对不能提供给客户端。
    HS256 = hashlib.sha256()
    HS256.update(data.encode('utf-8'))
    new_signature = HS256.hexdigest()

    if new_signature != signature:
        print("认证失败")
    else:
        print("认证通过")

```

**一定要注意secret (secret第三部分的秘钥，用来判断是不是自己的jwt，很重要，是保存在后端的，不能暴露给前端)**

# drf中引用jwt

安装

```
pip install djangorestframework-jwt
```

settings.py，配置jwt

```py
# drf配置
REST_FRAMEWORK = {
    # 自定义异常处理
    'EXCEPTION_HANDLER': 'luffycityapi.utils.exceptions.exception_handler',
    # 自定义认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # jwt认证
        'rest_framework.authentication.SessionAuthentication',           # session认证
        'rest_framework.authentication.BasicAuthentication',
    ),
}

import datetime
# jwt认证相关配置项
JWT_AUTH = {
    # 设置jwt的有效期
    # 如果内部站点，例如：运维开发系统，OA，往往配置的access_token有效期基本就是15分钟，30分钟，1~2个小时
    'JWT_EXPIRATION_DELTA': datetime.timedelta(weeks=1),
    # 一周有效，
}
```

- JWT_EXPIRATION_DELTA 指明token的有效期

## 生成jwt

官方文档：https://jpadilla.github.io/django-rest-framework-jwt/#creating-a-new-token-manually

手动签发JWT(看的玩玩，可以跳过)

```py
# 可以进入到django的终端下测试生成token的逻辑
python manage.py shell

# 引入jwt配置
from rest_framework_jwt.settings import api_settings
# 获取载荷生成函数
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# 获取token生成函数
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# 生成载荷需要的字典数据
# 此处，拿数据库中的用户信息进行测试
from users.models import User
user = User.objects.first()
payload = jwt_payload_handler(user)  # user用户模型对象
# 生成token
token = jwt_encode_handler(payload)
```

在用户注册或登录成功后，在序列化器中返回用户信息以后同时返回token即可。

## 后端实现登陆认证接口

Django REST framework-JWT为了方便开发者使用jwt提供了登录获取token的视图，开发者可以直接使用它绑定一个url地址即可。

在	urls.py中绑定登陆视图

```py
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path("login/", obtain_jwt_token, name="login"),
]

# obtain_jwt_token实际上就是 rest_framework_jwt.views.ObtainJSONWebToken.as_view()

# 当我们访问obtain_jwt_token这个路由，eg:http://127.0.0.1:8000/login 会返回token="xxxxxxxxxx"

```

进入obtain_jwt_token

![屏幕截图 2023-10-15 210225](D:\笔记\JWT\assets\屏幕截图 2023-10-15 210225.png)

```
# 登录视图，获取access_token
# obtain_jwt_token = ObtainJSONWebToken.as_view()
# 刷新token视图，依靠旧的access_token生成新的access_token
# refresh_jwt_token = RefreshJSONWebToken.as_view()
# 验证现有的access_token是否有效
# verify_jwt_token = VerifyJSONWebToken.as_view()
```

接下来可以通过postman来测试下功能，可以发送form表单，也可以发送json，username和password是必填字段（有用户）

![image-20220410091633460](D:\笔记\JWT\assets\image-20220410091633460.png)

## 自定义载荷

继承AbstractUser，使创建的user表有我们自己的字段。

model.py

```py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    money = models.DecimalField(max_digits=9, default=0.0, decimal_places=2, verbose_name="钱包余额")
    credit = models.IntegerField(default=0, verbose_name="积分")
    avatar = models.ImageField(upload_to="avatar/%Y", null=True, default="", verbose_name="个人头像")
    nickname = models.CharField(max_length=50, default="", null=True, verbose_name="用户昵称")

    class Meta:
        db_table = 'shen_users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
```



官方在载荷中定义的的数据太少了。我们将自己定义的user中的数据加入到载荷中。

在utils/authenticate.py 中，创建jwt_payload_handler函数重写返回值。

```py
from rest_framework_jwt.utils import jwt_payload_handler as payload_handler


def jwt_payload_handler(user):
    """
    自定义载荷信息
    :params user  用户模型实例对象
    """
    # 先让jwt模块生成自己的载荷信息
    payload = payload_handler(user)
    # 追加自己要返回的内容
    if hasattr(user, 'avatar'):
        # avatar的类型是ImageField所以是avatar.url，否则会报错
        """
        TypeError: Object of type ImageFieldFile is not JSON serializable
        """
        payload['avatar'] = user.avatar.url if user.avatar else ""
    if hasattr(user, 'nickname'):
        payload['nickname'] = user.nickname

    if hasattr(user, 'money'):
        payload['money'] = float(user.money)
    if hasattr(user, 'credit'):
        payload['credit'] = user.credit

    return payload

```

修改settings.py配置文件

```py
import datetime
# jwt认证相关配置项
JWT_AUTH = {
    # 设置jwt的有效期
    # 如果内部站点，例如：运维开发系统，OA，往往配置的access_token有效期基本就是15分钟，30分钟，1~2个小时
    'JWT_EXPIRATION_DELTA': datetime.timedelta(weeks=1), # 一周有效，
    # 自定义载荷
    'JWT_PAYLOAD_HANDLER': 'shencity.utils.authenticate.jwt_payload_handler',# 自定义载荷的位置。
    
}

```

## 多条件登录

我们不经想让用户使用username登录，还想让手机号，邮箱进行登录。

JWT扩展的登录视图，在收到用户名与密码时，也是调用Django的认证系统中提供的**authenticate()**来检查用户名与密码是否正确。

我们可以通过修改Django认证系统的认证后端（主要是authenticate方法）来支持登录账号既可以是用户名也可以是手机号。

**修改Django认证系统的认证后端需要继承django.contrib.auth.backends.ModelBackend，并重写authenticate方法。**

`authenticate(self, request, username=None, password=None, **kwargs)`方法的参数说明：

- request 本次认证的请求对象
- username 本次认证提供的用户账号
- password 本次认证提供的密码

**我们想要让用户既可以以用户名登录，也可以以手机号登录，那么对于authenticate方法而言，username参数即表示用户名或者手机号。**

重写authenticate方法的思路：

1. 根据username参数查找用户User对象，username参数可能是用户名，也可能是手机号
2. 若查找到User对象，调用User对象的check_password方法检查密码是否正确

![jwt认证过程中验证用户信息的代码流程分析](D:\笔记\JWT\assets\jwt认证过程中验证用户信息的代码流程分析.png)在utils/authenticate.py中编写：

使用django中的auth，就可以用下面代码，

```py
from rest_framework_jwt.utils import jwt_payload_handler as payload_handler
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q


def jwt_payload_handler(user):
    """
    自定义载荷信息
    :params user  用户模型实例对象
    """
    # 先让jwt模块生成自己的载荷信息
    payload = payload_handler(user)
    # 追加自己要返回的字段内容
    if hasattr(user, 'avatar'):
        payload['avatar'] = user.avatar.url if user.avatar else ""
    if hasattr(user, 'nickname'):
        payload['nickname'] = user.nickname
    if hasattr(user, 'money'):
        payload['money'] = float(user.money)
    if hasattr(user, 'credit'):
        payload['credit'] = user.credit

    return payload


def get_user_by_account(account):

    """
    根据帐号信息获取user模型实例对象
    :param account: 账号信息，可以是用户名，也可以是手机号，甚至其他的可用于识别用户身份的字段信息
    :return: User对象 或者 None
    """
    user = UserModel.objects.filter(Q(mobile=account) | Q(username=account) | Q(email=account)).first()
    return user


class CustomAuthBackend(ModelBackend):
    """
    自定义用户认证类[实现多条件登录]
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        多条件认证方法
        :param request: 本次客户端的http请求对象
        :param username:  本次客户端提交的用户信息，可以是user，也可以mobile或其他唯一字段
        :param password: 本次客户端提交的用户密码
        :param kwargs: 额外参数
        :return:
        """
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        if username is None or password is None:
            return
        # 根据用户名信息useranme获取账户信息
        user = get_user_by_account(username)
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
```

在配置文件settings/dev.py中告知Django使用我们自定义的认证后端，注意不是给drf添加设置。

```py
# django自定义认证
AUTHENTICATION_BACKENDS = ['shencity.utils.authenticate.CustomAuthBackend', ]
```

# 前端保存jwt

我们保存在浏览器的HTML5提供的本地存储对象中。

浏览器的本地存储提供了2个全局的js对象，给我们用于保存数据的，分别是sessionStorage 和 localStorage ：

- **sessionStorage** 会话存储，浏览器关闭即数据丢失。
- **localStorage** 永久存储，长期有效，浏览器关闭了也不会丢失。

我们可以通过浏览器提供的Application调试选项中的界面查看到保存在本地存储的数据。

![image-20210716121858268](D:\笔记\JWT\assets\image-20210716121858268.png)

注意：不同的域名或IP下的数据，互不干扰的，相互独立，也调用或访问不了其他域名下的数据。

sessionStorage和localStorage提供的操作一模一样，基本使用：

```py
// 添加/修改数据
sessionStorage.setItem("变量名","变量值")
// 简写：sessionStorage.变量名 = 变量值

// 读取数据
sessionStorage.getItem("变量名")
// 简写：sessionStorage.变量名

// 删除一条数据
sessionStorage.removeItem("变量名")
// 清空所有数据
sessionStorage.clear()  // 慎用，会清空当前域名下所有的存储在本地的数据



// 添加/修改数据
localStorage.setItem("变量名","变量值")
// 简写：localStorage.变量名 = 变量值

// 读取数据
localStorage.getItem("变量名")
// 简写：localStorage.变量名

// 删除数据
localStorage.removeItem("变量名")
// 清空数据
localStorage.clear()  // 慎用，会清空当前域名下所有的存储在本地的数据
```

登陆子组件，components/Login.vue，代码：

```vue
<script setup>
import user from "../api/user";
    //element-plus引入弹窗
import { ElMessage } from 'element-plus'

// 登录处理
const loginhandler = ()=>{
  if(user.account.length<1 || user.password.length<1){
    // 错误提示
    console.log("错了哦，用户名或密码不能为空！");
    (弹窗)
    ElMessage.error('错了哦，用户名或密码不能为空！');
    return;  // 在函数/方法中，可以阻止代码继续往下执行
  }

  // 发送请求
  user.login().then(response=>{
    // 保存token，并根据用户的选择，是否记住密码
    // 清空掉token，保证页面中没有，
    localStorage.removeItem("token");
    sessionStorage.removeItem("token");
    if(user.remember){ // 判断是否记住登录状态(用户时候选择是否记住密码)
      // 记住登录(记住密码)
      localStorage.token = response.data.token
      // 这两条是一样的
      localStorage.setItem ("token",response.data.token)
    }else{
      // 不记住登录，关闭浏览器以后就删除状态(不记住密码)
      sessionStorage.token = response.data.token;
      // 这两条是一样的
      sessionStorage.setItem ("token",response.data.token)
    }
    // 保存token，并根据用户的选择，是否记住密码
    // 成功提示(弹窗)
    ElMessage.success("登录成功！");
  }).catch(error=>{
    console.log(error);
  })
}

</script>
```


"""
=================================================
@Project -> File    ：flask2 -> settings
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/22 15:24
@用途               ：
==================================================
"""
from datetime import timedelta
from redis import Redis


class Config(object):
    DEBUG = True
    SECRET_KEY = "11111111"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)    # 设置session的时间为20分钟。
    SESSION_REFRESH_EACH_REQUEST= True
    SESSION_TYPE = "redis"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    SESSION_REDIS = Redis(host='127.0.0.1', port='6379')


class TestingConfig(Config):
    pass

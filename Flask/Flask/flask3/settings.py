"""
=================================================
@Project -> File    ：flask3 -> settings
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/27 10:04
@用途               ：
==================================================
"""
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/flasklianxi?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1
    SQLALCHEMY_TRACK_MODIFICATIONS=True
class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):

    DEBUG = True


class TestingConfig(Config):
    TESTING = True
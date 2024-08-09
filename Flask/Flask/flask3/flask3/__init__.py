"""
=================================================
@Project -> File    ：flask3 -> __init__.py
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/27 8:50
@用途               ：
==================================================
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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
    Auth(app)
    return app





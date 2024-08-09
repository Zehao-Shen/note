"""
=================================================
@Project -> File    ：flask2 -> __init__.py
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/22 15:22
@用途               ：
==================================================
"""
from flask import Flask, session
from .views import account
from .views import home
from flask_session import Session


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')
    # app.secret_key = "11111"
    app.register_blueprint(account.account)
    app.register_blueprint(home.home)


    #将session替换成redis session
    Session(app)
    return app

"""
=================================================
@Project -> File    ：flask2 -> home
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/22 15:45
@用途               ：
==================================================
"""
from flask import Blueprint, request, render_template, session, redirect, Flask
from uuid import uuid4

home = Blueprint("home", __name__)


@home.route("/index")
def index():
    user_info=session.get("user_info")
    print(user_info)
    session["user_info"]={"k1":1,"k2":2}
    user_info = session.get("user_info")
    print("原来的值", user_info)
    session["user_info"]["k1"] = 77777
    user_info = session.get("use_info")
    print("修改的值", user_info)
    # session["modified"] = True
    return "index"


@home.route("/test")
def test():
    user_info = session.get("user_info")
    print(user_info)

    return "test"

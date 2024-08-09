"""
=================================================
@Project -> File    ：flask2 -> account
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/22 15:24
@用途               ：
==================================================
"""
from flask import Blueprint, request, render_template, session, redirect, Flask

from uuid import uuid4

account = Blueprint("account", __name__)


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

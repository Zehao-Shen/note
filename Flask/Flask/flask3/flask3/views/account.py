"""
=================================================
@Project -> File    ：flask3 -> account
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/27 8:52
@用途               ：
==================================================
"""
from flask import blueprints,render_template,request,session,redirect,current_app
from flask3 import models
from flask3 import db
ac = blueprints.Blueprint('ac',__name__)

@ac.route('/login',methods=['GET','POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')

        obj = db.session.query(models.Users).filter(models.Users.name==user,models.Users.pwd==pwd).first()
        db.session.remove()
        if not obj:
            return render_template('login.html',msg='用户名或密码错误')

        current_app.auth_manager.login(user)
        return redirect('/index')


@ac.route('/logout')
def logout():
    print(current_app)
    current_app.auth_manager.logout()
    return redirect('/login')


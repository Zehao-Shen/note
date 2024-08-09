"""
=================================================
@Project -> File    ：flask3 -> home
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/29 9:47
@用途               ：
==================================================
"""
from flask import blueprints,render_template
from flask3 import models
from flask3 import db
hm = blueprints.Blueprint('hm',__name__)

@hm.route('/index')
def index():
    return render_template('index.html')